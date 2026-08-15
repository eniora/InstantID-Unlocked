<h1>InstantID: Unlocked. Zero-shot Identity-Preserving Generation</h1>

I think it's worth mentioning that I am not too good with python and the code is full of workarounds/hacks + I used a lot of help from AI chatbots, but at least it works really well and everything is working as I intended with no issues at all. :D

I originally started modifying InstantID for my own usage and to improve my experience and learn a bit more about python, then decided to release it as a fork. Many thanks to the InstantX team for this awesome project!
The code barely follows any DRY principles as it started as a personal modification project to imporve my experience and I slowly fixed/patched stuff over time. So now doing "DRY" on it would require a lot of time and possibly break things.

## This fork adds the following:

🖼️ Output & Metadata
- Autosave of every generated image into an output folder.
- “Open Output Folder” button in the Gradio GUI.
- PNG metadata writing for all autosaved images.
- Metadata reader box in the GUI (load metadata from a PNG and apply it back to all fields).

🎨 Models, LoRAs, Embeddings & Styles
- Model selector dropdown (choose your base SDXL model easily).
- Multiple LoRA loader. Load and combine up to 8 LoRAs with different weights.
- Embeddings loader with a dropdown menu to insert to prompt or negative prompt.
- New default model: eniora/Juggernaut_XL_Ragnarok (better than YamerMIX). Other good tested models: John6666/albedobase-xl-v31large-sdxl/, eniora/RealVisXL_V5.0, ProtoVision XL 6.6, misri/juggernautXL_juggXIByRundiffusion, John6666/cyberrealistic-xl-v58-sdxl.
- Added over 1100 styles, including many from Fooocus and StyleSelectorXL.
- New CN pose model by xinsir, found it a bit better than the original with better colors.
- In addition to the default diffusers format support for loading checkpoints, I added the ability to load single SDXL, Pony and Illustrious .safetensors files. They will automatically appear in the model dropdown selection menu when placed in the /models folder.

🧠 Control & Generation
- img2img mode integrated directly (no need to run a separate pipeline).
- Negative Prompt Profiles dropdown with many presets (General, Minimalist, Portraits, Realism, Anime, Fooocus, etc.).
- Detection Size selector for face detection in input/reference photos.
- Hires Fix support with upscaler drop down menu.
- Multiple schedulers available (beyond the original EulerDiscrete).
- VAE tiling option to improve VRAM efficiency.
- Resolution slider up to 4096px.
- Weight application method: added UI options to mimic how ForgeUI/A1111 or ComfyUI deal with (word:weight).
- Generate multiple images in one run, each with a random seed.
- Stop button.

👤 Face Enhancement
- Enhance Non-Face Region with adjustable padding with profiles: Default, Balanced, High, or Custom padding amount.

⚡ Performance
- Tweaks to improve VRAM usage compared to the original repo. Runs good on 12GB VRAM but 16GB+ is recommended.
- Works on 8GB GPUs, but expect slow generations (~5-10 minutes for 1280×960).

And many many more improvements such as a Standalone Image Upscaler with GFPGAN option.

I tried the most popular forgeui and comfyui implementations including the popular cubiq/ComfyUI_InstantID and it's really bad compared to my gradio fork of InstantID. cubiq/ComfyUI_InstantID (which was the best from the comfy implementations I tried) tends to screw up the faces and similarity sometimes no matter what options and workflows I tried, and the multi ID feature doesn't work well anyway and is overly complicated (even the author admits this). Try this and judge for yourself. I agree that comfyui instantid is faster but the quality isn't so good really. The good thing about cubiq/ComfyUI_InstantID is the stylization with "IP-Adapter plus VIT", I've been trying to make it work with this fork but I always failed, guess I am not skilled enough for this. :>

## How to use and run:

git clone https://github.com/eniora/InstantID-Unlocked

cd InstantID-Unlocked

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

pip install torch==2.13.0+cu132 torchvision==0.28.0+cu132 --index-url https://download.pytorch.org/whl/cu132

python instant-id-unlocked.py

_______________________________________________
Python and PIP packages are a pain in the ***, and a lot of stuff can go wrong with dependencies, installations, etc. So, if you want my whole InstantID-Unlocked folder with the venv and all the models, loras, embeddings, upscalers and everything you need to get it running without any headaches, here it is in 3 parts: (~26GB)

- Part 1: https://drive.google.com/file/d/1MRIgwvHuopDxCZLiuXRFf6hDYzKwCeM8/view?usp=sharing
- Part 2: https://drive.google.com/file/d/1HAob1D6ynIwWjG4HyXi7paTWRtxqz647/view?usp=sharing
- Part 3: https://drive.google.com/file/d/1Nysf6mJ9BrWP8MIt9nsRcT5k1Km2fb98/view?usp=sharing

Just download the files and extract with the latest 7zip, instructions are inside. You basically need to enter the folder with CMD/terminal and create a new venv using python 3.10.6 with "python -m venv venv" and copy over the included site-packages folder, overwriting the newly created one inside.
If you do this and use this folder, you don't need to install the requirements.txt or torch/nvidia cuda or anything. You need python 3.10.6 installed (or point to a 3.10.6 python folder in the cfg after creating the venv) as the venv folder inside was created with 3.10.6. Then basically run the bat file "_Run InstandID.bat"
Note that the "instant-id-unlocked.py" file inside won't be up to date obviously (currently at v7.5.0 in the folder), you'd need to replace it (and other .py files if necessary) in case I update the repo with new files, so if you go this route and download my full folder, download the latest repo files here (choose the green "code" button and then "download zip") and replace existing ones in the folder (all .py files like the pipeline files, instant-id-unlocked.py, ip_adapter/attention_processor.py etc.). Model files won't need to be updated and you can use any SDXL/Pony checkpoint in .safetensors format and place directly inside the models folder. Illustrious can be loaded but not all of them work good with InstantID.

- Tested only on Windows 10/11 and Python 3.10.6 and Nvidia GPUs, you may need to do extra steps to run successfully on MacOS/Linux or if you have an AMD GPU.

Here's a quick preview of the fork: (This is one of hundreds ways to generate different images with this fork, for example you can add a LoRA or multiple loras with different weights, or try with and without img2img, or try different styles, or try different models, or try with embeddings, etc.)

<img src='Preview/InstantID-Gradio-Unlocked_Preview_New_Features.png'>


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
