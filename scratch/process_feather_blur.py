import os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'

os.makedirs(web_dir, exist_ok=True)

# List of files fresh from desktop
files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
files.sort()

def create_feather_mask(size, feather_pixels=20):
    w, h = size
    # Create black mask
    mask = Image.new('L', (w, h), 255)
    draw = ImageDraw.Draw(mask)
    
    # Draw soft edges
    for i in range(feather_pixels):
        alpha = int(255 * (i / feather_pixels))
        # Top edge
        draw.line([(0, i), (w, i)], fill=alpha)
        # Bottom edge
        draw.line([(0, h - 1 - i), (w, h - 1 - i)], fill=alpha)
        # Left edge
        draw.line([(i, 0), (i, h)], fill=alpha)
        # Right edge
        draw.line([(w - 1 - i, 0), (w - 1 - i, h)], fill=alpha)
        
    return mask

def process_with_feather_blur(src_path, dest_path, target_w, target_h, scale_factor=0.55):
    with Image.open(src_path) as img:
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        w, h = img.size
        
        # 1. Create blurred background
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
        if img_ar > target_ar:
            new_h = int(target_h * scale_factor)
            new_w = int(new_h / img_ar)
        else:
            new_w = int(target_w * scale_factor)
            new_h = int(new_w * img_ar)
            
        fg_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # 3. Create feather mask for foreground
        mask = create_feather_mask(fg_resized.size, feather_pixels=15)
        
        # 4. Paste foreground centered onto blurred background using the feather mask
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        
        # Paste using RGBA transparency and feather mask
        bg_blurred.paste(fg_resized, (paste_x, paste_y), mask=mask)
        
        # Convert back to RGB to save as normal PNG
        final_img = bg_blurred.convert('RGB')
        final_img.save(dest_path, 'PNG')
        print(f"Created feather-blurred-padded image: {dest_path}")

# Process the three images:
p1 = os.path.join(web_dir, 'lab-grown-small-1.png')
p2 = os.path.join(web_dir, 'lab-grown-small-2.png')
p3 = os.path.join(web_dir, 'lab-grown-small-3.png')

process_with_feather_blur(os.path.join(src_dir, files[0]), p1, 768, 768, scale_factor=0.55)
process_with_feather_blur(os.path.join(src_dir, files[1]), p2, 768, 1180, scale_factor=0.52)
process_with_feather_blur(os.path.join(src_dir, files[2]), p3, 768, 768, scale_factor=0.55)
