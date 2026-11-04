# Shrinks every photo in the images/ folder so the site loads faster.
# Keeps the same file names, so you don't have to change any HTML.
# Run from inside the my-website folder:  python compress_images.py
 
from pathlib import Path
from PIL import Image, ImageOps
 
MAX_SIZE = 1600   # longest side in pixels
QUALITY = 80      # JPG quality (80 looks the same, much smaller file)
 
for path in Path("images").iterdir():
    if path.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        continue
 
    before = path.stat().st_size
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)   # keeps phone photos the right way up
    img.thumbnail((MAX_SIZE, MAX_SIZE))
 
    if path.suffix.lower() == ".png":
        img.save(path, optimize=True)
    else:
        img.convert("RGB").save(path, quality=QUALITY, optimize=True, progressive=True)
 
    after = path.stat().st_size
    print(f"{path.name}: {before // 1024} KB -> {after // 1024} KB")