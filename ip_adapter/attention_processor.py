# modified from https://github.com/huggingface/diffusers/blob/main/src/diffusers/models/attention_processor.py
import torch
import torch.nn as nn
import torch.nn.functional as F

try:
    import xformers
    import xformers.ops
    xformers_available = True
except Exception as e:
    xformers_available = False

class RegionControler(object):
    def __init__(self) -> None:
        self.prompt_image_conditioning = []
region_control = RegionControler()

def _region_mask_stage_shapes(h, w):
    latent_h, latent_w = h // 8, w // 8

    def real_downsample(x):
        return (x - 1) // 2 + 1

    stage1_h, stage1_w = real_downsample(latent_h), real_downsample(latent_w)
    stage2_h, stage2_w = real_downsample(stage1_h), real_downsample(stage1_w)
    return [(latent_h, latent_w), (stage1_h, stage1_w), (stage2_h, stage2_w)]

def _resize_region_mask(region_mask, seq_len):
    h, w = region_mask.shape[:2]
    for stage_h, stage_w in _region_mask_stage_shapes(h, w):
        if stage_h > 0 and stage_w > 0 and stage_h * stage_w == seq_len:
            return F.interpolate(region_mask[None, None], size=(stage_h, stage_w), mode='nearest').reshape([1, -1, 1])
    # Should never happen, but this is the last-resort fallback in case of no exact UNet stage matched:
    ratio = (h * w / seq_len) ** 0.5
    mask = F.interpolate(region_mask[None, None], scale_factor=1 / ratio, mode='nearest').reshape([1, -1, 1])
    if mask.shape[1] > seq_len:
        mask = mask[:, :seq_len]
    elif mask.shape[1] < seq_len:
        mask = F.pad(mask, (0, 0, 0, seq_len - mask.shape[1]), value=1.0)
    return mask

class AttnProcessor(nn.Module):
    r"""
    Default processor for performing attention-related computations.
    """
    def __init__(
        self,
        hidden_size=None,
        cross_attention_dim=None,
    ):
        super().__init__()

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)

        batch_size, sequence_length, _ = (
            hidden_states.shape if encoder_hidden_states is None else encoder_hidden_states.shape
        )
        attention_mask = attn.prepare_attention_mask(attention_mask, sequence_length, batch_size)

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
        elif attn.norm_cross:
            encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)

        key = attn.to_k(encoder_hidden_states)
        value = attn.to_v(encoder_hidden_states)

        query = attn.head_to_batch_dim(query)
        key = attn.head_to_batch_dim(key)
        value = attn.head_to_batch_dim(value)

        attention_probs = attn.get_attention_scores(query, key, attention_mask)
        hidden_states = torch.bmm(attention_probs, value)
        hidden_states = attn.batch_to_head_dim(hidden_states)

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states
    
    
class IPAttnProcessor(nn.Module):
    r"""
    Attention processor for IP-Adapater.
    Args:
        hidden_size (`int`):
            The hidden size of the attention layer.
        cross_attention_dim (`int`):
            The number of channels in the `encoder_hidden_states`.
        scale (`float`, defaults to 1.0):
            the weight scale of image prompt.
        num_tokens (`int`, defaults to 4 when do ip_adapter_plus it should be 16):
            The context length of the image features.
    """

    def __init__(self, hidden_size, cross_attention_dim=None, scale=1.0, num_tokens=4):
        super().__init__()

        self.hidden_size = hidden_size
        self.cross_attention_dim = cross_attention_dim
        self.scale = scale
        self.num_tokens = num_tokens

        self.to_k_ip = nn.Linear(cross_attention_dim or hidden_size, hidden_size, bias=False)
        self.to_v_ip = nn.Linear(cross_attention_dim or hidden_size, hidden_size, bias=False)

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)

        batch_size, sequence_length, _ = (
            hidden_states.shape if encoder_hidden_states is None else encoder_hidden_states.shape
        )
        attention_mask = attn.prepare_attention_mask(attention_mask, sequence_length, batch_size)

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        # Multi-ID support: encoder_hidden_states carries the text tokens followed by
        # one block of `self.num_tokens` image-prompt tokens per identity. The number
        # of identities currently active is communicated globally via
        # region_control.prompt_image_conditioning (one dict per identity, each
        # optionally holding that identity's own region_mask).
        num_identities = max(len(region_control.prompt_image_conditioning), 1)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
            ip_hidden_states_all = None
        else:
            # get encoder_hidden_states, ip_hidden_states
            end_pos = encoder_hidden_states.shape[1] - self.num_tokens * num_identities
            encoder_hidden_states, ip_hidden_states_all = encoder_hidden_states[:, :end_pos, :], encoder_hidden_states[:, end_pos:, :]
            if attn.norm_cross:
                encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)

        key = attn.to_k(encoder_hidden_states)
        value = attn.to_v(encoder_hidden_states)

        query = attn.head_to_batch_dim(query)
        key = attn.head_to_batch_dim(key)
        value = attn.head_to_batch_dim(value)

        if xformers_available:
            hidden_states = self._memory_efficient_attention_xformers(query, key, value, attention_mask)
        else:
            attention_probs = attn.get_attention_scores(query, key, attention_mask)
            hidden_states = torch.bmm(attention_probs, value)
        hidden_states = attn.batch_to_head_dim(hidden_states)

        # for ip-adapter - one attention pass per identity, each gated by its own region mask
        ip_hidden_states = 0
        for idx in range(num_identities):
            id_tokens = ip_hidden_states_all[:, idx * self.num_tokens: (idx + 1) * self.num_tokens, :]
            ip_key = self.to_k_ip(id_tokens)
            ip_value = self.to_v_ip(id_tokens)

            ip_key = attn.head_to_batch_dim(ip_key)
            ip_value = attn.head_to_batch_dim(ip_value)

            if xformers_available:
                ip_hidden_states_i = self._memory_efficient_attention_xformers(query, ip_key, ip_value, None)
            else:
                ip_attention_probs = attn.get_attention_scores(query, ip_key, None)
                ip_hidden_states_i = torch.bmm(ip_attention_probs, ip_value)
            ip_hidden_states_i = attn.batch_to_head_dim(ip_hidden_states_i)

            region_mask = None
            if idx < len(region_control.prompt_image_conditioning):
                region_mask = region_control.prompt_image_conditioning[idx].get('region_mask', None)
            mask = _resize_region_mask(region_mask, query.shape[1]) if region_mask is not None else torch.ones_like(ip_hidden_states_i)
            ip_hidden_states = ip_hidden_states + ip_hidden_states_i * mask

        hidden_states = hidden_states + self.scale * ip_hidden_states

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states


    def _memory_efficient_attention_xformers(self, query, key, value, attention_mask):
        # TODO attention_mask
        query = query.contiguous()
        key = key.contiguous()
        value = value.contiguous()
        hidden_states = xformers.ops.memory_efficient_attention(query, key, value, attn_bias=attention_mask)
        # hidden_states = self.reshape_batch_dim_to_heads(hidden_states)
        return hidden_states


class AttnProcessor2_0(torch.nn.Module):
    r"""
    Processor for implementing scaled dot-product attention (enabled by default if you're using PyTorch 2.0).
    """
    def __init__(
        self,
        hidden_size=None,
        cross_attention_dim=None,
    ):
        super().__init__()
        if not hasattr(F, "scaled_dot_product_attention"):
            raise ImportError("AttnProcessor2_0 requires PyTorch 2.0, to use it, please upgrade PyTorch to 2.0.")

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)

        batch_size, sequence_length, _ = (
            hidden_states.shape if encoder_hidden_states is None else encoder_hidden_states.shape
        )

        if attention_mask is not None:
            attention_mask = attn.prepare_attention_mask(attention_mask, sequence_length, batch_size)
            # scaled_dot_product_attention expects attention_mask shape to be
            # (batch, heads, source_length, target_length)
            attention_mask = attention_mask.view(batch_size, attn.heads, -1, attention_mask.shape[-1])

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
        elif attn.norm_cross:
            encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)

        key = attn.to_k(encoder_hidden_states)
        value = attn.to_v(encoder_hidden_states)

        inner_dim = key.shape[-1]
        head_dim = inner_dim // attn.heads

        query = query.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

        key = key.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)
        value = value.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

        # the output of sdp = (batch, num_heads, seq_len, head_dim)
        # TODO: add support for attn.scale when we move to Torch 2.1
        hidden_states = F.scaled_dot_product_attention(
            query, key, value, attn_mask=attention_mask, dropout_p=0.0, is_causal=False
        )

        hidden_states = hidden_states.transpose(1, 2).reshape(batch_size, -1, attn.heads * head_dim)
        hidden_states = hidden_states.to(query.dtype)

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states

class IPAttnProcessor2_0(torch.nn.Module):
    r"""
    Attention processor for IP-Adapater for PyTorch 2.0.
    Args:
        hidden_size (`int`):
            The hidden size of the attention layer.
        cross_attention_dim (`int`):
            The number of channels in the `encoder_hidden_states`.
        scale (`float`, defaults to 1.0):
            the weight scale of image prompt.
        num_tokens (`int`, defaults to 4 when do ip_adapter_plus it should be 16):
            The context length of the image features.
    """

    def __init__(self, hidden_size, cross_attention_dim=None, scale=1.0, num_tokens=4):
        super().__init__()

        if not hasattr(F, "scaled_dot_product_attention"):
            raise ImportError("AttnProcessor2_0 requires PyTorch 2.0, to use it, please upgrade PyTorch to 2.0.")

        self.hidden_size = hidden_size
        self.cross_attention_dim = cross_attention_dim
        self.scale = scale
        self.num_tokens = num_tokens

        self.to_k_ip = nn.Linear(cross_attention_dim or hidden_size, hidden_size, bias=False)
        self.to_v_ip = nn.Linear(cross_attention_dim or hidden_size, hidden_size, bias=False)

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)

        batch_size, sequence_length, _ = (
            hidden_states.shape if encoder_hidden_states is None else encoder_hidden_states.shape
        )

        if attention_mask is not None:
            attention_mask = attn.prepare_attention_mask(attention_mask, sequence_length, batch_size)
            # scaled_dot_product_attention expects attention_mask shape to be
            # (batch, heads, source_length, target_length)
            attention_mask = attention_mask.view(batch_size, attn.heads, -1, attention_mask.shape[-1])

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        # Multi-ID support: encoder_hidden_states carries the text tokens followed by
        # one block of `self.num_tokens` image-prompt tokens per identity. The number
        # of identities currently active is communicated globally via
        # region_control.prompt_image_conditioning (one dict per identity, each
        # optionally holding that identity's own region_mask).
        num_identities = max(len(region_control.prompt_image_conditioning), 1)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
            ip_hidden_states_all = None
        else:
            # get encoder_hidden_states, ip_hidden_states
            end_pos = encoder_hidden_states.shape[1] - self.num_tokens * num_identities
            encoder_hidden_states, ip_hidden_states_all = (
                encoder_hidden_states[:, :end_pos, :],
                encoder_hidden_states[:, end_pos:, :],
            )
            if attn.norm_cross:
                encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)

        key = attn.to_k(encoder_hidden_states)
        value = attn.to_v(encoder_hidden_states)

        inner_dim = key.shape[-1]
        head_dim = inner_dim // attn.heads

        query = query.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

        key = key.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)
        value = value.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

        # the output of sdp = (batch, num_heads, seq_len, head_dim)
        # TODO: add support for attn.scale when we move to Torch 2.1
        hidden_states = F.scaled_dot_product_attention(
            query, key, value, attn_mask=attention_mask, dropout_p=0.0, is_causal=False
        )

        hidden_states = hidden_states.transpose(1, 2).reshape(batch_size, -1, attn.heads * head_dim)
        hidden_states = hidden_states.to(query.dtype)

        # for ip-adapter - one attention pass per identity, each gated by its own region mask
        ip_hidden_states = 0
        for idx in range(num_identities):
            id_tokens = ip_hidden_states_all[:, idx * self.num_tokens: (idx + 1) * self.num_tokens, :]
            ip_key = self.to_k_ip(id_tokens)
            ip_value = self.to_v_ip(id_tokens)

            ip_key = ip_key.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)
            ip_value = ip_value.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

            # the output of sdp = (batch, num_heads, seq_len, head_dim)
            ip_hidden_states_i = F.scaled_dot_product_attention(
                query, ip_key, ip_value, attn_mask=None, dropout_p=0.0, is_causal=False
            )
            if idx == 0:
                self.attn_maps = []
            with torch.no_grad():
                identity_attn_map = query @ ip_key.transpose(-2, -1).softmax(dim=-1)
            self.attn_maps.append(identity_attn_map)
            if idx == 0:
                self.attn_map = identity_attn_map

            ip_hidden_states_i = ip_hidden_states_i.transpose(1, 2).reshape(batch_size, -1, attn.heads * head_dim)
            ip_hidden_states_i = ip_hidden_states_i.to(query.dtype)

            region_mask = None
            if idx < len(region_control.prompt_image_conditioning):
                region_mask = region_control.prompt_image_conditioning[idx].get('region_mask', None)
            if region_mask is not None:
                mask = _resize_region_mask(region_mask, query.shape[-2])
            else:
                mask = torch.ones_like(ip_hidden_states_i)
            ip_hidden_states = ip_hidden_states + ip_hidden_states_i * mask

        hidden_states = hidden_states + self.scale * ip_hidden_states

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states


class IdentityNetAttnProcessor(nn.Module):
    def __init__(self, num_tokens=16):
        super().__init__()
        self.num_tokens = num_tokens

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)

        batch_size, sequence_length, _ = (
            hidden_states.shape if encoder_hidden_states is None else encoder_hidden_states.shape
        )
        attention_mask = attn.prepare_attention_mask(attention_mask, sequence_length, batch_size)

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
            num_identities = 1
        else:
            if attn.norm_cross:
                encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)
            num_identities = max(len(region_control.prompt_image_conditioning), 1)

        query = attn.head_to_batch_dim(query)

        hidden_states = 0
        for idx in range(num_identities):
            id_tokens = encoder_hidden_states[:, idx * self.num_tokens: (idx + 1) * self.num_tokens, :]
            key = attn.to_k(id_tokens)
            value = attn.to_v(id_tokens)
            key = attn.head_to_batch_dim(key)
            value = attn.head_to_batch_dim(value)

            if xformers_available:
                hidden_states_i = self._memory_efficient_attention_xformers(query, key, value, None)
            else:
                attention_probs = attn.get_attention_scores(query, key, None)
                hidden_states_i = torch.bmm(attention_probs, value)
            hidden_states_i = attn.batch_to_head_dim(hidden_states_i)

            region_mask = None
            if idx < len(region_control.prompt_image_conditioning):
                region_mask = region_control.prompt_image_conditioning[idx].get('region_mask', None)
            mask = _resize_region_mask(region_mask, query.shape[1]) if region_mask is not None else torch.ones_like(hidden_states_i)
            hidden_states = hidden_states + hidden_states_i * mask

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states

    def _memory_efficient_attention_xformers(self, query, key, value, attention_mask):
        query = query.contiguous()
        key = key.contiguous()
        value = value.contiguous()
        hidden_states = xformers.ops.memory_efficient_attention(query, key, value, attn_bias=attention_mask)
        return hidden_states


class IdentityNetAttnProcessor2_0(torch.nn.Module):
    def __init__(self, num_tokens=16):
        super().__init__()
        if not hasattr(F, "scaled_dot_product_attention"):
            raise ImportError("IdentityNetAttnProcessor2_0 requires PyTorch 2.0, to use it, please upgrade PyTorch to 2.0.")
        self.num_tokens = num_tokens

    def forward(
        self,
        attn,
        hidden_states,
        encoder_hidden_states=None,
        attention_mask=None,
        temb=None,
    ):
        residual = hidden_states

        if attn.spatial_norm is not None:
            hidden_states = attn.spatial_norm(hidden_states, temb)

        input_ndim = hidden_states.ndim

        if input_ndim == 4:
            batch_size, channel, height, width = hidden_states.shape
            hidden_states = hidden_states.view(batch_size, channel, height * width).transpose(1, 2)
        else:
            batch_size = hidden_states.shape[0]

        if attn.group_norm is not None:
            hidden_states = attn.group_norm(hidden_states.transpose(1, 2)).transpose(1, 2)

        query = attn.to_q(hidden_states)

        if encoder_hidden_states is None:
            encoder_hidden_states = hidden_states
            num_identities = 1
        else:
            if attn.norm_cross:
                encoder_hidden_states = attn.norm_encoder_hidden_states(encoder_hidden_states)
            num_identities = max(len(region_control.prompt_image_conditioning), 1)

        inner_dim = attn.to_k.out_features
        head_dim = inner_dim // attn.heads

        query = query.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

        hidden_states = 0
        for idx in range(num_identities):
            id_tokens = encoder_hidden_states[:, idx * self.num_tokens: (idx + 1) * self.num_tokens, :]
            key = attn.to_k(id_tokens)
            value = attn.to_v(id_tokens)

            key = key.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)
            value = value.view(batch_size, -1, attn.heads, head_dim).transpose(1, 2)

            hidden_states_i = F.scaled_dot_product_attention(
                query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False
            )
            hidden_states_i = hidden_states_i.transpose(1, 2).reshape(batch_size, -1, attn.heads * head_dim)
            hidden_states_i = hidden_states_i.to(query.dtype)

            region_mask = None
            if idx < len(region_control.prompt_image_conditioning):
                region_mask = region_control.prompt_image_conditioning[idx].get('region_mask', None)
            if region_mask is not None:
                mask = _resize_region_mask(region_mask, query.shape[-2])
            else:
                mask = torch.ones_like(hidden_states_i)
            hidden_states = hidden_states + hidden_states_i * mask

        # linear proj
        hidden_states = attn.to_out[0](hidden_states)
        # dropout
        hidden_states = attn.to_out[1](hidden_states)

        if input_ndim == 4:
            hidden_states = hidden_states.transpose(-1, -2).reshape(batch_size, channel, height, width)

        if attn.residual_connection:
            hidden_states = hidden_states + residual

        hidden_states = hidden_states / attn.rescale_output_factor

        return hidden_states


def run_separate_identitynet(controlnet, sample, timestep, image_tokens,
                             identity_images, conditioning_scale, guess_mode,
                             added_cond_kwargs):
    """Run one original IdentityNet forward per identity, mask outputs, then sum.

    UNet regional attention state remains unchanged. Restore ControlNet processors
    even if a forward fails, so later ordinary Multi-ID runs use their old path.
    """
    regions = region_control.prompt_image_conditioning
    count = len(regions)
    if count < 2 or len(identity_images) != count:
        raise ValueError("Separate IdentityNet requires one landmark image and mask per identity.")
    if image_tokens.shape[1] % count:
        raise ValueError("Identity token count does not match the identity regions.")
    original = getattr(controlnet, "_identitynet_original_attn_procs", None)
    if original is None:
        raise ValueError("Separate IdentityNet requires the updated InstantID app initialization.")
    # Guess mode supplies only the conditional sample batch.
    if image_tokens.shape[0] == 2 * sample.shape[0]:
        image_tokens = image_tokens.chunk(2)[1]
    tokens_per_id = image_tokens.shape[1] // count
    saved_processors = dict(controlnet.attn_processors)
    down_sum, mid_sum = None, None
    try:
        controlnet.set_attn_processor(dict(original))
        for idx, (region, landmark_image) in enumerate(zip(regions, identity_images)):
            mask = region.get("region_mask")
            if mask is None:
                raise ValueError("Separate IdentityNet requires a mask for every identity.")
            if landmark_image.shape[0] == 2 * sample.shape[0]:
                landmark_image = landmark_image.chunk(2)[1]
            down, mid = controlnet(
                sample, timestep,
                encoder_hidden_states=image_tokens[:, idx * tokens_per_id:(idx + 1) * tokens_per_id],
                controlnet_cond=landmark_image,
                conditioning_scale=conditioning_scale, guess_mode=guess_mode,
                added_cond_kwargs=added_cond_kwargs, return_dict=False,
            )
            def mask_output(value):
                return value * F.interpolate(mask[None, None].to(value),
                                             size=value.shape[-2:], mode="bilinear", align_corners=False)
            down = [mask_output(value) for value in down]
            mid = mask_output(mid)
            down_sum = down if down_sum is None else [a + b for a, b in zip(down_sum, down)]
            mid_sum = mid if mid_sum is None else mid_sum + mid
        return down_sum, mid_sum
    finally:
        controlnet.set_attn_processor(saved_processors)
