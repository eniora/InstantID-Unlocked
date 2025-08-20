import sys
sys.path.append("./")

from typing import Tuple

import os
import cv2
import math
import torch
import random
import numpy as np
import gc
import warnings
import subprocess
import PIL.PngImagePlugin
import time

warnings.filterwarnings("ignore", message=".*timm.models.layers.*")
warnings.filterwarnings("ignore", message=".*timm.models.registry.*")
warnings.filterwarnings("ignore", message=".*Overwriting tiny_vit_.* in registry.*")
warnings.filterwarnings("ignore", message=".*peft_config.*multiple adapters.*")
warnings.filterwarnings("ignore", message=".*rcond.*will change to the default.*")
warnings.filterwarnings("ignore", message=".*MultiControlNetModel.*is deprecated.*")
warnings.filterwarnings("ignore", message=".*`resume_download` is deprecated.*")
warnings.filterwarnings("ignore", message=".*Should have .*<=t1 but got .*")
warnings.filterwarnings("ignore", message="unable to parse version details from package URL.")

os.environ["NO_ALBUMENTATIONS_UPDATE"] = "1"
# os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_CACHE"] = "models"
os.environ["HF_HUB_CACHE_OFFLINE"] = "true"
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
os.environ["GRADIO_DISABLE_TELEMETRY"] = "1"

vram_bytes = torch.cuda.get_device_properties(0).total_memory
vram_gb = vram_bytes / (1024**3)

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

from huggingface_hub import hf_hub_download

from insightface.app import FaceAnalysis

from style_template import styles
from pipeline_stable_diffusion_xl_instantid_full import StableDiffusionXLInstantIDPipeline
from pipeline_stable_diffusion_xl_instantid_img2img import StableDiffusionXLInstantIDImg2ImgPipeline
from model_util import load_models_xl, get_torch_device, torch_gc
from controlnet_util import openpose, get_depth_map, get_canny_image

import gradio as gr

MAX_SEED = np.iinfo(np.int32).max
device = get_torch_device()
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
    "Default Negative Profile": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, blurry, deformed cat, deformed photo",
    "Aggressive Negative Profile (InstantID default)": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    "Negative Profile 1 (General use)": "low quality, worst quality, text, watermark, deformed, ugly",
    "Negative Profile 2 (Minimalist)": "(worst quality, low quality:1.2), deformed, blurry, mutated, extra limbs",
    "Negative Profile 3 (Portraits)": "(worst quality:1.3), (low quality:1.2), bad anatomy, deformed, disfigured, fused fingers, missing fingers, extra limbs, poorly drawn face, poorly drawn hands, blurry",
    "Negative Profile 4 (SDXL default)": "(worst quality, low quality:1.3), watermark, signature, text, frame, jpeg artifacts, blurry, deformed, extra limbs, bad hands, fused fingers, poorly drawn face",
    "Negative Profile 5 (Realism)": "(worst quality, low quality:1.3), anime, cartoon, illustration, cgi, 3d render, painting, drawing, deformed, extra fingers, fused fingers, blurry, unrealistic",
    "Negative Profile 6 (Stylized / Illustration)": "(worst quality:1.3), bad anatomy, deformed eyes, bad hands, long neck, lowres, jpeg artifacts, text, watermark, extra fingers",
    "Negative Profile 7 (Digital Illustration)": "(worst quality, low quality:1.3), bad anatomy, blurry, duplicate, signature, watermark, jpeg artifacts",
    "Negative Profile 8 (Anime)": "(worst quality:1.2), photorealistic, real life, realistic skin, 3d render, painting, extra limbs, fused fingers, bad anatomy, blurry, text, watermark",
    "Negative Profile 9 (Ultra Minimal)": "low quality, deformed",
    "Negative Profile 10 (3D Render)": "photo, photorealistic, realistic, painting, sketch, drawing, anime, cartoon, 2d, flat color, low detail, text, watermark, blurry",
    "Negative Profile 11 (Plastic Toy Render)": "photo, illustration, sketch, painting, anime, blurry, lowres, noisy, realistic skin, lifelike eyes, textureless",
    "Negative Profile 12 (Game Character (Stylized 3D))": "photo, painting, sketch, drawing, anime, real skin texture, flat shading, realistic proportions, soft shadows, photorealistic",
    "Negative Profile 13 (Sculpted Statue Render)": "cartoon, photo, realism, painterly, anime, soft brush, flat colors, 2d, smooth shading",
    "Negative Profile 14 (Low Poly Stylized)": "realism, photo, anime, high detail, highres, 2d, blurry, smooth shading, overrendered, soft shadows",
    "Negative Profile 15 (Fooocus Enhance)": "(worst quality, low quality, normal quality, lowres, low details, oversaturated, undersaturated, overexposed, underexposed, grayscale, bw, bad photo, bad photography, bad art:1.4), (watermark, signature, text font, username, error, logo, words, letters, digits, autograph, trademark, name:1.2), (blur, blurry, grainy), morbid, ugly, asymmetrical, mutated malformed, mutilated, poorly lit, bad shadow, draft, cropped, out of frame, cut off, censored, jpeg artifacts, out of focus, glitch, duplicate, (airbrushed, cartoon, anime, semi-realistic, cgi, render, blender, digital art, manga, amateur:1.3), (3D ,3D Game, 3D Game Scene, 3D Character:1.1), (bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3)",
    "Negative Profile 16 (Fooocus Negative)": "deformed, bad anatomy, disfigured, poorly drawn face, mutated, extra limb, ugly, poorly drawn hands, missing limb, floating limbs, disconnected limbs, disconnected head, malformed hands, long neck, mutated hands and fingers, bad hands, missing fingers, cropped, worst quality, low quality, mutation, poorly drawn, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, missing fingers, fused fingers, abnormal eye proportion, Abnormal hands, abnormal legs, abnormal feet, abnormal fingers, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch",
}

DEFAULT_NEGATIVE_PROFILE = NEGATIVE_PROMPT_PRESETS["Default Negative Profile"]

def on_style_change(style_name):
    if style_name == "(No style)":
        return gr.update(), gr.update()
    else:
        print(f"Manual style selection: {style_name}")
        return gr.update(value=""), gr.update(value="")

def get_available_models():
    models_dir = "models"
    model_folders = []
    if os.path.exists(models_dir):
        for folder in os.listdir(models_dir):
            if folder.startswith("models--"):
                model_name = folder.replace("models--", "").replace("--", "/")
                model_folders.append(model_name)
    return model_folders

AVAILABLE_MODELS = get_available_models()
DEFAULT_MODEL = "eniora/RealVisXL_V5.0"

DET_SIZE_OPTIONS = {
    "160x160 (for very lowres portrait photos)": (160, 160),
    "320x320": (320, 320),
    "640x640 (default)": (640, 640),
    "800x800": (800, 800),
    "1024x1024": (1024, 1024),
    "1280x1280": (1280, 1280),
    "2560x2560 (Input/Reference image size should be larger than 2560x2560)": (2560, 2560)
}

current_det_size = (640, 640)
app = FaceAnalysis(
    name="antelopev2",
    root="./",
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
)
app.prepare(ctx_id=0, det_size=current_det_size)

def read_png_metadata(filepath):
    """Read metadata from PNG file"""
    if filepath is None:
        return "No image selected"

    try:
        with Image.open(filepath) as img:
            metadata = img.info
            if "Generation Parameters" in metadata:
                return metadata["Generation Parameters"]
            return "No generation metadata found in this PNG file."
    except Exception as e:
        return f"Error reading metadata: {str(e)}"

face_adapter = f"./checkpoints/ip-adapter.bin"
controlnet_path = f"./checkpoints/ControlNetModel"

controlnet_identitynet = ControlNetModel.from_pretrained(
    controlnet_path, torch_dtype=dtype
)

controlnet_pose_model = "thibaud/controlnet-openpose-sdxl-1.0"
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

def restart_server(open_browser):
    """Restart the current python process aggressively with browser toggle option."""
    python = sys.executable
    script = os.path.abspath(sys.argv[0])
    args = sys.argv[1:]

    os.environ["IN_BROWSER"] = "1" if open_browser else "0"

    torch.cuda.empty_cache()

    if sys.platform == "win32":
        subprocess.Popen([python, script] + args, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
    else:
        subprocess.Popen([python, script] + args, preexec_fn=os.setsid)

    os._exit(0)

def update_det_size(det_size_name):
    """Update the face detection size"""
    global app, current_det_size
    
    new_size = DET_SIZE_OPTIONS[det_size_name]
    if new_size != current_det_size:
        current_det_size = new_size
        app = FaceAnalysis(
            name="antelopev2",
            root="./",
            providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
        )
        app.prepare(ctx_id=0, det_size=current_det_size)
    
    return f"Detection size set to {current_det_size}"

def main(pretrained_model_name_or_path="eniora/RealVisXL_V5.0"):
    if pretrained_model_name_or_path.endswith(
        ".ckpt"
    ) or pretrained_model_name_or_path.endswith(".safetensors"):
        scheduler_kwargs = hf_hub_download(
            repo_id="eniora/RealVisXL_V5.0",
            subfolder="scheduler",
            filename="scheduler_config.json",
        )

        (tokenizers, text_encoders, unet, _, vae) = load_models_xl(
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
    if vram_gb >= 13:
        pipe.load_ip_adapter_instantid(face_adapter)
        pipe._current_model = pretrained_model_name_or_path

    file_prefix = DEFAULT_FILE_PREFIX

    def load_and_cache_controlnet_model(controlnet_type):
        if controlnet_type not in cached_controlnet_models:
            print(f"Loading ControlNet model: {controlnet_type}")
            model = ControlNetModel.from_pretrained(controlnet_model_paths[controlnet_type], torch_dtype=dtype).to(device)
            cached_controlnet_models[controlnet_type] = model
        return cached_controlnet_models[controlnet_type]

    def toggle_lora_ui(enable_lora_checkbox):
        return [gr.update(visible=enable_lora_checkbox)] * len(LORA_OUTPUTS)

    def randomize_seed_fn(seed: int, randomize_seed: bool) -> int:
        if randomize_seed:
            seed = random.randint(0, MAX_SEED)
        return seed

    def convert_from_cv2_to_image(img: np.ndarray) -> Image:
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    def convert_from_image_to_cv2(img: Image) -> np.ndarray:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    def draw_kps(
        image_pil,
        kps,
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
        out_img = (out_img * 0.6).astype(np.uint8)

        for idx_kp, kp in enumerate(kps):
            color = color_list[idx_kp]
            x, y = kp
            out_img = cv2.circle(out_img.copy(), (int(x), int(y)), 10, color, -1)

        out_img_pil = Image.fromarray(out_img.astype(np.uint8))
        return out_img_pil

    def resize_img(
        input_image,
        max_side=4096,
        min_side=512,
        size=None,
        pad_to_max_side=False,
        mode=PIL.Image.LANCZOS,
        base_pixel_number=64,
    ):
        w, h = input_image.size
        if size is not None:
            w_resize_new, h_resize_new = size
        else:
            ratio = min_side / min(h, w)
            w, h = round(ratio * w), round(ratio * h)
            ratio = max_side / max(h, w)
            input_image = input_image.resize([round(ratio * w), round(ratio * h)], mode)
            w_resize_new = (round(ratio * w) // base_pixel_number) * base_pixel_number
            h_resize_new = (round(ratio * h) // base_pixel_number) * base_pixel_number
        input_image = input_image.resize([w_resize_new, h_resize_new], mode)

        if pad_to_max_side:
            res = np.ones([max_side, max_side, 3], dtype=np.uint8) * 255
            offset_x = (max_side - w_resize_new) // 2
            offset_y = (max_side - h_resize_new) // 2
            res[
                offset_y : offset_y + h_resize_new, offset_x : offset_x + w_resize_new
            ] = np.array(input_image)
            input_image = Image.fromarray(res)
        return input_image

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

        if vram_gb >= 13:
            if pipe is not None:
                del pipe
                torch.cuda.empty_cache()
                gc.collect()

        if model_name.endswith(".ckpt") or model_name.endswith(".safetensors"):
            scheduler_kwargs = hf_hub_download(
                repo_id="eniora/RealVisXL_V5.0",
                subfolder="scheduler",
                filename="scheduler_config.json",
            )

            (tokenizers, text_encoders, unet, _, vae) = load_models_xl(
                pretrained_model_name_or_path=model_name,
                scheduler_name=None,
                weight_dtype=dtype,
            )

            scheduler = diffusers.DPMSolverMultistepScheduler.from_config(scheduler_kwargs)
            if enable_img2img:
                pipe = StableDiffusionXLInstantIDImg2ImgPipeline(
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
            if enable_img2img:
                pipe = StableDiffusionXLInstantIDImg2ImgPipeline.from_pretrained(
                    model_name,
                    controlnet=[controlnet_identitynet],
                    torch_dtype=dtype,
                    feature_extractor=None,
                ).to(device)
            else:
                pipe = StableDiffusionXLInstantIDPipeline.from_pretrained(
                    model_name,
                    controlnet=[controlnet_identitynet],
                    torch_dtype=dtype,
                    feature_extractor=None,
                ).to(device)

                pipe.scheduler = diffusers.DPMSolverMultistepScheduler.from_config(
                    pipe.scheduler.config
                )

        pipe.load_ip_adapter_instantid(face_adapter)
        if vram_gb >= 13:
            pipe._current_model = model_name

        return pipe

    def generate_image(
        resize_max_side,
        face_image_path,
        pose_image_path,
        prompt,
        negative_prompt,
        style_name,
        prompt_replacement_value,
        num_steps,
        identitynet_strength_ratio,
        adapter_strength_ratio,
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
        enhance_face_region,
        enhance_strength,
        custom_enhance_padding,
        num_outputs,
        model_name,
        det_size_name,
        file_prefix,
        enable_vae_tiling,
        resize_mode,
        pad_to_max_side,
        enable_custom_resize,
        custom_resize_width,
        custom_resize_height,
        enable_img2img,
        strength,
        progress=gr.Progress(),
    ):
        file_prefix = file_prefix.strip().translate(FILENAME_SAFE_TRANS)
        file_prefix = DEFAULT_FILE_PREFIX if not file_prefix else (f"{file_prefix}_" if not file_prefix.endswith('_') else file_prefix)
        nonlocal pipe
        overall_start_time = time.time()
        
        update_det_size(det_size_name)
        
        is_img2img_pipe = isinstance(pipe, StableDiffusionXLInstantIDImg2ImgPipeline)
        if (
            pipe is None
            or model_name != getattr(pipe, "_current_model", None)
            or (enable_img2img and not is_img2img_pipe)
            or (not enable_img2img and is_img2img_pipe)
        ):
            pipe = load_model_and_update_pipe(model_name, enable_img2img)
            pipe._current_model = model_name

        if enable_vae_tiling:
            pipe.enable_vae_tiling()
        else:
            pipe.disable_vae_tiling()

        if enable_lora:
            pipe.unload_lora_weights()

            loras_to_load = []
            if lora_selection and not disable_lora_1:
                lora_path_1 = os.path.join("./models/Loras", lora_selection)
                if os.path.exists(lora_path_1):
                    loras_to_load.append({"name": lora_selection, "scale": lora_scale})
                    print(f"LoRA 1 selected: {lora_selection} with scale {lora_scale}")
                else:
                    print(f"LoRA 1 not found at {lora_path_1}, skipping load.")
                    gr.Warning(f"LoRA 1 not found at {lora_path_1}. Skipping LoRA 1.")
            
            if lora_selection_2 and not disable_lora_2:
                lora_path_2 = os.path.join("./models/Loras", lora_selection_2)
                if os.path.exists(lora_path_2):
                    loras_to_load.append({"name": lora_selection_2, "scale": lora_scale_2})
                    print(f"LoRA 2 selected: {lora_selection_2} with scale {lora_scale_2}")
                else:
                    print(f"LoRA 2 not found at {lora_path_2}, skipping load.")
                    gr.Warning(f"LoRA 2 not found at {lora_path_2}. Skipping LoRA 2.")

            if lora_selection_3 and not disable_lora_3:
                lora_path_3 = os.path.join("./models/Loras", lora_selection_3)
                if os.path.exists(lora_path_3):
                    loras_to_load.append({"name": lora_selection_3, "scale": lora_scale_3})
                    print(f"LoRA 3 selected: {lora_selection_3} with scale {lora_scale_3}")
                else:
                    print(f"LoRA 3 not found at {lora_path_3}, skipping load.")
                    gr.Warning(f"LoRA 3 not found at {lora_path_3}. Skipping LoRA 3.")

            if lora_selection_4 and not disable_lora_4:
                lora_path_4 = os.path.join("./models/Loras", lora_selection_4)
                if os.path.exists(lora_path_4):
                    loras_to_load.append({"name": lora_selection_4, "scale": lora_scale_4})
                    print(f"LoRA 4 selected: {lora_selection_4} with scale {lora_scale_4}")
                else:
                    print(f"LoRA 4 not found at {lora_path_4}, skipping load.")
                    gr.Warning(f"LoRA 4 not found at {lora_path_4}. Skipping LoRA 4.")

            if lora_selection_5 and not disable_lora_5:
                lora_path_5 = os.path.join("./models/Loras", lora_selection_5)
                if os.path.exists(lora_path_5):
                    loras_to_load.append({"name": lora_selection_5, "scale": lora_scale_5})
                    print(f"LoRA 5 selected: {lora_selection_5} with scale {lora_scale_5}")
                else:
                    print(f"LoRA 5 not found at {lora_path_5}, skipping load.")
                    gr.Warning(f"LoRA 5 not found at {lora_path_5}. Skipping LoRA 5.")

            if lora_selection_6 and not disable_lora_6:
                lora_path_6 = os.path.join("./models/Loras", lora_selection_6)
                if os.path.exists(lora_path_6):
                    loras_to_load.append({"name": lora_selection_6, "scale": lora_scale_6})
                    print(f"LoRA 6 selected: {lora_selection_6} with scale {lora_scale_6}")
                else:
                    print(f"LoRA 6 not found at {lora_path_6}, skipping load.")
                    gr.Warning(f"LoRA 6 not found at {lora_path_6}. Skipping LoRA 6.")

            if lora_selection_7 and not disable_lora_7:
                lora_path_7 = os.path.join("./models/Loras", lora_selection_7)
                if os.path.exists(lora_path_7):
                    loras_to_load.append({"name": lora_selection_7, "scale": lora_scale_7})
                    print(f"LoRA 7 selected: {lora_selection_7} with scale {lora_scale_7}")
                else:
                    print(f"LoRA 7 not found at {lora_path_7}, skipping load.")
                    gr.Warning(f"LoRA 7 not found at {lora_path_7}. Skipping LoRA 7.")

            if lora_selection_8 and not disable_lora_8:
                lora_path_8 = os.path.join("./models/Loras", lora_selection_8)
                if os.path.exists(lora_path_8):
                    loras_to_load.append({"name": lora_selection_8, "scale": lora_scale_8})
                    print(f"LoRA 8 selected: {lora_selection_8} with scale {lora_scale_8}")
                else:
                    print(f"LoRA 8 not found at {lora_path_8}, skipping load.")
                    gr.Warning(f"LoRA 8 not found at {lora_path_8}. Skipping LoRA 8.")

            if loras_to_load:
                for i, lora_item in enumerate(loras_to_load):
                    sanitized_lora_name = lora_item['name'].replace('.safetensors', '').replace('.', '_')
                    adapter_name = f"lora_{i}_{sanitized_lora_name}"
                    pipe.load_lora_weights("./models/Loras", weight_name=lora_item["name"], adapter_name=adapter_name)
                
                adapter_names = [f"lora_{i}_{lora_item['name'].replace('.safetensors', '').replace('.', '_')}" for i, lora_item in enumerate(loras_to_load)]
                adapter_weights = [lora_item['scale'] for lora_item in loras_to_load]
                
                pipe.set_adapters(adapter_names, adapter_weights=adapter_weights)
                pipe.fuse_lora()
                print(f"Successfully loaded and fused {len(loras_to_load)} LoRAs.")
            else:
                pipe.disable_lora()
                print("No LoRAs selected or found, LoRA disabled.")
        else:
            pipe.disable_lora()

        face_image_filename = os.path.basename(face_image_path) if face_image_path else "None"
        pose_image_filename = os.path.basename(pose_image_path) if pose_image_path else "None"

        with torch.no_grad():
            scheduler_config = dict(pipe.scheduler.config.items())

            if not controlnet_selection:
                torch.cuda.empty_cache()

            use_karras = "Karras" in scheduler
            use_sde = "SDE" in scheduler
            scheduler_split = scheduler.split("-")[0]
            scheduler_class = getattr(diffusers, scheduler_split)
    
            if "DPMSolver" in scheduler_split:
                pipe.scheduler = scheduler_class.from_config(
                    scheduler_config,
                    use_karras_sigmas=use_karras,
                    algorithm_type="sde-dpmsolver++" if use_sde else "dpmsolver++"
                )
            elif scheduler_split in ["KDPM2AncestralDiscreteScheduler", "KDPM2DiscreteScheduler"]:
                pipe.scheduler = scheduler_class.from_config(
                    scheduler_config,
                    use_karras_sigmas=use_karras
                )
            else:
                pipe.scheduler = scheduler_class.from_config(scheduler_config)

        if face_image_path is None:
            if enable_lora:
                pipe.unfuse_lora()
                pipe.unload_lora_weights()
            raise gr.Error(
                f"Cannot find any input face image! Please upload the face image"
            )

        if not prompt:
            prompt = " " if prompt_replacement_value == "Empty (none)" else prompt_replacement_value

        prompt, negative_prompt = apply_style(style_name, prompt, negative_prompt)

        face_image = load_image(face_image_path)
        custom_size = None
        if enable_custom_resize:
            custom_size = (int(custom_resize_width), int(custom_resize_height))
        resize_mode_enum = getattr(PIL.Image, resize_mode)
        face_image = resize_img(face_image, size=custom_size, max_side=resize_max_side, mode=resize_mode_enum, pad_to_max_side=pad_to_max_side)
        face_image_cv2 = convert_from_image_to_cv2(face_image)
        height, width, _ = face_image_cv2.shape

        face_info = app.get(face_image_cv2)

        if len(face_info) == 0:
            if enable_lora:
                pipe.unfuse_lora()
                pipe.unload_lora_weights()
            raise gr.Error(
                f"Unable to detect a face in the image. Please upload a different photo with a clear face."
            )

        face_info = sorted(face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]))[-1]
        face_emb = face_info["embedding"]
        face_kps = draw_kps(convert_from_cv2_to_image(face_image_cv2), face_info["kps"])
        img_controlnet = face_image
        if pose_image_path is not None:
            pose_image = load_image(pose_image_path)
            pose_image = resize_img(pose_image, size=custom_size, max_side=resize_max_side, mode=resize_mode_enum, pad_to_max_side=pad_to_max_side)
            img_controlnet = pose_image
            pose_image_cv2 = convert_from_image_to_cv2(pose_image)

            face_info = app.get(pose_image_cv2)

            if len(face_info) == 0:
                if enable_lora:
                    pipe.unfuse_lora()
                    pipe.unload_lora_weights()
                raise gr.Error(
                    f"Cannot find any face in the reference image! Please upload another person image"
                )

            face_info = face_info[-1]
            face_kps = draw_kps(pose_image, face_info["kps"])

            width, height = face_kps.size

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

        if len(controlnet_selection) > 0:
            global cached_controlnet_models
            for k in list(cached_controlnet_models.keys()):
                if k not in controlnet_selection:
                    del cached_controlnet_models[k]
                    torch.cuda.empty_cache()
                    gc.collect()
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
        else:
            if cached_controlnet_models:
                for key in list(cached_controlnet_models.keys()):
                    del cached_controlnet_models[key]
                    torch.cuda.empty_cache()
                    gc.collect()
            pipe.controlnet = controlnet_identitynet
            control_scales = float(identitynet_strength_ratio)
            control_images = face_kps

        generator = torch.Generator(device=device).manual_seed(seed)

        print("Starting image generation...")
        print(f"Prompt: {prompt}\nNegative Prompt: {negative_prompt}")
        print(f"Detection size: {current_det_size}")
        print(f"Input face image: {os.path.basename(face_image_path) if face_image_path else 'None'}")
        print(f"Reference pose image: {os.path.basename(pose_image_path) if pose_image_path else 'None'}")
        print(f"Steps: {num_steps}")
        print(f"img2img Mode: {'Enabled' if enable_img2img else 'Disabled'}")
        if enable_img2img:
            print(f"img2img Denoising Strength: {strength}")
        print(f"Enhance non-face region: {'True' if enhance_face_region else 'False'} ({enhance_strength}{f' | Padding: {custom_enhance_padding:.2f}' if enhance_strength == 'Custom' else ''})")
        print(f"Guidance scale: {guidance_scale}")
        print(f"Model: {model_name}")
        print(f"Resize mode: {resize_mode}")
        print(f"Pad to max side: {pad_to_max_side}")
        print(f"Use custom resize: {enable_custom_resize}")
        if enable_custom_resize:
            print(f"Custom resize size: {custom_resize_width}x{custom_resize_height}")
        print(f"ControlNet selection: {controlnet_selection} | Strengths - Pose: {pose_strength}, Canny: {canny_strength}, Depth: {depth_strength}")
        print(f"IdentityNet strength: {identitynet_strength_ratio}")
        print(f"Adapter strength: {adapter_strength_ratio}")

        lora_info_str = "Disabled"
        if enable_lora:
            lora_details = []
            
            if lora_selection:
                if not disable_lora_1 and os.path.exists(os.path.join('./models/Loras', lora_selection)):
                    lora_details.append(f"LoRA 1: {lora_selection} (Scale: {lora_scale})")
                elif disable_lora_1:
                    lora_details.append("LoRA 1: Manually disabled")
                else:
                    lora_details.append(f"LoRA 1: {lora_selection} (Not found)")

            if lora_selection_2:
                if not disable_lora_2 and os.path.exists(os.path.join('./models/Loras', lora_selection_2)):
                    lora_details.append(f"LoRA 2: {lora_selection_2} (Scale: {lora_scale_2})")
                elif disable_lora_2:
                    lora_details.append("LoRA 2: Manually disabled")
                else:
                    lora_details.append(f"LoRA 2: {lora_selection_2} (Not found)")

            if lora_selection_3:
                if not disable_lora_3 and os.path.exists(os.path.join('./models/Loras', lora_selection_3)):
                    lora_details.append(f"LoRA 3: {lora_selection_3} (Scale: {lora_scale_3})")
                elif disable_lora_3:
                    lora_details.append("LoRA 3: Manually disabled")
                else:
                    lora_details.append(f"LoRA 3: {lora_selection_3} (Not found)")

            if lora_selection_4:
                if not disable_lora_4 and os.path.exists(os.path.join('./models/Loras', lora_selection_4)):
                    lora_details.append(f"LoRA 4: {lora_selection_4} (Scale: {lora_scale_4})")
                elif disable_lora_4:
                    lora_details.append("LoRA 4: Manually disabled")
                else:
                    lora_details.append(f"LoRA 4: {lora_selection_4} (Not found)")

            if lora_selection_5:
                if not disable_lora_5 and os.path.exists(os.path.join('./models/Loras', lora_selection_5)):
                    lora_details.append(f"LoRA 5: {lora_selection_5} (Scale: {lora_scale_5})")
                elif disable_lora_5:
                    lora_details.append("LoRA 5: Manually disabled")
                else:
                    lora_details.append(f"LoRA 5: {lora_selection_5} (Not found)")

            if lora_selection_6:
                if not disable_lora_6 and os.path.exists(os.path.join('./models/Loras', lora_selection_6)):
                    lora_details.append(f"LoRA 6: {lora_selection_6} (Scale: {lora_scale_6})")
                elif disable_lora_6:
                    lora_details.append("LoRA 6: Manually disabled")
                else:
                    lora_details.append(f"LoRA 6: {lora_selection_6} (Not found)")

            if lora_selection_7:
                if not disable_lora_7 and os.path.exists(os.path.join('./models/Loras', lora_selection_7)):
                    lora_details.append(f"LoRA 7: {lora_selection_7} (Scale: {lora_scale_7})")
                elif disable_lora_7:
                    lora_details.append("LoRA 7: Manually disabled")
                else:
                    lora_details.append(f"LoRA 7: {lora_selection_7} (Not found)")

            if lora_selection_8:
                if not disable_lora_8 and os.path.exists(os.path.join('./models/Loras', lora_selection_8)):
                    lora_details.append(f"LoRA 8: {lora_selection_8} (Scale: {lora_scale_8})")
                elif disable_lora_8:
                    lora_details.append("LoRA 8: Manually disabled")
                else:
                    lora_details.append(f"LoRA 8: {lora_selection_8} (Not found)")

            lora_info_str = "; ".join(lora_details)
        print(f"LoRA(s): {lora_info_str}")

        print(f"Scheduler: {scheduler}")
        print(f"Max resize side: {resize_max_side}")
        print(f"Image size: {width}x{height}\n")

        pipe.set_ip_adapter_scale(adapter_strength_ratio)
        images = []
        generation_infos = []
        for i in range(num_outputs):
            print(f"Generating image {i + 1} of {num_outputs}...\n")

            if enable_img2img:
                effective_steps = max(1, int(num_steps * strength))
                step_tracker = {"last": -1, "total": 0}
                is_slow_scheduler = any(x in scheduler for x in ["DPMSolverSDE", "KDPM2", "Heun"])
                if is_slow_scheduler:
                    def gradio_callback_lambda(pipe_obj, step, timestep, callback_kwargs):
                        if step != step_tracker["last"]:
                            step_tracker["last"] = step
                            step_tracker["total"] += 1

                        est_total = effective_steps * 2
                        pct = int((step_tracker["total"] / est_total) * 100)
                        progress(
                            ((i / num_outputs) + (step_tracker["total"] / est_total) / num_outputs),
                            desc=f"Generating image {i + 1} of {num_outputs} (Step {min(step_tracker['total'] // 2, effective_steps)}/{effective_steps})"
                        )
                        return callback_kwargs
                else:
                    gradio_callback_lambda = lambda pipe_obj, step, timestep, callback_kwargs: (
                        progress(
                            ((i / num_outputs) + (((step + 1) / effective_steps) / num_outputs)),
                            desc=f"Generating image {i + 1} of {num_outputs} (Step {step + 1}/{effective_steps})"
                        ),
                        callback_kwargs
                    )[1]
            else:
                step_tracker = {"last": -1, "total": 0}
                is_slow_scheduler = any(x in scheduler for x in ["DPMSolverSDE", "KDPM2", "Heun"])
                if is_slow_scheduler:
                    def gradio_callback_lambda(pipe_obj, step, timestep, callback_kwargs):
                        if step != step_tracker["last"]:
                            step_tracker["last"] = step
                            step_tracker["total"] += 1

                        est_total = num_steps * 2
                        pct = int((step_tracker["total"] / est_total) * 100)
                        progress(
                            ((i / num_outputs) + (step_tracker["total"] / est_total) / num_outputs),
                            desc=f"Generating image {i + 1} of {num_outputs} (Step {min(step_tracker['total'] // 2, num_steps)}/{num_steps})"
                        )
                        return callback_kwargs
                else:
                    gradio_callback_lambda = lambda pipe_obj, step, timestep, callback_kwargs: (
                        progress(
                            ((i / num_outputs) + (((step + 1) / num_steps) / num_outputs)),
                            desc=f"Generating image {i + 1} of {num_outputs} (Step {step + 1}/{num_steps})"
                        ),
                        callback_kwargs
                    )[1]

            print(f"Seed: {seed + i}\n")

            generator = torch.Generator(device=device).manual_seed(seed + i)
            if enable_img2img:
                result = pipe(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    image=face_image,
                    control_image=control_images,
                    strength=strength,
                    image_embeds=face_emb,
                    controlnet_conditioning_scale=control_scales,
                    num_inference_steps=num_steps,
                    guidance_scale=guidance_scale,
                    height=height,
                    width=width,
                    generator=generator,
                    callback_on_step_end=gradio_callback_lambda,
                )
                image = result.images[0]
                images.append(image)
            else:
                result = pipe(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    image_embeds=face_emb,
                    image=control_images,
                    control_mask=control_mask,
                    controlnet_conditioning_scale=control_scales,
                    num_inference_steps=num_steps,
                    guidance_scale=guidance_scale,
                    height=height,
                    width=width,
                    generator=generator,
                    callback_on_step_end=gradio_callback_lambda,
                )
                image = result.images[0]
                images.append(image)

            info_text = f"""Prompt: {prompt}
Negative Prompt: {negative_prompt}
Input Face Image: {face_image_filename}
Reference Pose Image: {pose_image_filename}
Detection size: {current_det_size}
Steps: {num_steps}
Guidance scale: {guidance_scale}
Seed: {seed + i}
Model: {model_name}
ControlNet selection: {controlnet_selection}
Max resize side: {resize_max_side}
Image size: {width}x{height}
Enhance non-face region: {enhance_face_region}
Enhance region profile: {enhance_strength}
Enhance padding ratio: {custom_enhance_padding}
Resize mode: {resize_mode}
Pad to max side: {pad_to_max_side}
Use custom resize: {enable_custom_resize}
Custom resize size: {custom_resize_width}x{custom_resize_height}
img2img Strength: {strength}
img2img Mode Enabled: {enable_img2img}
IdentityNet strength: {identitynet_strength_ratio}
Adapter strength: {adapter_strength_ratio}
Pose strength: {pose_strength}
Canny strength: {canny_strength}
Depth strength: {depth_strength}
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
Scheduler: {scheduler}"""

            png_info = PIL.PngImagePlugin.PngInfo()
            png_info.add_text("Generation Parameters", info_text)
            generation_infos.append(png_info)
            save_images([image], generation_info=[png_info], prefix=file_prefix)
            print(f"(√) Finished generating image {i + 1} of {num_outputs}\n")

            torch.cuda.empty_cache()

        if enable_lora:
            pipe.unfuse_lora()
            pipe.unload_lora_weights()

        gc.collect()
        overall_elapsed_time = time.time() - overall_start_time
        print(f"Total generation time: {overall_elapsed_time:.2f} seconds\n")
        return images

    article = r"""
    - Upload an image with a face. For images with multiple faces, only the largest face will be detected. Ensure the face is not too small and is clearly visible without significant obstructions or blurring.
    - (Optional) You can upload another image as a reference for the face pose. If you don't, the first detected face image will be used to extract facial landmarks. If you use a cropped face at step 1, it is recommended to upload it to define a new face pose.
    - (Optional) You can select multiple ControlNet models to control the generation process. The default is to use the IdentityNet only. The ControlNet models include pose skeleton, canny, and depth. You can adjust the strength of each ControlNet model to control the generation process.
    - Enter a text prompt, as done in normal text-to-image models.
    - Click the Generate button to begin customization.
    - img2img mode imports the "pipeline_stable_diffusion_xl_instantid_img2img" pipeline, it's good to experiment with it and I got quite good results using it. It uses a lot of VRAM though (~20GB). Enhance non-face region (control_mask) has no effect on this mode and that's by design.
    - In some cases, minimizing the browser/Gradio window while an image is being generated can help speed up the generation process. You can track the progress in the CMD/Terminal window.
    - Select a model to use for generation from the upper left corner dropdown. Only use SDXL and Pony. Illustrious can be loaded but isn't well supported.
    - You can select a scheduler from the upper right corner dropdown. DPMSolver, KDPM2 and Euler are usually the best.
    
    Other usage tips of InstantID:
    - If you're not satisfied with the similarity, try increasing the weight of "IdentityNet Strength" and "Adapter Strength."    
    - If you feel that the saturation is too high, first decrease the Adapter strength. If it remains too high, then decrease the IdentityNet strength.
    - If you find that text control is not as expected, decrease Adapter strength.
    - If you find that the style or generated images are not good enough, try another base model.
    - If you're having trouble detecting faces, try changing the "Face Detection Size" setting or try another input face photo.
    """
    css = """
    .gradio-container {width: 85% !important}
    """
    with gr.Blocks(css=css) as gui:
        with gr.Row():
            with gr.Column(scale=1):
                with gr.Row():
                    model_name = gr.Dropdown(
                        choices=AVAILABLE_MODELS,
                        value=DEFAULT_MODEL,
                        show_label=False,
                        container=False,
                        scale=5
                    )
                    refresh_models = gr.Button("🔄", scale=0, min_width=40, elem_classes="toolbutton")
            with gr.Column(scale=1):
                schedulers = [
                    "DPMSolverMultistepScheduler",
                    "DPMSolverMultistepScheduler-SDE",
                    "DPMSolverMultistepScheduler-Karras",
                    "DPMSolverMultistepScheduler-Karras-SDE",
                    "EulerDiscreteScheduler",
                    "DPMSolverSDEScheduler-Karras",
                    "DPMSolverSDEScheduler",
                    "KDPM2DiscreteScheduler",
                    "KDPM2DiscreteScheduler-Karras",
                    "KDPM2AncestralDiscreteScheduler-Karras",
                    "DPMSolverSinglestepScheduler",
                    "DPMSolverSinglestepScheduler-Karras",
                    "DPMSolverSinglestepScheduler-Karras-SDE",
                    "EulerAncestralDiscreteScheduler",
                    "DDIMScheduler",
                    "DDPMScheduler",
                    "HeunDiscreteScheduler",
                    "LMSDiscreteScheduler",
                    "UniPCMultistepScheduler",
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
                outputs=model_name
            )

        with gr.Row():
            with gr.Column():
                with gr.Row(equal_height=True):
                    face_file = gr.Image(
                        label="Upload a photo containing a face", type="filepath"
                    )
                    pose_file = gr.Image(
                        label="Upload a reference pose image (Optional)",
                        type="filepath"
                    )

                prompt = gr.Textbox(
                    label="Prompt",
                    info="Giving a simple prompt is enough to achieve good face fidelity",
                    placeholder="A man/woman/girl/boy in/with/as etc.",
                    value="",
                )
                negative_prompt = gr.Textbox(
                    label="Negative Prompt",
                    placeholder="You can select a negative prompt profile from the settings tab below.",
                    value=NEGATIVE_PROMPT_PRESETS["Default Negative Profile"]
                )
                with gr.Accordion("⚙️ Style templates and other settings including custom resolution", open=False) as style_settings_accordion:
                    with gr.Group():
                        style = gr.Dropdown(
                            label="Style templates",
                            choices=STYLE_NAMES,
                            value=DEFAULT_STYLE_NAME,
                            info="Selecting a style empties the prompt and negative prompt fields because styles have their own. It's good to add to the prompt field."
                        )
                        apply_selected_style_btn = gr.Button(
                            "⇄ Insert selected style text into prompt & negative prompt fields. '(No style)' will be selected after clicking this.",
                            size="sm",
                            variant="secondary"
                        )
                        style.change(
                            fn=on_style_change,
                            inputs=style,
                            outputs=[prompt, negative_prompt]
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
                            label="Negative Prompt Profile",
                            choices=list(NEGATIVE_PROMPT_PRESETS.keys()),
                            value="Default Negative Profile"
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
                        )
                        def apply_selected_negative_profile(selected_negative_profile):
                            return NEGATIVE_PROMPT_PRESETS[selected_negative_profile]

                        apply_negative_profile_btn.click(
                            fn=apply_selected_negative_profile,
                            inputs=negative_prompt_preset,
                            outputs=negative_prompt,
                        )
                    with gr.Row():
                        generate_alt_3 = gr.Button("Generate (Extra Settings Section Button)", variant="primary")
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
                    with gr.Row():
                        enable_vae_tiling = gr.Checkbox(
                            label="Enable VAE Tiling (saves VRAM for large images at the last generation step)",
                            value=True,
                            info="Processes images in tiles to reduce VRAM usage during the final VAE decoding step without any quality loss."
                        )
                    with gr.Row():
                        resize_mode_dropdown = gr.Dropdown(
                            label="Resize Interpolation Mode",
                            choices=[
                                "LANCZOS", "BILINEAR", "HAMMING", "BICUBIC", "BOX", "NEAREST"
                            ],
                            value="LANCZOS",
                            info="Interpolation method used when resizing input images, LANCZOS, BILINEAR and HAMMING are usually the best."
                        )
                    with gr.Row():
                        pad_to_max_checkbox = gr.Checkbox(
                            label="Pad resized image to square",
                            value=False,
                            info="If enabled, resized images are padded to a square shape. Usually slower and uses more VRAM due to the square shape resolution."
                        )
                    enable_custom_resize = gr.Checkbox(
                        label="Enable custom resolution",
                        value=False,
                        info="If enabled, you can set a custom resolution (width x height). This overrides Max image size for resizing. Only use if you know what you're doing. Don't use along with 'Pad resized image to square' option above this one."
                    )
                    custom_resize_width = gr.Slider(
                        label="Custom Width",
                        minimum=512,
                        maximum=4096,
                        step=64,
                        value=960,
                        visible=False,
                        interactive=True
                    )
                    custom_resize_height = gr.Slider(
                        label="Custom Height",
                        minimum=512,
                        maximum=4096,
                        step=64,
                        value=1280,
                        visible=False,
                        interactive=True
                    )
                    def toggle_custom_resize_controls(value):
                        return gr.update(visible=value), gr.update(visible=value)

                    enable_custom_resize.change(
                        fn=toggle_custom_resize_controls,
                        inputs=enable_custom_resize,
                        outputs=[custom_resize_width, custom_resize_height]
                    )
                resize_max_side_slider = gr.Slider(
                    label="Max image size for resizing (output resolution)",
                    minimum=512,
                    maximum=4096,
                    step=64,
                    value=1280,
                    info="Controls the max_side for input image resizing. Up to 1920 can be good. Above 2000 is for ultra wide/vertical images.",
                )
                with gr.Row():
                    generate = gr.Button("Generate", scale=8, variant="primary")
                    num_outputs = gr.Number(
                        value=1,
                        step=1,
                        minimum=1,
                        maximum=1000,
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
                with gr.Accordion("Controlnet", open=False) as controlnet_accordion:
                    controlnet_selection = gr.CheckboxGroup(
                        ["pose", "canny", "depth"], value=[], show_label=False,
                        info="Use pose for skeleton inference, canny for edge detection, and depth for depth map estimation. You can try all three to control the generation process"
                    )
                    pose_strength = gr.Slider(
                        label="Pose strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.40,
                    )
                    canny_strength = gr.Slider(
                        label="Canny strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.40,
                    )
                    depth_strength = gr.Slider(
                        label="Depth strength",
                        minimum=0,
                        maximum=1.5,
                        step=0.05,
                        value=0.40,
                    )
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
                        maximum=100,
                        step=1,
                        value=24,
                    )
                with gr.Row():
                    randomize_seed = gr.Checkbox(label="Randomize seed", scale=1, value=True)
                    seed = gr.Slider(
                        label="Seed value",
                        minimum=0,
                        maximum=MAX_SEED,
                        step=1,
                        scale=5,
                        value=42,
                    )
                with gr.Row():
                    enhance_face_region = gr.Checkbox(label="Enhance non-face region", scale=2, value=True)
                    enhance_strength = gr.Dropdown(
                        label="Enhance Non-Face Region Amount",
                        choices=["Default", "Balanced", "High", "Custom"],
                        value="Balanced",
                        scale=3,
                        info="Larger values retain more from the input image around the face (e.g., hairstyle). 'Balanced' is good but you can use 'Default' for more control."
                    )
                    custom_enhance_padding = gr.Slider(
                        label="Custom enhancement padding (%)",
                        minimum=0.0,
                        maximum=0.9,
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
                        outputs=custom_enhance_padding
                    )
                with gr.Row():
                    det_size_name = gr.Dropdown(
                        label="Face Detection Size",
                        choices=list(DET_SIZE_OPTIONS.keys()),
                        value="640x640 (default)",
                        info="Higher values can detect smaller faces better if the face in the input/reference image is too small/distant. Change the value only if you get 'No face detected', it can help a lot in some face input photos."
                    )
                with gr.Row():
                    generate_alt_2 = gr.Button("Generate (Extra Bottom Button)", variant="primary")
                    open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                    open_folder_btn.click(
                        fn=open_output_folder,
                        inputs=[],
                        outputs=[],
                        queue=False
                    )
            with gr.Column(scale=1):
                gallery = gr.Gallery(label="Generated Images")
                with gr.Row():
                    generate_alt = gr.Button("Generate (Extra Right Side Button)", variant="primary")
                    open_folder_btn = gr.Button("📁", min_width=60, scale=0)
                    open_folder_btn.click(
                        fn=open_output_folder,
                        inputs=[],
                        outputs=[],
                        queue=False
                    )
                with gr.Row():
                    enable_img2img = gr.Checkbox(label="Enable img2img mode", value=False, scale=2)
                    strength = gr.Slider(label="img2img Denoising Strength", minimum=0.1, maximum=1.0, value=0.95, step=0.05, visible=False, scale=5, info="Use this for more control over e.g., location setting, clothing style, pose, etc. A lower value preserves more of the original image. CFG scale of ~3 is recommended.")

                def toggle_img2img(enable):
                    return gr.update(visible=enable)

                enable_img2img.change(toggle_img2img, inputs=enable_img2img, outputs=strength)
                with gr.Accordion("PNG Metadata Reader", open=True):
                    with gr.Row():
                        metadata_input = gr.Image(
                            label="Drop PNG file here to read generation metadata",
                            type="filepath",
                            height=500,
                            width=500
                        )
                        metadata_output = gr.Textbox(
                            label="Generation Metadata",
                            interactive=False,
                            lines=22,
                            max_lines=22
                        )

                    with gr.Row():
                        apply_metadata_btn = gr.Button("Apply to all fields", variant="secondary")
            
                    metadata_input.upload(
                        fn=lambda x: (x, read_png_metadata(x) if x is not None else ""),
                        inputs=metadata_input,
                        outputs=[metadata_input, metadata_output]
                    )
                with gr.Column():
                    enable_lora = gr.Checkbox(
                        label="Enable LoRA(s) from your Models\Loras folder",
                        value=False,
                    )
                    lora_info = gr.Markdown(
                        "Up to eight LoRAs can be loaded. Only SDXL and Pony LoRAs supported. The 'Disable Lora' checkbox is only needed if you have a Lora selected.",
                        visible=False
                    )
                    enable_lora.change(
                        fn=lambda x: gr.Markdown(visible=x),
                        inputs=enable_lora,
                        outputs=lora_info
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
                            info="Select the first LoRA.",
                            scale=3
                        )
                        lora_scale = gr.Slider(
                            label="LoRA 1 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=1.0,
                            info="Strength of the first LoRA effect.",
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
                            info="Select a second LoRA.",
                            scale=3
                        )
                        lora_scale_2 = gr.Slider(
                            label="LoRA 2 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.7,
                            info="Strength of the second LoRA effect.",
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
                            info="Select a third LoRA.",
                            scale=3
                        )
                        lora_scale_3 = gr.Slider(
                            label="LoRA 3 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the third LoRA effect.",
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
                            info="Select a fourth LoRA.",
                            scale=3
                        )
                        lora_scale_4 = gr.Slider(
                            label="LoRA 4 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the fourth LoRA effect.",
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
                            info="Select a fifth LoRA.",
                            scale=3
                        )
                        lora_scale_5 = gr.Slider(
                            label="LoRA 5 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the fifth LoRA effect.",
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
                            info="Select a sixth LoRA.",
                            scale=3
                        )
                        lora_scale_6 = gr.Slider(
                            label="LoRA 6 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the sixth LoRA effect.",
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
                            info="Select a seventh LoRA.",
                            scale=3
                        )
                        lora_scale_7 = gr.Slider(
                            label="LoRA 7 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the seventh LoRA effect.",
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
                            info="Select an eighth LoRA.",
                            scale=3
                        )
                        lora_scale_8 = gr.Slider(
                            label="LoRA 8 Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=0.5,
                            info="Strength of the eighth LoRA effect.",
                            scale=3
                        )
                        disable_lora_8 = gr.Checkbox(
                            label="Disable LoRA 8",
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

                    def refresh_lora_list():
                        loras = [""] + get_available_loras()
                        return gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras), gr.update(choices=loras)
                    
                    refresh_loras.click(
                        fn=refresh_lora_list,
                        outputs=[lora_selection, lora_selection_2, lora_selection_3, lora_selection_4, lora_selection_5, lora_selection_6, lora_selection_7, lora_selection_8]
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
                            lora_selection, lora_selection_2, lora_selection_3, lora_selection_4, lora_selection_5, lora_selection_6, lora_selection_7, lora_selection_8,
                            disable_lora_1, disable_lora_2, disable_lora_3, disable_lora_4, disable_lora_5, disable_lora_6, disable_lora_7, disable_lora_8
                        ]
                    )

            shared_inputs = [
                resize_max_side_slider,
                face_file,
                pose_file,
                prompt,
                negative_prompt,
                style,
                prompt_replacement,
                num_steps,
                identitynet_strength_ratio,
                adapter_strength_ratio,
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
                enhance_face_region,
                enhance_strength,
                custom_enhance_padding,
                num_outputs,
                model_name,
                det_size_name,
                file_prefix,
                enable_vae_tiling,
                resize_mode_dropdown,
                pad_to_max_checkbox,
                enable_custom_resize,
                custom_resize_width,
                custom_resize_height,
                enable_img2img,
                strength,
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

            LORA_OUTPUTS = [
                lora_row_1, lora_selection, lora_scale,
                lora_row_2, lora_selection_2, lora_scale_2,
                lora_row_3, lora_selection_3, lora_scale_3,
                lora_row_4, lora_selection_4, lora_scale_4,
                lora_row_5, lora_selection_5, lora_scale_5,
                lora_row_6, lora_selection_6, lora_scale_6,
                lora_row_7, lora_selection_7, lora_scale_7,
                lora_row_8, lora_selection_8, lora_scale_8,
                refresh_loras, clear_loras
            ]

            enable_lora.input(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=LORA_OUTPUTS,
                queue=False,
            )

            def extract_all_settings(metadata_text):
                accordion_update = gr.update(open=False)
                settings = {
                    "prompt": "",
                    "negative_prompt": DEFAULT_NEGATIVE_PROFILE,
                    "resize_max_side": 1280,
                    "seed": 42,
                    "num_steps": 24,
                    "guidance_scale": 4.0,
                    "enable_img2img": False,
                    "strength": 0.95,
                    "identitynet_strength_ratio": 0.7,
                    "adapter_strength_ratio": 0.6,
                    "pose_strength": 0.40,
                    "canny_strength": 0.40,
                    "depth_strength": 0.40,
                    "scheduler": "DPMSolverMultistepScheduler",
                    "enable_lora": False,
                    "lora_scale": 1.0,
                    "lora_selection": None,
                    "lora_scale_2": 0.7,
                    "lora_selection_2": None,
                    "lora_scale_3": 0.5,
                    "lora_selection_3": None,
                    "lora_scale_4": 0.5,
                    "lora_selection_4": None,
                    "lora_scale_5": 0.5,
                    "lora_selection_5": None,
                    "lora_scale_6": 0.5,
                    "lora_selection_6": None,
                    "lora_scale_7": 0.5,
                    "lora_selection_7": None,
                    "lora_scale_8": 0.5,
                    "lora_selection_8": None,
                    "enhance_face_region": True,
                    "enhance_strength": "Balanced",
                    "custom_enhance_padding": 0.15,
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
                    "resize_mode": "LANCZOS",
                    "pad_to_max_side": False,
                    "enable_custom_resize": False,
                    "custom_resize_width": 960,
                    "custom_resize_height": 1280
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
                        elif line.startswith("LoRA Enabled:"):
                            settings["enable_lora"] = "true" in line.lower()
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
                        elif line.startswith("img2img Mode Enabled:"):
                            settings["enable_img2img"] = "true" in line.lower()
                        elif line.startswith("img2img Strength:"):
                            settings["strength"] = float(line.replace("img2img Strength:", "").strip())
                        elif line.startswith("Enhance non-face region:"):
                            settings["enhance_face_region"] = "true" in line.lower()
                        elif line.startswith("Enhance region profile:"):
                            settings["enhance_strength"] = line.replace("Enhance region profile:", "").strip()
                        elif line.startswith("Enhance padding ratio:"):
                            try:
                                settings["custom_enhance_padding"] = float(line.replace("Enhance padding ratio:", "").strip())
                            except:
                                pass
                        elif line.startswith("IdentityNet strength:"):
                            settings["identitynet_strength_ratio"] = float(line.replace("IdentityNet strength:", "").strip())
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
                            if model_name in AVAILABLE_MODELS:
                                settings["model_name"] = model_name
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
                        elif line.startswith("Use custom resize:"):
                            settings["enable_custom_resize"] = "true" in line.lower()
                        elif line.startswith("Custom resize size:"):
                            try:
                                dims = line.replace("Custom resize size:", "").strip().lower().split("x")
                                settings["custom_resize_width"] = int(dims[0])
                                settings["custom_resize_height"] = int(dims[1])
                            except:
                                pass

                open_settings_accordion = False

                if settings["enable_custom_resize"] or settings["pad_to_max_side"]:
                    open_settings_accordion = True

                return [
                    settings["prompt"],
                    settings["negative_prompt"],
                    settings["style"],
                    settings["num_steps"],
                    settings["enable_img2img"],
                    settings["strength"],
                    settings["identitynet_strength_ratio"],
                    settings["adapter_strength_ratio"],
                    settings["pose_strength"],
                    settings["canny_strength"],
                    settings["depth_strength"],
                    settings["guidance_scale"],
                    settings["seed"],
                    settings["scheduler"],
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
                    settings["resize_mode"],
                    settings["pad_to_max_side"],
                    settings["enable_custom_resize"],
                    settings["custom_resize_width"],
                    settings["custom_resize_height"],
                    accordion_update,
                    gr.update(open=open_settings_accordion)
                ]

            apply_metadata_btn.click(
                fn=extract_all_settings,
                inputs=metadata_output,
                outputs=[
                    prompt,
                    negative_prompt,
                    style,
                    num_steps,
                    enable_img2img,
                    strength,
                    identitynet_strength_ratio,
                    adapter_strength_ratio,
                    pose_strength,
                    canny_strength,
                    depth_strength,
                    guidance_scale,
                    seed,
                    scheduler,
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
                    resize_mode_dropdown,
                    pad_to_max_checkbox,
                    enable_custom_resize,
                    custom_resize_width,
                    custom_resize_height,
                    controlnet_accordion,
                    style_settings_accordion
                ]
            ).then(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=LORA_OUTPUTS
            )

        with gr.Accordion("📝 Click to show usage tips", open=False):
            gr.Markdown(article)
        gr.Markdown("<b>InstantID: Unlocked v4.2.0</b> - <a href='https://github.com/eniora/InstantID-Unlocked' target='_blank'><b>Github fork page for InstantID: Unlocked</b></a><br>")

        with gr.Row():
            with gr.Column():
                restart_browser_checkbox = gr.Checkbox(
                    label="Automatically open a new InstantID browser tab after the Restart Server button is clicked",
                    value=False
                )
                restart_btn = gr.Button("Restart Server", variant="stop", scale=1)
                restart_btn.click(
                    js="(open_browser) => { if (confirm('Are you sure you want to restart the server?')) return open_browser; else return null; }",
                    fn=lambda open_browser: restart_server(open_browser) if open_browser is not None else None,
                    inputs=restart_browser_checkbox,
                    outputs=None,
                    queue=False,
                )

    gui.launch(inbrowser=os.environ.get("IN_BROWSER", "1") == "1")

main()