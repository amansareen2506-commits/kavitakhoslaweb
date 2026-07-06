import os
import shutil

src = r"C:\Users\HP\Downloads\ChatGPT Image Jul 3, 2026, 12_52_21 AM.png"
dest = "pendant-set.png"

# 1. Backup original
bak = dest + ".bak"
if os.path.exists(dest) and not os.path.exists(bak):
    shutil.copy2(dest, bak)
    print(f"Backed up: {dest} to {bak}")

# 2. Replace image file
shutil.copy2(src, dest)
print("Replaced pendant-set.png file successfully!")

# 3. Update version token in natural-solitaire-and-diamonds.html for cache busting
html_path = 'natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html'
content = open(html_path, encoding='utf-8').read()

old_str = "src=/pendant-set.png?v=2030"
new_str = "src=/pendant-set.png?v=2035"

if old_str in content:
    content = content.replace(old_str, new_str)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Updated pendant-set cache-busting version token in natural-solitaire-and-diamonds.html.")
else:
    # Try with quotes
    old_str_quotes = 'src="/pendant-set.png?v=2030"'
    new_str_quotes = 'src="/pendant-set.png?v=2035"'
    if old_str_quotes in content:
        content = content.replace(old_str_quotes, new_str_quotes)
        open(html_path, 'w', encoding='utf-8').write(content)
        print("Updated pendant-set cache-busting version token (with quotes).")
    else:
        print("Could not find pendant-set.png tag in natural-solitaire-and-diamonds.html!")
