import os
import gc

import torch
import safetensors.torch
from transformers import CLIPVisionModelWithProjection, CLIPImageProcessor

from ip_adapter.resampler import Resampler
from ip_adapter.attention_processor import IPAttnProcessor, IPAttnProcessor2_0

class ImageProjModel(torch.nn.Module):
    def __init__(self, cross_attention_dim=1024, clip_embeddings_dim=1024, clip_extra_context_tokens=4):
        super().__init__()
        self.cross_attention_dim = cross_attention_dim
        self.clip_extra_context_tokens = clip_extra_context_tokens
        self.proj = torch.nn.Linear(clip_embeddings_dim, self.clip_extra_context_tokens * cross_attention_dim)
        self.norm = torch.nn.LayerNorm(cross_attention_dim)

    def forward(self, image_embeds):
        clip_extra_context_tokens = self.proj(image_embeds).reshape(
            -1, self.clip_extra_context_tokens, self.cross_attention_dim
        )
        return self.norm(clip_extra_context_tokens)

STYLE_ADAPTER_REPO_ID = "h94/IP-Adapter"
STYLE_ADAPTER_REPO_FILENAMES = {
    "plus": "sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors",
    "standard": "sdxl_models/ip-adapter_sdxl_vit-h.safetensors",
    "plus_face": "sdxl_models/ip-adapter-plus-face_sdxl_vit-h.safetensors",
    "sdxl_adapter_bigg": "sdxl_models/ip-adapter_sdxl.safetensors",
    "faceid": "ip-adapter-faceid_sdxl.bin",
    "faceid_plusv2": "ip-adapter-faceid-plusv2_sdxl.bin",
    "faceid_portrait": "ip-adapter-faceid-portrait_sdxl.bin",
    "faceid_portrait_unnorm": "ip-adapter-faceid-portrait_sdxl_unnorm.bin",
}
FACEID_VARIANTS = ("faceid", "faceid_plusv2", "faceid_portrait", "faceid_portrait_unnorm")
FACEID_REPO_ID = "h94/IP-Adapter-FaceID"
STYLE_ADAPTER_ENCODER_SUBFOLDER = "models/image_encoder"
STYLE_ADAPTER_ENCODER_SUBFOLDER_BIGG = "sdxl_models/image_encoder"
STYLE_ADAPTER_ENCODER_FILES = ("config.json", "model.safetensors")
STYLE_ADAPTER_ENCODER_DIRS = {
    "plus": ("image_encoder", STYLE_ADAPTER_ENCODER_SUBFOLDER),
    "standard": ("image_encoder", STYLE_ADAPTER_ENCODER_SUBFOLDER),
    "plus_face": ("image_encoder", STYLE_ADAPTER_ENCODER_SUBFOLDER),
    "sdxl_adapter_bigg": ("image_encoder_bigg", STYLE_ADAPTER_ENCODER_SUBFOLDER_BIGG),
    "faceid_plusv2": ("image_encoder", STYLE_ADAPTER_ENCODER_SUBFOLDER),
}

def _style_state(pipe):
    state = getattr(pipe.unet, "_style_adapter_state", None)
    if state is None:
        state = {"loaded": False}
        pipe.unet._style_adapter_state = state
    return state

def is_style_adapter_loaded(pipe):
    return _style_state(pipe).get("loaded", False)

def get_loaded_style_variant(pipe):
    state = _style_state(pipe)
    if not state.get("loaded", False):
        return None
    return state.get("variant")

def download_style_adapter_files(checkpoints_dir="./checkpoints", variant="plus"):
    from huggingface_hub import hf_hub_download

    repo_id = FACEID_REPO_ID if variant in FACEID_VARIANTS else STYLE_ADAPTER_REPO_ID
    repo_filename = STYLE_ADAPTER_REPO_FILENAMES[variant]
    adapter_ckpt_path = hf_hub_download(repo_id=repo_id, filename=repo_filename)

    if variant in ("faceid", "faceid_portrait", "faceid_portrait_unnorm"):
        return adapter_ckpt_path, None

    _, encoder_subfolder = STYLE_ADAPTER_ENCODER_DIRS[variant]
    for fname in STYLE_ADAPTER_ENCODER_FILES:
        encoder_path = hf_hub_download(
            repo_id=STYLE_ADAPTER_REPO_ID, filename=f"{encoder_subfolder}/{fname}"
        )
    image_encoder_dir = os.path.dirname(encoder_path)

    return adapter_ckpt_path, image_encoder_dir

def _load_style_checkpoint(model_ckpt):
    if str(model_ckpt).endswith(".safetensors"):
        raw = safetensors.torch.load_file(model_ckpt, device="cpu")
        if any(k.startswith("image_proj.") or k.startswith("ip_adapter.") for k in raw.keys()):
            state_dict = {"image_proj": {}, "ip_adapter": {}}
            for k, v in raw.items():
                prefix, _, rest = k.partition(".")
                state_dict[prefix][rest] = v
            return state_dict
        return raw
    return torch.load(model_ckpt, map_location="cpu")

def load_ip_adapter_style(
    pipe,
    model_ckpt,
    image_encoder_path,
    num_tokens=16,
    embedding_dim=1024,
    scale=1.0,
    variant="plus",
    independent_style_strength=False,
    style_injection_budget=2.0,
):
    if variant not in STYLE_ADAPTER_REPO_FILENAMES:
        raise ValueError(f"Unknown style adapter variant: {variant!r}")

    device = pipe.unet.device
    dtype = pipe.unet.dtype

    state = _style_state(pipe)

    state_dict = _load_style_checkpoint(model_ckpt) if variant in FACEID_VARIANTS else None
    style_image_encoder = None
    style_clip_image_processor = None
    if variant not in ("faceid", "faceid_portrait", "faceid_portrait_unnorm"):
        style_image_encoder = CLIPVisionModelWithProjection.from_pretrained(image_encoder_path).to(
            device, dtype=dtype
        )
        style_image_encoder.requires_grad_(False)
        style_clip_image_processor = CLIPImageProcessor()

    if variant == "faceid_portrait_unnorm":
        projection_weights = state_dict["image_proj"]
        num_tokens = projection_weights["latents"].shape[1]
        style_image_proj_model = Resampler(
            dim=1280,
            depth=4,
            dim_head=64,
            heads=20,
            num_queries=num_tokens,
            embedding_dim=512,
            output_dim=pipe.unet.config.cross_attention_dim,
            ff_mult=4,
        )
    elif variant in FACEID_VARIANTS:
        projection_weights = state_dict["image_proj"]
        output_dim = pipe.unet.config.cross_attention_dim
        num_tokens = projection_weights["proj.2.weight"].shape[0] // output_dim
        if variant == "faceid_plusv2":
            clip_dim = projection_weights["perceiver_resampler.proj_in.weight"].shape[1]
            style_image_proj_model = FaceIDPlusProjection(output_dim, num_tokens, clip_dim)
        else:
            style_image_proj_model = FaceIDProjection(output_dim, num_tokens)
    elif variant in ("plus", "plus_face"):
        style_image_proj_model = Resampler(
            dim=1280,
            depth=4,
            dim_head=64,
            heads=20,
            num_queries=num_tokens,
            embedding_dim=embedding_dim,
            output_dim=pipe.unet.config.cross_attention_dim,
            ff_mult=4,
        )
    else:
        style_image_proj_model = ImageProjModel(
            cross_attention_dim=pipe.unet.config.cross_attention_dim,
            clip_embeddings_dim=embedding_dim,
            clip_extra_context_tokens=num_tokens,
        )
    style_image_proj_model.eval()
    style_image_proj_model = style_image_proj_model.to(device, dtype=dtype)

    if state_dict is None:
        state_dict = _load_style_checkpoint(model_ckpt)
    image_proj_sd = state_dict["image_proj"] if "image_proj" in state_dict else state_dict
    style_image_proj_model.load_state_dict(image_proj_sd)

    ip_adapter_sd = state_dict["ip_adapter"] if "ip_adapter" in state_dict else state_dict
    faceid_lora_weights = {}
    if variant in FACEID_VARIANTS:
        import re
        faceid_lora_weights = {
            k: v for k, v in ip_adapter_sd.items()
            if re.fullmatch(r"\d+\.to_(?:q|k|v|out)_lora\.(?:down|up)\.weight", k)
        }
        ip_adapter_sd = {k: v for k, v in ip_adapter_sd.items() if k not in faceid_lora_weights}
    renamed_sd = {
        k.replace("to_k_ip.", "to_k_ip_style.").replace("to_v_ip.", "to_v_ip_style."): v
        for k, v in ip_adapter_sd.items()
    }

    style_layers = torch.nn.ModuleList()
    for attn_processor in pipe.unet.attn_processors.values():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            attn_processor.add_style_branch(num_tokens, style_scale=scale)
            attn_processor.independent_style_strength = bool(independent_style_strength)
            attn_processor.style_injection_budget = style_injection_budget
            attn_processor.multi_style_enabled = False
            attn_processor.to(device, dtype=dtype)
        style_layers.append(attn_processor)

    load_result = style_layers.load_state_dict(renamed_sd, strict=False)
    missing_style_keys = [
        key for key in load_result.missing_keys
        if "to_k_ip_style." in key or "to_v_ip_style." in key
    ]
    if missing_style_keys or load_result.unexpected_keys:
        for attn_processor in style_layers:
            if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
                attn_processor.remove_style_branch()

        raise RuntimeError(
            "Style adapter checkpoint did not match the attention layers.\n"
            f"Missing style weights: {missing_style_keys}\n"
            f"Unexpected weights: {load_result.unexpected_keys}"
        )

    state.update({
        "image_encoder": style_image_encoder,
        "image_proj_model": style_image_proj_model,
        "clip_image_processor": style_clip_image_processor,
        "num_tokens": num_tokens,
        "variant": variant,
        "independent_style_strength": bool(independent_style_strength),
        "style_injection_budget": style_injection_budget,
        "loaded": True,
    })
    if variant in FACEID_VARIANTS:
        state["faceid_lora_weights"] = faceid_lora_weights
        try:
            refresh_faceid_lora_hooks(pipe)
        except Exception:
            unload_ip_adapter_style(pipe)
            raise

def unload_ip_adapter_style(pipe):
    state = _style_state(pipe)
    if not state.get("loaded", False):
        return

    _remove_faceid_lora_hooks(state)
    for attn_processor in pipe.unet.attn_processors.values():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            attn_processor.remove_style_branch()

    state.clear()
    state["loaded"] = False

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def set_style_scale(pipe, scale):
    for attn_processor in pipe.unet.attn_processors.values():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            attn_processor.style_scale = scale

STYLE_ONLY_BLOCK_PREFIXES = ("up_blocks.0.attentions.1",)

def set_style_block_restriction(pipe, enabled, bleed_through=0.0, target_block_prefixes=STYLE_ONLY_BLOCK_PREFIXES):
    state = _style_state(pipe)
    for name, attn_processor in pipe.unet.attn_processors.items():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            if enabled:
                attn_processor.style_block_scale = 1.0 if name.startswith(target_block_prefixes) else float(bleed_through)
            else:
                attn_processor.style_block_scale = 1.0
    if state.get("loaded", False):
        state["style_restrict_to_style_layers"] = bool(enabled)
        state["style_restrict_bleed_through"] = float(bleed_through)

def get_style_block_restriction(pipe):
    return _style_state(pipe).get("style_restrict_to_style_layers", False)

def get_style_restrict_bleed_through(pipe):
    return _style_state(pipe).get("style_restrict_bleed_through", 0.0)

def set_independent_style_strength(pipe, enabled, budget=2.0):
    for attn_processor in pipe.unet.attn_processors.values():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            attn_processor.independent_style_strength = bool(enabled)
            attn_processor.style_injection_budget = budget
    state = _style_state(pipe)
    if state.get("loaded", False):
        state["independent_style_strength"] = bool(enabled)
        state["style_injection_budget"] = budget

def get_independent_style_strength(pipe):
    return _style_state(pipe).get("independent_style_strength", False)

def set_multi_style_enabled(pipe, enabled):
    for attn_processor in pipe.unet.attn_processors.values():
        if isinstance(attn_processor, (IPAttnProcessor, IPAttnProcessor2_0)):
            attn_processor.multi_style_enabled = bool(enabled)
    state = _style_state(pipe)
    if state.get("loaded", False):
        state["multi_style_enabled"] = bool(enabled)

def get_multi_style_enabled(pipe):
    return _style_state(pipe).get("multi_style_enabled", False)

@torch.no_grad()
def encode_style_images(pipe, style_images, num_images_per_prompt=1, do_classifier_free_guidance=True):
    if _style_state(pipe).get("variant") in FACEID_VARIANTS:
        return _encode_faceid_styles(pipe, style_images, num_images_per_prompt, do_classifier_free_guidance)
    device = pipe.unet.device
    dtype = pipe.unet.dtype
    state = _style_state(pipe)
    variant = state.get("variant", "plus")

    all_tokens = []
    all_uncond_tokens = []
    for style_image in style_images:
        pixel_values = state["clip_image_processor"](images=style_image, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device, dtype=dtype)

        if variant in ("plus", "plus_face"):
            clip_image_embeds = state["image_encoder"](pixel_values, output_hidden_states=True).hidden_states[-2]
            uncond_clip_image_embeds = state["image_encoder"](
                torch.zeros_like(pixel_values), output_hidden_states=True
            ).hidden_states[-2]
        else:
            clip_image_embeds = state["image_encoder"](pixel_values).image_embeds
            uncond_clip_image_embeds = torch.zeros_like(clip_image_embeds)

        all_tokens.append(state["image_proj_model"](clip_image_embeds))
        all_uncond_tokens.append(state["image_proj_model"](uncond_clip_image_embeds))

    style_tokens = torch.cat(all_tokens, dim=1)
    uncond_style_tokens = torch.cat(all_uncond_tokens, dim=1)

    if do_classifier_free_guidance:
        style_tokens = torch.cat([uncond_style_tokens, style_tokens], dim=0)

    bs_embed, seq_len, _ = style_tokens.shape
    style_tokens = style_tokens.repeat(1, num_images_per_prompt, 1)
    style_tokens = style_tokens.view(bs_embed * num_images_per_prompt, seq_len, -1)

    return style_tokens.to(device=device, dtype=dtype)

@torch.no_grad()
def encode_style_image(pipe, style_image, num_images_per_prompt=1, do_classifier_free_guidance=True):
    if _style_state(pipe).get("variant") in FACEID_VARIANTS:
        return _encode_faceid_styles(pipe, [style_image], num_images_per_prompt, do_classifier_free_guidance)
    device = pipe.unet.device
    dtype = pipe.unet.dtype
    state = _style_state(pipe)

    pixel_values = state["clip_image_processor"](images=style_image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device, dtype=dtype)

    if state.get("variant", "plus") in ("plus", "plus_face"):
        clip_image_embeds = state["image_encoder"](pixel_values, output_hidden_states=True).hidden_states[-2]
        uncond_clip_image_embeds = state["image_encoder"](
            torch.zeros_like(pixel_values), output_hidden_states=True
        ).hidden_states[-2]
    else:
        clip_image_embeds = state["image_encoder"](pixel_values).image_embeds
        uncond_clip_image_embeds = torch.zeros_like(clip_image_embeds)

    style_tokens = state["image_proj_model"](clip_image_embeds)
    uncond_style_tokens = state["image_proj_model"](uncond_clip_image_embeds)

    if do_classifier_free_guidance:
        style_tokens = torch.cat([uncond_style_tokens, style_tokens], dim=0)

    bs_embed, seq_len, _ = style_tokens.shape
    style_tokens = style_tokens.repeat(1, num_images_per_prompt, 1)
    style_tokens = style_tokens.view(bs_embed * num_images_per_prompt, seq_len, -1)

    return style_tokens.to(device=device, dtype=dtype)

class FaceIDProjection(torch.nn.Module):
    def __init__(self, output_dim, num_tokens):
        super().__init__()
        self.num_tokens = num_tokens
        self.output_dim = output_dim
        self.proj = torch.nn.Sequential(
            torch.nn.Linear(512, 1024), torch.nn.GELU(),
            torch.nn.Linear(1024, output_dim * num_tokens),
        )
        self.norm = torch.nn.LayerNorm(output_dim)

    def forward(self, identity):
        return self.norm(self.proj(identity).reshape(-1, self.num_tokens, self.output_dim))

class FaceIDResampler(torch.nn.Module):
    def __init__(self, dim, clip_dim):
        super().__init__()
        from ip_adapter.resampler import PerceiverAttention, FeedForward
        self.proj_in = torch.nn.Linear(clip_dim, dim)
        self.proj_out = torch.nn.Linear(dim, dim)
        self.norm_out = torch.nn.LayerNorm(dim)
        self.layers = torch.nn.ModuleList([
            torch.nn.ModuleList([PerceiverAttention(dim=dim, dim_head=64, heads=dim // 64),
                                 FeedForward(dim=dim, mult=4)])
            for _ in range(4)
        ])

    def forward(self, identity_tokens, clip_tokens):
        context = self.proj_in(clip_tokens)
        for attention, feed_forward in self.layers:
            identity_tokens = identity_tokens + attention(context, identity_tokens)
            identity_tokens = identity_tokens + feed_forward(identity_tokens)
        return self.norm_out(self.proj_out(identity_tokens))

class FaceIDPlusProjection(FaceIDProjection):
    def __init__(self, output_dim, num_tokens, clip_dim):
        super().__init__(output_dim, num_tokens)
        self.perceiver_resampler = FaceIDResampler(output_dim, clip_dim)

    def forward(self, identity, clip_tokens):
        tokens = super().forward(identity)
        return tokens + self.perceiver_resampler(tokens, clip_tokens)

def _remove_faceid_lora_hooks(state):
    for handle in state.pop("faceid_lora_handles", []):
        handle.remove()
    state.pop("faceid_lora_targets", None)

def set_faceid_lora_scale(pipe, scale=1.0):
    _style_state(pipe)["faceid_lora_scale"] = float(scale)

def refresh_faceid_lora_hooks(pipe):
    state = _style_state(pipe)
    weights = state.get("faceid_lora_weights", {})
    if not weights:
        return
    processor_names = list(pipe.unet.attn_processors)
    targets = []
    for prefix in sorted({key.rsplit(".", 2)[0] for key in weights}):
        index, projection = prefix.split(".")
        attention = pipe.unet.get_submodule(processor_names[int(index)].removesuffix(".processor"))
        attr = projection.removesuffix("_lora")
        module = attention.to_out[0] if attr == "to_out" else getattr(attention, attr)
        down = weights[prefix + ".down.weight"]
        up = weights[prefix + ".up.weight"]
        if down.shape[1] != module.in_features or up.shape[0] != module.out_features or down.shape[0] != up.shape[1]:
            raise ValueError(f"FaceID LoRA dimensions do not match {processor_names[int(index)]}/{attr}")
        targets.append((module, down, up))
    if [id(item[0]) for item in targets] == state.get("faceid_lora_targets"):
        return
    _remove_faceid_lora_hooks(state)
    handles = []
    try:
        for module, down, up in targets:
            down = down.to(device=module.weight.device, dtype=module.weight.dtype)
            up = up.to(device=module.weight.device, dtype=module.weight.dtype)
            def add_delta(layer, inputs, output, down=down, up=up):
                scale = state.get("faceid_lora_scale", 1.0)
                if scale == 0.0:
                    return output
                value = inputs[0].to(dtype=down.dtype)
                delta = torch.nn.functional.linear(torch.nn.functional.linear(value, down), up)
                delta = delta.to(dtype=output.dtype)
                return output + delta if scale == 1.0 else output + scale * delta
            handles.append(module.register_forward_hook(add_delta))
    except Exception:
        for handle in handles:
            handle.remove()
        raise
    state["faceid_lora_handles"] = handles
    state["faceid_lora_targets"] = [id(item[0]) for item in targets]

def _encode_faceid_styles(pipe, images, num_images_per_prompt, do_classifier_free_guidance):
    import numpy as np
    from PIL import Image
    from insightface.app import FaceAnalysis
    from insightface.utils import face_align
    state = _style_state(pipe)
    if "faceid_analyser" not in state:
        analyser = FaceAnalysis(name="buffalo_l", root="./", allowed_modules=["detection", "recognition"],
                                providers=["CPUExecutionProvider"])
        analyser.prepare(ctx_id=-1, det_size=(640, 640))
        state["faceid_analyser"] = analyser
    conditional, unconditional = [], []
    for index, image in enumerate(images):
        bgr = np.asarray(image.convert("RGB"))[:, :, ::-1].copy()
        faces = state["faceid_analyser"].get(bgr)
        if not faces:
            detector = state["faceid_analyser"].det_model
            original_size = detector.input_size
            try:
                print("\nNo face detected inside the style image used by FaceID, temporarily retrying at 320x320 det-size...\n")
                detector.input_size = (320, 320)
                faces = state["faceid_analyser"].get(bgr)
            finally:
                detector.input_size = original_size
        if not faces:
            raise ValueError(f"FaceID reference {index + 1}: no face detected. Upload a clear face photo.")
        face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
        if state["variant"] == "faceid_portrait_unnorm":
            identity = torch.from_numpy(np.asarray(face.embedding, dtype=np.float32)).reshape(1, 1, 512)
        else:
            identity = torch.from_numpy(np.asarray(face.normed_embedding, dtype=np.float32)).reshape(1, 512)
        identity = identity.to(device=pipe.unet.device, dtype=pipe.unet.dtype)
        projection = state["image_proj_model"]
        if state["variant"] == "faceid_plusv2":
            crop = face_align.norm_crop(bgr, landmark=face.kps, image_size=224)
            crop = Image.fromarray(crop[:, :, ::-1].copy())
            pixels = state["clip_image_processor"](images=crop, return_tensors="pt").pixel_values.to(identity)
            clip = state["image_encoder"](pixels, output_hidden_states=True).hidden_states[-2]
            zero_clip = state["image_encoder"](torch.zeros_like(pixels), output_hidden_states=True).hidden_states[-2]
            conditional.append(projection(identity, clip))
            unconditional.append(projection(torch.zeros_like(identity), zero_clip))
        else:
            conditional.append(projection(identity))
            unconditional.append(projection(torch.zeros_like(identity)))
    tokens = torch.cat(conditional, dim=1)
    if do_classifier_free_guidance:
        tokens = torch.cat([torch.cat(unconditional, dim=1), tokens], dim=0)
    batch, length, _ = tokens.shape
    return tokens.repeat(1, num_images_per_prompt, 1).view(batch * num_images_per_prompt, length, -1)

