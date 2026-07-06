import os
import shutil

src_1 = r"C:\Users\HP\Local Sites\khosla\app\public\wp-content\themes\bijoux\samples\small.jpg"
src_2 = r"C:\Users\HP\Local Sites\khosla\app\public\wp-content\uploads\2020\09\ann-KzamVRUeL4I-unsplash_v2-1-188x300.jpg"

dest_dir_web = 'lab-grown-diamonds-images'
dest_dir_desktop = r'C:\Users\HP\OneDrive\Desktop\KKJ images\Lab Grown Diamonds'

# Ensure directories exist
os.makedirs(dest_dir_web, exist_ok=True)
os.makedirs(dest_dir_desktop, exist_ok=True)

# Copy to web folder
shutil.copy2(src_1, os.path.join(dest_dir_web, 'lab-grown-4.png'))
shutil.copy2(src_2, os.path.join(dest_dir_web, 'lab-grown-5.png'))
print("Copied files to web folder.")

# Copy to desktop folder under their target names
shutil.copy2(src_1, os.path.join(dest_dir_desktop, 'ChatGPT Image Jul 3, 2026, 02_08_22 AM.png'))
shutil.copy2(src_2, os.path.join(dest_dir_desktop, '{176FB7AE-4AAA-4333-8F00-85B265F59007}.png'))
print("Copied files to desktop folder.")
