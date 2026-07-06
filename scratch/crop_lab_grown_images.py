import os
from PIL import Image

web_dir = 'lab-grown-diamonds-images'

def crop_to_square(img_path, dest_path):
    with Image.open(img_path) as img:
        w, h = img.size
        min_dim = min(w, h)
        left = (w - min_dim) / 2
        top = (h - min_dim) / 2
        right = (w + min_dim) / 2
        bottom = (h + min_dim) / 2
        
        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((768, 768), Image.Resampling.LANCZOS)
        resized.save(dest_path, 'PNG')
        print(f"Cropped {img_path} to square 768x768 and saved to {dest_path}")

def crop_to_tall(img_path, dest_path):
    # Tall target is 768x1180 (aspect ratio 1180 / 768 = 1.53645)
    target_ar = 1180 / 768
    with Image.open(img_path) as img:
        w, h = img.size
        current_ar = h / w
        
        if current_ar > target_ar:
            # Too tall, crop top and bottom
            new_h = w * target_ar
            left = 0
            top = (h - new_h) / 2
            right = w
            bottom = (h + new_h) / 2
        else:
            # Too wide, crop left and right
            new_w = h / target_ar
            left = (w - new_w) / 2
            top = 0
            right = (w + new_w) / 2
            bottom = h
            
        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((768, 1180), Image.Resampling.LANCZOS)
        resized.save(dest_path, 'PNG')
        print(f"Cropped {img_path} to tall 768x1180 and saved to {dest_path}")

# Run the crops:
# lab-grown-1.png -> square 1:1 (768x768)
# lab-grown-2.png -> tall 1:1.536 (768x1180)
# lab-grown-3.png -> square 1:1 (768x768)

p1 = os.path.join(web_dir, 'lab-grown-1.png')
p2 = os.path.join(web_dir, 'lab-grown-2.png')
p3 = os.path.join(web_dir, 'lab-grown-3.png')

crop_to_square(p1, p1)
crop_to_tall(p2, p2)
crop_to_square(p3, p3)
