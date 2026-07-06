import os
import shutil

src = r"C:\Users\HP\Downloads\ChatGPT Image Jul 3, 2026, 12_09_45 AM.png"

dest1 = "image-32@2x.98ec8bd9.png"
dest2 = "image-41@2x.a3c7c652.png"

# Backup originals
for d in [dest1, dest2]:
    bak = d + ".bak"
    if os.path.exists(d) and not os.path.exists(bak):
        shutil.copy2(d, bak)
        print(f"Backed up: {d} to {bak}")

# Copy new image to replace both
shutil.copy2(src, dest1)
shutil.copy2(src, dest2)
print("Successfully replaced banner images with the new ChatGPT image!")
