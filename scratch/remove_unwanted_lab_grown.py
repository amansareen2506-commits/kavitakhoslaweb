import os

desktop_dir = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'
web_dir = 'lab-grown-diamonds-images'
html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'

# 1. Delete the 2 unwanted files from the desktop folder
unwanted_files = [
    'ChatGPT Image Jul 3, 2026, 02_08_22 AM.png',
    '{176FB7AE-4AAA-4333-8F00-85B265F59007}.png'
]

for f in unwanted_files:
    p = os.path.join(desktop_dir, f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed from desktop: {f}")
    else:
        print(f"File not found on desktop: {f}")

# 2. Re-arrange and rename the remaining 3 files in the project assets folder
# Delete lab-grown-1.png and lab-grown-2.png
for f in ['lab-grown-1.png', 'lab-grown-2.png']:
    p = os.path.join(web_dir, f)
    if os.path.exists(p):
        os.remove(p)

# Rename:
# lab-grown-3.png -> lab-grown-1.png
# lab-grown-4.png -> lab-grown-2.png
# lab-grown-5.png -> lab-grown-3.png
rename_map = {
    'lab-grown-3.png': 'lab-grown-1.png',
    'lab-grown-4.png': 'lab-grown-2.png',
    'lab-grown-5.png': 'lab-grown-3.png'
}

for src, dest in rename_map.items():
    src_p = os.path.join(web_dir, src)
    dest_p = os.path.join(web_dir, dest)
    if os.path.exists(src_p):
        if os.path.exists(dest_p):
            os.remove(dest_p)
        os.rename(src_p, dest_p)
        print(f"Renamed project asset {src} to {dest}")

# 3. Revert the HTML changes and update the columns to only include the 3 correct images
content = open(html_path, encoding='utf-8').read()

# Let's revert Column 1 back to its original end:
col1_block_to_remove = """                      <div class=rectangle-parent14>
               <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">
 
               <img class=frame-child50 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
             </div>"""

# Let's find the added code in Column 1 and remove it
# Let's do a search and replace for the exact added markup in Column 1
content = content.replace("""                      <div class=rectangle-parent14>
               <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

               <img class=frame-child50 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
             </div>""", "")

# Let's also check if there's any spacing difference and remove the code
content = content.replace("""                      <div class=rectangle-parent14>
              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

              <img class=frame-child50 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
            </div>""", "")

# Now let's update Column 2 to only include the 3 remaining images (renamed to 1, 2, 3)
# We want to replace the added Column 2 code:
#             <div class=rectangle-parent17>
#               <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">
# 
#               <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-4.png?v=2030">
#             </div>
#             <div class=rectangle-parent17>
#               <img class=frame-child58 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-5.png?v=2030">
#             </div>
# With:
#             <div class=rectangle-parent17>
#               <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">
# 
#               <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
#             </div>
#             <div class=rectangle-parent17>
#               <img class=frame-child58 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">
#             </div>

old_col2_addition = """                      <div class=rectangle-parent17>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">

              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-4.png?v=2030">
            </div>
            <div class=rectangle-parent17>
              <img class=frame-child58 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-5.png?v=2030">
            </div>"""

new_col2_addition = """                      <div class=rectangle-parent17>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
            </div>
            <div class=rectangle-parent17>
              <img class=frame-child58 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">
            </div>"""

content = content.replace(old_col2_addition, new_col2_addition)

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated HTML file and matched Column 2 images successfully.")
