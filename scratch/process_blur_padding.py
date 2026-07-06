import os
from PIL import Image, ImageFilter

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'

os.makedirs(web_dir, exist_ok=True)

# List of files fresh from desktop
files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
files.sort()

print("Original files:", files)

def process_with_blur_padding(src_path, dest_path, target_w, target_h, scale_factor=0.55):
    with Image.open(src_path) as img:
        w, h = img.size
        
        # 1. Create blurred background
        # Resize original image to cover target size
        img_ar = h / w
        target_ar = target_h / target_w
        
        if img_ar > target_ar:
            bg_w = int(target_h / img_ar)
            bg_h = target_h
        else:
            bg_w = target_w
            bg_h = int(target_w * img_ar)
            
        bg_img = img.resize((bg_w, bg_h), Image.Resampling.LANCZOS)
        
        # Crop background to exact target dimensions
        left = (bg_w - target_w) // 2
        top = (bg_h - target_h) // 2
        bg_cropped = bg_img.crop((left, top, left + target_w, top + target_h))
        
        # Apply strong blur to background to make it a soft gradient matching the colors of the image
        bg_blurred = bg_cropped.filter(ImageFilter.GaussianBlur(radius=60))
        
        # 2. Scale down the foreground image
        # We want the ring to look small, so we scale it based on scale_factor
        if img_ar > target_ar:
            new_h = int(target_h * scale_factor)
            new_w = int(new_h / img_ar)
        else:
            new_w = int(target_w * scale_factor)
            new_h = int(new_w * img_ar)
            
        fg_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # 3. Paste foreground centered onto blurred background
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        
        # Optional: Add a very soft black outline/shadow or just paste directly
        bg_blurred.paste(fg_resized, (paste_x, paste_y))
        
        # Save as PNG
        bg_blurred.save(dest_path, 'PNG')
        print(f"Created blurred-padded image: {dest_path}")

# Process the three images:
# 1. Finger ring -> 768x768 square
# 2. Gold ring -> 768x1180 tall
# 3. Marquise ring -> 768x768 square
p1 = os.path.join(web_dir, 'lab-grown-small-1.png')
p2 = os.path.join(web_dir, 'lab-grown-small-2.png')
p3 = os.path.join(web_dir, 'lab-grown-small-3.png')

process_with_blur_padding(os.path.join(src_dir, files[0]), p1, 768, 768, scale_factor=0.55)
process_with_blur_padding(os.path.join(src_dir, files[1]), p2, 768, 1180, scale_factor=0.52)
process_with_blur_padding(os.path.join(src_dir, files[2]), p3, 768, 768, scale_factor=0.55)
