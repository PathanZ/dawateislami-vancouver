"""Make small, fast WebP copies of the downloaded pictures (assets/img/ext -> assets/img/opt).
Run after downloading pictures: python3 tools/optimize_images.py   (needs: pip install pillow)"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "assets/img/ext", ROOT / "assets/img/opt"
OUT.mkdir(parents=True, exist_ok=True)
SMALL = {"founder": 420}          # pictures shown small get a smaller copy
for f in sorted(SRC.iterdir()):
    if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
        continue
    dest = OUT / (f.name + ".webp")
    if dest.exists() and dest.stat().st_mtime >= f.stat().st_mtime:
        continue
    im = Image.open(f)
    im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
    width = next((w for k, w in SMALL.items() if k in f.name), 960)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(dest, "WEBP", quality=78, method=6)
    if im.width > 480:   # a smaller copy for phone-sized cards
        im.resize((480, round(im.height * 480 / im.width)), Image.LANCZOS).save(
            OUT / (f.name + ".480.webp"), "WEBP", quality=76, method=6)
    print(f"{f.name}: {f.stat().st_size // 1024} KB -> {dest.stat().st_size // 1024} KB")
