import os
from PIL import Image

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'

# Clean up and get original files
files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
files.sort()

def pad_and_scale_image(src_path, dest_path, target_w, target_h, scale_factor=0.45):
    with Image.open(src_path) as img:
        w, h = img.size
        # Sample background color from corners
        corners = [
            img.getpixel((5, 5)),
            img.getpixel((w - 6, 5)),
            img.getpixel((5, h - 6)),
            img.getpixel((w - 6, h - 6))
        ]
        avg_r = sum(c[0] for c in corners) // 4
        avg_g = sum(c[1] for c in corners) // 4
        avg_b = sum(c[2] for c in corners) // 4
        bg_color = (avg_r, avg_g, avg_b)
        
        img_ar = h / w
        target_ar = target_h / target_w
        
        if img_ar > target_ar:
            new_h = int(target_h * scale_factor)
            new_w = int(new_h / img_ar)
        else:
            new_w = int(target_w * scale_factor)
            new_h = int(new_w * img_ar)
            
        resized_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        canvas = Image.new('RGB', (target_w, target_h), bg_color)
        paste_x = (target_w - new_w) // 2
        paste_y = (target_h - new_h) // 2
        canvas.paste(resized_img, (paste_x, paste_y))
        
        canvas.save(dest_path, 'PNG')
        print(f"Processed: {dest_path} with scale {scale_factor} and bg {bg_color}")

# Process into new cache-busting filenames
p1 = os.path.join(web_dir, 'lab-grown-small-1.png')
p2 = os.path.join(web_dir, 'lab-grown-small-2.png')
p3 = os.path.join(web_dir, 'lab-grown-small-3.png')

pad_and_scale_image(os.path.join(src_dir, files[0]), p1, 768, 768, scale_factor=0.42)
pad_and_scale_image(os.path.join(src_dir, files[1]), p2, 768, 1180, scale_factor=0.42)
pad_and_scale_image(os.path.join(src_dir, files[2]), p3, 768, 768, scale_factor=0.42)

# Update HTML references to the new cache-busting names
html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

content = content.replace('lab-grown-1.png', 'lab-grown-small-1.png')
content = content.replace('lab-grown-2.png', 'lab-grown-small-2.png')
content = content.replace('lab-grown-3.png', 'lab-grown-small-3.png')

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated HTML file with new cache-busting names successfully.")
