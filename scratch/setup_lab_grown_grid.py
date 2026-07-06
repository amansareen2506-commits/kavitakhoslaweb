import os
import shutil
from PIL import Image

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
dest_dir = 'lab-grown-diamonds-images'
html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'

# 1. Copy the 5 new images to project folder
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

new_images = []
for f in os.listdir(src_dir):
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak'):
        new_images.append(os.path.join(src_dir, f))

# Sort to keep naming consistent
new_images.sort()

copied_paths = []
for idx, img_path in enumerate(new_images):
    dest_name = f'lab-grown-{idx+1}.png'
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(img_path, dest_path)
    copied_paths.append(dest_path)
    print(f"Copied {img_path} to {dest_path}")

# 2. List of 12 existing images in project root
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

# Total 17 images to balance
all_images = []
for f in existing_images:
    all_images.append({'src': f'/{f}', 'local_path': f})
for f in copied_paths:
    # use relative URL to root
    web_path = '/' + f.replace('\\', '/')
    all_images.append({'src': web_path, 'local_path': f})

# Compute aspect ratios (height / width)
def get_aspect_ratio(img_info):
    try:
        with Image.open(img_info['local_path']) as img:
            w, h = img.size
            return h / w
    except Exception as e:
        print(f"Error reading image size for {img_info['local_path']}: {e}")
        return 1.0

for img in all_images:
    img['ar'] = get_aspect_ratio(img)

# Sort images by aspect ratio descending for greedy balancing
sorted_images = sorted(all_images, key=lambda x: x['ar'], reverse=True)

# Distribute into 3 columns mathematically to balance heights
c1, c2, c3 = [], [], []
h1, h2, h3 = 0.0, 0.0, 0.0

col_size = (len(sorted_images) + 2) // 3

for img in sorted_images:
    # Find column with minimum height that isn't full
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
print(f"Column heights: {round(h1, 2)}, {round(h2, 2)}, {round(h3, 2)} | Diff: {round(max(h1, h2, h3) - min(h1, h2, h3), 3)}")

# 3. Build HTML block for the masonry grid
grid_html = ['        <section class="lab-grown-grid">']
for idx, img in enumerate(balanced_images):
    src = img['src']
    grid_html.append(f'          <img class="grid-image" loading="lazy" alt="Lab Grown Diamond {idx+1}" src="{src}?v=2026">')
grid_html.append('        </section>')
grid_markup = '\n'.join(grid_html)

# 4. Inject CSS style block in HTML
content = open(html_path, encoding='utf-8').read()

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

# Insert CSS before the first </style> tag in the file
style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + GRID_CSS + content[style_end:]

# Replace <section class=frame-parent22>...</section> with our new masonry markup
section_start = content.find('<section class=frame-parent22>')
section_end = content.find('</section>', section_start)

if section_start != -1 and section_end != -1:
    content = content[:section_start] + grid_markup + content[section_end + len('</section>'):]
    
# Change the grid header from "Ear Ornaments" to "Lab Grown Diamonds"
content = content.replace('<div class=ear-ornaments5>Ear Ornaments</div>', '<div class=ear-ornaments5>Lab Grown Diamonds</div>')

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated HTML markup and injected CSS style block successfully!")
