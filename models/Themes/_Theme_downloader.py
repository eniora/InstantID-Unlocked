import os
import re
import gradio as gr

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_SCRIPT_DIR) == "Themes" and os.path.basename(os.path.dirname(_SCRIPT_DIR)) == "models":
    _HUB_THEMES_CACHE_DIR = _SCRIPT_DIR
else:
    _HUB_THEMES_CACHE_DIR = os.path.join(_SCRIPT_DIR, "models", "Themes")

def _load_hub_theme_css(repo_id):
    os.makedirs(_HUB_THEMES_CACHE_DIR, exist_ok=True)
    cache_file = os.path.join(_HUB_THEMES_CACHE_DIR, re.sub(r"[^\w.-]", "_", repo_id) + ".css")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()
    css = gr.Theme.from_hub(repo_id)._get_theme_css()
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(css)
    return css

if __name__ == "__main__":
    # Add/remove repo ids here, then just run this script while online. InstantID will need a full reload after downloading new themes for the themes dropdown to update.
    repo_ids = [
        "gradio/seafoam", # example, which is from https://huggingface.co/spaces/gradio/seafoam/tree/main/themes. With this script it will automatically be converted to .css
    ]
    for repo_id in repo_ids:
        try:
            _load_hub_theme_css(repo_id)
            print(f"[theme] OK: {repo_id}")
        except Exception as e:
            print(f"[theme] Failed: {repo_id} ({e})")