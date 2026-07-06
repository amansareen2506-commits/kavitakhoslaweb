import os
import shutil

src = r"D:\Downloads\ChatGPT Image Jul 3, 2026, 10_59_37 PM.png"
dest = "Rectangle-73@2x.8be13022.png"

# 1. Backup original
bak = dest + ".bak"
if os.path.exists(dest) and not os.path.exists(bak):
    shutil.copy2(dest, bak)
    print(f"Backed up: {dest} to {bak}")

# 2. Replace file
shutil.copy2(src, dest)
print("Replaced Rectangle-73@2x.8be13022.png with the new download successfully!")

# 3. Update version query parameter in index.html for cache busting
html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

old_str = "src=/Rectangle-73@2x.8be13022.png?v=2030"
new_str = "src=/Rectangle-73@2x.8be13022.png?v=2035"

if old_str in content:
    content = content.replace(old_str, new_str)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Updated Rectangle-73 version query parameter in index.html successfully.")
else:
    print("Could not find Rectangle-73 v=2030 tag in index.html!")
