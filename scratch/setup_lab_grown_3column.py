import os
import shutil
from PIL import Image

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'
html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'

os.makedirs(web_dir, exist_ok=True)

# 1. Clean up and get original files from desktop
files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
files.sort()

print("Original files from desktop:", files)

# 2. Crop the 3 images to standard aspect ratios (768x768 and 768x1180) to match other images
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

def crop_to_tall(img_path, dest_path):
    target_ar = 1180 / 768
    with Image.open(img_path) as img:
        w, h = img.size
        current_ar = h / w
        
        if current_ar > target_ar:
            new_h = w * target_ar
            left = 0
            top = (h - new_h) / 2
            right = w
            bottom = (h + new_h) / 2
        else:
            new_w = h / target_ar
            left = (w - new_w) / 2
            top = 0
            right = (w + new_w) / 2
            bottom = h
            
        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((768, 1180), Image.Resampling.LANCZOS)
        resized.save(dest_path, 'PNG')

p1 = os.path.join(web_dir, 'lab-grown-1.png')
p2 = os.path.join(web_dir, 'lab-grown-2.png')
p3 = os.path.join(web_dir, 'lab-grown-3.png')

# {3FEB6EB8...} -> lab-grown-1 (square)
crop_to_square(os.path.join(src_dir, files[0]), p1)
# {6C97A3B1...} -> lab-grown-2 (tall)
crop_to_tall(os.path.join(src_dir, files[1]), p2)
# {91A74BCA...} -> lab-grown-3 (square)
crop_to_square(os.path.join(src_dir, files[2]), p3)

print("Images cropped successfully.")

# 3. Create the list of all 15 images to balance
existing_images = [
    'Rectangle-119@2x.d1b6059c.png',
    'Rectangle-37@2x.8710ad2b.png',
    'Rectangle-121@2x.741e9614.png',
    'Rectangle-109@2x.9f643b65.png',
    'Rectangle-118@2x.bfc93ef1.png',
    'Rectangle-84@2x.d0389893.png',
    'Rectangle-107@2x.3fb6c261.png',
    'Rectangle-36@2x.7237bee6.png',
    'Rectangle-12@2x.532be98b.png',
    'new-ring@2x.daf57d6f.png',
    'Rectangle-108@2x.113db84c.png',
    'Rectangle-83@2x.58e9e4e6.png'
]

all_images = []
for f in existing_images:
    all_images.append({'src': f'/{f}', 'local_path': f})
for f in [p1, p2, p3]:
    web_path = '/' + f.replace('\\', '/')
    all_images.append({'src': web_path, 'local_path': f})

# Calculate aspect ratios
def get_aspect_ratio(img_info):
    with Image.open(img_info['local_path']) as img:
        w, h = img.size
        return h / w

for img in all_images:
    img['ar'] = get_aspect_ratio(img)

# Sort images by aspect ratio descending for greedy balancing
sorted_images = sorted(all_images, key=lambda x: x['ar'], reverse=True)

# Distribute into 3 columns
c1, c2, c3 = [], [], []
h1, h2, h3 = 0.0, 0.0, 0.0
col_size = (len(sorted_images) + 2) // 3

for img in sorted_images:
    candidates = []
    if len(c1) < col_size:
        candidates.append((h1, 'c1'))
    if len(c2) < col_size:
        candidates.append((h2, 'c2'))
    if len(c3) < len(sorted_images) - 2 * col_size or len(c3) < col_size:
        candidates.append((h3, 'c3'))
        
    candidates.sort(key=lambda x: x[0])
    chosen = candidates[0][1]
    
    if chosen == 'c1':
        c1.append(img)
        h1 += img['ar']
    elif chosen == 'c2':
        c2.append(img)
        h2 += img['ar']
    else:
        c3.append(img)
        h3 += img['ar']

# Re-combine in balanced column order
balanced_images = c1 + c2 + c3
print(f"Balanced Column Heights: {round(h1,2)}, {round(h2,2)}, {round(h3,2)}")

# 4. Build HTML markup
grid_html = ['        <section class="lab-grown-grid">']
for idx, img in enumerate(balanced_images):
    src = img['src']
    grid_html.append(f'          <img class="grid-image" loading="lazy" alt="Lab Grown Diamond {idx+1}" src="{src}?v=2032">')
grid_html.append('        </section>')
grid_markup = '\n'.join(grid_html)

# 5. Modify HTML file content
content = open(html_path, encoding='utf-8').read()

# Remove previous style grid overrides if any
style_end = content.find('</style>')
GRID_CSS = """
  /* Responsive masonry layout for Lab Grown Diamonds */
  .lab-grown-grid {
    column-count: 3 !important;
    column-gap: 16px !important;
    width: 100% !important;
    max-width: 1200px !important;
    margin: 16px auto !important;
    box-sizing: border-box !important;
    padding: 0 16px !important;
  }
  .lab-grown-grid .grid-image {
    width: 100% !important;
    height: auto !important;
    display: block !important;
    margin-bottom: 16px !important;
    border-radius: 8px !important;
    transition: transform 0.3s ease !important;
    break-inside: avoid !important;
    image-rendering: -webkit-optimize-contrast !important;
    image-rendering: crisp-edges !important;
  }
  .lab-grown-grid .grid-image:hover {
    transform: scale(1.02) !important;
  }
  @media screen and (max-width: 768px) {
    .lab-grown-grid {
      column-count: 2 !important;
      column-gap: 12px !important;
    }
    .lab-grown-grid .grid-image {
      margin-bottom: 12px !important;
    }
  }
  @media screen and (max-width: 480px) {
    .lab-grown-grid {
      column-count: 1 !important;
      column-gap: 0 !important;
    }
    .lab-grown-grid .grid-image {
      margin-bottom: 16px !important;
    }
  }
"""

if GRID_CSS not in content:
    content = content[:style_end] + GRID_CSS + content[style_end:]

# Replace the parent section with the new grid markup
section_start = content.find('<section class=frame-parent22>')
section_end = content.find('</section>', section_start)

if section_start != -1 and section_end != -1:
    content = content[:section_start] + grid_markup + content[section_end + len('</section>'):]
    print("Injected grid layout.")
else:
    print("Could not find section class=frame-parent22!")

open(html_path, 'w', encoding='utf-8').write(content)
print("File successfully updated with 3-column layout!")
