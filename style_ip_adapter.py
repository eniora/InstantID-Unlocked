import os
import gc
import shutil

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
}
STYLE_ADAPTER_ENCODER_SUBFOLDER = "models/image_encoder"
STYLE_ADAPTER_ENCODER_FILES = ("config.json", "model.safetensors")

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

    os.makedirs(checkpoints_dir, exist_ok=True)

    repo_filename = STYLE_ADAPTER_REPO_FILENAMES[variant]
    adapter_ckpt_path = os.path.join(checkpoints_dir, os.path.basename(repo_filename))
    if not os.path.exists(adapter_ckpt_path):
        print(f"[style adapter] Downloading {repo_filename} from {STYLE_ADAPTER_REPO_ID}...")
        downloaded = hf_hub_download(repo_id=STYLE_ADAPTER_REPO_ID, filename=repo_filename)
        shutil.copyfile(downloaded, adapter_ckpt_path)

    image_encoder_dir = os.path.join(checkpoints_dir, "image_encoder")
    os.makedirs(image_encoder_dir, exist_ok=True)
    for fname in STYLE_ADAPTER_ENCODER_FILES:
        dest = os.path.join(image_encoder_dir, fname)
        if not os.path.exists(dest):
            repo_path = f"{STYLE_ADAPTER_ENCODER_SUBFOLDER}/{fname}"
            print(f"[style adapter] Downloading {repo_path} from {STYLE_ADAPTER_REPO_ID}...")
            downloaded = hf_hub_download(repo_id=STYLE_ADAPTER_REPO_ID, filename=repo_path)
            shutil.copyfile(downloaded, dest)

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
    if variant not in ("plus", "standard"):
        raise ValueError(f"Unknown style adapter variant: {variant!r}")

    device = pipe.unet.device
    dtype = pipe.unet.dtype

    state = _style_state(pipe)

    style_image_encoder = CLIPVisionModelWithProjection.from_pretrained(image_encoder_path).to(
        device, dtype=dtype
    )
    style_image_encoder.requires_grad_(False)
    style_clip_image_processor = CLIPImageProcessor()

    if variant == "plus":
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

    state_dict = _load_style_checkpoint(model_ckpt)
    image_proj_sd = state_dict["image_proj"] if "image_proj" in state_dict else state_dict
    style_image_proj_model.load_state_dict(image_proj_sd)

    ip_adapter_sd = state_dict["ip_adapter"] if "ip_adapter" in state_dict else state_dict
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
            attn_processor.to(device, dtype=dtype)
        style_layers.append(attn_processor)

    style_layers.load_state_dict(renamed_sd, strict=False)

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

def unload_ip_adapter_style(pipe):
    state = _style_state(pipe)
    if not state.get("loaded", False):
        return

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
    
@torch.no_grad()
def encode_style_image(pipe, style_image, num_images_per_prompt=1, do_classifier_free_guidance=True):
    device = pipe.unet.device
    dtype = pipe.unet.dtype
    state = _style_state(pipe)

    pixel_values = state["clip_image_processor"](images=style_image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device, dtype=dtype)

    if state.get("variant", "plus") == "plus":
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
