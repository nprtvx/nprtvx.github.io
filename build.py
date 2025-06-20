import os
import shutil
from src.write_pages import home_page, about_page, contact_page

TEMPLATES_DIR = 'templates'
ASSETS_DIR = 'assets'
OUTPUT_DIR = 'static'

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy_templates():
    ensure_dir(OUTPUT_DIR)
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.endswith('.html'):
            src = os.path.join(TEMPLATES_DIR, filename)
            dst = os.path.join(OUTPUT_DIR, filename)
            shutil.copyfile(src, dst)
            print(f"Copied {src} to {dst}")

def copy_assets():
    if not os.path.exists(ASSETS_DIR):
        return
    dst_assets = os.path.join(OUTPUT_DIR, 'assets')
    shutil.copytree(ASSETS_DIR, dst_assets, dirs_exist_ok=True)
    print(f"Copied {ASSETS_DIR} to {dst_assets}")

if __name__ == "__main__":
    pages = [home_page, about_page, contact_page]
    for page in pages:
        page.write()
    copy_templates()
    copy_assets()
    print("Static site generated in", OUTPUT_DIR)
