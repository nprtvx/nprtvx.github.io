import os
import shutil
from PIL import Image

from src.home import page as home
from src.about import page as about
from src.contact import page as contact
from src.popeye import page as popeye
from src.a404 import page as a404

TEMPLATES_DIR = 'templates'
ASSETS_DIR = 'assets'
OUTPUT_DIR = 'static'
LOGO = Image.open('assets/logo.png')

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy_templates():
    ensure_dir(OUTPUT_DIR)
    for root, dirs, files in os.walk(TEMPLATES_DIR):
        for filename in files:
            if filename.endswith('.html'):
                rel_dir = os.path.relpath(root, TEMPLATES_DIR)
                dest_dir = os.path.join(OUTPUT_DIR, rel_dir)
                ensure_dir(dest_dir)
                src = os.path.join(root, filename)
                dst = os.path.join(dest_dir, filename)
                shutil.copyfile(src, dst)
                print(f"Copied {src} to {dst}")

def copy_assets():
    if not os.path.exists(ASSETS_DIR):
        return
    dst_assets = os.path.join(OUTPUT_DIR, 'assets')
    shutil.copytree(ASSETS_DIR, dst_assets, dirs_exist_ok=True)
    print(f"Copied {ASSETS_DIR} to {dst_assets}")

if __name__ == "__main__":
    pages = [home, about, contact, popeye, a404]
    for page in pages:
	if not page.logo:
		page.logo = LOGO
        page.write()
    copy_templates()
    copy_assets()
    print("Static site generated in", OUTPUT_DIR)
