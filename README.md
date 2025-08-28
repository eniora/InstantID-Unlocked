<h1>InstantID: Unlocked. Zero-shot Identity-Preserving Generation</h1>

I think it's worth mentioning that I am not too good with python and the code is full of workarounds/hacks + I used a lot of help from AI chatbots, but at least it works really well and everything is working as I intended with no issues at all. :D
I originally started modifying InstantID for my own usage and to improve my experience and learn a bit more about python, then decided to release it as a fork. Many thanks to the InstantX team for this awesome project!
The code barely follows any DRY principles as it started as a personal modification project to imporve my experience and I slowly fixed/patched stuff over time. So now doing "DRY" on it would require a lot of time and possibly break things.

## This fork adds the following:
- Autosave of each generated image in the "output" folder, with an "Open Output Folder" button in the gradio GUI.
- Resolution slider, up to 4096.
- Multiple Lora loader
- Model selector dropdown.
- img2img mode that natively imports the already existing stable_diffusion_xl_instantid_img2img pipeline, without needing to launch two separate apps.
- PNG metadata writer in the autosaved images and a gradio box to read info from them and apply the metadata fields to all boxes.
- Dropdown menu for the ability to change the Det Size for face detection in input/reference photos.
- Negative Prompt Profiles dropdown.
- New default RealVisXL_V5.0 model, which is much better than the default YamerMIX. You can still download the base model of your choice by changing the huggingface model path inside instant-id-gradio-unlocked.py file and replacing all "eniora/RealVisXL_V5.0" fields and it will be downloaded automatically in the "models" folder on root. /John6666/albedobase-xl-v31large-sdxl/, ProtoVision XL 6.6, misri/juggernautXL_juggXIByRundiffusion and John6666/cyberrealistic-xl-v58-sdxl are very good models for styles and general use as well.
- Ability to choose how many images to be generated after clicking on "generate", each with random seed.
- Improved VRAM usage compared to the original repo.
- Added many more styles in the style template. Including many from "fooocus" and "StyleSelectorXL" (sources: https://github.com/lllyasviel/Fooocus/discussions/2082 and https://github.com/ahgsql/StyleSelectorXL). For a total of over 1100 styles.
- Enhance Non-Face Region Custom Padding Amount.
- VAE tiling option.
- Multiple schedulers to choose from.
- And many many more improvements.

I tried the most popular forgeui and comfyui implementations including the popular cubiq/ComfyUI_InstantID and it's really bad compared to my gradio fork of InstantID. cubiq/ComfyUI_InstantID (which was the best from the comfy implementations I tried) tends to screw up the faces and similarity sometimes no matter what options and workflows I tried, and the multi ID feature doesn't work well anyway and is overly complicated (even the author admits this). Try this and judge for yourself. I agree that comfyui instantid is faster but the quality isn't so good really. The good thing about cubiq/ComfyUI_InstantID is the stylization with "IP-Adapter plus VIT", I've been trying to make it work with this fork but I always failed, I am just not skilled enough for this. :>

## How to use and run:
Git clone this fork (Git clone https://github.com/eniora/InstantID-Unlocked/) then:
- To avoid conflicts, it's recommended to create a python venv by doing in terminal/CMD window: "python -m venv venv" then activate the venv with "venv\Scripts\activate"
- With the venv activated, install the requirements.txt file with "pip install -r requirements.txt" and then install torch and cuda with "pip install torch==2.7.1+cu128 torchvision==0.22.1+cu128 --index-url https://download.pytorch.org/whl/cu128"
- For downloading the necessary models: face encoder models, controlnet models and IPAdatper etc. I uploaded all the necesseray files here:
https://drive.google.com/file/d/1RdoGwK-6054eCnNw0ipi-j3bbgD8gj9J/view?usp=sharing
This is my whole models and checkpoints folder except for the SDXL model(s).
Just download the file, extract it and copy the folders into your root InstantID folder. Then you will only need an SDXL model to start generating. It will be downloaded automatically from huggingface when you start InstantID.

- Run by using "python instant-id-gradio-unlocked.py".

- Tested only on Windows and Python 3.10.6 and Nvidia GPUs, you may need to do extra steps to run the gradio interface successfully on MacOS/Linux or if you have an AMD GPU.

- InstantID requires a lot of VRAM (even after my tweaks to make it faster and more VRAM efficient). Based on my testing with different GPUs, the minimum you need is 12GB, 16GB or more is strongly recommended. With 8GB it took ~15 minutes to generate a 1280x960 photo.

Preview of the fork:
<img src='Preview/InstantID-Gradio-Unlocked_Preview.png'>


_______________________________________________
InstantX Credits:

[**Qixun Wang**](https://github.com/wangqixun)<sup>12</sup> · [**Xu Bai**](https://huggingface.co/baymin0220)<sup>12</sup> · [**Haofan Wang**](https://haofanwang.github.io/)<sup>12*</sup> · [**Zekui Qin**](https://github.com/ZekuiQin)<sup>12</sup> · [**Anthony Chen**](https://antonioo-c.github.io/)<sup>123</sup>

Huaxia Li<sup>2</sup> · Xu Tang<sup>2</sup> · Yao Hu<sup>2</sup>

<sup>1</sup>InstantX Team · <sup>2</sup>Xiaohongshu Inc · <sup>3</sup>Peking University

<sup>*</sup>corresponding authors

<a href='https://instantid.github.io/'><img src='https://img.shields.io/badge/Project-Page-green'></a>
<a href='https://arxiv.org/abs/2401.07519'><img src='https://img.shields.io/badge/Technique-Report-red'></a>
<a href='https://huggingface.co/papers/2401.07519'><img src='https://img.shields.io/static/v1?label=Paper&message=Huggingface&color=orange'></a> 
[![GitHub](https://img.shields.io/github/stars/InstantID/InstantID?style=social)](https://github.com/InstantID/InstantID)

<a href='https://huggingface.co/spaces/InstantX/InstantID'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'></a>
[![ModelScope](https://img.shields.io/badge/ModelScope-Studios-blue)](https://modelscope.cn/studios/instantx/InstantID/summary)
[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)](https://openxlab.org.cn/apps/detail/InstantX/InstantID)

InstantID is a new state-of-the-art tuning-free method to achieve ID-Preserving generation with only single image, supporting various downstream tasks.





























