import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# Original section HTML block
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

# Find the start of the section class=frame-parent22
start_idx = content.find('<section class=frame-parent22>')
end_idx = content.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    clean_content = content[:start_idx] + ORIGINAL_SECTION + content[end_idx + len('</section>'):]
    open(html_path, 'w', encoding='utf-8').write(clean_content)
    print("Successfully reverted HTML layout to original 12 images.")
else:
    print("Could not find section class=frame-parent22 inside the HTML file!")

# Clean up project assets folder lab-grown-diamonds-images
if os.path.exists('lab-grown-diamonds-images'):
    import shutil
    shutil.rmtree('lab-grown-diamonds-images')
    print("Removed copied images from project assets.")
