#! bin/python
from pathlib import Path
import shutil
from popeye import HOME as POPEYE

TEMPLATES_DIR = Path('templates')
ASSETS_DIR = Path('assets')
OUTPUT_DIR = Path('static')

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def copy_templates():
    ensure_dir(OUTPUT_DIR)
    for template_path in TEMPLATES_DIR.rglob('*.html'):
        rel_path = template_path.relative_to(TEMPLATES_DIR)
        dest_path = OUTPUT_DIR / rel_path.parent
        ensure_dir(dest_path)
        shutil.copyfile(template_path, dest_path / template_path.name)
        print(f"Copied {template_path} to {dest_path / template_path.name}")

def copy_assets():
    if not ASSETS_DIR.exists():
        return
    dst_assets = OUTPUT_DIR / 'assets'
    shutil.copytree(ASSETS_DIR, dst_assets, dirs_exist_ok=True)
    print(f"Copied {ASSETS_DIR} to {dst_assets}")

if __name__ == "__main__":
    """create a list of pages"""
    pages = [POPEYE]
    """loop over each page and write them"""
    for page in pages:
        """page logo defaults to None. Change path argument to update/replace"""
        if not page.logo:
            page.logo = Path('assets/logo.png') if page.title == "Home" else Path('../assets/logo.png')
        #print("is this not printing - ", page.body)
        page.write()
    copy_templates()
    copy_assets()
    print(f"Static site generated in {OUTPUT_DIR}")

# EoF
