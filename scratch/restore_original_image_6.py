import os
import shutil

dest = "image-6@2x.8c88ef1c.png"
bak = dest + ".bak"

# 1. Restore from backup
if os.path.exists(bak):
    shutil.copy2(bak, dest)
    print(f"Restored {dest} from {bak}.")
else:
    print(f"Error: Backup file {bak} not found!")

# 2. Update version token in index.html for cache busting
html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

old_str = "src=/image-6@2x.8c88ef1c.png?v=2035"
new_str = "src=/image-6@2x.8c88ef1c.png?v=2040"

if old_str in content:
    content = content.replace(old_str, new_str)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Updated image-6 cache-busting token to v=2040.")
else:
    print("Could not find image-6 v=2035 tag in index.html!")
