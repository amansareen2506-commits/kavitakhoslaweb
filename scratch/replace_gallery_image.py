import os
import shutil

src = r"C:\Users\HP\Downloads\ChatGPT Image Jul 3, 2026, 12_52_21 AM.png"
dest = "image-6@2x.8c88ef1c.png"

# 1. Backup original
bak = dest + ".bak"
if os.path.exists(dest) and not os.path.exists(bak):
    shutil.copy2(dest, bak)
    print(f"Backed up: {dest} to {bak}")

# 2. Replace image
shutil.copy2(src, dest)
print("Replaced image-6@2x.8c88ef1c.png with new ChatGPT image successfully!")
