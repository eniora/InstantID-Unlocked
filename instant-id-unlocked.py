import sys
sys.path.append("./")

from typing import Tuple

import os
import re
import cv2
import math
import torch
import torch.nn.functional as F
import random
import numpy as np
import gc
import warnings
import threading
import subprocess
import PIL.PngImagePlugin
import time
from safetensors.torch import load_file as load_safetensors_file

warning_messages = [
    ".*timm.models.layers.*",
    ".*timm.models.registry.*",
    ".*Overwriting tiny_vit_.* in registry.*",
    ".*peft_config.*multiple adapters.*",
    ".*rcond.*will change to the default.*",
    ".*MultiControlNetModel.*is deprecated.*",
    ".*`resume_download` is deprecated.*",
    ".*Should have .*<=t1 but got .*",
    ".*unable to parse version details from package URL.*",
    ".*cache-system uses symlinks by default.*",
    ".*The parameter 'pretrained' is deprecated*",
    ".*Arguments other than a weight enum or `None` for 'weights' are deprecated*",
    ".*Already unmerged. Nothing to do.*",
]
for msg in warning_messages:
    warnings.filterwarnings("ignore", message=msg)
import logging
logger = logging.getLogger("transformers.tokenization_utils_base")
logger.addFilter(lambda record: "Token indices sequence length is longer" not in record.getMessage())
logger = logging.getLogger("transformers.modeling_utils")
logger.addFilter(lambda record: "mean_resizing" not in record.getMessage())
logger = logging.getLogger("diffusers.loaders.single_file_utils")
logger.addFilter(lambda record: "text_model.embeddings.position_ids" not in record.getMessage())
logger = logging.getLogger("diffusers.pipelines.pipeline_utils")
logger.addFilter(lambda record: "please unset the `HF_HUB_OFFLINE` environment" not in record.getMessage())
logger.addFilter(lambda record: "requires_aesthetics_score" not in record.getMessage())
logger = logging.getLogger("diffusers.configuration_utils")
logger.addFilter(lambda record: "were passed to LCMScheduler" not in record.getMessage())
logger.addFilter(lambda record: "requires_aesthetics_score" not in record.getMessage())
logger = logging.getLogger("diffusers.schedulers.scheduling_dpmsolver_singlestep")
logger.addFilter(lambda record: "`last_sigmas_type='zero'` is not supported" not in record.getMessage())
logger.addFilter(lambda record: "Please make sure to always use an even number" not in record.getMessage())

os.environ["NO_ALBUMENTATIONS_UPDATE"] = "1"
# os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_CACHE"] = "models"
os.environ["HF_HUB_CACHE_OFFLINE"] = "true"
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
os.environ["GRADIO_DISABLE_TELEMETRY"] = "1"

import psutil
ram_bytes = psutil.virtual_memory().total
ram_gb = ram_bytes / (1024**3)
vram_bytes = torch.cuda.get_device_properties(0).total_memory
vram_gb = vram_bytes / (1024**3)
gpu_name = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU"

original_sdpa = F.scaled_dot_product_attention
try:
    from sageattention import sageattn
    SAGE_SUPPORTED_HEADDIM = {64, 96, 128}
    SAGE_ATTENTION_AVAILABLE = True
    def sdpa_sage(query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None):
        head_dim = query.shape[-1]
        if (
            attn_mask is not None
            or dropout_p > 0.0
            or head_dim not in SAGE_SUPPORTED_HEADDIM
            or query.dtype not in (torch.float16, torch.bfloat16)
        ):
            return original_sdpa(query, key, value, attn_mask=attn_mask,
                                   dropout_p=dropout_p, is_causal=is_causal, scale=scale)
        return sageattn(query, key, value, is_causal=is_causal)
except ImportError:
    SAGE_ATTENTION_AVAILABLE = False
    sdpa_sage = None
def apply_sage_attention(enabled: bool):
    if enabled and SAGE_ATTENTION_AVAILABLE:
        F.scaled_dot_product_attention = sdpa_sage
        torch.nn.functional.scaled_dot_product_attention = sdpa_sage
    else:
        if enabled and not SAGE_ATTENTION_AVAILABLE:
            gr.Warning("SageAttention is not available. Falling back to the default SDPA. See console message for more info.")
            print("\nSageAttention enabled in the UI but wasn't found. You can install it with 'pip install sageattention==1.0.6' and 'pip install triton-windows==3.7.1'. Falling back to the default SDPA.\n")
        F.scaled_dot_product_attention = original_sdpa
        torch.nn.functional.scaled_dot_product_attention = original_sdpa

class GenerationStopped(Exception):
    pass

def open_output_folder():
    path = os.path.abspath("output")
    if sys.platform == "win32":
        os.system(f'start "" "{path}"')
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

import PIL
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

DEFAULT_FILE_PREFIX = "InstantID_"
FILENAME_SAFE_TRANS = str.maketrans('', '', '\\/:*?"<>|')

def save_images(images, output_dir="output", generation_info=None, prefix=DEFAULT_FILE_PREFIX):
    os.makedirs(output_dir, exist_ok=True)

    existing = [f for f in os.listdir(output_dir) if f.startswith(prefix) and f.endswith(".png")]
    used_numbers = [int(f[len(prefix):].split(".")[0]) for f in existing if f[len(prefix):].split(".")[0].isdigit()]
    start_index = max(used_numbers, default=-1) + 1

    paths = []
    for i, img in enumerate(images):
        filename = f"{prefix}{start_index + i}.png"
        path = os.path.join(output_dir, filename)
        img.save(path, pnginfo=generation_info[i] if generation_info else None)
        paths.append(path)
    return paths

cached_controlnet_models = {}

import diffusers
from diffusers.utils import load_image
from diffusers.models import ControlNetModel
from diffusers.pipelines.controlnet.multicontrolnet import MultiControlNetModel
from accelerate.hooks import remove_hook_from_module

from insightface.app import FaceAnalysis

from style_template import styles
from pipeline_stable_diffusion_xl_instantid_full import StableDiffusionXLInstantIDPipeline
from pipeline_stable_diffusion_xl_instantid_img2img import StableDiffusionXLInstantIDImg2ImgPipeline
from model_util import load_models_xl, get_torch_device, torch_gc

from controlnet_aux import OpenposeDetector
from transformers import DPTImageProcessor, DPTForDepthEstimation
device = get_torch_device()
depth_estimator = DPTForDepthEstimation.from_pretrained("Intel/dpt-hybrid-midas").to(device)
feature_extractor = DPTImageProcessor.from_pretrained("Intel/dpt-hybrid-midas")
openpose = OpenposeDetector.from_pretrained("lllyasviel/ControlNet")

def get_depth_map(image):
    image = feature_extractor(images=image, return_tensors="pt").pixel_values.to("cuda")
    with torch.no_grad(), torch.autocast("cuda"):
        depth_map = depth_estimator(image).predicted_depth

    depth_map = torch.nn.functional.interpolate(
        depth_map.unsqueeze(1),
        size=(1024, 1024),
        mode="bicubic",
        align_corners=False,
    )
    depth_min = torch.amin(depth_map, dim=[1, 2, 3], keepdim=True)
    depth_max = torch.amax(depth_map, dim=[1, 2, 3], keepdim=True)
    depth_map = (depth_map - depth_min) / (depth_max - depth_min)
    image = torch.cat([depth_map] * 3, dim=1)

    image = image.permute(0, 2, 3, 1).cpu().numpy()[0]
    image = Image.fromarray((image * 255.0).clip(0, 255).astype(np.uint8))
    return image

def get_canny_image(image, t1=100, t2=200):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    edges = cv2.Canny(image, t1, t2)
    return Image.fromarray(edges).convert("L")

import gradio as gr
import gradio.themes as gr_themes
import json

CUSTOM_THEMES_DIR = os.path.join("models", "Themes")
def load_custom_themes():
    themes = {}
    if os.path.isdir(CUSTOM_THEMES_DIR):
        filenames = [f for f in os.listdir(CUSTOM_THEMES_DIR) if f.endswith(".css")]
        for filename in sorted(filenames, key=str.lower):
            name = os.path.splitext(filename)[0]
            try:
                with open(os.path.join(CUSTOM_THEMES_DIR, filename), "r", encoding="utf-8") as f:
                    themes[name] = f.read()
            except Exception as e:
                print(f"[theme] Skipping '{name}': {e}")
    return themes

def create_theme_dropdown(default_theme="Default Theme"):
    theme_classes = {
        "Default Theme": gr_themes.Default(),
        "Origin": gr_themes.Origin(),
        "Base": gr_themes.Base(),
        "Soft": gr_themes.Soft(),
        "Glass": gr_themes.Glass(),
        "Monochrome": gr_themes.Monochrome(),
        "Citrus": gr_themes.Citrus(),
        "Ocean": gr_themes.Ocean(),
    }
    theme_css_map = {name: theme_classes[name]._get_theme_css() for name in theme_classes}
    theme_css_map.update(load_custom_themes())
    names = list(theme_css_map.keys())
    theme_css_map_json = json.dumps(theme_css_map)
    default_theme_json = json.dumps(default_theme)
    dropdown = gr.Dropdown(
        choices=names,
        value=default_theme,
        label=None,
        show_label=False,
        container=False,
        scale=0,
        min_width=200,
        elem_id="theme_dropdown",
        render=False,
    )
    js = f"""
    (theme) => {{
        const THEME_CSS = {theme_css_map_json};
        let theme_elem = document.querySelector('.gradio-theme-css');
        if (!theme_elem) {{
            theme_elem = document.createElement('style');
            theme_elem.classList.add('gradio-theme-css');
            document.head.appendChild(theme_elem);
        }}
        theme_elem.innerHTML = THEME_CSS[theme] || "";
        try {{ localStorage.setItem('instantid_theme', theme); }} catch (e) {{}}
    }}
    """
    load_js = f"""
    () => {{
        const THEME_CSS = {theme_css_map_json};
        let theme = {default_theme_json};
        try {{
            const saved = localStorage.getItem('instantid_theme');
            if (saved && THEME_CSS[saved]) theme = saved;
        }} catch (e) {{}}
        let theme_elem = document.querySelector('.gradio-theme-css');
        if (!theme_elem) {{
            theme_elem = document.createElement('style');
            theme_elem.classList.add('gradio-theme-css');
            document.head.appendChild(theme_elem);
        }}
        theme_elem.innerHTML = THEME_CSS[theme] || "";
        return theme;
    }}
    """
    return dropdown, js, load_js

import starlette.responses as _starlette_responses
_orig_set_stat_headers = _starlette_responses.FileResponse.set_stat_headers
def _set_stat_headers_no_content_length(self, stat_result):
    _orig_set_stat_headers(self, stat_result)
    try:
        del self.headers["content-length"]
    except KeyError:
        pass
_starlette_responses.FileResponse.set_stat_headers = _set_stat_headers_no_content_length

MAX_SEED = 2**53 - 1
MAX_SEED_RAND = np.iinfo(np.uint32).max - 1
dtype = torch.float16 if str(device).__contains__("cuda") else torch.float32
STYLE_NAMES = list(styles.keys())
DEFAULT_STYLE_NAME = "(No style)"

def get_random_style_prompt(prompt_substitute="person"):
    available_styles = [s for s in STYLE_NAMES if s != DEFAULT_STYLE_NAME]
    if not available_styles:
        return "", DEFAULT_NEGATIVE_PROFILE, DEFAULT_STYLE_NAME
    selected_style = random.choice(available_styles)
    print(f"Inserted random style: {selected_style}")
    style_prompt, style_neg_prompt = styles[selected_style]
    replacement = " " if prompt_substitute == "Empty (none)" else prompt_substitute
    random_prompt = style_prompt.replace("{prompt}", replacement).strip()
    return random_prompt, style_neg_prompt, DEFAULT_STYLE_NAME

def apply_selected_style(style_name, prompt_substitute="person"):
    if style_name == "(No style)":
        return gr.update(), gr.update(), gr.update()
    print(f"Inserted selected style: {style_name}")
    style_prompt, style_neg_prompt = styles[style_name]
    replacement = " " if prompt_substitute == "Empty (none)" else prompt_substitute
    return (
        style_prompt.replace("{prompt}", replacement).strip(),
        style_neg_prompt,
        "(No style)"
    )

NEGATIVE_PROMPT_PRESETS = {
    "Default Negative Profile": "lowres, low quality, worst quality, text, watermark, frame, deformed",
    "Aggressive Negative Profile (InstantID default)": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    "Negative Profile 1 (Minimalist)": "(worst quality, low quality:1.2), deformed, blurry, mutated, extra limbs",
    "Negative Profile 2 (Portraits)": "(worst quality:1.3), (low quality:1.2), bad anatomy, deformed, disfigured, fused fingers, missing fingers, extra limbs, poorly drawn face, poorly drawn hands, blurry",
    "Negative Profile 3 (SDXL default)": "(worst quality, low quality:1.3), watermark, signature, text, frame, jpeg artifacts, blurry, deformed, extra limbs, bad hands, fused fingers, poorly drawn face",
    "Negative Profile 4 (Realism)": "(worst quality, low quality:1.3), anime, cartoon, illustration, cgi, 3d render, painting, drawing, deformed, extra fingers, fused fingers, blurry, unrealistic",
    "Negative Profile 5 (Stylized / Illustration)": "(worst quality:1.3), bad anatomy, deformed eyes, bad hands, long neck, lowres, jpeg artifacts, text, watermark, extra fingers",
    "Negative Profile 6 (Digital Illustration)": "(worst quality, low quality:1.3), bad anatomy, blurry, duplicate, signature, watermark, jpeg artifacts",
    "Negative Profile 7 (Anime)": "(worst quality:1.2), photorealistic, real life, realistic skin, 3d render, painting, extra limbs, fused fingers, bad anatomy, blurry, text, watermark",
    "Negative Profile 8 (Ultra Minimal)": "low quality, deformed",
    "Negative Profile 9 (3D Render)": "photo, photorealistic, realistic, painting, sketch, drawing, anime, cartoon, 2d, flat color, low detail, text, watermark, blurry",
    "Negative Profile 10 (Plastic Toy Render)": "photo, illustration, sketch, painting, anime, blurry, lowres, noisy, realistic skin, lifelike eyes, textureless",
    "Negative Profile 11 (Game Character (Stylized 3D))": "photo, painting, sketch, drawing, anime, real skin texture, flat shading, realistic proportions, soft shadows, photorealistic",
    "Negative Profile 12 (Sculpted Statue Render)": "cartoon, photo, realism, painterly, anime, soft brush, flat colors, 2d, smooth shading",
    "Negative Profile 13 (Low Poly Stylized)": "realism, photo, anime, high detail, highres, 2d, blurry, smooth shading, overrendered, soft shadows",
    "Negative Profile 14 (Fooocus Enhance)": "(worst quality, low quality, normal quality, lowres, low details, oversaturated, undersaturated, overexposed, underexposed, grayscale, bw, bad photo, bad photography, bad art:1.4), (watermark, signature, text font, username, error, logo, words, letters, digits, autograph, trademark, name:1.2), (blur, blurry, grainy), morbid, ugly, asymmetrical, mutated malformed, mutilated, poorly lit, bad shadow, draft, cropped, out of frame, cut off, censored, jpeg artifacts, out of focus, glitch, duplicate, (airbrushed, cartoon, anime, semi-realistic, cgi, render, blender, digital art, manga, amateur:1.3), (3D ,3D Game, 3D Game Scene, 3D Character:1.1), (bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3)",
    "Negative Profile 15 (Fooocus Negative)": "deformed, bad anatomy, disfigured, poorly drawn face, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, disconnected head, malformed hands, long neck, mutated hands and fingers, bad hands, missing fingers, cropped, worst quality, low quality, mutation, poorly drawn, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, missing fingers, fused fingers, abnormal eye proportion, Abnormal hands, abnormal legs, abnormal feet, abnormal fingers, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch",
}

DEFAULT_NEGATIVE_PROFILE = NEGATIVE_PROMPT_PRESETS["Default Negative Profile"]

def on_style_change(style_name):
    if style_name == "(No style)":
        return gr.update(), gr.update()
    else:
        print(f"Manual style selection: {style_name}")
        return gr.update(value=""), gr.update(value="")

EXCLUDED_MODELS = {
    "diffusers/controlnet-canny-sdxl-1.0",
    "diffusers/controlnet-depth-sdxl-1.0-small",
    "Intel/dpt-hybrid-midas",
    "lllyasviel/Annotators",
    "lllyasviel/ControlNet",
    "xinsir/controlnet-openpose-sdxl-1.0",
    "stabilityai/stable-diffusion-xl-base-1.0"
}
EXCLUDED_MODELS_LOWER = {m.lower() for m in EXCLUDED_MODELS}
SAFETENSORS_CHECKPOINTS_DIR = "models"

def get_available_safetensors_checkpoints():
    if not os.path.exists(SAFETENSORS_CHECKPOINTS_DIR):
        return []
    checkpoint_files = []
    for file in sorted(os.listdir(SAFETENSORS_CHECKPOINTS_DIR)):
        if file.lower().endswith((".safetensors", ".ckpt")):
            checkpoint_files.append(
                os.path.join(SAFETENSORS_CHECKPOINTS_DIR, file).replace("\\", "/")
            )
    return checkpoint_files

def get_available_models():
    models_dir = "models"
    model_folders = []
    if os.path.exists(models_dir):
        for folder in os.listdir(models_dir):
            if folder.startswith("models--"):
                model_name = folder.replace("models--", "").replace("--", "/")
                if model_name.lower() in EXCLUDED_MODELS_LOWER:
                    continue
                model_folders.append(model_name)
    model_folders.extend(get_available_safetensors_checkpoints())
    return model_folders

AVAILABLE_MODELS = get_available_models()
DEFAULT_MODEL = "eniora/Juggernaut_XL_Ragnarok"

DET_SIZE_OPTIONS = {
    "160x160": (160, 160),
    "320x320": (320, 320),
    "640x640 (default)": (640, 640),
    "800x800": (800, 800),
    "1024x1024": (1024, 1024),
    "1280x1280": (1280, 1280),
    "2560x2560": (2560, 2560)
}

current_det_size = (640, 640)
app = FaceAnalysis(
    name="antelopev2",
    root="./",
    providers=["CPUExecutionProvider"],
)
app.prepare(ctx_id=0, det_size=current_det_size)

def read_png_metadata(filepath):
    if filepath is None:
        return "No image selected"

    try:
        with Image.open(filepath) as img:
            metadata = img.info
            if "Generation Parameters" in metadata:
                return metadata["Generation Parameters"]
            return "No generation metadata found in this image file."
    except Exception as e:
        return f"Error reading metadata: {str(e)}"

face_adapter = f"./checkpoints/ip-adapter.bin"
controlnet_path = f"./checkpoints/ControlNetModel"

controlnet_identitynet = ControlNetModel.from_pretrained(
    controlnet_path, torch_dtype=dtype
)

controlnet_pose_model = "xinsir/controlnet-openpose-sdxl-1.0"
controlnet_canny_model = "diffusers/controlnet-canny-sdxl-1.0"
controlnet_depth_model = "diffusers/controlnet-depth-sdxl-1.0-small"

controlnet_model_paths = {
    "pose": controlnet_pose_model,
    "canny": controlnet_canny_model,
    "depth": controlnet_depth_model,
}
controlnet_map_fn = {
    "pose": openpose,
    "canny": get_canny_image,
    "depth": get_depth_map,
}

def get_available_loras():
    loras_dir = "./models/Loras"
    if not os.path.exists(loras_dir):
        return []
    
    lora_files = []
    for file in os.listdir(loras_dir):
        if file.endswith(('.safetensors', '.ckpt', '.pt')):
            lora_files.append(file)
    return lora_files

UPSCALERS_DIR = "./models/Upscalers"
DEFAULT_UPSCALER = "4x_NMKD-Superscale-SP_178000_G.pth"

def get_available_upscalers():
    if not os.path.exists(UPSCALERS_DIR):
        return []
    upscaler_files = []
    for file in os.listdir(UPSCALERS_DIR):
        if file.lower().endswith(('.pth', '.safetensors', '.pt')):
            upscaler_files.append(file)
    return sorted(upscaler_files)

_upscaler_model_cache = {}

def load_upscaler_model(upscaler_name):
    if upscaler_name in _upscaler_model_cache:
        return _upscaler_model_cache[upscaler_name]
    upscaler_path = os.path.join(UPSCALERS_DIR, upscaler_name)
    if not os.path.exists(upscaler_path):
        raise gr.Error(f"Upscaler model not found at {upscaler_path}")
    try:
        from spandrel import ModelLoader, UnsupportedDtypeError
    except ImportError:
        raise gr.Error(
            "The 'spandrel' package is required for Hires Fix upscaling. "
            "Install it with: pip install spandrel"
        )
    model = ModelLoader().load_from_file(upscaler_path)
    model = model.to(device)
    try:
        model = model.to(dtype=torch.float16)
    except UnsupportedDtypeError as e:
        print(f"Upscaler '{upscaler_name}' does not support fp16 ({e}); falling back to fp32 for this model.\n")
        model = model.to(dtype=torch.float32)
    model.eval()
    _upscaler_model_cache[upscaler_name] = model
    return model

def _tile_starts(total, tile, stride):
    if total <= tile:
        return [0]
    starts = list(range(0, total - tile + 1, stride))
    if not starts or starts[-1] != total - tile:
        starts.append(total - tile)
    return starts

@torch.no_grad()
def run_upscaler_model(model, image, tile_size=512, tile_overlap=32):
    model_dtype = model.dtype
    img = np.array(image.convert("RGB")).astype(np.float32) / 255.0
    img_tensor = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).to(device=device, dtype=model_dtype)
    scale = getattr(model, "scale", None) or 4
    _, _, h, w = img_tensor.shape
    stride = max(tile_size - tile_overlap, 1)
    if h <= tile_size and w <= tile_size:
        output = model(img_tensor)
    else:
        output = torch.zeros((1, 3, h * scale, w * scale), device=device, dtype=model_dtype)
        weight = torch.zeros_like(output)
        for y in _tile_starts(h, tile_size, stride):
            for x in _tile_starts(w, tile_size, stride):
                tile = img_tensor[:, :, y:y + tile_size, x:x + tile_size]
                tile_out = model(tile)
                oy, ox = y * scale, x * scale
                oh, ow = tile_out.shape[2], tile_out.shape[3]
                output[:, :, oy:oy + oh, ox:ox + ow] += tile_out
                weight[:, :, oy:oy + oh, ox:ox + ow] += 1.0
        output = output / weight.clamp(min=1e-8)
    output = output.clamp(0, 1).float().squeeze(0).permute(1, 2, 0).cpu().numpy()
    return Image.fromarray((output * 255.0).round().astype(np.uint8))

def prescale_for_upscaler_model(source_image, target_w, target_h, model_scale, headroom=1.30, min_dim=8):
    src_w, src_h = source_image.size
    needed_scale = max(target_w / src_w, target_h / src_h) * headroom
    prescale = min(needed_scale / model_scale, 1.0)
    if prescale >= 0.999:
        return source_image
    new_w = max(min_dim, int(round(src_w * prescale)))
    new_h = max(min_dim, int(round(src_h * prescale)))
    if new_w == src_w and new_h == src_h:
        return source_image
    return source_image.resize((new_w, new_h), PIL.Image.LANCZOS)

GFPGAN_DIR = "./models/GFPGAN"
GFPGAN_MODEL_NAME = "GFPGANv1.4.pth"
GFPGAN_MODEL_URL = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth"

_gfpgan_model_cache = {}

def _patch_basicsr_torchvision_compat():
    import importlib
    try:
        importlib.import_module("torchvision.transforms.functional_tensor")
        return
    except ModuleNotFoundError:
        pass
    import types
    import torchvision.transforms.functional as _tv_functional
    shim = types.ModuleType("torchvision.transforms.functional_tensor")
    shim.rgb_to_grayscale = _tv_functional.rgb_to_grayscale
    sys.modules["torchvision.transforms.functional_tensor"] = shim

def _patch_facexlib_weights_dir():
    import importlib
    try:
        import facexlib.utils.misc as _facexlib_misc
    except ImportError:
        return

    if getattr(_facexlib_misc.load_file_from_url, "_instantid_patched", False):
        return

    _original_load_file_from_url = _facexlib_misc.load_file_from_url

    def _patched_load_file_from_url(*args, **kwargs):
        kwargs["model_dir"] = GFPGAN_DIR
        kwargs["save_dir"] = GFPGAN_DIR
        return _original_load_file_from_url(*args, **kwargs)
    _patched_load_file_from_url._instantid_patched = True

    _facexlib_misc.load_file_from_url = _patched_load_file_from_url
    for _mod_name in ("facexlib.detection", "facexlib.parsing", "facexlib.utils"):
        try:
            _mod = importlib.import_module(_mod_name)
            if hasattr(_mod, "load_file_from_url"):
                _mod.load_file_from_url = _patched_load_file_from_url
        except ImportError:
            pass

def load_gfpgan_model(upscale=1):
    cache_key = upscale
    if cache_key in _gfpgan_model_cache:
        return _gfpgan_model_cache[cache_key]

    _patch_basicsr_torchvision_compat()
    try:
        from gfpgan.utils import GFPGANer
    except ImportError:
        raise gr.Error(
            "The 'gfpgan' package is required for face restoration. "
            "Install it with: pip install gfpgan"
        )
    _patch_facexlib_weights_dir()
    from basicsr.utils.download_util import load_file_from_url

    os.makedirs(GFPGAN_DIR, exist_ok=True)
    model_path = os.path.join(GFPGAN_DIR, GFPGAN_MODEL_NAME)
    if not os.path.isfile(model_path):
        print(f"\nGFPGAN model not found, downloading to {GFPGAN_DIR}...\n")
        model_path = load_file_from_url(
            url=GFPGAN_MODEL_URL,
            model_dir=GFPGAN_DIR,
            progress=True,
            file_name=GFPGAN_MODEL_NAME,
        )

    restorer = GFPGANer(
        model_path=model_path,
        upscale=upscale,
        arch="clean",
        channel_multiplier=2,
        bg_upsampler=None,
        device=device,
    )
    _gfpgan_model_cache[cache_key] = restorer
    return restorer

def unload_gfpgan_model():
    for restorer in list(_gfpgan_model_cache.values()):
        try:
            if hasattr(restorer, "gfpgan"):
                del restorer.gfpgan
            face_helper = getattr(restorer, "face_helper", None)
            if face_helper is not None:
                if hasattr(face_helper, "face_det"):
                    del face_helper.face_det
                if hasattr(face_helper, "face_parse"):
                    del face_helper.face_parse
        except Exception:
            pass
    _gfpgan_model_cache.clear()
    gc.collect()
    torch.cuda.empty_cache()

@torch.no_grad()
def restore_faces_gfpgan(pil_image, weight=0.5):
    try:
        restorer = load_gfpgan_model(upscale=1)
        img_bgr = cv2.cvtColor(np.array(pil_image.convert("RGB")), cv2.COLOR_RGB2BGR)
        _, _, restored_img = restorer.enhance(
            img_bgr,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=weight,
        )
        if restored_img.shape != img_bgr.shape:
            img_bgr = cv2.resize(img_bgr, (restored_img.shape[1], restored_img.shape[0]))
        blended = cv2.addWeighted(restored_img, weight, img_bgr, 1 - weight, 0)
        return Image.fromarray(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
    finally:
        unload_gfpgan_model()

@torch.no_grad()
def encode_image_to_latents(vae_pipe, pil_image, generator=None):
    vae = vae_pipe.vae
    image_processor = vae_pipe.image_processor
    exec_device = getattr(vae_pipe, "_execution_device", None) or vae.device

    image_tensor = image_processor.preprocess(pil_image).to(device=exec_device, dtype=torch.float32)

    latents_mean = latents_std = None
    if hasattr(vae.config, "latents_mean") and vae.config.latents_mean is not None:
        latents_mean = torch.tensor(vae.config.latents_mean).view(1, 4, 1, 1)
    if hasattr(vae.config, "latents_std") and vae.config.latents_std is not None:
        latents_std = torch.tensor(vae.config.latents_std).view(1, 4, 1, 1)

    needs_upcasting = vae.dtype == torch.float16 and bool(getattr(vae.config, "force_upcast", False))
    original_vae_dtype = vae.dtype
    try:
        if needs_upcasting:
            image_tensor = image_tensor.float()
            vae.to(dtype=torch.float32)

        latents = vae.encode(image_tensor).latent_dist.sample(generator=generator)
    finally:
        if needs_upcasting:
            vae.to(dtype=original_vae_dtype)
    latents = latents.to(original_vae_dtype)

    if latents_mean is not None and latents_std is not None:
        latents_mean = latents_mean.to(device=exec_device, dtype=original_vae_dtype)
        latents_std = latents_std.to(device=exec_device, dtype=original_vae_dtype)
        latents = (latents - latents_mean) * vae.config.scaling_factor / latents_std
    else:
        latents = vae.config.scaling_factor * latents

    return latents

def latent_space_upscale(latents, target_pixel_height, target_pixel_width, mode="bicubic", antialias=True):
    target_h = max(1, round(target_pixel_height / 8))
    target_w = max(1, round(target_pixel_width / 8))
    kwargs = {"mode": mode}
    if mode in ("bicubic", "bilinear"):
        kwargs["align_corners"] = False
        kwargs["antialias"] = antialias
    return F.interpolate(latents, size=(target_h, target_w), **kwargs)

EMBEDDINGS_DIR = "./models/Embeddings"

def get_available_embeddings():
    if not os.path.exists(EMBEDDINGS_DIR):
        return []

    embedding_files = []
    for file in os.listdir(EMBEDDINGS_DIR):
        if file.lower().endswith(('.safetensors', '.pt', '.bin')):
            embedding_files.append(file)
    return embedding_files

def embedding_token_from_filename(filename):
    stem = os.path.splitext(filename)[0]
    token = re.sub(r'[^A-Za-z0-9_]+', '_', stem).strip('_')
    token = token if token else stem
    return f"<{token}>"

def get_embedding_choices():
    embeddings = get_available_embeddings()
    if not embeddings:
        return []
    return [(f"{file} → {embedding_token_from_filename(file)}", embedding_token_from_filename(file))
            for file in embeddings]

def insert_token_into_text(current_text, token, weight=1.0):
    if not token:
        return gr.update()
    try:
        weight = float(weight)
    except (TypeError, ValueError):
        weight = 1.0
    insertion = f"({token}:{weight:.1f})"
    current_text = current_text or ""
    stripped = current_text.strip()
    if not stripped:
        return insertion
    if stripped.endswith(","):
        return f"{stripped} {insertion}"
    return f"{stripped}, {insertion}"

def update_det_size(det_size_name):
    global app, current_det_size
    
    new_size = DET_SIZE_OPTIONS[det_size_name]
    if new_size != current_det_size:
        current_det_size = new_size
        app = FaceAnalysis(
            name="antelopev2",
            root="./",
            providers=["CPUExecutionProvider"],
        )
        app.prepare(ctx_id=0, det_size=current_det_size)
    
    return f"Detection size set to {current_det_size}"

def main(pretrained_model_name_or_path="eniora/Juggernaut_XL_Ragnarok"):
    stop_event = threading.Event()
    embedding_state = {"loaded": False, "tokens": []}
    lora_state = {"signature": None, "adapter_ids": {}}
    hires_sibling_pipe = None

    def request_stop():
        stop_event.set()
        gr.Info("A request to stop all currently running tasks has been initiated. Generation will stop when the current task or step has finished processing.")

    if vram_gb >= 15 or ram_gb <= 30:
        pipe = None

    else:
        if pretrained_model_name_or_path.endswith(
            ".ckpt"
        ) or pretrained_model_name_or_path.endswith(".safetensors"):
            (tokenizers, text_encoders, unet, scheduler_kwargs, vae) = load_models_xl(
                pretrained_model_name_or_path=pretrained_model_name_or_path,
                scheduler_name=None,
                weight_dtype=dtype,
            )

            scheduler = diffusers.DPMSolverMultistepScheduler.from_config(scheduler_kwargs)
            pipe = StableDiffusionXLInstantIDPipeline(
                vae=vae,
                text_encoder=text_encoders[0],
                text_encoder_2=text_encoders[1],
                tokenizer=tokenizers[0],
                tokenizer_2=tokenizers[1],
                unet=unet,
                scheduler=scheduler,
                controlnet=[controlnet_identitynet],
            ).to(device)

        else:
            pipe = StableDiffusionXLInstantIDPipeline.from_pretrained(
                pretrained_model_name_or_path,
                controlnet=[controlnet_identitynet],
                torch_dtype=dtype,
                feature_extractor=None,
            ).to(device)

            pipe.scheduler = diffusers.DPMSolverMultistepScheduler.from_config(
                pipe.scheduler.config
            )

    print(f"\nDetected GPU: {gpu_name} with {vram_gb:.2f} GB VRAM | Detected total system memory: {ram_gb:.2f} GB of RAM\n")

    def load_and_cache_controlnet_model(controlnet_type):
        if controlnet_type not in cached_controlnet_models:
            print(f"Loading ControlNet model: {controlnet_type}")
            model = ControlNetModel.from_pretrained(controlnet_model_paths[controlnet_type], torch_dtype=dtype).to(device)
            cached_controlnet_models[controlnet_type] = model
        return cached_controlnet_models[controlnet_type]

    def toggle_lora_ui(enable_lora_checkbox):
        return [gr.update(visible=enable_lora_checkbox)] * len(LORA_OUTPUTS)

    def toggle_embeddings_ui(enable_embeddings_checkbox):
        return [gr.update(visible=enable_embeddings_checkbox)] * len(EMBEDDINGS_OUTPUTS)

    def get_embedding_vector_dim(state_dict):
        if not isinstance(state_dict, dict):
            return None
        if "string_to_param" in state_dict:
            try:
                tensor = list(state_dict["string_to_param"].values())[0]
                return int(tensor.shape[-1])
            except Exception:
                return None
        for v in state_dict.values():
            if torch.is_tensor(v):
                return int(v.shape[-1])
        return None

    def load_all_embeddings(pipe, required_tokens=None):
        print("\nLoading embeddings found in prompt/negative prompt boxes...")
        loaded_tokens = []
        embedding_files = get_available_embeddings()

        if required_tokens is not None:
            required_lower = {t.lower() for t in required_tokens}
            embedding_files = [
                f for f in embedding_files
                if embedding_token_from_filename(f).lower() in required_lower
            ]

        dual_state_dicts, dual_tokens = [], []
        single_state_dicts, single_tokens = [], []

        for emb_file in embedding_files:
            token = embedding_token_from_filename(emb_file)
            emb_path = os.path.join(EMBEDDINGS_DIR, emb_file)

            try:
                if emb_file.lower().endswith(".safetensors"):
                    state_dict = load_safetensors_file(emb_path)
                else:
                    state_dict = torch.load(emb_path, map_location="cpu")
            except Exception as e:
                print(f"Failed to read embedding {emb_file}: {e}")
                gr.Warning(f"Failed to load embedding '{emb_file}': {e}")
                continue

            if isinstance(state_dict, dict) and "clip_g" in state_dict and "clip_l" in state_dict:
                dual_state_dicts.append(state_dict)
                dual_tokens.append(token)
                continue

            dim = get_embedding_vector_dim(state_dict)
            if dim == 768:
                print(f"Skipping embedding '{emb_file}': looks like an SD1.5-only embedding "
                      f"(single 768-dim vector), which isn't compatible with this SDXL pipeline.")
                continue

            single_state_dicts.append(state_dict)
            single_tokens.append(token)

        if dual_state_dicts:
            try:
                pipe.load_textual_inversion(
                    [sd["clip_g"] for sd in dual_state_dicts], token=list(dual_tokens),
                    text_encoder=pipe.text_encoder_2, tokenizer=pipe.tokenizer_2,
                )
                pipe.load_textual_inversion(
                    [sd["clip_l"] for sd in dual_state_dicts], token=list(dual_tokens),
                    text_encoder=pipe.text_encoder, tokenizer=pipe.tokenizer,
                )
                loaded_tokens.extend(dual_tokens)
            except Exception as e:
                print(f"Batched dual-encoder load failed ({e}), falling back to per-file loading")
                for sd, token in zip(dual_state_dicts, dual_tokens):
                    try:
                        pipe.load_textual_inversion(
                            sd["clip_g"], token=token,
                            text_encoder=pipe.text_encoder_2, tokenizer=pipe.tokenizer_2,
                        )
                        pipe.load_textual_inversion(
                            sd["clip_l"], token=token,
                            text_encoder=pipe.text_encoder, tokenizer=pipe.tokenizer,
                        )
                        loaded_tokens.append(token)
                    except Exception as e2:
                        print(f"Failed to load embedding for token {token}: {e2}.")
                        gr.Warning(f"Failed to load embedding '{token}': {e2}.")

        if single_state_dicts:
            try:
                pipe.load_textual_inversion(single_state_dicts, token=list(single_tokens))
                loaded_tokens.extend(single_tokens)
                print(f"Loaded {len(single_tokens)} single-encoder embedding(s): {', '.join(single_tokens)}")
            except Exception as e:
                print(f"Batched single-encoder load failed ({e}), falling back to per-file loading")
                for sd, token in zip(single_state_dicts, single_tokens):
                    try:
                        pipe.load_textual_inversion(sd, token=token)
                        loaded_tokens.append(token)
                    except Exception as e2:
                        print(f"Failed to load embedding for token {token}: {e2}")
                        gr.Warning(f"Failed to load embedding '{token}': {e2}")

        return loaded_tokens

    def randomize_seed_fn(seed: int, randomize_seed: bool) -> int:
        if randomize_seed:
            seed = random.randint(0, MAX_SEED_RAND)
        return seed

    def convert_from_cv2_to_image(img: np.ndarray) -> Image:
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    def convert_from_image_to_cv2(img: Image) -> np.ndarray:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    def draw_kps(
        image_pil,
        kps,
        kps_brightness=0.6,
        color_list=[
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
        ],
    ):
        stickwidth = 4
        limbSeq = np.array([[0, 2], [1, 2], [3, 2], [4, 2]])
        kps = np.array(kps)

        w, h = image_pil.size
        out_img = np.zeros([h, w, 3])

        for i in range(len(limbSeq)):
            index = limbSeq[i]
            color = color_list[index[0]]

            x = kps[index][:, 0]
            y = kps[index][:, 1]
            length = ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5
            angle = math.degrees(math.atan2(y[0] - y[1], x[0] - x[1]))
            polygon = cv2.ellipse2Poly(
                (int(np.mean(x)), int(np.mean(y))),
                (int(length / 2), stickwidth),
                int(angle),
                0,
                360,
                1,
            )
            out_img = cv2.fillConvexPoly(out_img.copy(), polygon, color)
        out_img = (out_img * kps_brightness).astype(np.uint8)

        for idx_kp, kp in enumerate(kps):
            color = color_list[idx_kp]
            x, y = kp
            out_img = cv2.circle(out_img.copy(), (int(x), int(y)), 10, color, -1)

        out_img_pil = Image.fromarray(out_img.astype(np.uint8))
        return out_img_pil

    def resize_img(
        input_image,
        max_side=1280,
        min_side=1024,
        size=None,
        pad_to_max_side=False,
        mode=PIL.Image.LANCZOS,
        base_pixel_number=8,
    ):
        w, h = input_image.size
        if size is not None:
            w_resize_new, h_resize_new = size
        elif base_pixel_number == 64:
            ratio = min_side / min(h, w)
            w, h = round(ratio * w), round(ratio * h)
            ratio = max_side / max(h, w)
            input_image = input_image.resize([round(ratio * w), round(ratio * h)], mode)
            w_resize_new = (round(ratio * w) // base_pixel_number) * base_pixel_number
            h_resize_new = (round(ratio * h) // base_pixel_number) * base_pixel_number
        else:
            ratio = max_side / max(w, h)
            w_scaled = w * ratio
            h_scaled = h * ratio

            if w >= h:
                w_resize_new = (round(w_scaled) // base_pixel_number) * base_pixel_number
                aspect_ratio = h / w
                h_resize_new = int(round(w_resize_new * aspect_ratio / base_pixel_number) * base_pixel_number)
            else:
                h_resize_new = (round(h_scaled) // base_pixel_number) * base_pixel_number
                aspect_ratio = w / h
                w_resize_new = int(round(h_resize_new * aspect_ratio / base_pixel_number) * base_pixel_number)

            w_resize_new = max(w_resize_new, base_pixel_number)
            h_resize_new = max(h_resize_new, base_pixel_number)

        input_image = input_image.resize([w_resize_new, h_resize_new], mode)

        if pad_to_max_side and size is None:
            res = np.ones([max_side, max_side, 3], dtype=np.uint8) * 255
            offset_x = (max_side - w_resize_new) // 2
            offset_y = (max_side - h_resize_new) // 2
            res[
                offset_y : offset_y + h_resize_new, offset_x : offset_x + w_resize_new
            ] = np.array(input_image)
            input_image = Image.fromarray(res)
        return input_image

    def fit_image_to_canvas(input_image, target_size, mode=PIL.Image.LANCZOS, pad_to_max_side=False):
        target_w, target_h = target_size
        input_image = input_image.convert("RGB")
        if not pad_to_max_side:
            return input_image.resize((target_w, target_h), mode)
        src_w, src_h = input_image.size
        if src_w == target_w and src_h == target_h:
            return input_image
        scale = min(target_w / src_w, target_h / src_h)
        new_w = max(1, round(src_w * scale))
        new_h = max(1, round(src_h * scale))
        resized = input_image.resize((new_w, new_h), mode)
        canvas = np.full((target_h, target_w, 3), 255, dtype=np.uint8)
        offset_x = (target_w - new_w) // 2
        offset_y = (target_h - new_h) // 2
        canvas[offset_y: offset_y + new_h, offset_x: offset_x + new_w] = np.array(resized)

        return Image.fromarray(canvas)

    def resize_control_images(control_images, size):
        if control_images is None:
            return control_images
        if isinstance(control_images, list):
            return [img.resize(size, PIL.Image.LANCZOS) if hasattr(img, "resize") else img for img in control_images]
        return control_images.resize(size, PIL.Image.LANCZOS) if hasattr(control_images, "resize") else control_images

    def _remap_face_info(face_info_list, scale_x, scale_y):
        remapped = []
        for fi in face_info_list:
            fi = dict(fi)
            fi["kps"] = np.array(fi["kps"], dtype=np.float32).copy()
            fi["kps"][:, 0] *= scale_x
            fi["kps"][:, 1] *= scale_y
            fi["bbox"] = np.array(fi["bbox"], dtype=np.float32).copy()
            fi["bbox"][0] *= scale_x
            fi["bbox"][1] *= scale_y
            fi["bbox"][2] *= scale_x
            fi["bbox"][3] *= scale_y
            remapped.append(fi)
        return remapped

    def detect_face_info(
        original_image,
        canvas_image,
        canvas_cv2,
        resize_mode_enum,
        enable_custom_resize,
        label="image",
        need_kps=True,
        temp_app=None,
    ):
        canvas_w, canvas_h = canvas_image.size
        face_info = []
        fallback_detect_image = None
        fallback_detect_cv2 = None

        if enable_custom_resize:
            fallback_detect_image = resize_img(
                original_image,
                size=None,
                max_side=1280,
                mode=resize_mode_enum,
                pad_to_max_side=False,
                base_pixel_number=8,
            )
            fallback_detect_cv2 = convert_from_image_to_cv2(fallback_detect_image)
            face_info = app.get(fallback_detect_cv2)
            if len(face_info) > 0 and need_kps:
                det_w, det_h = fallback_detect_image.size
                scale_x, scale_y = canvas_w / det_w, canvas_h / det_h
                face_info = _remap_face_info(face_info, scale_x, scale_y)

        if len(face_info) == 0:
            if enable_custom_resize:
                print(f"\nYour custom resolution possibly stretched {label} and no face was found on the aspect-preserving resize either. Retrying detection directly on the custom-resized image...\n")
            face_info = app.get(canvas_cv2)

        if len(face_info) == 0 and current_det_size >= (640, 640):
            print(f"\nNo face detected at the current detection size ({current_det_size[0]}x{current_det_size[1]}) for {label}. Temporarily retrying at 320x320...\n")
            if temp_app is None:
                temp_app = FaceAnalysis(
                    name="antelopev2",
                    root="./",
                    providers=["CPUExecutionProvider"],
                )
                temp_app.prepare(ctx_id=0, det_size=(320, 320))
            if enable_custom_resize and fallback_detect_cv2 is not None:
                fallback_face_info = temp_app.get(fallback_detect_cv2)
                if len(fallback_face_info) > 0:
                    if need_kps:
                        det_w, det_h = fallback_detect_image.size
                        scale_x, scale_y = canvas_w / det_w, canvas_h / det_h
                        face_info = _remap_face_info(fallback_face_info, scale_x, scale_y)
                    else:
                        face_info = fallback_face_info
            if len(face_info) == 0:
                face_info = temp_app.get(canvas_cv2)

        return face_info, temp_app

    def get_sibling_pipe(base_pipe, target_class):
        if isinstance(base_pipe, target_class):
            return base_pipe

        cached = getattr(base_pipe, "_sibling_pipe", None)
        if cached is not None and isinstance(cached, target_class):
            return cached

        try:
            sibling_pipe = target_class(**base_pipe.components)
            if not hasattr(base_pipe.unet, "_hf_hook"):
                sibling_pipe = sibling_pipe.to(device)
            sibling_pipe.image_proj_model = base_pipe.image_proj_model
            sibling_pipe.image_proj_model_in_features = base_pipe.image_proj_model_in_features
            sibling_pipe._current_model = getattr(base_pipe, "_current_model", None)
        except Exception as e:
            print(f"Could not build a lightweight sibling pipeline ({e}); "
                  f"falling back to a full reload instead.")
            sibling_pipe = load_model_and_update_pipe(
                getattr(base_pipe, "_current_model", DEFAULT_MODEL),
                target_class is StableDiffusionXLInstantIDImg2ImgPipeline,
            )
            lora_state["signature"] = None

        sibling_pipe._sibling_pipe = base_pipe
        base_pipe._sibling_pipe = sibling_pipe
        return sibling_pipe

    def get_img2img_sibling_pipe(base_pipe):
        nonlocal hires_sibling_pipe
        hires_sibling_pipe = get_sibling_pipe(base_pipe, StableDiffusionXLInstantIDImg2ImgPipeline)
        return hires_sibling_pipe

    def apply_style(
        style_name: str, positive: str, negative: str = ""
    ) -> Tuple[str, str]:
        p, n = styles.get(style_name, styles[DEFAULT_STYLE_NAME])
        if style_name != DEFAULT_STYLE_NAME and negative:
            return p.replace("{prompt}", positive), n + ", " + negative
        else:
            return p.replace("{prompt}", positive), n + negative

    def load_model_and_update_pipe(model_name, enable_img2img):
        nonlocal pipe
        global controlnet_identitynet
        if (vram_gb >= 15 or ram_gb <= 30) and pipe is not None:
            del pipe
            gc.collect()
            torch.cuda.empty_cache()

        if controlnet_identitynet is None:
            controlnet_identitynet = ControlNetModel.from_pretrained(
                controlnet_path, torch_dtype=dtype
            )

        PipeClass = StableDiffusionXLInstantIDImg2ImgPipeline if enable_img2img else StableDiffusionXLInstantIDPipeline

        if model_name.endswith((".ckpt", ".safetensors")):
            tokenizers, text_encoders, unet, scheduler_kwargs, vae = load_models_xl(
                pretrained_model_name_or_path=model_name,
                scheduler_name=None,
                weight_dtype=dtype,
            )
            scheduler = diffusers.DPMSolverMultistepScheduler.from_config(scheduler_kwargs)
            pipe = PipeClass(
                vae=vae,
                text_encoder=text_encoders[0],
                text_encoder_2=text_encoders[1],
                tokenizer=tokenizers[0],
                tokenizer_2=tokenizers[1],
                unet=unet,
                scheduler=scheduler,
                controlnet=[controlnet_identitynet],
            ).to(device)
        else:
            pipe = PipeClass.from_pretrained(
                model_name,
                controlnet=[controlnet_identitynet],
                torch_dtype=dtype,
                feature_extractor=None,
            ).to(device)
            pipe.scheduler = diffusers.DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

        pipe.load_ip_adapter_instantid(face_adapter)
        if vram_gb >= 15 or ram_gb <= 30:
            pipe._current_model = model_name

        return pipe

    def generate_image(
        resize_max_side,
        face_image_path,
        enable_multi_ref,
        multi_ref_files,
        normalize_multi_ref,
        pose_image_path,
        prompt,
        negative_prompt,
        weight_application_method,
        clip_skip,
        style_name,
        prompt_replacement_value,
        num_steps,
        identitynet_strength_ratio,
        identitynet_start,
        identitynet_end,
        adapter_strength_ratio,
        adapter_start,
        adapter_end,
        adapter_smooth_transition,
        pose_strength,
        canny_strength,
        depth_strength,
        controlnet_selection,
        guidance_scale,
        seed,
        scheduler,
        enable_lora,
        disable_lora_1,
        lora_scale,
        lora_selection,
        disable_lora_2,
        lora_scale_2,
        lora_selection_2,
        disable_lora_3,
        lora_scale_3,
        lora_selection_3,
        disable_lora_4,
        lora_scale_4,
        lora_selection_4,
        disable_lora_5,
        lora_scale_5,
        lora_selection_5,
        disable_lora_6,
        lora_scale_6,
        lora_selection_6,
        disable_lora_7,
        lora_scale_7,
        lora_selection_7,
        disable_lora_8,
        lora_scale_8,
        lora_selection_8,
        disable_lora_9,
        lora_scale_9,
        lora_selection_9,
        disable_lora_10,
        lora_scale_10,
        lora_selection_10,
        enable_embeddings,
        enhance_face_region,
        enhance_strength,
        custom_enhance_padding,
        num_outputs,
        model_name,
        det_size_name,
        file_prefix,
        rng_source,
        enable_vae_tiling,
        enable_cpu_offloading,
        enable_sage_attention,
        enable_upscaler_prescale,
        upscaler_prescale_headroom,
        resize_mode,
        pad_to_max_side,
        kps_brightness,
        enable_custom_resize,
        custom_resize_width,
        custom_resize_height,
        enable_img2img,
        strength,
        enable_img2img_upscaler,
        img2img_upscaler,
        ratio_base_pixel_number,
        enable_hires_fix,
        hires_upscaler,
        hires_upscale_by,
        hires_steps,
        hires_denoising_strength,
        save_hires_original,
        progress=gr.Progress(),
    ):
        def _fix_guidance_range(start, end, label):
            start, end = float(start), float(end)
            if start >= end:
                fallback_end = round(min(1.0, start + 0.05), 2)
                print(f"\n[Start/End fallback for adapters] {label}: start step {start} >= end step {end}; using {fallback_end} for end step instead.")
                end = fallback_end
            return start, end
        identitynet_start, identitynet_end = _fix_guidance_range(
            identitynet_start, identitynet_end, "IdentityNet guidance range"
        )
        adapter_start, adapter_end = _fix_guidance_range(
            adapter_start, adapter_end, "IP-Adapter guidance range"
        )
        file_prefix = file_prefix.strip().translate(FILENAME_SAFE_TRANS)
        file_prefix = DEFAULT_FILE_PREFIX if not file_prefix else (f"{file_prefix}_" if not file_prefix.endswith('_') else file_prefix)
        generator_device = "cpu" if rng_source == "CPU" else device
        nonlocal pipe, hires_sibling_pipe
        stop_event.clear()
        overall_start_time = time.time()
        
        update_det_size(det_size_name)
        
        target_pipe_class = StableDiffusionXLInstantIDImg2ImgPipeline if enable_img2img else StableDiffusionXLInstantIDPipeline
        needs_full_reload = pipe is None or model_name.lower() != (getattr(pipe, "_current_model", None) or "").lower()

        if needs_full_reload:
            if pipe is not None:
                pipe._sibling_pipe = None
            if hires_sibling_pipe is not None:
                hires_sibling_pipe._sibling_pipe = None

            if vram_gb >= 15 or ram_gb <= 30:
                if pipe is not None:
                    del pipe
                    pipe = None
                if hires_sibling_pipe is not None:
                    del hires_sibling_pipe
                    hires_sibling_pipe = None
                global cached_controlnet_models
                for k in list(cached_controlnet_models.keys()):
                    del cached_controlnet_models[k]

                gc.collect()
                torch.cuda.empty_cache()

            print(f"\nLoading model: {model_name}\n")
            pipe = load_model_and_update_pipe(model_name, enable_img2img)
            pipe._current_model = model_name
            embedding_state["loaded"] = False
            embedding_state["tokens"] = []
            lora_state["signature"] = None

            hires_sibling_pipe = get_img2img_sibling_pipe(pipe)
        elif not isinstance(pipe, target_pipe_class):
            pipe = get_sibling_pipe(pipe, target_pipe_class)
            pipe._current_model = model_name

        if enable_vae_tiling:
            pipe.enable_vae_tiling()
        else:
            pipe.disable_vae_tiling()

        apply_sage_attention(enable_sage_attention)

        if enable_lora:
            lora_slots = [
                (lora_selection, disable_lora_1, lora_scale, 1),
                (lora_selection_2, disable_lora_2, lora_scale_2, 2),
                (lora_selection_3, disable_lora_3, lora_scale_3, 3),
                (lora_selection_4, disable_lora_4, lora_scale_4, 4),
                (lora_selection_5, disable_lora_5, lora_scale_5, 5),
                (lora_selection_6, disable_lora_6, lora_scale_6, 6),
                (lora_selection_7, disable_lora_7, lora_scale_7, 7),
                (lora_selection_8, disable_lora_8, lora_scale_8, 8),
                (lora_selection_9, disable_lora_9, lora_scale_9, 9),
                (lora_selection_10, disable_lora_10, lora_scale_10, 10),
            ]

            def file_adapter_name(filename):
                if filename not in lora_state["adapter_ids"]:
                    lora_state["adapter_ids"][filename] = len(lora_state["adapter_ids"])
                sanitized = filename.replace('.safetensors', '').replace('.', '_')
                return f"lora_{lora_state['adapter_ids'][filename]}_{sanitized}"

            desired_by_file = {}
            slot_usage = {}
            for selection, disabled, scale, idx in lora_slots:
                if selection and not disabled:
                    lora_path = os.path.join("./models/Loras", selection)
                    if os.path.exists(lora_path):
                        desired_by_file[selection] = desired_by_file.get(selection, 0.0) + float(scale)
                        slot_usage.setdefault(selection, []).append(idx)
                    else:
                        print(f"LoRA {idx} not found at {lora_path}, skipping load.")
                        gr.Warning(f"LoRA {idx} not found at {lora_path}. Skipping LoRA {idx}.")

            for name, slots in slot_usage.items():
                if len(slots) > 1:
                    print(f"LoRA '{name}' selected in slots {slots} - total combined scale: {desired_by_file[name]:.3f} (summed).")
                else:
                    print(f"LoRA selected: {name} with scale {desired_by_file[name]} (slot {slots[0]})")

            desired_lora_signature = tuple(
                sorted((name, round(scale, 4)) for name, scale in desired_by_file.items())
            )

            if desired_lora_signature == lora_state["signature"]:
                if desired_by_file:
                    pipe.enable_lora()
                    print(f"\nReusing {len(desired_by_file)} already-fused LoRA(s).\n")
                else:
                    pipe.disable_lora()
            else:
                previous_by_file = dict(lora_state["signature"] or ())
                previous_files = set(previous_by_file)
                desired_files = set(desired_by_file)
                removed_files = previous_files - desired_files
                added_files = desired_files - previous_files

                try:
                    if lora_state["signature"]:
                        pipe.unfuse_lora()

                    if removed_files:
                        pipe.delete_adapters([file_adapter_name(f) for f in removed_files])
                        gc.collect()
                        torch.cuda.empty_cache()
                        print(f"Unloaded LoRA(s): {', '.join(sorted(removed_files))}")

                    for name in added_files:
                        pipe.load_lora_weights("./models/Loras", weight_name=name, adapter_name=file_adapter_name(name))

                    if desired_by_file:
                        adapter_names = [file_adapter_name(name) for name in desired_by_file]
                        adapter_weights = [scale for scale in desired_by_file.values()]
                        pipe.enable_lora()
                        pipe.set_adapters(adapter_names, adapter_weights=adapter_weights)
                        pipe.fuse_lora()
                        reused_count = len(desired_by_file) - len(added_files)
                        print(
                            f"Fused {len(desired_by_file)} LoRA(s): {len(added_files)} newly loaded, "
                            f"{reused_count} reused, {len(removed_files)} dropped."
                        )
                    else:
                        pipe.disable_lora()
                        print("No LoRAs selected or found, LoRA disabled.")

                    lora_state["signature"] = desired_lora_signature

                except Exception as e:
                    print(f"Incremental LoRA update failed ({e}); falling back to a full reload.")
                    try:
                        pipe.unload_lora_weights()
                    except Exception:
                        pass
                    gc.collect()
                    torch.cuda.empty_cache()

                    if desired_by_file:
                        loaded_files = {}
                        failed_files = []
                        for name, scale in desired_by_file.items():
                            try:
                                pipe.load_lora_weights("./models/Loras", weight_name=name, adapter_name=file_adapter_name(name))
                                loaded_files[name] = scale
                            except Exception as load_err:
                                failed_files.append(name)
                                hint = " (likely wrong base architecture, e.g. an SD1.5 LoRA on an SDXL model)" if "size mismatch" in str(load_err) else ""
                                print(f"Skipping incompatible LoRA '{name}'{hint}: {load_err}".splitlines()[0])
                        if failed_files:
                            print(f"Skipped {len(failed_files)} incompatible LoRA(s): {', '.join(failed_files)}")
                        if loaded_files:
                            adapter_names = [file_adapter_name(name) for name in loaded_files]
                            adapter_weights = [scale for scale in loaded_files.values()]
                            pipe.enable_lora()
                            pipe.set_adapters(adapter_names, adapter_weights=adapter_weights)
                            pipe.fuse_lora()
                            print(f"Successfully loaded and fused {len(loaded_files)} LoRA(s).")
                            lora_state["signature"] = tuple(sorted((n, round(s, 4)) for n, s in loaded_files.items()))
                        else:
                            pipe.disable_lora()
                            print("No compatible LoRAs could be loaded; LoRA disabled.")
                            lora_state["signature"] = None
                    else:
                        pipe.disable_lora()
                        print("No LoRAs selected or found, LoRA disabled.")
                        lora_state["signature"] = None
        else:
            if lora_state["signature"]:
                pipe.unfuse_lora()
                pipe.unload_lora_weights()
                lora_state["signature"] = None
                gc.collect()
                torch.cuda.empty_cache()
            pipe.disable_lora()

        if not prompt:
            prompt = " " if prompt_replacement_value == "Empty (none)" else prompt_replacement_value

        prompt, negative_prompt = apply_style(style_name, prompt, negative_prompt)

        loaded_embedding_tokens = []
        if enable_embeddings:
            combined_text = f"{prompt}\n{negative_prompt}"
            needed_tokens = [
                embedding_token_from_filename(f) for f in get_available_embeddings()
                if re.search(re.escape(embedding_token_from_filename(f)), combined_text, flags=re.IGNORECASE)
            ]

            already_loaded_lower = {t.lower() for t in embedding_state["tokens"]}
            missing_tokens = [t for t in needed_tokens if t.lower() not in already_loaded_lower]

            if missing_tokens:
                newly_loaded = load_all_embeddings(pipe, required_tokens=missing_tokens)
                embedding_state["tokens"] = embedding_state["tokens"] + newly_loaded
                embedding_state["loaded"] = True
                if newly_loaded:
                    print(f"\nSuccessfully loaded {len(newly_loaded)} embedding(s): {', '.join(newly_loaded)}")

            needed_lower = {t.lower() for t in needed_tokens}
            loaded_embedding_tokens = [t for t in embedding_state["tokens"] if t.lower() in needed_lower]
            if loaded_embedding_tokens:
                print(f"\nUsing {len(loaded_embedding_tokens)} embedding(s) for this generation: {', '.join(loaded_embedding_tokens)}\n")
            else:
                print("\nNo matching embeddings found in prompt or negative prompt.\n")

        face_image_filename = os.path.basename(face_image_path) if face_image_path else "None"
        pose_image_filename = os.path.basename(pose_image_path) if pose_image_path else "None"

        if not controlnet_selection:
            torch.cuda.empty_cache()

        scheduler_config = dict(pipe.scheduler.config.items())
        parts = scheduler.split("-")
        scheduler_split = parts[0]
        suffixes = parts[1:]
        use_karras = "Karras" in suffixes
        use_exponential = "Exponential" in suffixes
        use_beta = "Beta" in suffixes
        use_sde = "SDE" in suffixes
        scheduler_class = getattr(diffusers, scheduler_split)

        if scheduler_split in ["DPMSolverMultistepScheduler", "DPMSolverSinglestepScheduler"]:
            pipe.scheduler = scheduler_class.from_config(
                scheduler_config,
                use_karras_sigmas=use_karras,
                use_exponential_sigmas=use_exponential,
                use_beta_sigmas=use_beta,
                algorithm_type="sde-dpmsolver++" if use_sde else "dpmsolver++"
            )
        elif scheduler_split == "DEISMultistepScheduler":
            pipe.scheduler = scheduler_class.from_config(
                scheduler_config,
                use_karras_sigmas=use_karras,
                use_exponential_sigmas=use_exponential,
                use_beta_sigmas=use_beta,
                algorithm_type="deis"
            )
        elif scheduler_split in [
            "KDPM2AncestralDiscreteScheduler",
            "KDPM2DiscreteScheduler",
            "DPMSolverSDEScheduler",
            "EulerDiscreteScheduler",
            "HeunDiscreteScheduler",
            "LMSDiscreteScheduler",
            "UniPCMultistepScheduler",
        ]:
            pipe.scheduler = scheduler_class.from_config(
                scheduler_config,
                use_karras_sigmas=use_karras,
                use_exponential_sigmas=use_exponential,
                use_beta_sigmas=use_beta,
            )
        else:
            pipe.scheduler = scheduler_class.from_config(scheduler_config)

        if face_image_path is None:
            raise gr.Error(
                f"Cannot find any input face image! Please upload the face image"
            )

        prompt_for_generation = prompt
        negative_prompt_for_generation = negative_prompt
        if enable_embeddings and loaded_embedding_tokens:
            def _normalize_embedding_casing(text, tokens):
                for tok in tokens:
                    text = re.sub(re.escape(tok), tok, text, flags=re.IGNORECASE)
                return text

            prompt_normalized = _normalize_embedding_casing(prompt, loaded_embedding_tokens)
            negative_prompt_normalized = _normalize_embedding_casing(negative_prompt, loaded_embedding_tokens)

            prompt_for_generation = pipe.maybe_convert_prompt(prompt_normalized, pipe.tokenizer)
            negative_prompt_for_generation = pipe.maybe_convert_prompt(negative_prompt_normalized, pipe.tokenizer)

        used_embedding_tokens = [
            tok for tok in loaded_embedding_tokens
            if re.search(re.escape(tok), prompt_for_generation, flags=re.IGNORECASE)
            or re.search(re.escape(tok), negative_prompt_for_generation, flags=re.IGNORECASE)
        ]

        face_image = load_image(face_image_path)
        original_face_image = face_image
        custom_size = None
        if enable_custom_resize:
            custom_size = (int(custom_resize_width), int(custom_resize_height))
        resize_mode_enum = getattr(PIL.Image, resize_mode)
        face_image = resize_img(face_image, size=custom_size, max_side=resize_max_side, mode=resize_mode_enum, pad_to_max_side=pad_to_max_side, base_pixel_number=ratio_base_pixel_number)
        face_image_cv2 = convert_from_image_to_cv2(face_image)
        height, width, _ = face_image_cv2.shape

        temp_app = None
        face_info, temp_app = detect_face_info(
            original_face_image, face_image, face_image_cv2,
            resize_mode_enum, enable_custom_resize,
            label="the face/pose image",
            temp_app=temp_app,
        )
        if len(face_info) == 0:
            raise gr.Error(
                f"Unable to detect a face in the image. Please upload a different photo with a clear face."
            )

        face_info = sorted(face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]))[-1]
        face_emb = face_info["embedding"]
        face_kps = draw_kps(convert_from_cv2_to_image(face_image_cv2), face_info["kps"], kps_brightness)
        img_controlnet = face_image

        multi_ref_used = 0
        multi_ref_filenames = []
        if enable_multi_ref and multi_ref_files:
            multi_ref_embeddings = [face_emb]
            for additional_item in multi_ref_files:
                additional_path = additional_item[0] if isinstance(additional_item, (list, tuple)) else additional_item
                try:
                    additional_image = load_image(additional_path)
                    original_additional_image = additional_image
                    additional_image_resized = resize_img(
                        additional_image, size=None, max_side=resize_max_side,
                        mode=resize_mode_enum, pad_to_max_side=pad_to_max_side,
                        base_pixel_number=ratio_base_pixel_number,
                    )
                    additional_image_cv2 = convert_from_image_to_cv2(additional_image_resized)

                    additional_face_info, temp_app = detect_face_info(
                        original_additional_image, additional_image_resized, additional_image_cv2,
                        resize_mode_enum, enable_custom_resize,
                        label=f"additional face image '{os.path.basename(additional_path)}'",
                        need_kps=False,
                        temp_app=temp_app,
                    )

                    if len(additional_face_info) == 0:
                        print(f"\nNo face detected in additional face image '{os.path.basename(additional_path)}'. Skipping it.\n")
                        gr.Warning(f"No face detected in additional face image '{os.path.basename(additional_path)}'. Skipping it.")
                        continue
                    additional_face_info = sorted(additional_face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]))[-1]
                    multi_ref_embeddings.append(additional_face_info["embedding"])
                    multi_ref_filenames.append(os.path.basename(additional_path))
                except Exception as e:
                    print(f"\nFailed to process additional face image '{os.path.basename(additional_path)}': {e}\n")
            if len(multi_ref_embeddings) > 1:
                mean_embedding = np.mean(multi_ref_embeddings, axis=0)
                if normalize_multi_ref:
                    mean_embedding_norm = np.linalg.norm(mean_embedding)
                    target_embedding_norm = np.mean([np.linalg.norm(e) for e in multi_ref_embeddings])
                    if mean_embedding_norm > 0:
                        face_emb = mean_embedding / mean_embedding_norm * target_embedding_norm
                    else:
                        face_emb = mean_embedding
                else:
                    face_emb = mean_embedding
                multi_ref_used = len(multi_ref_embeddings)
                print(f"Using an averaged face embedding from {multi_ref_used} face images (normalization: {'enabled' if normalize_multi_ref else 'disabled'}).\n")
        additional_images_used_text = ", ".join(multi_ref_filenames) if multi_ref_filenames else "None"
        if pose_image_path is not None:
            pose_image = load_image(pose_image_path)
            original_pose_image = pose_image
            pose_image = resize_img(pose_image, size=custom_size, max_side=resize_max_side, mode=resize_mode_enum, pad_to_max_side=pad_to_max_side, base_pixel_number=ratio_base_pixel_number)
            img_controlnet = pose_image
            pose_image_cv2 = convert_from_image_to_cv2(pose_image)

            face_info, temp_app = detect_face_info(
                original_pose_image, pose_image, pose_image_cv2,
                resize_mode_enum, enable_custom_resize,
                label="the pose image",
                temp_app=temp_app,
            )
            if len(face_info) == 0:
                raise gr.Error(
                    f"Cannot find any face in the reference image! Please upload another person image"
                )

            face_info = face_info[-1]
            face_kps = draw_kps(pose_image, face_info["kps"], kps_brightness)

            width, height = face_kps.size
        if temp_app is not None:
            del temp_app

        if enhance_face_region:
            control_mask = np.zeros([height, width, 3], dtype=np.uint8)
            x1, y1, x2, y2 = face_info["bbox"]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            if enhance_strength == "Balanced":
                padding_ratio = 0.15
            elif enhance_strength == "High":
                padding_ratio = 0.3
            elif enhance_strength == "Custom":
                padding_ratio = custom_enhance_padding
            else:
                padding_ratio = 0.0

            padding_x = int((x2 - x1) * padding_ratio)
            padding_y = int((y2 - y1) * padding_ratio)

            x1 = max(0, x1 - padding_x)
            y1 = max(0, y1 - padding_y)
            x2 = min(width, x2 + padding_x)
            y2 = min(height, y2 + padding_y)

            control_mask[y1:y2, x1:x2] = 255
            control_mask = Image.fromarray(control_mask)
        else:
            control_mask = None

        if hasattr(controlnet_identitynet, "_hf_hook"):
            remove_hook_from_module(controlnet_identitynet, recurse=True)

        if len(controlnet_selection) > 0:
            for k in list(cached_controlnet_models.keys()):
                if k not in controlnet_selection:
                    del cached_controlnet_models[k]
                    gc.collect()
                    torch.cuda.empty_cache()
            controlnet_scales = {
                "pose": pose_strength,
                "canny": canny_strength,
                "depth": depth_strength,
            }
            controlnet_models_to_use = []
            controlnet_images = []
            for s in controlnet_selection:
                model = load_and_cache_controlnet_model(s) 
                controlnet_models_to_use.append(model)
                controlnet_images.append(controlnet_map_fn[s](img_controlnet).resize((width, height)))
            pipe.controlnet = MultiControlNetModel([controlnet_identitynet] + controlnet_models_to_use)
            control_scales = [float(identitynet_strength_ratio)] + [controlnet_scales[s] for s in controlnet_selection]
            control_images = [face_kps] + controlnet_images
            control_guidance_start = [float(identitynet_start)] + [0.0] * len(controlnet_selection)
            control_guidance_end = [float(identitynet_end)] + [1.0] * len(controlnet_selection)
        else:
            if cached_controlnet_models:
                for key in list(cached_controlnet_models.keys()):
                    del cached_controlnet_models[key]
                    gc.collect()
                    torch.cuda.empty_cache()
            pipe.controlnet = controlnet_identitynet
            control_scales = float(identitynet_strength_ratio)
            control_images = face_kps
            control_guidance_start = float(identitynet_start)
            control_guidance_end = float(identitynet_end)

        sibling_pipe = getattr(pipe, "_sibling_pipe", None)
        if sibling_pipe is not None:
            sibling_pipe.controlnet = pipe.controlnet

        if enable_cpu_offloading:
            pipe.enable_model_cpu_offload(device=device)
        else:
            if hasattr(pipe.unet, "_hf_hook"):
                pipe.remove_all_hooks()
                pipe.to(device)
        
        generator = torch.Generator(device=generator_device).manual_seed(seed)

        print("Starting image generation...")
        print(f"Prompt: {prompt}\nNegative Prompt: {negative_prompt}")
        print(f"Detection size: {current_det_size}")
        print(f"Input face image: {os.path.basename(face_image_path) if face_image_path else 'None'}")
        if multi_ref_used:
            print(f"Multiple face images: Enabled - averaged {multi_ref_used} face embeddings, normalization {'enabled' if normalize_multi_ref else 'disabled'} (additional face(s): {', '.join(multi_ref_filenames)})")
        print(f"Reference pose image: {os.path.basename(pose_image_path) if pose_image_path else 'None'}")
        print(f"Steps: {num_steps}")
        print(f"img2img Mode: {'Enabled' if enable_img2img else 'Disabled'}")
        if enable_img2img:
            print(f"img2img Denoising Strength: {strength}")
            print(f"img2img Upscaler: {'Enabled - ' + img2img_upscaler if enable_img2img_upscaler else 'Disabled'}")
        print(f"Hires Fix: {'Enabled' if enable_hires_fix else 'Disabled'}")
        if enable_hires_fix:
            print(f"Hires Upscaler: {hires_upscaler}")
            print(f"Hires Upscale By: {hires_upscale_by}")
            print(f"Hires Steps: {hires_steps}{' (Auto)' if hires_steps == 0 else ''}")
            print(f"Hires Denoising Strength: {hires_denoising_strength}")
            print(f"Upscaler Prescale Optimization: {enable_upscaler_prescale}")
            if enable_upscaler_prescale:
                print(f"Upscaler Prescale Headroom: {upscaler_prescale_headroom}")
        print(f"Enhance non-face region: {'True' if enhance_face_region else 'False'} ({enhance_strength}{f' | Padding: {custom_enhance_padding:.2f}' if enhance_strength == 'Custom' else ''})")
        print(f"Guidance scale: {guidance_scale}")
        print(f"Model: {model_name}")
        print(f"Resize mode: {resize_mode}")
        print(f"Pad to max side: {pad_to_max_side}")
        print(f"Sage Attention: {enable_sage_attention}")
        print(f"KPS Brightness: {kps_brightness}")
        print(f"Use custom resize: {enable_custom_resize}")
        if enable_custom_resize:
            print(f"Custom resize size: {custom_resize_width}x{custom_resize_height}")
        if controlnet_selection:
            cn_strengths = {
                "pose": pose_strength,
                "canny": canny_strength,
                "depth": depth_strength,
            }
            cn_strength_str = ", ".join(
                f"{s.capitalize()}: {cn_strengths[s]}" for s in controlnet_selection if s in cn_strengths
            )
            print(f"ControlNet selection: {controlnet_selection} | Strength(s) - {cn_strength_str}")
        else:
            print("ControlNet selection: None (Disabled)")
        print(f"IdentityNet strength: {identitynet_strength_ratio}")
        print(f"Adapter strength: {adapter_strength_ratio}")
        if (identitynet_start, identitynet_end, adapter_start, adapter_end) != (0.0, 1.0, 0.0, 1.0):
            print(f"Control step ranges: IdentityNet: {identitynet_start} - {identitynet_end} | Image adapter: {adapter_start} - {adapter_end} | Smooth transition: {adapter_smooth_transition}")

        lora_info_str = "Disabled"
        if enable_lora:
            lora_details = []
            lora_selections = [
                (lora_selection, disable_lora_1, lora_scale, 1),
                (lora_selection_2, disable_lora_2, lora_scale_2, 2),
                (lora_selection_3, disable_lora_3, lora_scale_3, 3),
                (lora_selection_4, disable_lora_4, lora_scale_4, 4),
                (lora_selection_5, disable_lora_5, lora_scale_5, 5),
                (lora_selection_6, disable_lora_6, lora_scale_6, 6),
                (lora_selection_7, disable_lora_7, lora_scale_7, 7),
                (lora_selection_8, disable_lora_8, lora_scale_8, 8),
                (lora_selection_9, disable_lora_9, lora_scale_9, 9),
                (lora_selection_10, disable_lora_10, lora_scale_10, 10),
            ]
            for selection, disabled, scale, idx in lora_selections:
                if selection:
                    path = os.path.join("./models/Loras", selection)
                    if not disabled and os.path.exists(path):
                        lora_details.append(f"LoRA {idx}: {selection} (Scale: {scale})")
                    elif disabled:
                        lora_details.append(f"LoRA {idx}: Manually disabled")
                    else:
                        lora_details.append(f"LoRA {idx}: {selection} (Not found)")
            if lora_details:
                lora_info_str = "; ".join(lora_details)

        print(f"LoRA(s): {lora_info_str}")
        if not enable_embeddings:
            print("Embeddings: Disabled")
        elif used_embedding_tokens:
            print(f"Embeddings: Enabled | Embeddings Used: {', '.join(used_embedding_tokens)}")
        else:
            print("Embeddings: Enabled but none found in prompt or negative prompt")

        print(f"Scheduler: {scheduler}")
        print(f"Noise RNG device: {rng_source}")
        print(f"Ratio base pixel number: {ratio_base_pixel_number}")
        print(f"Weight application method: {weight_application_method}")
        print(f"Clip skip: {clip_skip}")
        print(f"Max resize side: {resize_max_side}")
        print(f"Image size: {width}x{height}\n")

        images = []
        generation_infos = []
        saved_output_paths = []
        stopped_early = False

        i2i_upscaled_image = None
        i2i_latent_encode_source = None
        use_latent_upscale_i2i = False
        if enable_img2img and enable_img2img_upscaler:
            use_latent_upscale_i2i = (img2img_upscaler == "Latent (bicubic)")
            effective_pad_to_max_side_i2i = pad_to_max_side and custom_size is None
            if not use_latent_upscale_i2i:
                i2i_upscaler_model = load_upscaler_model(img2img_upscaler)
                i2i_upscaled_image = run_upscaler_model(i2i_upscaler_model, original_face_image)
                i2i_upscaled_image = fit_image_to_canvas(
                    i2i_upscaled_image, (width, height), PIL.Image.LANCZOS, effective_pad_to_max_side_i2i
                )
            else:
                native_w, native_h = original_face_image.size
                target_ratio = width / height
                if native_w >= native_h:
                    enc_w = native_w
                    enc_h = round(native_w / target_ratio)
                else:
                    enc_h = native_h
                    enc_w = round(native_h * target_ratio)
                enc_w = max(8, (enc_w // 8) * 8)
                enc_h = max(8, (enc_h // 8) * 8)
                i2i_latent_encode_source = fit_image_to_canvas(
                    original_face_image, (enc_w, enc_h), PIL.Image.LANCZOS, effective_pad_to_max_side_i2i
                )

        for i in range(num_outputs):
            if stop_event.is_set():
                print("Stop requested - halting before starting generation.\n")
                stopped_early = True
                break

            print(f"Generating image {i + 1} of {num_outputs}...\n")

            steps = max(1, int(num_steps * strength)) if enable_img2img else num_steps
            step_tracker = {"last": -1, "total": 0}
            is_slow_scheduler = any(x in scheduler for x in ["DPMSolverSDE", "KDPM2", "Heun"])

            if is_slow_scheduler:
                def gradio_callback_lambda(pipe_obj, step, timestep, callback_kwargs):
                    if stop_event.is_set():
                        raise GenerationStopped()
                    if step != step_tracker["last"]:
                        step_tracker["last"] = step
                        step_tracker["total"] += 1

                    est_total = steps * 2
                    progress(
                        ((i / num_outputs) + (step_tracker["total"] / est_total) / num_outputs),
                        desc=f"Generating image {i + 1} of {num_outputs} "
                             f"(Step {min(step_tracker['total'] // 2, steps)}/{steps})"
                    )
                    if vram_gb <= 18 and enable_img2img and step == 0:
                        torch.cuda.empty_cache()
                    return callback_kwargs
            else:
                def gradio_callback_lambda(pipe_obj, step, timestep, callback_kwargs):
                    if stop_event.is_set():
                        raise GenerationStopped()
                    progress(
                        ((i / num_outputs) + (((step + 1) / steps) / num_outputs)),
                        desc=f"Generating image {i + 1} of {num_outputs} (Step {step + 1}/{steps})"
                    )
                    if vram_gb <= 18 and enable_img2img and step == 0:
                        torch.cuda.empty_cache()
                    return callback_kwargs

            print(f"Seed: {seed + i}\n")
            if enable_hires_fix:
                hires_preview_width = max(8, int(round((width * hires_upscale_by) / 8) * 8))
                hires_preview_height = max(8, int(round((height * hires_upscale_by) / 8) * 8))
                print(f"Running the first main pass of {width}x{height} before proceeding to the Hires Fix pass ({hires_upscale_by}x for {hires_preview_width}x{hires_preview_height})...\n")

            generator = torch.Generator(device=generator_device).manual_seed(seed + i)

            if enable_img2img and enable_img2img_upscaler:
                if use_latent_upscale_i2i:
                    i2i_base_latents = encode_image_to_latents(pipe, i2i_latent_encode_source, generator=generator)
                    img2img_source_image = latent_space_upscale(i2i_base_latents, height, width, mode="bicubic", antialias=False)
                else:
                    img2img_source_image = i2i_upscaled_image
            else:
                img2img_source_image = face_image

            common_kwargs = dict(
                prompt=prompt_for_generation,
                negative_prompt=negative_prompt_for_generation,
                weight_application_method=weight_application_method,
                clip_skip=clip_skip if clip_skip else None,
                image_embeds=face_emb,
                controlnet_conditioning_scale=control_scales,
                control_guidance_start=control_guidance_start,
                control_guidance_end=control_guidance_end,
                ip_adapter_scale=adapter_strength_ratio,
                ip_adapter_scale_start=float(adapter_start),
                ip_adapter_scale_end=float(adapter_end),
                smooth_range_transition=bool(adapter_smooth_transition),
                num_inference_steps=num_steps,
                guidance_scale=guidance_scale,
                height=height,
                width=width,
                generator=generator,
                callback_on_step_end=gradio_callback_lambda,
            )
            torch.cuda.empty_cache()
            try:
                if enable_img2img:
                    result = pipe(
                        **common_kwargs,
                        image=img2img_source_image,
                        control_image=control_images,
                        strength=strength,
                        control_mask=control_mask,
                    )
                else:
                    result = pipe(
                        **common_kwargs,
                        image=control_images,
                        control_mask=control_mask,
                    )
            except GenerationStopped:
                print(f"Stop requested - generation of image {i + 1} was interrupted mid-way.\n")
                stopped_early = True
                torch.cuda.empty_cache()
                break
            except Exception:
                print(f"\nGeneration failed on image {i + 1}: forcing a full model reload on next generation since this crash can leave the pipeline in a corrupted state.\n")
                pipe._current_model = None
                hires_sibling_pipe = None
                gc.collect()
                torch.cuda.empty_cache()
                raise

            image = result.images[0]

            info_text = f"""Prompt: {prompt}
Negative Prompt: {negative_prompt}
Input Face Image: {face_image_filename}
Reference Pose Image: {pose_image_filename}
Detection size: {current_det_size}
Additional face image(s) used: {additional_images_used_text}
Normalize averaged face embedding: {normalize_multi_ref}
Steps: {num_steps}
Guidance scale: {guidance_scale}
Seed: {seed + i}
Model: {model_name}
ControlNet selection: {controlnet_selection}
Max resize side: {resize_max_side}
Image size: {width}x{height}
Ratio base pixel number: {ratio_base_pixel_number}
Enhance non-face region: {enhance_face_region}
Enhance region profile: {enhance_strength}
Enhance padding ratio: {custom_enhance_padding}
Resize mode: {resize_mode}
Pad to max side: {pad_to_max_side}
KPS Brightness: {kps_brightness}
Use custom resize: {enable_custom_resize}
Custom resize size: {custom_resize_width}x{custom_resize_height}
img2img Strength: {strength}
img2img Mode Enabled: {enable_img2img}
img2img Upscaler Enabled: {enable_img2img_upscaler}
img2img Upscaler: {img2img_upscaler}
Hires Fix Enabled: {enable_hires_fix}
Hires Upscaler: {hires_upscaler}
Hires Upscale By: {hires_upscale_by}
Hires Steps: {hires_steps}
Hires Denoising Strength: {hires_denoising_strength}
Upscaler Prescale Optimization: {enable_upscaler_prescale}
Upscaler Prescale Headroom: {upscaler_prescale_headroom}
IdentityNet strength: {identitynet_strength_ratio}
Adapter strength: {adapter_strength_ratio}
Ranges: IdentityNet: {identitynet_start} - {identitynet_end} | Adapter: {adapter_start} - {adapter_end} | Smooth Transition: {adapter_smooth_transition}
Pose strength: {pose_strength}
Canny strength: {canny_strength}
Depth strength: {depth_strength}
Noise RNG device: {rng_source}
LoRA Enabled: {enable_lora}
LoRA 1 selection: {'None' if disable_lora_1 or not (enable_lora and lora_selection and os.path.exists(os.path.join('./models/Loras', lora_selection))) else lora_selection}
LoRA 1 scale: {'Disabled' if disable_lora_1 or not (enable_lora and lora_selection and os.path.exists(os.path.join('./models/Loras', lora_selection))) else lora_scale}
LoRA 2 selection: {'None' if disable_lora_2 or not (enable_lora and lora_selection_2 and os.path.exists(os.path.join('./models/Loras', lora_selection_2))) else lora_selection_2}
LoRA 2 scale: {'Disabled' if disable_lora_2 or not (enable_lora and lora_selection_2 and os.path.exists(os.path.join('./models/Loras', lora_selection_2))) else lora_scale_2}
LoRA 3 selection: {'None' if disable_lora_3 or not (enable_lora and lora_selection_3 and os.path.exists(os.path.join('./models/Loras', lora_selection_3))) else lora_selection_3}
LoRA 3 scale: {'Disabled' if disable_lora_3 or not (enable_lora and lora_selection_3 and os.path.exists(os.path.join('./models/Loras', lora_selection_3))) else lora_scale_3}
LoRA 4 selection: {'None' if disable_lora_4 or not (enable_lora and lora_selection_4 and os.path.exists(os.path.join('./models/Loras', lora_selection_4))) else lora_selection_4}
LoRA 4 scale: {'Disabled' if disable_lora_4 or not (enable_lora and lora_selection_4 and os.path.exists(os.path.join('./models/Loras', lora_selection_4))) else lora_scale_4}
LoRA 5 selection: {'None' if disable_lora_5 or not (enable_lora and lora_selection_5 and os.path.exists(os.path.join('./models/Loras', lora_selection_5))) else lora_selection_5}
LoRA 5 scale: {'Disabled' if disable_lora_5 or not (enable_lora and lora_selection_5 and os.path.exists(os.path.join('./models/Loras', lora_selection_5))) else lora_scale_5}
LoRA 6 selection: {'None' if disable_lora_6 or not (enable_lora and lora_selection_6 and os.path.exists(os.path.join('./models/Loras', lora_selection_6))) else lora_selection_6}
LoRA 6 scale: {'Disabled' if disable_lora_6 or not (enable_lora and lora_selection_6 and os.path.exists(os.path.join('./models/Loras', lora_selection_6))) else lora_scale_6}
LoRA 7 selection: {'None' if disable_lora_7 or not (enable_lora and lora_selection_7 and os.path.exists(os.path.join('./models/Loras', lora_selection_7))) else lora_selection_7}
LoRA 7 scale: {'Disabled' if disable_lora_7 or not (enable_lora and lora_selection_7 and os.path.exists(os.path.join('./models/Loras', lora_selection_7))) else lora_scale_7}
LoRA 8 selection: {'None' if disable_lora_8 or not (enable_lora and lora_selection_8 and os.path.exists(os.path.join('./models/Loras', lora_selection_8))) else lora_selection_8}
LoRA 8 scale: {'Disabled' if disable_lora_8 or not (enable_lora and lora_selection_8 and os.path.exists(os.path.join('./models/Loras', lora_selection_8))) else lora_scale_8}
LoRA 9 selection: {'None' if disable_lora_9 or not (enable_lora and lora_selection_9 and os.path.exists(os.path.join('./models/Loras', lora_selection_9))) else lora_selection_9}
LoRA 9 scale: {'Disabled' if disable_lora_9 or not (enable_lora and lora_selection_9 and os.path.exists(os.path.join('./models/Loras', lora_selection_9))) else lora_scale_9}
LoRA 10 selection: {'None' if disable_lora_10 or not (enable_lora and lora_selection_10 and os.path.exists(os.path.join('./models/Loras', lora_selection_10))) else lora_selection_10}
LoRA 10 scale: {'Disabled' if disable_lora_10 or not (enable_lora and lora_selection_10 and os.path.exists(os.path.join('./models/Loras', lora_selection_10))) else lora_scale_10}
Embeddings Enabled: {enable_embeddings}
Embeddings Used: {', '.join(used_embedding_tokens) if used_embedding_tokens else 'None'}
GPU used: {gpu_name}
Weight application method: {weight_application_method}
Clip skip: {clip_skip}
Sage Attention: {enable_sage_attention}
Scheduler: {scheduler}"""

            png_info = PIL.PngImagePlugin.PngInfo()
            png_info.add_text("Generation Parameters", info_text)

            if enable_hires_fix:
                if save_hires_original:
                    original_info_text = info_text.replace("Hires Fix Enabled: True", "Hires Fix Enabled: False")
                    original_png_info = PIL.PngImagePlugin.PngInfo()
                    original_png_info.add_text("Generation Parameters", original_info_text)
                    original_saved_paths = save_images([image], generation_info=[original_png_info], prefix=file_prefix)
                    images.append(image)
                    saved_output_paths.append(original_saved_paths[0])
                    print("\nOriginal non-upscaled image saved.")
                torch.cuda.empty_cache()
                print(f"\nRunning the Hires Fix pass and upscaling the image by {hires_upscale_by}x to a final output resolution of {hires_preview_width}x{hires_preview_height}...\n")
                progress(
                    0.0,
                    desc=f"Hires Fix: upscaling image {i + 1} of {num_outputs}"
                )
                hires_width = max(8, int(round((width * hires_upscale_by) / 8) * 8))
                hires_height = max(8, int(round((height * hires_upscale_by) / 8) * 8))

                use_pixel_resize = (hires_upscaler == "Pixel resize (Lanczos)")
                use_latent_upscale = (hires_upscaler == "Latent (bicubic)")
                use_builtin_resize = use_pixel_resize or use_latent_upscale

                if not use_builtin_resize:
                    upscaler_model = load_upscaler_model(hires_upscaler)
                    if enable_upscaler_prescale:
                        hires_model_scale = getattr(upscaler_model, "scale", None) or 4
                        hires_prescaled_source = prescale_for_upscaler_model(
                            image, hires_width, hires_height, hires_model_scale, headroom=upscaler_prescale_headroom
                        )
                        upscaled_image = run_upscaler_model(upscaler_model, hires_prescaled_source)
                    else:
                        upscaled_image = run_upscaler_model(upscaler_model, image)
                    upscaled_image = upscaled_image.resize((hires_width, hires_height), PIL.Image.LANCZOS)
                elif use_pixel_resize:
                    upscaled_image = image.resize((hires_width, hires_height), PIL.Image.LANCZOS)

                hires_pipe = get_img2img_sibling_pipe(pipe)
                hires_pipe.controlnet = pipe.controlnet
                hires_pipe.scheduler = pipe.scheduler
                hires_control_images = resize_control_images(control_images, (hires_width, hires_height))
                hires_control_mask = resize_control_images(control_mask, (hires_width, hires_height))
                if hires_steps and hires_steps > 0:
                    effective_hires_steps = max(1, math.ceil(hires_steps / max(hires_denoising_strength, 1e-4)))
                    display_hires_steps = int(hires_steps)
                else:
                    effective_hires_steps = max(1, math.ceil(num_steps * 1.4))
                    if int(effective_hires_steps * hires_denoising_strength) < 1:
                        print("Auto Hires Steps * Hires denoising strength results in 0 actual steps. Hires Steps value has been temporarily set to 2 to compensate...\n")
                        effective_hires_steps = math.ceil(2 / max(hires_denoising_strength, 1e-4))
                    display_hires_steps = max(1, int(effective_hires_steps * hires_denoising_strength))

                if hires_steps == 0:
                    info_text = info_text.replace(
                        "Hires Steps: 0",
                        f"Hires Steps: 0 - Auto ({display_hires_steps} used for the pass)",
                    )
                    png_info = PIL.PngImagePlugin.PngInfo()
                    png_info.add_text("Generation Parameters", info_text)

                hires_generator = torch.Generator(device=generator_device).manual_seed(seed + i)

                if use_latent_upscale:
                    base_latents = encode_image_to_latents(hires_pipe, image, generator=hires_generator)
                    hires_pass_image = latent_space_upscale(base_latents, hires_height, hires_width, mode="bicubic", antialias=False)
                else:
                    hires_pass_image = upscaled_image

                def hires_gradio_callback_lambda(pipe_obj, step, timestep, callback_kwargs):
                    if stop_event.is_set():
                        raise GenerationStopped()
                    divisor = 2 if is_slow_scheduler else 1
                    current_step = min((step + 1) // divisor, display_hires_steps)
                    progress(
                        (current_step / display_hires_steps),
                        desc=f"Hires Fix: denoising image {i + 1} of {num_outputs} (Step {current_step}/{display_hires_steps})"
                    )
                    if vram_gb <= 22 and step == 0:
                        torch.cuda.empty_cache()
                    return callback_kwargs

                try:
                    hires_result = hires_pipe(
                        prompt=prompt_for_generation,
                        negative_prompt=negative_prompt_for_generation,
                        weight_application_method=weight_application_method,
                        clip_skip=clip_skip if clip_skip else None,
                        image_embeds=face_emb,
                        image=hires_pass_image,
                        control_image=hires_control_images,
                        controlnet_conditioning_scale=control_scales,
                        control_guidance_start=control_guidance_start,
                        control_guidance_end=control_guidance_end,
                        ip_adapter_scale=adapter_strength_ratio,
                        ip_adapter_scale_start=float(adapter_start),
                        ip_adapter_scale_end=float(adapter_end),
                        smooth_range_transition=bool(adapter_smooth_transition),
                        strength=hires_denoising_strength,
                        num_inference_steps=effective_hires_steps,
                        guidance_scale=guidance_scale,
                        height=hires_height,
                        width=hires_width,
                        generator=hires_generator,
                        callback_on_step_end=hires_gradio_callback_lambda,
                        control_mask=hires_control_mask,
                    )
                    image = hires_result.images[0]
                except GenerationStopped:
                    print(f"Stop requested - Hires Fix pass of image {i + 1} was interrupted mid-way.\n")
                    stopped_early = True
                    torch.cuda.empty_cache()
                    break
                except Exception:
                    print(f"\nHires Fix pass failed on image {i + 1}: forcing a full model reload on next generation since this crash can leave the pipeline in a corrupted state.\n")
                    pipe._current_model = None
                    hires_sibling_pipe = None
                    gc.collect()
                    torch.cuda.empty_cache()
                    raise
                torch.cuda.empty_cache()

            images.append(image)

            generation_infos.append(png_info)
            final_saved_paths = save_images([image], generation_info=[png_info], prefix=file_prefix)
            saved_output_paths.append(final_saved_paths[0])
            print(f"\n(√) Finished generating image {i + 1} of {num_outputs}\n")

            torch.cuda.empty_cache()

        stop_event.clear()
        if stopped_early:
            gr.Warning(f"Generation stopped by user. {len(images)} of {num_outputs} image(s) were completed.")

        gc.collect()
        torch.cuda.empty_cache()

        overall_elapsed_time = time.time() - overall_start_time
        if overall_elapsed_time >= 60:
            minutes = int(overall_elapsed_time // 60)
            seconds = int(overall_elapsed_time % 60)
            print(f"Total generation time: {overall_elapsed_time:.2f} seconds ({minutes} minutes and {seconds} seconds)\n")
        else:
            print(f"Total generation time: {overall_elapsed_time:.2f} seconds\n")
        return saved_output_paths

    article = r"""
    - Upload an image with a face. For images with multiple faces, only the largest face will be detected. Ensure the face is not too small and is clearly visible without significant obstructions or blurring.
    - (Optional) You can upload another image as a reference for the face pose. If you don't, the first detected face image will be used to extract facial landmarks. If you used a cropped face as main photo, it is recommended to upload a reference photo to define a new face pose.
    - (Optional) You can select multiple ControlNet models to control the generation process. The default is to use the IdentityNet only. The ControlNet models include pose skeleton, canny, and depth. You can adjust the strength of each ControlNet model to control the generation process, 0.3 for each is the recommended value.
    - Enter a text prompt, as done in normal text-to-image AI tools such as ComfuUI or A1111/ForgeUI.
    - Click the Generate button to begin image generation.
    - The "Add more face images" option averages the face embeddings from multiple images into a single identity. Add photos of the same person to improve likeness and consistency, or photos of different people to create a blended identity. Keep "Normalize averaged embedding" enabled to preserve the original embedding strength after averaging, or disable it to use the plain average.
    - img2img mode imports the "pipeline_stable_diffusion_xl_instantid_img2img" (also used by the Hires Fix pass). It is effective at preserving input image details, depending on the denoising strength you set.
    - Upscale and use Enable Hires Fix to generate images with a resolution of what SDXL is best at (usually ~1024-1280 max side) to prevent anatomy errors like long necks while still producing good quality images.
    - Enable i2i Upscaler upscales your input image before the generation pass, using IdentityNet to sharpen and enhance facial detail as it scales. Best for lowres or soft input photos. Recommended settings: LCM Scheduler + DMD2 LoRA, 10–15 steps, ~0.2 img2img denoising strength. You can also use this to upscale an image you've already generated: just feed it back in as the face image, reuse the same seed, prompt and other settings, then bump up the target resolution to make it higher than the input image (no need for Hires Fix).
    - Select a model to use for generation from the upper left corner dropdown. Only use SDXL and Pony. Illustrious models can be loaded but not all of them are well supported and some produce broken colors.
    - You can select a scheduler from the upper right corner dropdown. DPMSolver, KDPM2 and Euler are usually the best.
    - The "Weight application method" option controls how (word:weight) prompt weighting is applied: "Original InstantID per-token" uses InstantID's own method, which is EOS-interpolation loop (interpolates each token toward the chunk's end-of-text embedding). "ForgeUI per-encoder rescale" (it's how ForgeUI/A1111 work with weights) and "ForgeUI global rescale" both scale each token's embedding directly by its weight, then rescale to preserve the original mean - either per text encoder (CLIP-L and CLIP-G separately) or globally (one combined mean across both). "ComfyUI (blank prompt interpolation)" reproduces ComfyUI's default method: it separately encodes a completely blank prompt of the same length, then interpolates each weighted token toward that blank prompt's embedding at the same position rather than toward its own chunk's EOS embedding or a rescaled mean. This entire "Weight application method" has no effect at all if your prompt/negative prompt fields don't have any weights in them, such as "(anime style:1.5)" for example.
    - Clip Skip option: it picks which text-encoder layer generates your prompt embeddings, instead of always using the final one. Earlier layers give a more literal, less-refined read on the prompt (some checkpoints, especially anime ones like this). 0 is default, one layer back from the end. -1 is the true final layer, fully processed, zero skip. Positive values (1, 2, 3...) skip progressively further back toward the raw embedding layer, with 1-2 being the common useful range. Going below -1 jumps straight to that same raw layer at -2, then walks back toward the final layer again as you keep decreasing, it isn't extending further into "raw," it's retracing the positive range in reverse. This app uses two text encoders, CLIP-L and CLIP-G, and they retrace at different points: CLIP-L loops back on itself by -14/+11, while CLIP-G keeps producing new results all the way to -34/+31. So past ±11-14, only CLIP-G is still shifting the result, while CLIP-L has started repeating a layer it already showed you closer to zero.
    - SageAttention speeds up generation by quantizing part of the attention math to lower precision (int8/fp8) instead of running it in full fp16/bf16. In practice this means noticeably faster steps with lower VRAM overhead, especially on newer NVIDIA GPUs.
    
    Other usage tips of InstantID:
    - If you're not satisfied with the similarity, try increasing the weight of "IdentityNet Strength" and "Image adapter strength".
    - If you feel that the saturation/contrast is too high, first decrease the "Image adapter strength". If it remains too high, decrease the "IdentityNet Strength".
    - If you find that text control is not as expected, decrease "Image adapter strength".
    - If you find that the style or generated images are not good enough, try another model.
    - If you're having trouble detecting faces, try changing the "Face Detection Size" setting or try another input photo.
    """
    ctrl_enter_js = """
    () => {
        document.addEventListener("keydown", (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
                e.preventDefault();
                const btn = document.querySelector("#generate_btn_settings button, button#generate_btn_settings");
                if (btn) {
                    btn.click();
                }
            }
        });

        document.addEventListener("keydown", (e) => {
            if (!(e.ctrlKey || e.metaKey)) return;
            if (e.key !== "ArrowUp" && e.key !== "ArrowDown") return;

            const target = e.target;
            if (!target || target.tagName !== "TEXTAREA") return;
            if (!target.closest("#prompt_textbox, #negative_prompt_textbox")) return;

            e.preventDefault();

            const text = target.value;
            let start = target.selectionStart;
            let end = target.selectionEnd;

            if (start === end) {
                const isWordChar = (c) => c !== undefined && !/[\\s,()\\[\\]{}]/.test(c);
                while (start > 0 && isWordChar(text[start - 1])) start--;
                while (end < text.length && isWordChar(text[end])) end++;
            }
            if (start === end) return;

            let wrapStart = start;
            let wrapEnd = end;
            let inner = text.slice(start, end);
            let weight = null;
            if (text[start - 1] === "(") {
                const after = text.slice(end);
                const m = after.match(/^:([0-9]*\\.?[0-9]+)\\)/);
                if (m) {
                    weight = parseFloat(m[1]);
                    wrapStart = start - 1;
                    wrapEnd = end + m[0].length;
                }
            }

            const step = 0.1;
            const delta = e.key === "ArrowUp" ? step : -step;
            let newWeight = Math.round(((weight !== null ? weight : 1.0) + delta) * 100) / 100;
            newWeight = Math.max(0.1, newWeight);

            let newText, newSelStart, newSelEnd;
            if (Math.abs(newWeight - 1.0) < 0.001) {
                newText = text.slice(0, wrapStart) + inner + text.slice(wrapEnd);
                newSelStart = wrapStart;
                newSelEnd = wrapStart + inner.length;
            } else {
                const replacement = "(" + inner + ":" + newWeight.toFixed(1) + ")";
                newText = text.slice(0, wrapStart) + replacement + text.slice(wrapEnd);
                newSelStart = wrapStart + 1;
                newSelEnd = newSelStart + inner.length;
            }

            target.value = newText;
            target.selectionStart = newSelStart;
            target.selectionEnd = newSelEnd;
            target.dispatchEvent(new Event("input", { bubbles: true }));
        });
    }
    """
    with gr.Blocks(title="InstantID Unlocked v8.9.3", js=ctrl_enter_js, css="""
    #gen_gallery:not(.fullscreen) {
        max-height: 400px !important;
    }
    #gen_gallery:not(.fullscreen) .grid-wrap {
        max-height: 400px !important;
        overflow-y: auto !important;
        box-sizing: border-box !important;
    }
    #gen_gallery:not(.fullscreen) .grid-container > * {
        height: 384px !important;
    }
    #gen_gallery .icon-wrap,
    #gen_gallery .wrap svg {
        display: none !important;
    }
    #gen_gallery .wrap.default:not(:has(.error)):not(:has(.progress-level-inner))::before,
    #gen_gallery .wrap.generating:not(:has(.error)):not(:has(.progress-level-inner))::before {
        content: "Loading, please wait...";
        display: block;
        text-align: center;
        font-size: 16px;
        color: var(--body-text-color);
        padding: 16px;
    }
    #multi_ref_gallery:not(.fullscreen) {
        max-height: 230px !important;
    }
    #multi_ref_gallery:not(.fullscreen) .grid-wrap {
        max-height: 230px !important;
        overflow-y: auto !important;
        box-sizing: border-box !important;
    }
    .apply-fields-custom {
        background: #1d4ed8 !important;
        color: white !important;
        border: none !important;
    }
    .apply-fields-custom:hover {
        background: #1e40af !important;
    }
    """) as gui:
        with gr.Row():
            with gr.Column(scale=1):
                with gr.Row():
                    model_name = gr.Dropdown(
                        choices=AVAILABLE_MODELS,
                        value=DEFAULT_MODEL,
                        show_label=False,
                        container=False,
                        allow_custom_value=True,
                        scale=5
                    )
                    refresh_models = gr.Button("🔄", scale=0, min_width=40, elem_classes="toolbutton")
            with gr.Column(scale=1):
                schedulers = [
                    "DPMSolverMultistepScheduler",
                    "DPMSolverMultistepScheduler-SDE",
                    "DPMSolverMultistepScheduler-Karras",
                    "DPMSolverMultistepScheduler-Karras-SDE",
                    "DPMSolverMultistepScheduler-Exponential",
                    "DPMSolverMultistepScheduler-Exponential-SDE",
                    "DPMSolverMultistepScheduler-Beta",
                    "DPMSolverMultistepScheduler-Beta-SDE",
                    "DPMSolverSinglestepScheduler",
                    "DPMSolverSinglestepScheduler-SDE",
                    "DPMSolverSinglestepScheduler-Karras",
                    "DPMSolverSinglestepScheduler-Karras-SDE",
                    "DPMSolverSinglestepScheduler-Exponential",
                    "DPMSolverSinglestepScheduler-Exponential-SDE",
                    "DPMSolverSinglestepScheduler-Beta",
                    "DPMSolverSinglestepScheduler-Beta-SDE",
                    "DPMSolverSDEScheduler",
                    "DPMSolverSDEScheduler-Karras",
                    "DPMSolverSDEScheduler-Exponential",
                    "DPMSolverSDEScheduler-Beta",
                    "KDPM2DiscreteScheduler",
                    "KDPM2DiscreteScheduler-Karras",
                    "KDPM2DiscreteScheduler-Exponential",
                    "KDPM2DiscreteScheduler-Beta",
                    "KDPM2AncestralDiscreteScheduler",
                    "KDPM2AncestralDiscreteScheduler-Karras",
                    "KDPM2AncestralDiscreteScheduler-Exponential",
                    "KDPM2AncestralDiscreteScheduler-Beta",
                    "EulerDiscreteScheduler",
                    "EulerDiscreteScheduler-Karras",
                    "EulerDiscreteScheduler-Exponential",
                    "EulerDiscreteScheduler-Beta",
                    "EulerAncestralDiscreteScheduler",
                    "HeunDiscreteScheduler",
                    "HeunDiscreteScheduler-Karras",
                    "HeunDiscreteScheduler-Exponential",
                    "HeunDiscreteScheduler-Beta",
                    "DEISMultistepScheduler",
                    "DEISMultistepScheduler-Karras",
                    "DEISMultistepScheduler-Exponential",
                    "DEISMultistepScheduler-Beta",
                    "LMSDiscreteScheduler",
                    "LMSDiscreteScheduler-Karras",
                    "LMSDiscreteScheduler-Exponential",
                    "LMSDiscreteScheduler-Beta",
                    "UniPCMultistepScheduler",
                    "UniPCMultistepScheduler-Karras",
                    "UniPCMultistepScheduler-Exponential",
                    "UniPCMultistepScheduler-Beta",
                    "DDIMScheduler",
                    "DDPMScheduler",
                    "LCMScheduler",
                    ]
                with gr.Row():
                    scheduler = gr.Dropdown(
                        choices=schedulers,
                        value="DPMSolverMultistepScheduler",
                        container=False
                    )
            def refresh_model_list():
                global AVAILABLE_MODELS
                AVAILABLE_MODELS = get_available_models()
                return gr.update(choices=AVAILABLE_MODELS)

            refresh_models.click(
                fn=refresh_model_list,
                outputs=model_name,
                queue=False
            )

        with gr.Row():
            with gr.Column():
                with gr.Row():
                    with gr.Column():
                        with gr.Group():
                            face_file = gr.Image(
                                label="Upload a photo containing a face", height=400, type="filepath"
                            )
                            enable_multi_ref = gr.Checkbox(
                                label="Add more face images (averages face embeddings)",
                                value=False,
                            )
                            normalize_multi_ref = gr.Checkbox(
                                label="Normalize averaged embedding (recommended)",
                                value=True,
                                visible=False,
                            )
                            additional_face_image_file_types = [
                                    ".jpe", ".jpg", ".jpeg", ".gif", ".png", ".bmp", ".ico",
                                    ".svg", ".svgz", ".tif", ".tiff", ".ai", ".drw", ".pct",
                                    ".psp", ".xcf", ".psd", ".raw", ".webp", ".heic", ".avif", ".jxl", "image",
                                ]
                            multi_ref_files = gr.Gallery(
                                label="Additional face images",
                                visible=False,
                                columns=4,
                                height=230,
                                object_fit="cover",
                                type="filepath",
                                show_label=False,
                                interactive=True,
                                file_types=additional_face_image_file_types,
                                elem_id="multi_ref_gallery",
                            )
                            selected_ref_index = gr.State(None)
                            remove_selected_ref_btn = gr.Button(
                                "🗑 Remove selected face image (click a thumbnail above first)",
                                size="sm",
                                visible=False,
                            )
                            add_more_ref_btn = gr.UploadButton(
                                "➕ Add more faces",
                                file_count="multiple",
                                type="filepath",
                                size="sm",
                                visible=False,
                                file_types=additional_face_image_file_types,
                            )
                            def toggle_multi_ref_section(enabled, gallery_value):
                                has_items = enabled and bool(gallery_value)
                                return (
                                    gr.update(visible=enabled),
                                    gr.update(visible=has_items),
                                    gr.update(visible=has_items),
                                    gr.update(visible=enabled),
                                )
                            enable_multi_ref.change(
                                fn=toggle_multi_ref_section,
                                inputs=[enable_multi_ref, multi_ref_files],
                                outputs=[multi_ref_files, remove_selected_ref_btn, add_more_ref_btn, normalize_multi_ref],
                                queue=False,
                            )
                            def track_ref_selection(evt: gr.SelectData):
                                return evt.index
                            multi_ref_files.select(
                                fn=track_ref_selection,
                                inputs=None,
                                outputs=selected_ref_index,
                                queue=False,
                            )
                            def toggle_ref_buttons(gallery_value):
                                visible = bool(gallery_value)
                                return gr.update(visible=visible), gr.update(visible=visible)
                            multi_ref_files.change(
                                fn=toggle_ref_buttons,
                                inputs=multi_ref_files,
                                outputs=[remove_selected_ref_btn, add_more_ref_btn],
                                queue=False,
                            )
                            def add_more_additional_images(new_files, gallery_value):
                                existing = list(gallery_value) if gallery_value else []
                                newly_added = list(new_files) if new_files else []
                                return existing + newly_added
                            add_more_ref_btn.upload(
                                fn=add_more_additional_images,
                                inputs=[add_more_ref_btn, multi_ref_files],
                                outputs=multi_ref_files,
                                queue=False,
                            )
                            def remove_selected_additional_image(gallery_value, selected_index):
                                if gallery_value is None or selected_index is None:
                                    still_has_items = bool(gallery_value)
                                    return gallery_value, None, gr.update(visible=still_has_items), gr.update(visible=still_has_items)
                                if selected_index < 0 or selected_index >= len(gallery_value):
                                    still_has_items = bool(gallery_value)
                                    return gallery_value, None, gr.update(visible=still_has_items), gr.update(visible=still_has_items)
                                new_value = list(gallery_value)
                                del new_value[selected_index]
                                still_has_items = bool(new_value)
                                return new_value, None, gr.update(visible=still_has_items), gr.update(visible=still_has_items)
                            remove_selected_ref_btn.click(
                                fn=remove_selected_additional_image,
                                inputs=[multi_ref_files, selected_ref_index],
                                outputs=[multi_ref_files, selected_ref_index, remove_selected_ref_btn, add_more_ref_btn],
                                queue=False,
                            )
                    pose_file = gr.Image(
                        label="Reference pose image (Optional)",
                        height=400,
                        type="filepath"
                    )
                    def update_img_resolution(img_path, default_label):
                        if img_path:
                            try:
                                with Image.open(img_path) as img:
                                    w, h = img.size
                                return gr.update(label=f"{default_label} ({w}x{h})")
                            except Exception:
                                pass
                        return gr.update(label=default_label)
                    face_file.upload(
                        fn=lambda x: update_img_resolution(x, "Upload a photo containing a face"),
                        inputs=face_file,
                        outputs=face_file,
                        queue=False
                    )
                    face_file.clear(
                        fn=lambda: gr.update(label="Upload a photo containing a face"),
                        inputs=None,
                        outputs=face_file,
                        queue=False
                    )
                    pose_file.upload(
                        fn=lambda x: update_img_resolution(x, "Reference pose image (Optional)"),
                        inputs=pose_file,
                        outputs=pose_file,
                        queue=False
                    )
                    pose_file.clear(
                        fn=lambda: gr.update(label="Reference pose image (Optional)"),
                        inputs=None,
                        outputs=pose_file,
                        queue=False
                    )
                prompt = gr.Textbox(
                    label="Prompt",
                    info="Giving a simple prompt is usually enough. You can highlight text & use Ctrl + ↑/↓ keys to change the weight.",
                    placeholder="A man/woman/girl/boy in/with/as etc.",
                    value="",
                    elem_id="prompt_textbox",
                )
                negative_prompt = gr.Textbox(
                    label="Negative Prompt",
                    placeholder="You can select a negative prompt profile from the settings accordion below.",
                    value=NEGATIVE_PROMPT_PRESETS["Default Negative Profile"],
                    elem_id="negative_prompt_textbox",
                )
                with gr.Accordion("📋 Style templates and other settings", open=False):
                    with gr.Group():
                        style = gr.Dropdown(
                            label="Style templates",
                            choices=STYLE_NAMES,
                            value=DEFAULT_STYLE_NAME,
                            info="Selecting a style empties the prompt and negative prompt fields because styles have their own. You can add to both fields."
                        )
                        apply_selected_style_btn = gr.Button(
                            "⇄ Insert selected style text into prompt & negative prompt fields. '(No style)' will be selected after clicking this.",
                            size="sm",
                            variant="secondary"
                        )
                        style.change(
                            fn=on_style_change,
                            inputs=style,
                            outputs=[prompt, negative_prompt],
                            queue=False
                        )
                    feeling_lucky_btn = gr.Button("🎰 Insert a random style from the style templates into prompt & negative prompt fields.", size="md", variant="secondary")
                    prompt_replacement = gr.Radio(
                        label="Replace '{prompt}' in Style templates with this (and if the prompt field is empty or a style inserted):",
                        choices=["person", "girl", "woman", "boy", "man", "Empty (none)"],
                        value="person"
                    )
                    prompt_replacement.change(
                        fn=lambda _: None,
                        inputs=prompt_replacement,
                        outputs=[],
                        queue=False
                    )
                    apply_selected_style_btn.click(
                        fn=apply_selected_style,
                        inputs=[style, prompt_replacement],
                        outputs=[prompt, negative_prompt, style],
                        queue=False
                    )
                    feeling_lucky_btn.click(
                        fn=get_random_style_prompt,
                        inputs=[prompt_replacement],
                        outputs=[prompt, negative_prompt, style],
                        queue=False
                    )
                    with gr.Group():
                        negative_prompt_preset = gr.Dropdown(
                            choices=list(NEGATIVE_PROMPT_PRESETS.keys()),
                            value="Default Negative Profile",
                            show_label=False,
                            container=False
                        )
                        apply_negative_profile_btn = gr.Button(
                            "Apply selected negative prompt profile", 
                            size="sm",
                            min_width=200
                        )
                        negative_prompt_preset.change(
                            fn=lambda x: NEGATIVE_PROMPT_PRESETS[x],
                            inputs=negative_prompt_preset,
                            outputs=negative_prompt,
                            queue=False,
                        )
                        def apply_selected_negative_profile(selected_negative_profile):
                            return NEGATIVE_PROMPT_PRESETS[selected_negative_profile]

                        apply_negative_profile_btn.click(
                            fn=apply_selected_negative_profile,
                            inputs=negative_prompt_preset,
                            outputs=negative_prompt,
                            queue=False,
                        )
                    with gr.Row():
                        generate_alt_2 = gr.Button("Generate (Extra Settings Section Button)", variant="primary", elem_id="generate_btn_settings")
                        stop_btn_2 = gr.Button("⏹", scale=0, min_width=60, variant="stop")
                        open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                        open_folder_btn.click(
                            fn=open_output_folder,
                            inputs=[],
                            outputs=[],
                            queue=False
                        )
                    with gr.Row():
                        file_prefix = gr.Textbox(
                            label="Saved file name prefix.",
                            value=DEFAULT_FILE_PREFIX,
                            placeholder="Enter your custom prefix (e.g., 'myprefix' becomes myprefix_0.png) etc."
                        )
                with gr.Group():
                    resize_max_side_slider = gr.Slider(
                        label="Output Resolution (max_side).",
                        minimum=256,
                        maximum=8192,
                        step=8,
                        value=1280,
                        show_label=False,
                        info="Output Resolution (max_side). Max width/height resizing in pixels. Using Hires Fix is preferable to raising this too high.",
                    )
                    with gr.Accordion("📐 Custom resolution, resize step and square padding (advanced, adjust only if needed)", open=False) as resolution_settings_accordion:
                        with gr.Group():
                            enable_custom_resize = gr.Checkbox(
                                label="📏 Enable custom resolution (disables & overrides all other resolution & resizing options)",
                                value=False
                            )
                            custom_resize_width = gr.Slider(
                                label="↔️ Custom Width",
                                minimum=64,
                                maximum=16384,
                                step=8,
                                value=960,
                                visible=False,
                                interactive=True
                            )
                            custom_resize_height = gr.Slider(
                                label="↕️ Custom Height",
                                minimum=64,
                                maximum=16384,
                                step=8,
                                value=1280,
                                visible=False,
                                interactive=True
                            )
                            with gr.Row():
                                ratio_base_pixel_number = gr.Radio(
                                    label="Resize step in pixels for aspect ratio (8 = most accurate)",
                                    choices=[8, 16, 32, 64],
                                    value=8,
                                )
                                pad_to_max_checkbox = gr.Checkbox(
                                    label="Square padding (keeps subject proportions intact)",
                                    value=False
                                )
                            def toggle_custom_resize_controls(value):
                                return (
                                    gr.update(visible=value),
                                    gr.update(visible=value),
                                    gr.update(interactive=not value),
                                    gr.update(interactive=not value),
                                    gr.update(interactive=not value)
                                )
                            enable_custom_resize.change(
                                fn=toggle_custom_resize_controls,
                                inputs=enable_custom_resize,
                                outputs=[
                                    custom_resize_width,
                                    custom_resize_height,
                                    resize_max_side_slider,
                                    pad_to_max_checkbox,
                                    ratio_base_pixel_number
                                ],
                                queue=False
                            )
                            def toggle_resize_step(ratio_base_pixel_number):
                                return gr.update(step=ratio_base_pixel_number)
                            ratio_base_pixel_number.change(
                                fn=toggle_resize_step,
                                inputs=ratio_base_pixel_number,
                                outputs=[resize_max_side_slider],
                                queue=False
                            )
                with gr.Row():
                    generate = gr.Button("Generate (Control + Enter)", scale=8, variant="primary")
                    stop_btn = gr.Button("⏹", scale=0, min_width=60, variant="stop")
                    num_outputs = gr.Number(
                        value=1,
                        step=1,
                        minimum=1,
                        scale=0,
                        min_width=70,
                        container=False,
                        show_label=False
                    )
                    open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                    open_folder_btn.click(
                        fn=open_output_folder,
                        inputs=[],
                        outputs=[],
                        queue=False
                    )
                with gr.Group():
                    identitynet_strength_ratio = gr.Slider(
                        label="IdentityNet strength (weight of face fidelity retention from the input photo)",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.7,
                    )
                    adapter_strength_ratio = gr.Slider(
                        label="Image adapter strength (weight of detail retention from the input photo)",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.6,
                    )
                    with gr.Accordion("📊 IdentityNet & Image adapter start/end ranges (controls when each begins and stops applying during generation)", open=False) as adapters_range_accordion:
                        with gr.Group():
                            with gr.Row():
                                identitynet_start_slider = gr.Slider(
                                    label="IdentityNet Start",
                                    minimum=0.0,
                                    maximum=0.95,
                                    step=0.01,
                                    value=0.0,
                                    show_label=False,
                                    info="IdentityNet Start Step (%)",
                                )
                                identitynet_end_slider = gr.Slider(
                                    label="IdentityNet End",
                                    minimum=0.0,
                                    maximum=1.0,
                                    step=0.01,
                                    value=1.0,
                                    show_label=False,
                                    info="IdentityNet End Step (%)",
                                )
                            with gr.Row():
                                adapter_start_slider = gr.Slider(
                                    label="Image Adapter Start",
                                    minimum=0.0,
                                    maximum=0.95,
                                    step=0.01,
                                    value=0.0,
                                    show_label=False,
                                    info="Image Adapter Start Step (%)",
                                )
                                adapter_end_slider = gr.Slider(
                                    label="Image Adapter End",
                                    minimum=0.0,
                                    maximum=1.0,
                                    step=0.01,
                                    value=1.0,
                                    show_label=False,
                                    info="Image Adapter End Step (%)",
                                )
                            adapter_smooth_transition = gr.Checkbox(
                                label="Smooth start/end transition via fractional step blending (close values e.g. 0.1 vs 0.11 produce distinct results)",
                                value=True,
                            )
                            def toggle_range_slider_step(smooth_enabled):
                                new_step = 0.01 if smooth_enabled else 0.05
                                return (
                                    gr.update(step=new_step),
                                    gr.update(step=new_step),
                                    gr.update(step=new_step),
                                    gr.update(step=new_step),
                                )
                            adapter_smooth_transition.change(
                                fn=toggle_range_slider_step,
                                inputs=adapter_smooth_transition,
                                outputs=[
                                    identitynet_start_slider,
                                    identitynet_end_slider,
                                    adapter_start_slider,
                                    adapter_end_slider,
                                ],
                                queue=False
                            )
                with gr.Accordion("🛠️ Advanced Options", open=False) as advanced_settings_accordion:
                    with gr.Row():
                        clip_skip = gr.Slider(
                            label="Clip Skip (adjusts how many CLIP layers are used when reading the prompt). See usage tips.",
                            minimum=-34,
                            maximum=31,
                            step=1,
                            value=0,
                        )
                    with gr.Row():
                        weight_application_method = gr.Radio(
                            label="Weight application method for (word:weight). You can read about it in the usage tips below.",
                            choices=[
                                "Original InstantID per-token",
                                "ForgeUI per-encoder rescale",
                                "ForgeUI global rescale",
                                "ComfyUI (blank prompt interpolation)",
                            ],
                            value="Original InstantID per-token",
                        )
                    with gr.Group():
                        with gr.Row():
                            kps_brightness_slider = gr.Slider(
                                label="Pose Skeleton (KPS) Brightness",
                                minimum=0.0,
                                maximum=1.0,
                                step=0.05,
                                value=0.6,
                                info="Skeleton KPS brightness for face landmarks.",
                                show_label=False
                            )
                            enable_upscaler_prescale = gr.Checkbox(
                                label="Prescale images for Hires Fix upscalers",
                                value=False,
                                info="Speeds up upscaling. Visual results vary by upscaler model.",
                            )
                        with gr.Row():
                            upscaler_prescale_headroom = gr.Slider(
                                label="Prescale Headroom",
                                minimum=1.05,
                                maximum=1.95,
                                step=0.05,
                                value=1.3,
                                show_label=False,
                                info="Prescale Headroom (Extra margin before upscaling. Higher values shrink the source less, closer to original behavior)",
                                visible=False,
                            )
                            def toggle_upscaler_prescale_ui(enable):
                                return gr.update(visible=enable)
                            enable_upscaler_prescale.change(
                                fn=toggle_upscaler_prescale_ui,
                                inputs=enable_upscaler_prescale,
                                outputs=upscaler_prescale_headroom,
                                queue=False
                            )
                    with gr.Group():
                        with gr.Row():
                            enable_vae_tiling = gr.Checkbox(
                                label="Enable VAE Tiling",
                                value=True,
                                scale=2
                            )
                            enable_cpu_offloading = gr.Checkbox(
                                label="CPU Offload (saves VRAM)",
                                value=False,
                                scale=2
                            )
                            enable_sage_attention = gr.Checkbox(
                                label="Enable SageAttention Optimization",
                                value=False,
                                scale=3
                            )
                    with gr.Group():
                        with gr.Row():
                            resize_mode_dropdown = gr.Dropdown(
                                label="Resize Interpolation Mode (LANCZOS, BILINEAR and HAMMING are usually the best)",
                                choices=[
                                    "LANCZOS", "BILINEAR", "HAMMING", "BICUBIC", "BOX", "NEAREST"
                                ],
                                value="LANCZOS",
                                scale=3
                            )
                            rng_source = gr.Radio(
                                label="Noise RNG device:",
                                choices=["GPU", "CPU"],
                                value="GPU",
                                scale=1
                            )
                with gr.Accordion("🎚️ Controlnet", open=False) as controlnet_accordion:
                    controlnet_selection = gr.CheckboxGroup(
                        ["pose", "canny", "depth"], value=[], show_label=False,
                        info="Use pose for skeleton inference, canny for edge detection, and depth for depth map estimation."
                    )
                    pose_strength = gr.Slider(
                        label="Pose strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.30,
                    )
                    canny_strength = gr.Slider(
                        label="Canny strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.30,
                    )
                    depth_strength = gr.Slider(
                        label="Depth strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.30,
                    )
                with gr.Group():
                    with gr.Row():
                        guidance_scale = gr.Slider(
                            label="Guidance scale (CFG)",
                            minimum=1.0,
                            maximum=20.0,
                            step=0.1,
                            value=4,
                        )
                        num_steps = gr.Slider(
                            label="Sampling steps",
                            minimum=1,
                            maximum=200,
                            step=1,
                            value=20,
                        )
                with gr.Row():
                    randomize_seed = gr.Checkbox(label="Randomize seed", scale=1, value=True)
                    seed = gr.Number(
                        minimum=0,
                        maximum=MAX_SEED,
                        step=1,
                        value=12345,
                        show_label=False,
                        scale=2
                    )
                    det_size_name = gr.Dropdown(
                        label="Face Detection Size",
                        choices=list(DET_SIZE_OPTIONS.keys()),
                        value="640x640 (default)",
                        info="Face Detection Size. Only change this if you get 'No face detected'.",
                        show_label=False,
                        scale=4
                    )
                with gr.Row():
                    enhance_face_region = gr.Checkbox(label="Enhance non-face region", scale=2, value=True)
                    enhance_strength = gr.Dropdown(
                        label="Non-Face Region Mask Size",
                        choices=["Default", "Balanced", "High", "Custom"],
                        value="Balanced",
                        scale=4,
                        info="Larger values retain more from the input image around the face (e.g., hairstyle)."
                    )
                    custom_enhance_padding = gr.Slider(
                        label="Custom enhancement padding (%)",
                        minimum=0.0,
                        maximum=1.0,
                        step=0.05,
                        value=0.15,
                        visible=False,
                        scale=3,
                        interactive=True
                    )
                    def toggle_custom_padding_dropdown(value):
                        return gr.update(visible=(value == "Custom"))

                    enhance_strength.change(
                        fn=toggle_custom_padding_dropdown,
                        inputs=enhance_strength,
                        outputs=custom_enhance_padding,
                        queue=False
                    )
                with gr.Accordion("🔍 Standalone Image Upscaler with GFPGAN (don't use while an image is being generated)", open=False) as standalone_upscaler_accordion:
                    with gr.Row():
                        standalone_upscale_input = gr.Image(
                            label="Image to Upscale",
                            type="filepath",
                            height=300,
                            scale=1
                        )
                        standalone_upscale_output = gr.Image(
                            label="Upscaled Result",
                            type="filepath",
                            height=300,
                            interactive=False,
                            scale=1
                        )
                    with gr.Row():
                        standalone_upscaler_model = gr.Dropdown(
                            label="Upscaler Model",
                            choices=get_available_upscalers() or [DEFAULT_UPSCALER],
                            value=DEFAULT_UPSCALER if DEFAULT_UPSCALER in get_available_upscalers() else (get_available_upscalers()[0] if get_available_upscalers() else DEFAULT_UPSCALER),
                            allow_custom_value=True,
                            info=f"Upscaler model. Place in models/Upscalers",
                            show_label=False,
                            scale=4
                        )
                        refresh_standalone_upscalers = gr.Button("🔄", scale=0, min_width=40)
                    with gr.Row():
                        standalone_upscale_by = gr.Slider(
                            label="Upscale By",
                            minimum=1.0,
                            maximum=8.0,
                            step=0.1,
                            value=2.0,
                            info="Final image size = original size * this factor.",
                            scale=4
                        )
                    with gr.Row():
                        standalone_restore_faces = gr.Checkbox(
                            label="Restore Faces with GFPGAN",
                            value=True,
                            scale=1
                        )
                        standalone_gfpgan_weight = gr.Slider(
                            label="GFPGAN Strength",
                            minimum=0.0,
                            maximum=1.0,
                            step=0.05,
                            value=0.5,
                            info="Higher values can distort face features.",
                            scale=2
                        )
                    with gr.Row():
                        run_standalone_upscale_btn = gr.Button("Upscale Image", variant="primary")
                    standalone_upscale_status = gr.Markdown("")

                    with gr.Row():
                        delete_pipe_checkbox = gr.Checkbox(
                            label="When 'Upscale Image' is clicked, unload the main pipelines (models) from VRAM for faster upscaling.",
                            value=True
                        )
                    def refresh_standalone_upscaler_list():
                        choices = get_available_upscalers() or [DEFAULT_UPSCALER]
                        return gr.update(choices=choices)

                    refresh_standalone_upscalers.click(
                        fn=refresh_standalone_upscaler_list,
                        outputs=standalone_upscaler_model,
                        queue=False
                    )

                    standalone_upscale_input.upload(
                        fn=lambda x: update_img_resolution(x, "Image to Upscale"),
                        inputs=standalone_upscale_input,
                        outputs=standalone_upscale_input,
                        queue=False
                    )
                    standalone_upscale_input.clear(
                        fn=lambda: gr.update(label="Image to Upscale"),
                        inputs=None,
                        outputs=standalone_upscale_input,
                        queue=False
                    )

                    def run_standalone_upscale(input_image_path, upscaler_name, upscale_by, delete_pipe_checkbox, restore_faces, gfpgan_weight, progress=gr.Progress()):
                        nonlocal pipe, hires_sibling_pipe

                        if not input_image_path:
                            raise gr.Error("Please provide an image to upscale first.")
                        if not upscaler_name:
                            raise gr.Error("Please select an upscaler model.")

                        if delete_pipe_checkbox:
                            if pipe is not None:
                                del pipe
                                pipe = None
                            if hires_sibling_pipe is not None:
                                del hires_sibling_pipe
                                hires_sibling_pipe = None

                            global cached_controlnet_models
                            for k in list(cached_controlnet_models.keys()):
                                del cached_controlnet_models[k]

                            gc.collect()
                            torch.cuda.empty_cache()

                        progress(0, desc="Loading upscaler model...")
                        model = load_upscaler_model(upscaler_name)

                        progress(0.2, desc="Upscaling image...")
                        input_image = load_image(input_image_path)
                        orig_width, orig_height = input_image.size
                        target_width = max(1, round(orig_width * upscale_by))
                        target_height = max(1, round(orig_height * upscale_by))

                        torch.cuda.empty_cache()
                        print(f"\nStandalone Image Upscaler: upscaling image by {upscale_by}x from {orig_width}x{orig_height} to {target_width}x{target_height} using '{upscaler_name}'...\n")

                        upscaled = run_upscaler_model(model, input_image)

                        if upscaled.size != (target_width, target_height):
                            progress(0.8, desc="Resizing to target scale...")
                            upscaled = upscaled.resize((target_width, target_height), PIL.Image.LANCZOS)

                        if restore_faces:
                            progress(0.85, desc="Restoring faces with GFPGAN...")
                            print("Running GFPGAN face restoration...")
                            upscaled = restore_faces_gfpgan(upscaled, weight=gfpgan_weight)
                            torch.cuda.empty_cache()

                        progress(0.9, desc="Saving result...")
                        saved_paths = save_images([upscaled], output_dir=os.path.join("output", "upscaled_images"), prefix="InstantID_Upscaled_")

                        torch.cuda.empty_cache()
                        print(f"Finished upscaling image ({orig_width}x{orig_height} -> {target_width}x{target_height}). Saved to {saved_paths[0]}\n")

                        return gr.update(value=saved_paths[0], label=f"Upscaled Result ({target_width}x{target_height})"), f"✅ Saved to `{saved_paths[0]}` ({target_width}x{target_height})"

                    run_standalone_upscale_btn.click(
                        fn=run_standalone_upscale,
                        inputs=[standalone_upscale_input, standalone_upscaler_model, standalone_upscale_by, delete_pipe_checkbox, standalone_restore_faces, standalone_gfpgan_weight],
                        outputs=[standalone_upscale_output, standalone_upscale_status]
                    )
                with gr.Row():
                    generate_alt_3 = gr.Button("Generate (Extra Bottom Section Button)", variant="primary")
                    stop_btn_3 = gr.Button("⏹", scale=0, min_width=60, variant="stop")
                    open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                    open_folder_btn.click(
                        fn=open_output_folder,
                        inputs=[],
                        outputs=[],
                        queue=False
                    )
            with gr.Column(scale=1):
                gallery = gr.Gallery(label="Generation preview", height=400, object_fit="contain", elem_id="gen_gallery")
                with gr.Row():
                    generate_alt = gr.Button("Generate (Extra Right Side Button)", variant="primary")
                    stop_btn_alt = gr.Button("⏹", scale=0, min_width=60, variant="stop")
                    open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                    open_folder_btn.click(
                        fn=open_output_folder,
                        inputs=[],
                        outputs=[],
                        queue=False
                    )
                with gr.Group():
                    with gr.Row():
                        enable_img2img = gr.Checkbox(
                            label="Enable img2img mode",
                            value=False,
                            info="Preserves more details from input.",
                            scale=2
                        )
                        strength = gr.Slider(label="img2img Denoising Strength", minimum=0.05, maximum=1.0, value=0.95, step=0.05, visible=False, show_label=False, scale=5, info="Denoising Strength. Adjust for more control over clothing style, pose, etc.")
                    with gr.Row(visible=False) as img2img_upscaler_row:
                        enable_img2img_upscaler = gr.Checkbox(
                            label="Enable i2i upscaler (optional, few use cases)",
                            value=False,
                            info="Mainly for a denoising value of 0.15 - 0.2, best to use with DMD2 LoRA and LCMScheduler.",
                            scale=4
                        )
                        img2img_upscaler = gr.Dropdown(
                            label="Upscaler Model",
                            choices=["Latent (bicubic)"] + (get_available_upscalers() or [DEFAULT_UPSCALER]),
                            value=DEFAULT_UPSCALER if DEFAULT_UPSCALER in get_available_upscalers() else (get_available_upscalers()[0] if get_available_upscalers() else DEFAULT_UPSCALER),
                            allow_custom_value=True,
                            info=f"Upscaler model. Place in models/Upscalers",
                            visible=False,
                            show_label=False,
                            scale=5
                        )
                        refresh_img2img_upscalers = gr.Button("🔄", scale=0, min_width=40, visible=False)

                    def toggle_img2img(enable):
                        return gr.update(visible=enable), gr.update(visible=enable)

                    enable_img2img.change(toggle_img2img, inputs=enable_img2img, outputs=[strength, img2img_upscaler_row], queue=False)

                    def toggle_img2img_upscaler_ui(enable):
                        return gr.update(visible=enable), gr.update(visible=enable)

                    enable_img2img_upscaler.change(
                        fn=toggle_img2img_upscaler_ui,
                        inputs=enable_img2img_upscaler,
                        outputs=[img2img_upscaler, refresh_img2img_upscalers],
                        queue=False
                    )

                    def refresh_img2img_upscaler_list():
                        choices = ["Latent (bicubic)"] + (get_available_upscalers() or [DEFAULT_UPSCALER])
                        return gr.update(choices=choices)

                    refresh_img2img_upscalers.click(
                        fn=refresh_img2img_upscaler_list,
                        outputs=img2img_upscaler,
                        queue=False
                    )

                with gr.Group():
                    with gr.Row():
                        enable_hires_fix = gr.Checkbox(label="Enable Hires Fix", value=False, scale=1)
                        hires_upscaler = gr.Dropdown(
                            label="Upscaler Model",
                            choices=["Pixel resize (Lanczos)", "Latent (bicubic)"] + (get_available_upscalers() or [DEFAULT_UPSCALER]),
                            value=DEFAULT_UPSCALER if DEFAULT_UPSCALER in get_available_upscalers() else (get_available_upscalers()[0] if get_available_upscalers() else DEFAULT_UPSCALER),
                            allow_custom_value=True,
                            info=f"Upscaler model. Place in models/Upscalers",
                            visible=False,
                            show_label=False,
                            scale=4
                        )
                        refresh_hires_upscalers = gr.Button("🔄", scale=0, min_width=40, visible=False)
                        save_hires_original = gr.Checkbox(
                            label="Save non-upscaled too",
                            value=False,
                            visible=False,
                            scale=2
                        )
                    with gr.Row(visible=False) as hires_fix_row:
                        def _hires_round8(px):
                            return max(8, int(round(px / 8) * 8))

                        def _get_hires_info_text(max_side, use_custom, custom_w, custom_h, upscale_by):
                            if use_custom:
                                target_w = _hires_round8(custom_w * upscale_by)
                                target_h = _hires_round8(custom_h * upscale_by)
                                return f"Target = {target_w} x {target_h}px."
                            else:
                                target_px = _hires_round8(max_side * upscale_by)
                                return f"Target = max_side * this value = {target_px}px."

                        hires_upscale_by = gr.Slider(
                            label="Hires Upscale By",
                            minimum=1.0,
                            maximum=4.0,
                            step=0.05,
                            value=1.5,
                            info=_get_hires_info_text(resize_max_side_slider.value, enable_custom_resize.value, custom_resize_width.value, custom_resize_height.value, 1.5),
                            scale=3
                        )
                        def update_hires_upscale(max_side, upscale_by, use_custom, custom_w, custom_h):
                            return gr.update(
                                info=_get_hires_info_text(max_side, use_custom, custom_w, custom_h, upscale_by)
                            )

                        _hires_upscale_inputs = [resize_max_side_slider, hires_upscale_by, enable_custom_resize, custom_resize_width, custom_resize_height]

                        resize_max_side_slider.release(
                            fn=update_hires_upscale,
                            inputs=_hires_upscale_inputs,
                            outputs=[hires_upscale_by],
                            queue=False
                        )
                        hires_upscale_by.release(
                            fn=update_hires_upscale,
                            inputs=_hires_upscale_inputs,
                            outputs=[hires_upscale_by],
                            queue=False
                        )
                        enable_custom_resize.change(
                            fn=update_hires_upscale,
                            inputs=_hires_upscale_inputs,
                            outputs=[hires_upscale_by],
                            queue=False
                        )
                        custom_resize_width.release(
                            fn=update_hires_upscale,
                            inputs=_hires_upscale_inputs,
                            outputs=[hires_upscale_by],
                            queue=False
                        )
                        custom_resize_height.release(
                            fn=update_hires_upscale,
                            inputs=_hires_upscale_inputs,
                            outputs=[hires_upscale_by],
                            queue=False
                        )
                        hires_steps = gr.Slider(
                            label="Hires Steps",
                            minimum=0,
                            maximum=100,
                            step=1,
                            value=0,
                            info="0 = Auto (original steps * 1.4 * denoising strength).",
                            scale=3
                        )
                        hires_denoising_strength = gr.Slider(
                            label="Denoising Strength",
                            minimum=0.05,
                            maximum=1.0,
                            step=0.05,
                            value=0.35,
                            info="Lower preserves more of the upscaled image.",
                            scale=3
                        )

                    def toggle_hires_fix_ui(enable):
                        return gr.update(visible=enable), gr.update(visible=enable), gr.update(visible=enable), gr.update(visible=enable)

                    enable_hires_fix.change(
                        fn=toggle_hires_fix_ui,
                        inputs=enable_hires_fix,
                        outputs=[hires_upscaler, refresh_hires_upscalers, hires_fix_row, save_hires_original],
                        queue=False
                    )

                    def refresh_hires_upscaler_list():
                        choices = ["Pixel resize (Lanczos)", "Latent (bicubic)"] + (get_available_upscalers() or [DEFAULT_UPSCALER])
                        return gr.update(choices=choices)

                    refresh_hires_upscalers.click(
                        fn=refresh_hires_upscaler_list,
                        outputs=hires_upscaler,
                        queue=False
                    )
                with gr.Accordion("PNG Metadata Reader & Loader (for images generated with InstantID)", open=True):
                    with gr.Row():
                        metadata_input = gr.Image(
                            label="Drop PNG file here to read generation metadata",
                            type="filepath",
                            height=400
                        )
                        metadata_output = gr.Textbox(
                            label="Generation Metadata",
                            interactive=False,
                            lines=17,
                            max_lines=17
                        )
                    with gr.Row():
                        apply_metadata_btn = gr.Button("Apply to all fields (resets all fields if no generation metadata)", elem_classes="apply-fields-custom")
                    apply_lcm_profile_btn = gr.Button(
                        "⚡ Apply DMD2 LCM profile (LCMScheduler, CFG 1, 10 steps, and dmd2 sdxl lora in the first empty slot)",
                        size="sm",
                        variant="secondary"
                    )
                    metadata_input.upload(
                        fn=lambda x: (x, read_png_metadata(x) if x is not None else ""),
                        inputs=metadata_input,
                        outputs=[metadata_input, metadata_output],
                        queue=False
                    )
                with gr.Column():
                    enable_lora = gr.Checkbox(
                        label="Enable LoRA(s) from your Models\\Loras folder (only SDXL & its variants)",
                        value=False,
                    )
                    with gr.Row():
                        refresh_loras = gr.Button("🔄 Refresh LoRAs Lists", scale=2, elem_classes="toolbutton", visible=False)
                        clear_loras = gr.Button("♻️ Clear all LoRA selections", scale=1, elem_classes="toolbutton", visible=False)

                    with gr.Row(visible=False) as lora_row_1:
                        lora_selection = gr.Dropdown(
                            label="Select LoRA 1",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="1. Select the first LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale = gr.Slider(
                            label="LoRA 1 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=1.0,
                            info="Strength of the first LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_1 = gr.Checkbox(
                            label="Disable LoRA 1",
                            value=False,
                            scale=1
                        )

                    with gr.Row(visible=False) as lora_row_2:
                        lora_selection_2 = gr.Dropdown(
                            label="Select LoRA 2",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="2. Select a second LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_2 = gr.Slider(
                            label="LoRA 2 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the second LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_2 = gr.Checkbox(
                            label="Disable LoRA 2",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_3:
                        lora_selection_3 = gr.Dropdown(
                            label="Select LoRA 3",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="3. Select a third LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_3 = gr.Slider(
                            label="LoRA 3 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the third LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_3 = gr.Checkbox(
                            label="Disable LoRA 3",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_4:
                        lora_selection_4 = gr.Dropdown(
                            label="Select LoRA 4",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="4. Select a fourth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_4 = gr.Slider(
                            label="LoRA 4 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the fourth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_4 = gr.Checkbox(
                            label="Disable LoRA 4",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_5:
                        lora_selection_5 = gr.Dropdown(
                            label="Select LoRA 5",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="5. Select a fifth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_5 = gr.Slider(
                            label="LoRA 5 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the fifth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_5 = gr.Checkbox(
                            label="Disable LoRA 5",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_6:
                        lora_selection_6 = gr.Dropdown(
                            label="Select LoRA 6",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="6. Select a sixth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_6 = gr.Slider(
                            label="LoRA 6 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the sixth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_6 = gr.Checkbox(
                            label="Disable LoRA 6",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_7:
                        lora_selection_7 = gr.Dropdown(
                            label="Select LoRA 7",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="7. Select a seventh LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_7 = gr.Slider(
                            label="LoRA 7 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the seventh LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_7 = gr.Checkbox(
                            label="Disable LoRA 7",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_8:
                        lora_selection_8 = gr.Dropdown(
                            label="Select LoRA 8",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="8. Select an eighth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_8 = gr.Slider(
                            label="LoRA 8 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the eighth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_8 = gr.Checkbox(
                            label="Disable LoRA 8",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_9:
                        lora_selection_9 = gr.Dropdown(
                            label="Select LoRA 9",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="9. Select a ninth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_9 = gr.Slider(
                            label="LoRA 9 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the ninth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_9 = gr.Checkbox(
                            label="Disable LoRA 9",
                            value=False,
                            scale=1
                        )
                    with gr.Row(visible=False) as lora_row_10:
                        lora_selection_10 = gr.Dropdown(
                            label="Select LoRA 10",
                            choices=[""] + get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="10. Select a tenth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        lora_scale_10 = gr.Slider(
                            label="LoRA 10 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the tenth LoRA.",
                            show_label=False,
                            scale=3
                        )
                        disable_lora_10 = gr.Checkbox(
                            label="Disable LoRA 10",
                            value=False,
                            scale=1
                        )

                    disable_lora_1.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_1,
                        outputs=[lora_selection, lora_scale],
                        queue=False
                    )
                    disable_lora_2.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_2,
                        outputs=[lora_selection_2, lora_scale_2],
                        queue=False
                    )
                    disable_lora_3.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_3,
                        outputs=[lora_selection_3, lora_scale_3],
                        queue=False
                    )
                    disable_lora_4.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_4,
                        outputs=[lora_selection_4, lora_scale_4],
                        queue=False
                    )
                    disable_lora_5.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_5,
                        outputs=[lora_selection_5, lora_scale_5],
                        queue=False
                    )
                    disable_lora_6.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_6,
                        outputs=[lora_selection_6, lora_scale_6],
                        queue=False
                    )
                    disable_lora_7.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_7,
                        outputs=[lora_selection_7, lora_scale_7],
                        queue=False
                    )
                    disable_lora_8.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_8,
                        outputs=[lora_selection_8, lora_scale_8],
                        queue=False
                    )
                    disable_lora_9.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_9,
                        outputs=[lora_selection_9, lora_scale_9],
                        queue=False
                    )
                    disable_lora_10.change(
                        fn=lambda x: [gr.update(interactive=not x), gr.update(interactive=not x)],
                        inputs=disable_lora_10,
                        outputs=[lora_selection_10, lora_scale_10],
                        queue=False
                    )

                    def refresh_lora_list():
                        loras = [""] + get_available_loras()
                        return gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras)
                    
                    refresh_loras.click(
                        fn=refresh_lora_list,
                        outputs=[lora_selection, lora_selection_2, lora_selection_3, lora_selection_4, lora_selection_5, lora_selection_6, lora_selection_7, lora_selection_8, lora_selection_9, lora_selection_10],
                        queue=False,
                    )

                    def clear_lora_list():
                        return (
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=None),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False),
                            gr.update(value=False)
                        )
                    
                    clear_loras.click(
                        fn=clear_lora_list,
                        outputs=[
                            lora_selection, lora_selection_2, lora_selection_3, lora_selection_4, lora_selection_5, lora_selection_6, lora_selection_7, lora_selection_8, lora_selection_9, lora_selection_10,
                            disable_lora_1, disable_lora_2, disable_lora_3, disable_lora_4, disable_lora_5, disable_lora_6, disable_lora_7, disable_lora_8, disable_lora_9, disable_lora_10
                        ],
                        queue=False
                    )

                    enable_embeddings = gr.Checkbox(
                        label="Enable Embeddings from your Models\\Embeddings folder (only SDXL & its variants)",
                        value=False,
                    )
                    with gr.Row():
                        embeddings_dropdown = gr.Dropdown(
                            label="Available Embeddings. Select one then click a button to insert its trigger word into prompt or negative prompt.",
                            choices=get_embedding_choices(),
                            value=None,
                            visible=False
                        )
                        refresh_embeddings = gr.Button("🔄", scale=0, min_width=40, elem_classes="toolbutton", visible=False)
                    embeddings_weight = gr.Slider(
                        label="Embedding Weight",
                        minimum=0.1,
                        maximum=3.0,
                        value=1.0,
                        step=0.1,
                        visible=False
                    )
                    with gr.Row():
                        insert_embedding_prompt = gr.Button("➕ Insert into Prompt", scale=1, visible=False)
                        insert_embedding_negative = gr.Button("➕ Insert into Negative Prompt", scale=1, visible=False)

                    def refresh_embeddings_list():
                        return gr.update(choices=get_embedding_choices(), value=None)

                    refresh_embeddings.click(
                        fn=refresh_embeddings_list,
                        outputs=[embeddings_dropdown],
                        queue=False
                    )
                    insert_embedding_prompt.click(
                        fn=insert_token_into_text,
                        inputs=[prompt, embeddings_dropdown, embeddings_weight],
                        outputs=[prompt],
                        queue=False
                    )

                    insert_embedding_negative.click(
                        fn=insert_token_into_text,
                        inputs=[negative_prompt, embeddings_dropdown, embeddings_weight],
                        outputs=[negative_prompt],
                        queue=False
                    )

                    EMBEDDINGS_OUTPUTS = [embeddings_dropdown, embeddings_weight, insert_embedding_prompt, insert_embedding_negative, refresh_embeddings]

                    enable_embeddings.input(
                        fn=toggle_embeddings_ui,
                        inputs=[enable_embeddings],
                        outputs=EMBEDDINGS_OUTPUTS,
                        queue=False,
                    )

            shared_inputs = [
                resize_max_side_slider,
                face_file,
                enable_multi_ref,
                multi_ref_files,
                normalize_multi_ref,
                pose_file,
                prompt,
                negative_prompt,
                weight_application_method,
                clip_skip,
                style,
                prompt_replacement,
                num_steps,
                identitynet_strength_ratio,
                identitynet_start_slider,
                identitynet_end_slider,
                adapter_strength_ratio,
                adapter_start_slider,
                adapter_end_slider,
                adapter_smooth_transition,
                pose_strength,
                canny_strength,
                depth_strength,
                controlnet_selection,
                guidance_scale,
                seed,
                scheduler,
                enable_lora,
                disable_lora_1,
                lora_scale,
                lora_selection,
                disable_lora_2,
                lora_scale_2,
                lora_selection_2,
                disable_lora_3,
                lora_scale_3,
                lora_selection_3,
                disable_lora_4,
                lora_scale_4,
                lora_selection_4,
                disable_lora_5,
                lora_scale_5,
                lora_selection_5,
                disable_lora_6,
                lora_scale_6,
                lora_selection_6,
                disable_lora_7,
                lora_scale_7,
                lora_selection_7,
                disable_lora_8,
                lora_scale_8,
                lora_selection_8,
                disable_lora_9,
                lora_scale_9,
                lora_selection_9,
                disable_lora_10,
                lora_scale_10,
                lora_selection_10,
                enable_embeddings,
                enhance_face_region,
                enhance_strength,
                custom_enhance_padding,
                num_outputs,
                model_name,
                det_size_name,
                file_prefix,
                rng_source,
                enable_vae_tiling,
                enable_cpu_offloading,
                enable_sage_attention,
                enable_upscaler_prescale,
                upscaler_prescale_headroom,
                resize_mode_dropdown,
                pad_to_max_checkbox,
                kps_brightness_slider,
                enable_custom_resize,
                custom_resize_width,
                custom_resize_height,
                enable_img2img,
                strength,
                enable_img2img_upscaler,
                img2img_upscaler,
                ratio_base_pixel_number,
                enable_hires_fix,
                hires_upscaler,
                hires_upscale_by,
                hires_steps,
                hires_denoising_strength,
                save_hires_original,
            ]
            generate.click(fn=randomize_seed_fn, inputs=[seed, randomize_seed], outputs=seed, queue=False, api_name=False).then(
                fn=generate_image, inputs=shared_inputs, outputs=[gallery]
            )
            generate_alt.click(fn=randomize_seed_fn, inputs=[seed, randomize_seed], outputs=seed, queue=False, api_name=False).then(
                fn=generate_image, inputs=shared_inputs, outputs=[gallery]
            )
            generate_alt_2.click(fn=randomize_seed_fn, inputs=[seed, randomize_seed], outputs=seed, queue=False, api_name=False).then(
                fn=generate_image, inputs=shared_inputs, outputs=[gallery]
            )
            generate_alt_3.click(fn=randomize_seed_fn, inputs=[seed, randomize_seed], outputs=seed, queue=False, api_name=False).then(
                fn=generate_image, inputs=shared_inputs, outputs=[gallery]
            )

            stop_btn.click(fn=request_stop, inputs=[], outputs=[], queue=True, api_name=False)
            stop_btn_alt.click(fn=request_stop, inputs=[], outputs=[], queue=True, api_name=False)
            stop_btn_2.click(fn=request_stop, inputs=[], outputs=[], queue=True, api_name=False)
            stop_btn_3.click(fn=request_stop, inputs=[], outputs=[], queue=True, api_name=False)

            LORA_OUTPUTS = [
                lora_row_1, lora_selection, lora_scale,
                lora_row_2, lora_selection_2, lora_scale_2,
                lora_row_3, lora_selection_3, lora_scale_3,
                lora_row_4, lora_selection_4, lora_scale_4,
                lora_row_5, lora_selection_5, lora_scale_5,
                lora_row_6, lora_selection_6, lora_scale_6,
                lora_row_7, lora_selection_7, lora_scale_7,
                lora_row_8, lora_selection_8, lora_scale_8,
                lora_row_9, lora_selection_9, lora_scale_9,
                lora_row_10, lora_selection_10, lora_scale_10,
                refresh_loras, clear_loras
            ]

            enable_lora.input(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=LORA_OUTPUTS,
                queue=False,
            )
            def apply_lcm_profile(ls1, ls2, ls3, ls4, ls5, ls6, ls7, ls8, ls9, ls10,
                                   dl1, dl2, dl3, dl4, dl5, dl6, dl7, dl8, dl9, dl10):
                slot_values = [ls1, ls2, ls3, ls4, ls5, ls6, ls7, ls8, ls9, ls10]
                disable_values = [dl1, dl2, dl3, dl4, dl5, dl6, dl7, dl8, dl9, dl10]
                dmd2_lora = "dmd2_sdxl_4step_lora_fp16.safetensors"
                dmd2_variants = {"dmd2_sdxl_4step_lora_fp16.safetensors", "dmd2_sdxl_4step_lora.safetensors"}
                dmd2_indices = [i for i, v in enumerate(slot_values) if v in dmd2_variants]
                duplicate_idx = dmd2_indices[-1] if len(dmd2_indices) > 1 else None
                if duplicate_idx is not None:
                    slot_values[duplicate_idx] = None
                existing = next((v for v in slot_values if v in dmd2_variants), None)
                if existing is not None:
                    target = slot_values.index(existing)
                    lora_value = existing
                else:
                    target = next((i for i, v in enumerate(slot_values) if not v), 0)
                    lora_value = dmd2_lora
                other_loras_present = any(
                    v and not disable_values[i]
                    for i, v in enumerate(slot_values)
                    if i != target
                )
                scale = 0.8 if other_loras_present else 1
                lora_updates = []
                for i in range(10):
                    if i == target:
                        lora_updates.extend([
                            gr.update(value=lora_value),
                            gr.update(value=scale),
                            gr.update(value=False),
                        ])
                    elif i == duplicate_idx:
                        lora_updates.extend([
                            gr.update(value=None),
                            gr.update(),
                            gr.update(),
                        ])
                    else:
                        lora_updates.extend([gr.update(), gr.update(), gr.update()])
                return (
                    gr.update(value="LCMScheduler"),
                    gr.update(value=1),
                    gr.update(value=10),
                    gr.update(value=True),
                    *lora_updates,
                )
            apply_lcm_profile_btn.click(
                fn=apply_lcm_profile,
                inputs=[
                    lora_selection, lora_selection_2, lora_selection_3, lora_selection_4,
                    lora_selection_5, lora_selection_6, lora_selection_7, lora_selection_8,
                    lora_selection_9, lora_selection_10,
                    disable_lora_1, disable_lora_2, disable_lora_3, disable_lora_4,
                    disable_lora_5, disable_lora_6, disable_lora_7, disable_lora_8,
                    disable_lora_9, disable_lora_10,
                ],
                outputs=[
                    scheduler, guidance_scale, num_steps, enable_lora,
                    lora_selection, lora_scale, disable_lora_1,
                    lora_selection_2, lora_scale_2, disable_lora_2,
                    lora_selection_3, lora_scale_3, disable_lora_3,
                    lora_selection_4, lora_scale_4, disable_lora_4,
                    lora_selection_5, lora_scale_5, disable_lora_5,
                    lora_selection_6, lora_scale_6, disable_lora_6,
                    lora_selection_7, lora_scale_7, disable_lora_7,
                    lora_selection_8, lora_scale_8, disable_lora_8,
                    lora_selection_9, lora_scale_9, disable_lora_9,
                    lora_selection_10, lora_scale_10, disable_lora_10,
                ],
                queue=False
            ).then(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=LORA_OUTPUTS,
                queue=False
            )
            def extract_all_settings(metadata_text):
                accordion_update = gr.update(open=False)
                settings = {
                    "prompt": "",
                    "negative_prompt": DEFAULT_NEGATIVE_PROFILE,
                    "weight_application_method": "Original InstantID per-token",
                    "clip_skip": 0,
                    "resize_max_side": 1280,
                    "seed": 12345,
                    "num_steps": 20,
                    "guidance_scale": 4.0,
                    "enable_img2img": False,
                    "strength": 0.95,
                    "enable_img2img_upscaler": False,
                    "img2img_upscaler": DEFAULT_UPSCALER,
                    "identitynet_strength_ratio": 0.7,
                    "identitynet_start": 0.0,
                    "identitynet_end": 1.0,
                    "adapter_strength_ratio": 0.6,
                    "adapter_start": 0.0,
                    "adapter_end": 1.0,
                    "adapter_smooth_transition": True,
                    "pose_strength": 0.30,
                    "canny_strength": 0.30,
                    "depth_strength": 0.30,
                    "scheduler": "DPMSolverMultistepScheduler",
                    "ratio_base_pixel_number": 8,
                    "rng_source": "GPU",
                    "enable_lora": False,
                    "lora_scale": 1.0,
                    "lora_selection": None,
                    "lora_scale_2": 0.7,
                    "lora_selection_2": None,
                    "lora_scale_3": 0.7,
                    "lora_selection_3": None,
                    "lora_scale_4": 0.7,
                    "lora_selection_4": None,
                    "lora_scale_5": 0.7,
                    "lora_selection_5": None,
                    "lora_scale_6": 0.7,
                    "lora_selection_6": None,
                    "lora_scale_7": 0.7,
                    "lora_selection_7": None,
                    "lora_scale_8": 0.7,
                    "lora_selection_8": None,
                    "lora_scale_9": 0.7,
                    "lora_selection_9": None,
                    "lora_scale_10": 0.7,
                    "lora_selection_10": None,
                    "enable_embeddings": False,
                    "enhance_face_region": True,
                    "enhance_strength": "Balanced",
                    "custom_enhance_padding": 0.15,
                    "kps_brightness": 0.6,
                    "style": DEFAULT_STYLE_NAME,
                    "randomize_seed": True,
                    "controlnet_selection": [],
                    "model_name": DEFAULT_MODEL,
                    "det_size_name": "640x640 (default)",
                    "disable_lora_1": False,
                    "disable_lora_2": False,
                    "disable_lora_3": False,
                    "disable_lora_4": False,
                    "disable_lora_5": False,
                    "disable_lora_6": False,
                    "disable_lora_7": False,
                    "disable_lora_8": False,
                    "disable_lora_9": False,
                    "disable_lora_10": False,
                    "resize_mode": "LANCZOS",
                    "pad_to_max_side": False,
                    "enable_sage_attention": False,
                    "enable_upscaler_prescale": False,
                    "upscaler_prescale_headroom": 1.3,
                    "enable_custom_resize": False,
                    "custom_resize_width": 960,
                    "custom_resize_height": 1280,
                    "enable_hires_fix": False,
                    "hires_upscaler": DEFAULT_UPSCALER,
                    "hires_upscale_by": 1.5,
                    "hires_steps": 0,
                    "hires_denoising_strength": 0.35,
                    "enable_multi_ref": False,
                    "normalize_multi_ref": True
                }
                if metadata_text:
                    lines = metadata_text.split('\n')
                    for idx, line in enumerate(lines):
                        stripped_line = line.strip()
                        if stripped_line.startswith("Prompt:"):
                            prompt_value = line[len("Prompt:"):]
                            if prompt_value.startswith(" "):
                                prompt_value = prompt_value[1:]
                            prompt_lines = [prompt_value]
                            continue_idx = idx + 1
                            while continue_idx < len(lines):
                                next_line = lines[continue_idx]
                                if next_line.strip().startswith("Negative Prompt:"):
                                    break
                                prompt_lines.append(next_line)
                                continue_idx += 1
                            settings["prompt"] = "\n".join(prompt_lines)
                        elif stripped_line.startswith("Negative Prompt:"):
                            negative_prompt_value = line[len("Negative Prompt:"):]
                            if negative_prompt_value.startswith(" "):
                                negative_prompt_value = negative_prompt_value[1:]
                            negative_lines = [negative_prompt_value]
                            continue_idx = idx + 1
                            while continue_idx < len(lines):
                                next_line = lines[continue_idx]
                                if next_line.strip().startswith(("Input Face Image:", "Detection size:")):
                                    break
                                negative_lines.append(next_line)
                                continue_idx += 1
                            settings["negative_prompt"] = "\n".join(negative_lines)
                        elif line.startswith("Seed:"):
                            settings["seed"] = int(line.replace("Seed:", "").strip())
                        elif line.startswith("Steps:"):
                            settings["num_steps"] = int(line.replace("Steps:", "").strip())
                        elif line.startswith("Guidance scale:"):
                            settings["guidance_scale"] = float(line.replace("Guidance scale:", "").strip())
                        elif line.startswith("Ratio base pixel number:"):
                            try:
                                settings["ratio_base_pixel_number"] = int(line.replace("Ratio base pixel number:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("LoRA Enabled:"):
                            settings["enable_lora"] = "true" in line.lower()
                        elif line.startswith("Embeddings Enabled:"):
                            settings["enable_embeddings"] = "true" in line.lower()
                        elif line.startswith("LoRA 1 selection:"):
                            lora_selection = line.replace("LoRA 1 selection:", "").strip()
                            settings["lora_selection"] = lora_selection if lora_selection != "None" else None
                        elif line.startswith("LoRA 1 scale:"):
                            lora_scale_str = line.replace("LoRA 1 scale:", "").strip()
                            if lora_scale_str != "Disabled":
                                settings["lora_scale"] = float(lora_scale_str)
                        elif line.startswith("LoRA 2 selection:"):
                            lora_selection_2 = line.replace("LoRA 2 selection:", "").strip()
                            settings["lora_selection_2"] = lora_selection_2 if lora_selection_2 != "None" else None
                        elif line.startswith("LoRA 2 scale:"):
                            lora_scale_2_str = line.replace("LoRA 2 scale:", "").strip()
                            if lora_scale_2_str != "Disabled":
                                settings["lora_scale_2"] = float(lora_scale_2_str)
                        elif line.startswith("LoRA 3 selection:"):
                            lora_selection_3 = line.replace("LoRA 3 selection:", "").strip()
                            settings["lora_selection_3"] = lora_selection_3 if lora_selection_3 != "None" else None
                        elif line.startswith("LoRA 3 scale:"):
                            lora_scale_3_str = line.replace("LoRA 3 scale:", "").strip()
                            if lora_scale_3_str != "Disabled":
                                settings["lora_scale_3"] = float(lora_scale_3_str)
                        elif line.startswith("LoRA 4 selection:"):
                            lora_selection_4 = line.replace("LoRA 4 selection:", "").strip()
                            settings["lora_selection_4"] = lora_selection_4 if lora_selection_4 != "None" else None
                        elif line.startswith("LoRA 4 scale:"):
                            lora_scale_4_str = line.replace("LoRA 4 scale:", "").strip()
                            if lora_scale_4_str != "Disabled":
                                settings["lora_scale_4"] = float(lora_scale_4_str)
                        elif line.startswith("LoRA 5 selection:"):
                            lora_selection_5 = line.replace("LoRA 5 selection:", "").strip()
                            settings["lora_selection_5"] = lora_selection_5 if lora_selection_5 != "None" else None
                        elif line.startswith("LoRA 5 scale:"):
                            lora_scale_5_str = line.replace("LoRA 5 scale:", "").strip()
                            if lora_scale_5_str != "Disabled":
                                settings["lora_scale_5"] = float(lora_scale_5_str)
                        elif line.startswith("LoRA 6 selection:"):
                            lora_selection_6 = line.replace("LoRA 6 selection:", "").strip()
                            settings["lora_selection_6"] = lora_selection_6 if lora_selection_6 != "None" else None
                        elif line.startswith("LoRA 6 scale:"):
                            lora_scale_6_str = line.replace("LoRA 6 scale:", "").strip()
                            if lora_scale_6_str != "Disabled":
                                settings["lora_scale_6"] = float(lora_scale_6_str)
                        elif line.startswith("LoRA 7 selection:"):
                            lora_selection_7 = line.replace("LoRA 7 selection:", "").strip()
                            settings["lora_selection_7"] = lora_selection_7 if lora_selection_7 != "None" else None
                        elif line.startswith("LoRA 7 scale:"):
                            lora_scale_7_str = line.replace("LoRA 7 scale:", "").strip()
                            if lora_scale_7_str != "Disabled":
                                settings["lora_scale_7"] = float(lora_scale_7_str)
                        elif line.startswith("LoRA 8 selection:"):
                            lora_selection_8 = line.replace("LoRA 8 selection:", "").strip()
                            settings["lora_selection_8"] = lora_selection_8 if lora_selection_8 != "None" else None
                        elif line.startswith("LoRA 8 scale:"):
                            lora_scale_8_str = line.replace("LoRA 8 scale:", "").strip()
                            if lora_scale_8_str != "Disabled":
                                settings["lora_scale_8"] = float(lora_scale_8_str)
                        elif line.startswith("LoRA 9 selection:"):
                            lora_selection_9 = line.replace("LoRA 9 selection:", "").strip()
                            settings["lora_selection_9"] = lora_selection_9 if lora_selection_9 != "None" else None
                        elif line.startswith("LoRA 9 scale:"):
                            lora_scale_9_str = line.replace("LoRA 9 scale:", "").strip()
                            if lora_scale_9_str != "Disabled":
                                settings["lora_scale_9"] = float(lora_scale_9_str)
                        elif line.startswith("LoRA 10 selection:"):
                            lora_selection_10 = line.replace("LoRA 10 selection:", "").strip()
                            settings["lora_selection_10"] = lora_selection_10 if lora_selection_10 != "None" else None
                        elif line.startswith("LoRA 10 scale:"):
                            lora_scale_10_str = line.replace("LoRA 10 scale:", "").strip()
                            if lora_scale_10_str != "Disabled":
                                settings["lora_scale_10"] = float(lora_scale_10_str)
                        elif line.startswith("img2img Mode Enabled:"):
                            settings["enable_img2img"] = "true" in line.lower()
                        elif line.startswith("img2img Strength:"):
                            settings["strength"] = float(line.replace("img2img Strength:", "").strip())
                        elif line.startswith("img2img Upscaler Enabled:"):
                            settings["enable_img2img_upscaler"] = "true" in line.lower()
                        elif line.startswith("img2img Upscaler:"):
                            i2i_upscaler_value = line.replace("img2img Upscaler:", "").strip()
                            if i2i_upscaler_value:
                                settings["img2img_upscaler"] = i2i_upscaler_value
                        elif line.startswith("Hires Fix Enabled:"):
                            settings["enable_hires_fix"] = "true" in line.lower()
                        elif line.startswith("Hires Upscaler:"):
                            upscaler_value = line.replace("Hires Upscaler:", "").strip()
                            if upscaler_value:
                                settings["hires_upscaler"] = upscaler_value
                        elif line.startswith("Hires Upscale By:"):
                            try:
                                settings["hires_upscale_by"] = float(line.replace("Hires Upscale By:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("Hires Steps:"):
                            try:
                                settings["hires_steps"] = int(line.replace("Hires Steps:", "").strip().split()[0])
                            except ValueError:
                                pass
                        elif line.startswith("Hires Denoising Strength:"):
                            try:
                                settings["hires_denoising_strength"] = float(line.replace("Hires Denoising Strength:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("Upscaler Prescale Optimization:"):
                            settings["enable_upscaler_prescale"] = "true" in line.lower()
                        elif line.startswith("Upscaler Prescale Headroom:"):
                            try:
                                settings["upscaler_prescale_headroom"] = float(line.replace("Upscaler Prescale Headroom:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("Enhance non-face region:"):
                            settings["enhance_face_region"] = "true" in line.lower()
                        elif line.startswith("Enhance region profile:"):
                            settings["enhance_strength"] = line.replace("Enhance region profile:", "").strip()
                        elif line.startswith("Enhance padding ratio:"):
                            try:
                                settings["custom_enhance_padding"] = float(line.replace("Enhance padding ratio:", "").strip())
                            except:
                                pass
                        elif line.startswith("KPS Brightness:"):
                            try:
                                settings["kps_brightness"] = float(line.replace("KPS Brightness:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("IdentityNet strength:"):
                            settings["identitynet_strength_ratio"] = float(line.replace("IdentityNet strength:", "").strip())
                        elif line.startswith("Ranges:"):
                            match = re.search(
                                r"IdentityNet:\s*([\d.]+)\s*-\s*([\d.]+)\s*\|\s*Adapter:\s*([\d.]+)\s*-\s*([\d.]+)",
                                line,
                            )
                            if match:
                                try:
                                    settings["identitynet_start"] = float(match.group(1))
                                    settings["identitynet_end"] = float(match.group(2))
                                    settings["adapter_start"] = float(match.group(3))
                                    settings["adapter_end"] = float(match.group(4))
                                except ValueError:
                                    pass
                            smooth_match = re.search(r"Smooth Transition:\s*(True|False)", line)
                            if smooth_match:
                                settings["adapter_smooth_transition"] = smooth_match.group(1) == "True"
                        elif line.startswith("Weight application method:"):
                            method_text = line.replace("Weight application method:", "").strip()
                            valid_methods = [
                                "Original InstantID per-token",
                                "ForgeUI per-encoder rescale",
                                "ForgeUI global rescale",
                                "ComfyUI (blank prompt interpolation)",
                            ]
                            if method_text in valid_methods:
                                settings["weight_application_method"] = method_text
                        elif line.startswith("Clip skip:"):
                            try:
                                settings["clip_skip"] = int(line.replace("Clip skip:", "").strip())
                            except ValueError:
                                pass
                        elif line.startswith("Scheduler:"):
                            scheduler_text = line.replace("Scheduler:", "").strip()
                            if "scheduling_" in scheduler_text:
                                scheduler_name = scheduler_text.split(".")[-1].replace("'>", "").replace("Scheduler", "Scheduler")
                            else:
                                scheduler_name = scheduler_text
                            if scheduler_name in schedulers:
                                settings["scheduler"] = scheduler_name
                        elif line.startswith("Adapter strength:"):
                            settings["adapter_strength_ratio"] = float(line.replace("Adapter strength:", "").strip())
                        elif line.startswith("Pose strength:"):
                            settings["pose_strength"] = float(line.replace("Pose strength:", "").strip())
                        elif line.startswith("Canny strength:"):
                            settings["canny_strength"] = float(line.replace("Canny strength:", "").strip())
                        elif line.startswith("Depth strength:"):
                            settings["depth_strength"] = float(line.replace("Depth strength:", "").strip())
                        elif line.startswith("ControlNet selection:"):
                            cn_selection = line.replace("ControlNet selection:", "").strip()
                            if cn_selection.startswith("["):
                                try:
                                    cn_list = eval(cn_selection)
                                    if isinstance(cn_list, list):
                                        clean_list = [x.strip("'\" ") for x in cn_list]
                                        settings["controlnet_selection"] = clean_list
                                        known_cn = {"pose", "canny", "depth"}
                                        if set(clean_list) & known_cn:
                                            accordion_update = gr.update(open=True)
                                except:
                                    pass
                        elif line.startswith("Model:"):
                            model_name = line.replace("Model:", "").strip()
                            current_models = get_available_models()
                            match = next((m for m in current_models if m.lower() == model_name.lower()), None)
                            if match:
                                settings["model_name"] = match
                            else:
                                print(
                                    f"\nModel '{model_name}' used for this image can't be found in your models folder. Falling back to the default model.\n"
                                )
                        elif line.startswith("Detection size:"):
                            size = line.replace("Detection size:", "").strip()
                            for key, value in DET_SIZE_OPTIONS.items():
                                if str(value) == size:
                                    settings["det_size_name"] = key
                        elif line.startswith("Max resize side:"):
                            size_str = line.replace("Max resize side:", "").strip()
                            if size_str.isdigit():
                                settings["resize_max_side"] = int(size_str)
                        elif line.startswith("Resize mode:"):
                            settings["resize_mode"] = line.replace("Resize mode:", "").strip().upper()
                        elif line.startswith("Pad to max side:"):
                            settings["pad_to_max_side"] = "true" in line.lower()
                        elif line.startswith("Sage Attention:"):
                            settings["enable_sage_attention"] = "true" in line.lower()
                        elif line.startswith("Noise RNG device:"):
                            rng_value = line.replace("Noise RNG device:", "").strip()
                            if rng_value in ("GPU", "CPU"):
                                settings["rng_source"] = rng_value
                        elif line.startswith("Use custom resize:"):
                            settings["enable_custom_resize"] = "true" in line.lower()
                        elif line.startswith("Custom resize size:"):
                            try:
                                dims = line.replace("Custom resize size:", "").strip().lower().split("x")
                                settings["custom_resize_width"] = int(dims[0])
                                settings["custom_resize_height"] = int(dims[1])
                            except:
                                pass
                        elif line.startswith("Additional face image(s) used:"):
                            additional_face_value = line.replace("Additional face image(s) used:", "").strip()
                            settings["enable_multi_ref"] = additional_face_value not in ("", "None")
                        elif line.startswith("Normalize averaged face embedding:"):
                            settings["normalize_multi_ref"] = "true" in line.lower()

                open_resolution_accordion = False
                open_advanced_accordion = False
                open_range_accordion = False

                if settings["enable_custom_resize"] or settings["pad_to_max_side"] or settings["ratio_base_pixel_number"] != 8:
                    open_resolution_accordion = True
                if settings["rng_source"] == "CPU" or settings["enable_sage_attention"] or settings["enable_upscaler_prescale"] or settings["clip_skip"] != 0 or settings["kps_brightness"] != 0.6 or settings["resize_mode"] != "LANCZOS" or settings["weight_application_method"] != "Original InstantID per-token":
                    open_advanced_accordion = True
                if settings["identitynet_start"] != 0.0 or settings["identitynet_end"] != 1.0 or settings["adapter_start"] != 0.0 or settings["adapter_end"] != 1.0:
                    open_range_accordion = True

                return [
                    settings["prompt"],
                    settings["negative_prompt"],
                    settings["weight_application_method"],
                    settings["clip_skip"],
                    settings["style"],
                    settings["num_steps"],
                    settings["enable_img2img"],
                    settings["strength"],
                    settings["enable_img2img_upscaler"],
                    settings["img2img_upscaler"],
                    settings["identitynet_strength_ratio"],
                    settings["identitynet_start"],
                    settings["identitynet_end"],
                    settings["adapter_strength_ratio"],
                    settings["adapter_start"],
                    settings["adapter_end"],
                    settings["adapter_smooth_transition"],
                    settings["pose_strength"],
                    settings["canny_strength"],
                    settings["depth_strength"],
                    settings["guidance_scale"],
                    settings["seed"],
                    settings["scheduler"],
                    settings["rng_source"],
                    settings["enable_lora"],
                    settings["enhance_face_region"],
                    settings["enhance_strength"],
                    settings["custom_enhance_padding"],
                    settings["lora_scale"],
                    settings["lora_selection"],
                    settings["lora_scale_2"],
                    settings["lora_selection_2"],
                    settings["lora_scale_3"],
                    settings["lora_selection_3"],
                    settings["lora_scale_4"],
                    settings["lora_selection_4"],
                    settings["lora_scale_5"],
                    settings["lora_selection_5"],
                    settings["lora_scale_6"],
                    settings["lora_selection_6"],
                    settings["lora_scale_7"],
                    settings["lora_selection_7"],
                    settings["lora_scale_8"],
                    settings["lora_selection_8"],
                    settings["lora_scale_9"],
                    settings["lora_selection_9"],
                    settings["lora_scale_10"],
                    settings["lora_selection_10"],
                    settings["randomize_seed"],
                    settings["controlnet_selection"],
                    settings["model_name"],
                    settings["det_size_name"],
                    settings["resize_max_side"],
                    settings["disable_lora_1"],
                    settings["disable_lora_2"],
                    settings["disable_lora_3"],
                    settings["disable_lora_4"],
                    settings["disable_lora_5"],
                    settings["disable_lora_6"],
                    settings["disable_lora_7"],
                    settings["disable_lora_8"],
                    settings["disable_lora_9"],
                    settings["disable_lora_10"],
                    settings["resize_mode"],
                    settings["pad_to_max_side"],
                    settings["enable_sage_attention"],
                    settings["enable_upscaler_prescale"],
                    settings["upscaler_prescale_headroom"],
                    settings["kps_brightness"],
                    settings["enable_custom_resize"],
                    settings["custom_resize_width"],
                    settings["custom_resize_height"],
                    settings["ratio_base_pixel_number"],
                    settings["enable_embeddings"],
                    settings["enable_hires_fix"],
                    settings["hires_upscaler"],
                    settings["hires_upscale_by"],
                    settings["hires_steps"],
                    settings["hires_denoising_strength"],
                    settings["enable_multi_ref"],
                    settings["normalize_multi_ref"],
                    accordion_update,
                    gr.update(open=open_resolution_accordion),
                    gr.update(open=open_advanced_accordion),
                    gr.update(open=open_range_accordion)
                ]

            apply_metadata_btn.click(
                fn=extract_all_settings,
                inputs=metadata_output,
                outputs=[
                    prompt,
                    negative_prompt,
                    weight_application_method,
                    clip_skip,
                    style,
                    num_steps,
                    enable_img2img,
                    strength,
                    enable_img2img_upscaler,
                    img2img_upscaler,
                    identitynet_strength_ratio,
                    identitynet_start_slider,
                    identitynet_end_slider,
                    adapter_strength_ratio,
                    adapter_start_slider,
                    adapter_end_slider,
                    adapter_smooth_transition,
                    pose_strength,
                    canny_strength,
                    depth_strength,
                    guidance_scale,
                    seed,
                    scheduler,
                    rng_source,
                    enable_lora,
                    enhance_face_region,
                    enhance_strength,
                    custom_enhance_padding,
                    lora_scale,
                    lora_selection,
                    lora_scale_2,
                    lora_selection_2,
                    lora_scale_3,
                    lora_selection_3,
                    lora_scale_4,
                    lora_selection_4,
                    lora_scale_5,
                    lora_selection_5,
                    lora_scale_6,
                    lora_selection_6,
                    lora_scale_7,
                    lora_selection_7,
                    lora_scale_8,
                    lora_selection_8,
                    lora_scale_9,
                    lora_selection_9,
                    lora_scale_10,
                    lora_selection_10,
                    randomize_seed,
                    controlnet_selection,
                    model_name,
                    det_size_name,
                    resize_max_side_slider,
                    disable_lora_1,
                    disable_lora_2,
                    disable_lora_3,
                    disable_lora_4,
                    disable_lora_5,
                    disable_lora_6,
                    disable_lora_7,
                    disable_lora_8,
                    disable_lora_9,
                    disable_lora_10,
                    resize_mode_dropdown,
                    pad_to_max_checkbox,
                    enable_sage_attention,
                    enable_upscaler_prescale,
                    upscaler_prescale_headroom,
                    kps_brightness_slider,
                    enable_custom_resize,
                    custom_resize_width,
                    custom_resize_height,
                    ratio_base_pixel_number,
                    enable_embeddings,
                    enable_hires_fix,
                    hires_upscaler,
                    hires_upscale_by,
                    hires_steps,
                    hires_denoising_strength,
                    enable_multi_ref,
                    normalize_multi_ref,
                    controlnet_accordion,
                    resolution_settings_accordion,
                    advanced_settings_accordion,
                    adapters_range_accordion
                ],
                queue=False
            ).then(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=LORA_OUTPUTS,
                queue=False
            ).then(
                fn=toggle_embeddings_ui,
                inputs=[enable_embeddings],
                outputs=EMBEDDINGS_OUTPUTS,
                queue=False
            ).then(
                fn=update_hires_upscale,
                inputs=[resize_max_side_slider, hires_upscale_by, enable_custom_resize, custom_resize_width, custom_resize_height],
                outputs=[hires_upscale_by],
                queue=False
            )

        with gr.Accordion("📝 Click to show/hide usage tips", open=False):
            gr.Markdown(article)
        gr.Markdown("<b>InstantID Unlocked v8.9.3</b> - <a href='https://github.com/eniora/InstantID-Unlocked' target='_blank'><b>Github fork page for InstantID Unlocked</b></a><br>")

        with gr.Row():
            with gr.Column():
                force_cuda_empty_cache = gr.Button("Empty CUDA Cache (helpful during Hires Fix/img2img passes on low VRAM GPUs)", variant="secondary", scale=1)
                def force_cuda_empty_cache_fn():
                    torch.cuda.empty_cache()
                force_cuda_empty_cache.click(
                    fn=force_cuda_empty_cache_fn,
                    inputs=None,
                    outputs=None,
                    queue=False,
                )
            with gr.Column():
                delete_all_pipelines = gr.Button("Delete all models from memory and VRAM - (don't click during image generation!)", variant="stop", scale=1)
                def delete_all_pipelines_fn():
                    nonlocal pipe, hires_sibling_pipe
                    if pipe is not None:
                        try:
                            pipe.unfuse_lora()
                            pipe.unload_lora_weights()
                        except Exception:
                            pass
                        del pipe
                        pipe = None
                    if hires_sibling_pipe is not None:
                        del hires_sibling_pipe
                        hires_sibling_pipe = None
                    global cached_controlnet_models, controlnet_identitynet
                    for k in list(cached_controlnet_models.keys()):
                        del cached_controlnet_models[k]
                    if controlnet_identitynet is not None:
                        del controlnet_identitynet
                        controlnet_identitynet = None

                    lora_state["signature"] = None
                    lora_state["adapter_ids"] = {}

                    gc.collect()
                    torch.cuda.empty_cache()
                    print("\nSuccessfully released all models and pipelines from memory.\n")

                delete_all_pipelines.click(
                    js="() => { if (!confirm('Are you sure you want to delete and release all models from memory?')) { throw new Error('Cancelled'); } }",
                    fn=delete_all_pipelines_fn,
                    inputs=None,
                    outputs=None,
                    queue=False,
                )

        with gr.Row():
            gr.Markdown("")
            theme_dropdown, theme_change_js, theme_load_js = create_theme_dropdown(default_theme="Default Theme")
            theme_dropdown.render()
            gr.Markdown("")
        theme_dropdown.change(fn=None, inputs=theme_dropdown, outputs=None, js=theme_change_js)
        gui.load(fn=None, inputs=None, outputs=theme_dropdown, js=theme_load_js)

    gui.launch(inbrowser=os.environ.get("IN_BROWSER", "1") == "1")

main()