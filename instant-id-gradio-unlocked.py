import sys
sys.path.append("./")

from typing import Tuple

import os
import cv2
import math
import torch
import random
import numpy as np
import argparse
import warnings
import PIL.PngImagePlugin

warnings.filterwarnings("ignore", message=".*Overwriting tiny_vit_.* in registry.*")

os.environ["NO_ALBUMENTATIONS_UPDATE"] = "1"
# os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_CACHE"] = "models"
os.environ["HF_HUB_CACHE_OFFLINE"] = "true"

def open_output_folder():
    path = os.path.abspath("output")
    os.system(f'start "" "{path}"')

import PIL
from PIL import Image

DEFAULT_FILE_PREFIX = "InstantID_"

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

import diffusers
from diffusers.utils import load_image
from diffusers.models import ControlNetModel
from diffusers.pipelines.controlnet.multicontrolnet import MultiControlNetModel

from huggingface_hub import hf_hub_download

from insightface.app import FaceAnalysis

from style_template import styles
from pipeline_stable_diffusion_xl_instantid_full import StableDiffusionXLInstantIDPipeline
from model_util import load_models_xl, get_torch_device, torch_gc
from controlnet_util import openpose, get_depth_map, get_canny_image

import gradio as gr


# global variable
MAX_SEED = np.iinfo(np.int32).max
device = get_torch_device()
dtype = torch.float16 if str(device).__contains__("cuda") else torch.float32
STYLE_NAMES = list(styles.keys())
DEFAULT_STYLE_NAME = "(No style)"

# Negative prompt presets
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
}

DEFAULT_NEGATIVE_PROFILE = NEGATIVE_PROMPT_PRESETS["Default Negative Profile"]

def on_style_change(style_name):
    if style_name == "(No style)":
        return gr.update(value=DEFAULT_NEGATIVE_PROFILE)
    else:
        return gr.update(value="")

# Get available models from the models folder
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
DEFAULT_MODEL = "stablediffusionapi/protovision-xl-high-fidel"

# Detection size options
DET_SIZE_OPTIONS = {
    "320x320 (for very lowres portrait photos that are less than 320x320 in resolution)": (320, 320),
    "640x640 (default)": (640, 640),
    "800x800": (800, 800),
    "1024x1024": (1024, 1024),
    "1280x1280 (Input/Reference image size should be larger than 1280x1280)": (1280, 1280)
}

# Initialize face analysis with default size
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

# Path to InstantID models
face_adapter = f"./checkpoints/ip-adapter.bin"
controlnet_path = f"./checkpoints/ControlNetModel"

# Load pipeline face ControlNetModel
controlnet_identitynet = ControlNetModel.from_pretrained(
    controlnet_path, torch_dtype=dtype
)

# controlnet-pose
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

def restart_server():
    """Restart the current python process"""
    python = sys.executable
    script = os.path.abspath(sys.argv[0])
    args = sys.argv[1:]
    os.environ["IN_BROWSER"] = "0"
    
    # Clear GPU memory
    torch.cuda.empty_cache()
    
    # Kill the current process
    os.execl(python, python, script, *args)

def update_det_size(det_size_name):
    """Update the face detection size"""
    global app, current_det_size
    
    new_size = DET_SIZE_OPTIONS[det_size_name]
    if new_size != current_det_size:
        current_det_size = new_size
        # Reinitialize face analysis with new size
        app = FaceAnalysis(
            name="antelopev2",
            root="./",
            providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
        )
        app.prepare(ctx_id=0, det_size=current_det_size)
    
    return f"Detection size set to {current_det_size}"

def main(pretrained_model_name_or_path="stablediffusionapi/protovision-xl-high-fidel", enable_lora_arg=False):
    if pretrained_model_name_or_path.endswith(
        ".ckpt"
    ) or pretrained_model_name_or_path.endswith(".safetensors"):
        scheduler_kwargs = hf_hub_download(
            repo_id="stablediffusionapi/protovision-xl-high-fidel",
            subfolder="scheduler",
            filename="scheduler_config.json",
        )

        (tokenizers, text_encoders, unet, _, vae) = load_models_xl(
            pretrained_model_name_or_path=pretrained_model_name_or_path,
            scheduler_name=None,
            weight_dtype=dtype,
        )

        scheduler = diffusers.EulerDiscreteScheduler.from_config(scheduler_kwargs)
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

        pipe.scheduler = diffusers.EulerDiscreteScheduler.from_config(
            pipe.scheduler.config
        )

    file_prefix = DEFAULT_FILE_PREFIX

    def toggle_lora_ui(enable_lora):
        return [
            gr.update(visible=enable_lora),
            gr.update(visible=enable_lora),
            gr.update(visible=enable_lora)
        ]

    def randomize_seed_fn(seed: int, randomize_seed: bool) -> int:
        if randomize_seed:
            seed = random.randint(0, MAX_SEED)
        return seed

    def remove_tips():
        return gr.update(visible=False)

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
        max_side=4084,
        min_side=754,
        size=None,
        pad_to_max_side=False,
        mode=PIL.Image.BILINEAR,
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
        return p.replace("{prompt}", positive), n + " " + negative

    def load_model_and_update_pipe(model_name):
        nonlocal pipe
        
        if model_name.endswith(".ckpt") or model_name.endswith(".safetensors"):
            scheduler_kwargs = hf_hub_download(
                repo_id="stablediffusionapi/protovision-xl-high-fidel",
                subfolder="scheduler",
                filename="scheduler_config.json",
            )

            (tokenizers, text_encoders, unet, _, vae) = load_models_xl(
                pretrained_model_name_or_path=model_name,
                scheduler_name=None,
                weight_dtype=dtype,
            )

            scheduler = diffusers.EulerDiscreteScheduler.from_config(scheduler_kwargs)
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
                model_name,
                controlnet=[controlnet_identitynet],
                torch_dtype=dtype,
                feature_extractor=None,
            ).to(device)

            pipe.scheduler = diffusers.EulerDiscreteScheduler.from_config(
                pipe.scheduler.config
            )

        pipe.load_ip_adapter_instantid(face_adapter)

        return pipe

    def generate_image(
        resize_max_side,
        face_image_path,
        pose_image_path,
        prompt,
        negative_prompt,
        style_name,
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
        lora_scale,
        lora_selection,
        enhance_face_region,
        enhance_strength,
        custom_enhance_padding,
        num_outputs,
        model_name,
        det_size_name,
        file_prefix,
        enable_vae_tiling,
        progress=gr.Progress(track_tqdm=True),
    ):
        file_prefix = f"InstantID_{file_prefix}" if file_prefix.strip() else "InstantID_"
        nonlocal pipe
        import time
        overall_start_time = time.time()
        
        # Update detection size if changed
        update_det_size(det_size_name)
        
        # Load selected model if it's different from current
        if model_name != getattr(pipe, "_current_model", None):
            pipe = load_model_and_update_pipe(model_name)
            pipe._current_model = model_name

        if enable_vae_tiling:
            pipe.enable_vae_tiling()
        else:
            pipe.disable_vae_tiling()

        if enable_lora and lora_selection:
            lora_path = os.path.join("./models/Loras", lora_selection)
            if os.path.exists(lora_path):
                pipe.load_lora_weights("./models/Loras", weight_name=lora_selection)
                pipe.fuse_lora(lora_scale=lora_scale)
                print(f"LoRA {lora_selection} loaded with scale {lora_scale}")
            else:
                print(f"LoRA not found at {lora_path}, skipping load.")
                gr.Warning(f"LoRA not found at {lora_path}. Skipping LoRA.")
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
    
            if "DPMSolver" in scheduler.split("-")[0]:
                scheduler_class = getattr(diffusers, scheduler.split("-")[0])
                pipe.scheduler = scheduler_class.from_config(
                    scheduler_config,
                    use_karras_sigmas=use_karras,
                    algorithm_type="sde-dpmsolver++" if use_sde else "dpmsolver++"
                )
            else:
                scheduler_class = getattr(diffusers, scheduler.split("-")[0])
                if scheduler.split("-")[0] in ["KDPM2AncestralDiscreteScheduler", "KDPM2DiscreteScheduler"] and use_karras:
                    pipe.scheduler = scheduler_class.from_config(
                        scheduler_config,
                        use_karras_sigmas=use_karras
                    )
                else:
                    pipe.scheduler = scheduler_class.from_config(scheduler_config)

        if face_image_path is None:
            if enable_lora and lora_selection:
                pipe.unfuse_lora()
                pipe.unload_lora_weights()
            raise gr.Error(
                f"Cannot find any input face image! Please upload the face image"
            )

        if not prompt:
            prompt = "high quality"

        # apply the style template
        prompt, negative_prompt = apply_style(style_name, prompt, negative_prompt)

        face_image = load_image(face_image_path)
        face_image = resize_img(face_image, max_side=resize_max_side)
        face_image_cv2 = convert_from_image_to_cv2(face_image)
        height, width, _ = face_image_cv2.shape

        # Extract face features
        face_info = app.get(face_image_cv2)

        if len(face_info) == 0:
            if enable_lora and lora_selection:
                pipe.unfuse_lora()
                pipe.unload_lora_weights()
            raise gr.Error(
                f"Unable to detect a face in the image. Please upload a different photo with a clear face."
            )

        face_info = sorted(face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*(x['bbox'][3]-x['bbox'][1]))[-1]  # only use the maximum face
        face_emb = face_info["embedding"]
        face_kps = draw_kps(convert_from_cv2_to_image(face_image_cv2), face_info["kps"])
        img_controlnet = face_image
        if pose_image_path is not None:
            pose_image = load_image(pose_image_path)
            pose_image = resize_img(pose_image, max_side=resize_max_side)
            img_controlnet = pose_image
            pose_image_cv2 = convert_from_image_to_cv2(pose_image)

            face_info = app.get(pose_image_cv2)

            if len(face_info) == 0:
                if enable_lora and lora_selection:
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

            # Determine padding ratio
            if enhance_strength == "Balanced":
                padding_ratio = 0.2
            elif enhance_strength == "High":
                padding_ratio = 0.4
            elif enhance_strength == "Custom":
                padding_ratio = custom_enhance_padding
            else:
                padding_ratio = 0.0  # Default

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
            controlnet_scales = {
                "pose": pose_strength,
                "canny": canny_strength,
                "depth": depth_strength,
            }
            controlnet_models = []
            controlnet_images = []
            for s in controlnet_selection:
                model = ControlNetModel.from_pretrained(controlnet_model_paths[s], torch_dtype=dtype).to(device)
                controlnet_models.append(model)
                controlnet_images.append(controlnet_map_fn[s](img_controlnet).resize((width, height)))
            pipe.controlnet = MultiControlNetModel([controlnet_identitynet] + controlnet_models)
            control_scales = [float(identitynet_strength_ratio)] + [controlnet_scales[s] for s in controlnet_selection]
            control_images = [face_kps] + controlnet_images
        else:
            pipe.controlnet = controlnet_identitynet
            control_scales = float(identitynet_strength_ratio)
            control_images = face_kps

        generator = torch.Generator(device=device).manual_seed(seed)

        print("Start inference...")
        print(f"Prompt: {prompt}\nNegative Prompt: {negative_prompt}")
        print(f"Detection size: {current_det_size}")

        pipe.set_ip_adapter_scale(adapter_strength_ratio)
        images = []
        generation_infos = []
        for i in range(num_outputs):
            print(f"Generating image {i + 1} of {num_outputs}...")
            print(f"Input face image: {os.path.basename(face_image_path) if face_image_path else 'None'}")
            print(f"Reference pose image: {os.path.basename(pose_image_path) if pose_image_path else 'None'}")
            print(f"Steps: {num_steps}")
            print(f"Enhance non-face region: {'True' if enhance_face_region else 'False'} ({enhance_strength}{f' | Padding: {custom_enhance_padding:.2f}' if enhance_strength == 'Custom' else ''})")
            print(f"Guidance scale: {guidance_scale}")
            print(f"Seed: {seed + i}")
            print(f"Model: {model_name}")
            print(f"ControlNet selection: {controlnet_selection} | Strengths - Pose: {pose_strength}, Canny: {canny_strength}, Depth: {depth_strength}")
            print(f"IdentityNet strength: {identitynet_strength_ratio}")
            print(f"Adapter strength: {adapter_strength_ratio}")
            print(f"LoRA scale: {'Disabled' if not (enable_lora and lora_selection and os.path.exists(os.path.join('./models/Loras', lora_selection))) else lora_scale}")
            print(f"LoRA selection: {'None' if not (enable_lora and lora_selection and os.path.exists(os.path.join('./models/Loras', lora_selection))) else lora_selection}")
            print(f"Scheduler: {scheduler}")
            print(f"Max resize side: {resize_max_side}")
            print(f"Image size: {width}x{height}\n")

            generator = torch.Generator(device=device).manual_seed(seed + i)
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
                callback=lambda step, timestep, latents: print(f"Step {step + 1} of {num_steps}"),
                callback_steps=1,
            )
            image = result.images[0]
            images.append(image)

            # Create generation info
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
IdentityNet strength: {identitynet_strength_ratio}
Adapter strength: {adapter_strength_ratio}
Pose strength: {pose_strength}
Canny strength: {canny_strength}
Depth strength: {depth_strength}
LoRA scale: {'Disabled' if not (enable_lora and lora_selection and os.path.exists(os.path.join("./models/Loras", lora_selection))) else lora_scale}
LoRA selection: {'None' if not (enable_lora and lora_selection and os.path.exists(os.path.join("./models/Loras", lora_selection))) else lora_selection}
Scheduler: {scheduler}"""

            png_info = PIL.PngImagePlugin.PngInfo()
            png_info.add_text("Generation Parameters", info_text)
            generation_infos.append(png_info)
            save_images([image], generation_info=[png_info], prefix=file_prefix)
            print(f"(√) Finished generating image {i + 1} of {num_outputs}\n")

            torch.cuda.empty_cache()

        if enable_lora and lora_selection:
            pipe.unfuse_lora()
            pipe.unload_lora_weights()

        import gc; gc.collect()
        overall_elapsed_time = time.time() - overall_start_time
        print(f"Total generation time: {overall_elapsed_time:.2f} seconds\n")
        return images, gr.update(visible=True)

    # Description
    title = r"""
    <h1 align="center">InstantID: Unlocked. Zero-shot Identity-Preserving Generation</h1>
    """

    description = r"""
    """

    article = r"""
    ---
    📝 **Tips**
    ```bibtex
    1. Upload an image with a face. For images with multiple faces, we will only detect the largest face. Ensure the face is not too small and is clearly visible without significant obstructions or blurring.
    2. (Optional) You can upload another image as a reference for the face pose. If you don't, the first detected face image will be used to extract facial landmarks. If you use a cropped face at step 1, it is recommended to upload it to define a new face pose.
    3. (Optional) You can select multiple ControlNet models to control the generation process. The default is to use the IdentityNet only. The ControlNet models include pose skeleton, canny, and depth. You can adjust the strength of each ControlNet model to control the generation process.
    4. Enter a text prompt, as done in normal text-to-image models.
    5. Click the Generate button to begin customization.
    6. In some cases, minimizing the browser/Gradio window while an image is being generated can help speed up the generation process significantly. You can track the progress in the CMD/Terminal window.
    ```
    <b>Github fork page</b> for <a href='https://github.com/eniora/InstantID-Unlocked' target='_blank'><b>InstantID: Unlocked</b></a>.<br>
    """

    tips = r"""
    ### Usage tips of InstantID
    1. If you're not satisfied with the similarity, try increasing the weight of "IdentityNet Strength" and "Adapter Strength."    
    2. If you feel that the saturation is too high, first decrease the Adapter strength. If it remains too high, then decrease the IdentityNet strength.
    3. If you find that text control is not as expected, decrease Adapter strength.
    4. If you find that the style or generated images are not good enough, try another base model.
    5. If you're having trouble detecting faces, try changing the "Face Detection Size" setting or try another input face photo.
    """

    css = """
    .gradio-container {width: 85% !important}
    """
    with gr.Blocks(css=css) as demo:
        # description
        gr.Markdown(title)
        gr.Markdown(description)

        with gr.Row():
            with gr.Column():
                with gr.Row(equal_height=True):
                    # upload face image
                    face_file = gr.Image(
                        label="Upload a photo containing a face", type="filepath"
                    )
                    # optional: upload a reference pose image
                    pose_file = gr.Image(
                        label="Upload a reference pose image (Optional)",
                        type="filepath"
                    )

                # prompt
                prompt = gr.Textbox(
                    label="Prompt",
                    info="Giving a simple prompt is enough to achieve good face fidelity",
                    placeholder="A man/woman/girl/boy in/with/as etc.",
                    value="",
                )
                negative_prompt = gr.Textbox(
                    label="Negative Prompt",
                    placeholder="When a Style template is selected, this becomes empty because styles have their own neg prompts. You can still add to it",
                    value=NEGATIVE_PROMPT_PRESETS["Default Negative Profile"]
                )
                with gr.Accordion("Style template and other settings", open=False):
                    style = gr.Dropdown(
                        label="Style template",
                        choices=STYLE_NAMES,
                        value=DEFAULT_STYLE_NAME,
                    )
                    negative_prompt_preset = gr.Dropdown(
                        label="Negative Prompt Profile",
                        choices=list(NEGATIVE_PROMPT_PRESETS.keys()),
                        value="Default Negative Profile",
                        info="Select a Negative Prompt Profile, default one is fine but you may want to select a different one depending on your prompt style"
                    )
                    file_prefix = gr.Textbox(
                        label="Saved file name prefix. Leave empty to use the default 'InstantID_'",
                        value="",
                        placeholder="Optional, append a name to be added after 'InstantID_' in the saved images",
                    )
                    enable_vae_tiling = gr.Checkbox(
                        label="Enable VAE Tiling (saves VRAM for large images at the last generation step)",
                        value=False,
                        info="Processes images in tiles to reduce VRAM usage during the final VAE decoding step without any quality loss."
                    )
                resize_max_side_slider = gr.Slider(
                    label="Max image size for resizing",
                    minimum=754,
                    maximum=4084,
                    step=90,
                    value=1280,
                    info="Controls the max_side for face/pose image resizing. Default is 1280 which is good. Up to 1924 can sometimes yield good results. Above 2000 is mostly only for super ultra wide/vertical input/reference pose photos where the resolution will be high only on one side, and it works well.",
                )
                num_outputs = gr.Slider(
                    label="Number of images to generate",
                    minimum=1, maximum=50, step=1, value=1,
                )
                generate = gr.Button("Generate", variant="primary")
                open_folder_btn = gr.Button("Open Output Folder")
                open_folder_btn.click(
                    fn=open_output_folder,
                    inputs=[],
                    outputs=[],
                    queue=False,
                )
                # strength
                identitynet_strength_ratio = gr.Slider(
                    label="IdentityNet strength (for fidelity)",
                    minimum=0,
                    maximum=1.5,
                    step=0.05,
                    value=0.7,
                )
                adapter_strength_ratio = gr.Slider(
                    label="Image adapter strength (for detail)",
                    minimum=0,
                    maximum=1.5,
                    step=0.05,
                    value=0.65,
                )
                with gr.Accordion("Controlnet", open=False) as controlnet_accordion:
                    controlnet_selection = gr.CheckboxGroup(
                        ["pose", "canny", "depth"], label="Controlnet", value=[],
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
                with gr.Accordion(open=True, label="Advanced Options"):
                    style.change(fn=on_style_change, inputs=style, outputs=negative_prompt)
                    num_steps = gr.Slider(
                        label="Number of sample steps",
                        minimum=1,
                        maximum=100,
                        step=1,
                        value=25,
                    )
                    guidance_scale = gr.Slider(
                        label="Guidance scale",
                        minimum=0.1,
                        maximum=20.0,
                        step=0.1,
                        value=4,
                    )
                    seed = gr.Slider(
                        label="Seed",
                        minimum=0,
                        maximum=MAX_SEED,
                        step=1,
                        value=42,
                    )
                    schedulers = [
                        "DPMSolverMultistepScheduler",
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
                    scheduler = gr.Dropdown(
                        label="Schedulers",
                        choices=schedulers,
                        value="DPMSolverMultistepScheduler",
                        info="DPMSolver, KDPM2 and Euler are usually the best."
                    )
                    randomize_seed = gr.Checkbox(label="Randomize seed", value=True)
                    with gr.Row():
                        enhance_face_region = gr.Checkbox(label="Enhance non-face region", value=True)
                        enhance_strength = gr.Dropdown(
                            label="Enhance Non-Face Region Amount",
                            choices=["Default", "Balanced", "High", "Custom"],
                            value="Balanced",
                            info="Controls how much area around the face is enhanced. More = bigger mask. Default is best if you for example want to change the hair style from the input image."
                        )
                        custom_enhance_padding = gr.Slider(
                            label="Custom enhancement padding (%)",
                            minimum=0.0,
                            maximum=0.9,
                            step=0.05,
                            value=0.2,
                            visible=False,
                            interactive=True
                        )
                    model_name = gr.Dropdown(
                        label="Model",
                        choices=AVAILABLE_MODELS,
                        value=DEFAULT_MODEL,
                        info="Select the model to use for generation. For some models, setting the guidance scale to '3.5' is generally better."
                    )
                    def toggle_custom_padding_dropdown(value):
                        return gr.update(visible=(value == "Custom"))

                    enhance_strength.change(
                        fn=toggle_custom_padding_dropdown,
                        inputs=enhance_strength,
                        outputs=custom_enhance_padding
                    )
                    det_size_name = gr.Dropdown(
                        label="Face Detection Size",
                        choices=list(DET_SIZE_OPTIONS.keys()),
                        value="640x640 (default)",
                        info="Higher values can detect smaller faces if the face in the input/reference image is too small/distant or if you get a 'No face detected' message. Otherwise you don't need to change this value for most of the cases as the differences are barely noticeable."
                    )
                    enable_lora = gr.Checkbox(
                        label="Enable a LoRA from your Loras folder",
                        value=enable_lora_arg,
                    )
                    lora_info = gr.Markdown(
                        "Only one lora can be loaded. Sometimes it's good to decrease IdentityNet/Adapter strengths when using a LoRA.",
                        visible=enable_lora_arg
                    )
                    enable_lora.change(
                        fn=lambda x: gr.Markdown(visible=x),
                        inputs=enable_lora,
                        outputs=lora_info
                    )
                    with gr.Row(visible=False) as lora_row:
                        lora_selection = gr.Dropdown(
                            label="Select LoRA",
                            choices=get_available_loras(),
                            value=None,
                            allow_custom_value=True,
                            info="Select a LoRA from your /models/Loras folder. Only SDXL, pony and Illustrious Loras supported"
                        )
                        lora_scale = gr.Slider(
                            label="LoRA Scale",
                            minimum=0.0,
                            maximum=2.0,
                            step=0.05,
                            value=1.0,
                            info="Strength of the LoRA effect. Not recommended to go above ~1.3"
                        )
                        refresh_loras = gr.Button("🔄", elem_classes="toolbutton")
                    
                    def refresh_lora_list():
                        loras = get_available_loras()
                        return gr.update(choices=loras, value=None)
                    
                    refresh_loras.click(
                        fn=refresh_lora_list,
                        outputs=lora_selection
                    )

            with gr.Column(scale=1):
                gallery = gr.Gallery(label="Generated Images")
                usage_tips = gr.Markdown(
                    label="InstantID Usage Tips", value=tips, visible=False
                )

            # Update negative prompt when preset is changed
            negative_prompt_preset.change(
                fn=lambda x: NEGATIVE_PROMPT_PRESETS[x],
                inputs=negative_prompt_preset,
                outputs=negative_prompt,
            )

            generate.click(
                fn=remove_tips,
                outputs=usage_tips,
            ).then(
                fn=randomize_seed_fn,
                inputs=[seed, randomize_seed],
                outputs=seed,
                queue=False,
                api_name=False,
            ).then(
                fn=generate_image,
                inputs=[
                    resize_max_side_slider,
                    face_file,
                    pose_file,
                    prompt,
                    negative_prompt,
                    style,
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
                    lora_scale,
                    lora_selection,
                    enhance_face_region,
                    enhance_strength,
                    custom_enhance_padding,
                    num_outputs,
                    model_name,
                    det_size_name,
                    file_prefix,
                    enable_vae_tiling,
                ],
                outputs=[gallery, usage_tips],
            )

            enable_lora.input(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=[lora_row, lora_selection, lora_scale],
                queue=False,
            )

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
                    lines=10,
                    max_lines=20
                )

            with gr.Row():
                apply_metadata_btn = gr.Button("Apply to all fields", variant="secondary")
            
            metadata_input.upload(
                fn=lambda x: (x, read_png_metadata(x) if x is not None else ""),
                inputs=metadata_input,
                outputs=[metadata_input, metadata_output]
            )
            def extract_all_settings(metadata_text):
                accordion_update = gr.update(open=False)
                settings = {
                    "prompt": "",
                    "negative_prompt": "",
                    "resize_max_side": 1280,
                    "seed": 42,
                    "num_steps": 25,
                    "guidance_scale": 4.0,
                    "identitynet_strength_ratio": 0.7,
                    "adapter_strength_ratio": 0.65,
                    "pose_strength": 0.40,
                    "canny_strength": 0.40,
                    "depth_strength": 0.40,
                    "scheduler": "DPMSolverMultistepScheduler",
                    "enable_lora": False,
                    "lora_scale": 1.0,
                    "enhance_face_region": True,
                    "enhance_strength": "Balanced",
                    "custom_enhance_padding": 0.20,
                    "style": DEFAULT_STYLE_NAME,
                    "lora_selection": "",
                    "randomize_seed": True,
                    "controlnet_selection": [],
                    "model_name": DEFAULT_MODEL,
                    "det_size_name": "640x640 (default)"
                }
                if metadata_text:
                    for line in metadata_text.split('\n'):
                        line = line.strip()
                        if line.startswith("Prompt:"):
                            settings["prompt"] = line.replace("Prompt:", "").strip()
                        elif line.startswith("Negative Prompt:"):
                            settings["negative_prompt"] = line.replace("Negative Prompt:", "").strip()
                        elif line.startswith("Seed:"):
                            settings["seed"] = int(line.replace("Seed:", "").strip())
                        elif line.startswith("Steps:"):
                            settings["num_steps"] = int(line.replace("Steps:", "").strip())
                        elif line.startswith("Guidance scale:"):
                            settings["guidance_scale"] = float(line.replace("Guidance scale:", "").strip())
                        elif line.startswith("LoRA selection:"):
                            lora_selection = line.replace("LoRA selection:", "").strip()
                            settings["lora_selection"] = lora_selection if lora_selection != "None" else None
                            settings["enable_lora"] = lora_selection != "None"
                        elif line.startswith("LoRA scale:"):
                            lora_scale_str = line.replace("LoRA scale:", "").strip()
                            if lora_scale_str != "Disabled":
                                settings["lora_scale"] = float(lora_scale_str)
                            settings["enable_lora"] = lora_scale_str != "Disabled"
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
                            if "scheduling_" in scheduler_text:  # If it's a full class path
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
                        elif line.startswith("Style:"):
                            style_name = line.replace("Style:", "").strip()
                            settings["style"] = style_name if style_name in STYLE_NAMES else DEFAULT_STYLE_NAME
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

                return [
                    settings["prompt"],
                    settings["negative_prompt"],
                    settings["style"],
                    settings["num_steps"],
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
                    settings["lora_selection"] if settings["enable_lora"] else None,
                    settings["randomize_seed"],
                    settings["controlnet_selection"],
                    settings["model_name"],
                    settings["det_size_name"],
                    settings["resize_max_side"],
                    accordion_update
                ]

            apply_metadata_btn.click(
                fn=extract_all_settings,
                inputs=metadata_output,
                outputs=[
                    prompt,
                    negative_prompt,
                    style,
                    num_steps,
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
                    randomize_seed,
                    controlnet_selection,
                    model_name,
                    det_size_name,
                    resize_max_side_slider,
                    controlnet_accordion
                ]
            ).then(
                fn=toggle_lora_ui,
                inputs=[enable_lora],
                outputs=[lora_row, lora_selection, lora_scale]
            )

        gr.Markdown(article)

        with gr.Row():
            restart_btn = gr.Button("Restart Server", variant="stop", scale=1)
            restart_btn.click(
                fn=restart_server,
                inputs=None,
                outputs=None,
                queue=False,
            )

    demo.launch(inbrowser=os.environ.get("IN_BROWSER", "1") == "1")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pretrained_model_name_or_path", type=str, default="stablediffusionapi/protovision-xl-high-fidel"
    )
    parser.add_argument(
        "--enable_lora", type=bool, default=os.environ.get("ENABLE_lora", False)
    )
    args = parser.parse_args()

    main(args.pretrained_model_name_or_path, args.enable_lora)