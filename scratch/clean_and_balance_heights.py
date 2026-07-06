import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# Let's clean the HTML by finding the exact original columns structure and replacing the entire section
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
    # 1. First reset the section to its clean original state
    clean_content = content[:start_idx] + ORIGINAL_SECTION + content[end_idx + len('</section>'):]
    
    # 2. Now copy the new files to ensure they exist in web assets folder
    web_dir = 'lab-grown-diamonds-images'
    os.makedirs(web_dir, exist_ok=True)
    src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
    new_images = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
    new_images.sort()
    
    import shutil
    for idx, img_name in enumerate(new_images):
        dest_name = f'lab-grown-{idx+1}.png'
        shutil.copy2(os.path.join(src_dir, img_name), os.path.join(web_dir, dest_name))
        print(f"Copied {img_name} as {dest_name}")
        
    # 3. Define the new balanced image blocks (using compact height classes: frame-child57, frame-child51, frame-child56)
    # Column 1 (Left) gets lab-grown-1.png and lab-grown-2.png inside a new rectangle-parent14 block at the bottom
    col1_addition = """            <div class=rectangle-parent14>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

              <img class=frame-child51 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
            </div>
          </div>"""

    # Column 2 (Right) gets lab-grown-3.png inside a new rectangle-parent17 block at the bottom
    col2_addition = """            <div class=rectangle-parent17>
              <img class=frame-child56 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">
            </div>
          </div>"""

    # Find the ends of the columns inside the clean section to inject our blocks
    # Column 1 target end in original section
    target_col1_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
            </div>
          </div>"""

    # Column 2 target end in original section
    target_col2_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
            </div>
          </div>"""

    idx1 = clean_content.find(target_col1_end)
    if idx1 != -1:
        clean_content = clean_content[:idx1 + len(target_col1_end) - 6] + col1_addition + clean_content[idx1 + len(target_col1_end):]
        print("Injected Column 1.")
    else:
        print("Could not find Column 1 end!")

    idx2 = clean_content.find(target_col2_end)
    if idx2 != -1:
        clean_content = clean_content[:idx2 + len(target_col2_end) - 6] + col2_addition + clean_content[idx2 + len(target_col2_end):]
        print("Injected Column 2.")
    else:
        print("Could not find Column 2 end!")

    open(html_path, 'w', encoding='utf-8').write(clean_content)
    print("HTML file successfully reset and updated with balanced layout!")
else:
    print("Could not find section class=frame-parent22 inside the HTML file!")
