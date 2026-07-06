import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# 1. Remove the injected GRID_CSS
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

if GRID_CSS in content:
    content = content.replace(GRID_CSS, "")
    print("Removed GRID_CSS.")
else:
    print("GRID_CSS not found in file.")

# 2. Revert the grid header
content = content.replace('<div class=ear-ornaments5>Lab Grown Diamonds</div>', '<div class=ear-ornaments5>Ear Ornaments</div>')
print("Reverted grid header to 'Ear Ornaments'.")

# 3. Find the new lab-grown-grid section and replace it with the original frame-parent22 section
ORIGINAL_SECTION = """        <section class=frame-parent22>
          <div class=frame-parent23>
            <div class=rectangle-parent14>
              <img class=frame-child49 loading=lazy alt src=/Rectangle-119@2x.d1b6059c.png?v=2030>

              <img class=frame-child50 loading=lazy alt src=/Rectangle-37@2x.8710ad2b.png?v=2030>
            </div>
            <div class=rectangle-parent15>
              <img class=frame-child51 loading=lazy alt src=/Rectangle-121@2x.741e9614.png?v=2030>

              <img class=frame-child49 loading=lazy alt src=/Rectangle-109@2x.9f643b65.png?v=2030>
            </div>
            <div class=rectangle-parent14>
              <img class=frame-child49 loading=lazy alt src=/Rectangle-118@2x.bfc93ef1.png?v=2030>

              <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
            </div>
          </div>
          <div class=frame-parent24>
            <div class=rectangle-parent17>
              <img class=frame-child49 loading=lazy alt src=/Rectangle-107@2x.3fb6c261.png?v=2030>

              <img class=frame-child56 loading=lazy alt src=/Rectangle-36@2x.7237bee6.png?v=2030>
            </div>
            <div class=rectangle-parent17>
              <img class=frame-child57 loading=lazy alt src=/Rectangle-12@2x.532be98b.png?v=2030>

              <img class=frame-child49 loading=lazy alt src=/new-ring@2x.daf57d6f.png?v=2030>
            </div>
            <div class=rectangle-parent17>
              <img class=frame-child58 loading=lazy alt src=/Rectangle-108@2x.113db84c.png?v=2030>

              <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
            </div>
          </div>
        </section>"""

grid_start = content.find('        <section class="lab-grown-grid">')
grid_end = content.find('        </section>', grid_start)

if grid_start != -1 and grid_end != -1:
    content = content[:grid_start] + ORIGINAL_SECTION + content[grid_end + len('        </section>'):]
    print("Reverted image section back to frame-parent22.")
else:
    print("New grid section not found in file.")

open(html_path, 'w', encoding='utf-8').write(content)
print("File successfully reverted!")

# 4. Optional: Clean up project assets folder lab-grown-diamonds-images
if os.path.exists('lab-grown-diamonds-images'):
    import shutil
    shutil.rmtree('lab-grown-diamonds-images')
    print("Removed copied images from project assets.")
