import os
import re
import json
import requests
import gradio as gr
from gradio.themes.utils import fonts
from huggingface_hub import list_repo_files

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(_SCRIPT_DIR) == "Themes" and os.path.basename(os.path.dirname(_SCRIPT_DIR)) == "models":
    _HUB_THEMES_CACHE_DIR = _SCRIPT_DIR
else:
    _HUB_THEMES_CACHE_DIR = os.path.join(_SCRIPT_DIR, "models", "Themes")
def _latest_schema_filename(repo_id):
    files = list_repo_files(repo_id, repo_type="space")
    schema_files = [f for f in files if f.startswith("themes/theme_schema@") and f.endswith(".json")]
    if not schema_files:
        raise FileNotFoundError(f"No theme_schema json found in {repo_id}")
    def version_key(f):
        v = f.split("@")[1].rsplit(".json", 1)[0]
        return tuple(int(p) for p in v.split("."))
    return sorted(schema_files, key=version_key)[-1]

def _load_hub_theme_css(repo_id):
    os.makedirs(_HUB_THEMES_CACHE_DIR, exist_ok=True)
    cache_file = os.path.join(_HUB_THEMES_CACHE_DIR, re.sub(r"[^\w.-]", "_", repo_id) + ".css")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    filename = _latest_schema_filename(repo_id)
    url = f"https://huggingface.co/spaces/{repo_id}/resolve/main/{filename}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = json.loads(resp.text, object_hook=fonts.as_font)
    theme = gr.themes.ThemeClass.from_dict(data)
    if theme.name is None:
        theme.name = re.sub(r"[^\w.-]", "_", repo_id)
    css = theme._get_theme_css()

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