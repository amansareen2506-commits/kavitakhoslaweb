import os
from PIL import Image, ImageOps

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'

os.makedirs(web_dir, exist_ok=True)

# Copy and list files fresh from desktop
files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
files.sort()

print("Original files from desktop:", files)

# We have 3 files:
# 1. {3FEB6EB8...}.png -> lab-grown-1 (finger oval ring, target square 768x768)
# 2. {6C97A3B1...}.png -> lab-grown-2 (gold oval ring, target tall 768x1180)
# 3. {91A74BCA...}.png -> lab-grown-3 (marquise ring, target square 768x768)

def pad_and_scale_image(src_path, dest_path, target_w, target_h, scale_factor=0.5):
    with Image.open(src_path) as img:
        # Step 1: Sample background color from corners (average of four corners)
        w, h = img.size
        corners = [
            img.getpixel((5, 5)),
            img.getpixel((w - 6, 5)),
            img.getpixel((5, h - 6)),
            img.getpixel((w - 6, h - 6))
        ]
        
        # Calculate average RGB
        avg_r = sum(c[0] for c in corners) // 4
        avg_g = sum(c[1] for c in corners) // 4
        avg_b = sum(c[2] for c in corners) // 4
        bg_color = (avg_r, avg_g, avg_b)
        print(f"Sampleed background color for {os.path.basename(src_path)}: {bg_color}")
        
        # Step 2: Resize the original image down so the ring itself is smaller
        # Calculate new size based on scale_factor
        img_ar = h / w
        target_ar = target_h / target_w
        
        if img_ar > target_ar:
            # Image is taller relative to target, scale based on height
            new_h = int(target_h * scale_factor)
            new_w = int(new_h / img_ar)
        else:
            # Image is wider relative to target, scale based on width
            new_w = int(target_w * scale_factor)
            new_h = int(new_w * img_ar)
            
        resized_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Step 3: Create target canvas and paste resized image centered
        canvas = Image.new('RGB', (target_w, target_h), bg_color)
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        canvas.paste(resized_img, (paste_x, paste_y))
        
        canvas.save(dest_path, 'PNG')
        print(f"Successfully processed {dest_path}")

# Apply processing
pad_and_scale_image(os.path.join(src_dir, files[0]), os.path.join(web_dir, 'lab-grown-1.png'), 768, 768, scale_factor=0.55)
pad_and_scale_image(os.path.join(src_dir, files[1]), os.path.join(web_dir, 'lab-grown-2.png'), 768, 1180, scale_factor=0.55)
pad_and_scale_image(os.path.join(src_dir, files[2]), os.path.join(web_dir, 'lab-grown-3.png'), 768, 768, scale_factor=0.55)
