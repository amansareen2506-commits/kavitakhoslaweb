import os
import shutil

src_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
dest_dir = 'lab-grown-diamonds-images'
html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'

# 1. Copy the 5 images to project folder
os.makedirs(dest_dir, exist_ok=True)
new_images = [f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.lower().endswith('.bak')]
new_images.sort()

for idx, img_name in enumerate(new_images):
    dest_name = f'lab-grown-{idx+1}.png'
    shutil.copy2(os.path.join(src_dir, img_name), os.path.join(dest_dir, dest_name))
    print(f"Copied {img_name} as {dest_name}")

# 2. Modify the HTML file to append the images to the columns without altering layout structure
content = open(html_path, encoding='utf-8').read()

# Define the HTML blocks to append to each column
col1_append = """            <div class=rectangle-parent14>
              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

              <img class=frame-child50 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
            </div>
          </div>"""

col2_append = """            <div class=rectangle-parent17>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">

              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-4.png?v=2030">
            </div>
            <div class=rectangle-parent17>
              <img class=frame-child58 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-5.png?v=2030">
            </div>
          </div>"""

# Find the end of the first column (div.frame-parent23)
# The column markup ends with:
#             <div class=rectangle-parent14>
#               <img class=frame-child49 loading=lazy alt src=/Rectangle-118@2x.bfc93ef1.png?v=2030>
# 
#               <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
#             </div>
#           </div>

target_col1_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
            </div>
          </div>"""

idx1 = content.find(target_col1_end)
if idx1 != -1:
    content = content[:idx1 + len(target_col1_end) - 6] + col1_append + content[idx1 + len(target_col1_end):]
    print("Appended images to Column 1.")
else:
    print("Could not find the end of Column 1!")

# Find the end of the second column (div.frame-parent24)
# The column markup ends with:
#             <div class=rectangle-parent17>
#               <img class=frame-child58 loading=lazy alt src=/Rectangle-108@2x.113db84c.png?v=2030>
# 
#               <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
#             </div>
#           </div>

target_col2_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
            </div>
          </div>"""

idx2 = content.find(target_col2_end)
if idx2 != -1:
    content = content[:idx2 + len(target_col2_end) - 6] + col2_append + content[idx2 + len(target_col2_end):]
    print("Appended images to Column 2.")
else:
    print("Could not find the end of Column 2!")

open(html_path, 'w', encoding='utf-8').write(content)
print("File successfully updated with original layout layout intact.")
