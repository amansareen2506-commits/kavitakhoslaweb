import os
from PIL import Image

image_path = 'pendant-set.png'

if os.path.exists(image_path):
    with Image.open(image_path) as img:
        w, h = img.size
        print(f"Original dimensions: {w}x{h}")
        
        # Crop to center square
        min_dim = min(w, h)
        left = (w - min_dim) / 2
        top = (h - min_dim) / 2
        right = (w + min_dim) / 2
        bottom = (h + min_dim) / 2
        
        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((1160, 1160), Image.Resampling.LANCZOS)
        
        # Save back to pendant-set.png
        resized.save(image_path, 'PNG')
        print(f"Successfully cropped and resized pendant-set.png to perfect square 1160x1160.")
else:
    print("pendant-set.png not found!")
