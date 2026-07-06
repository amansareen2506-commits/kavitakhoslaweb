import os
import shutil

src = r"D:\Downloads\ChatGPT Image Jul 4, 2026, 01_09_10 AM.png"
dest = "rings-images/ring-24.png"

# 1. Backup original
bak = dest + ".bak"
if os.path.exists(dest) and not os.path.exists(bak):
    shutil.copy2(dest, bak)
    print(f"Backed up: {dest} to {bak}")

# 2. Replace file
shutil.copy2(src, dest)
print("Replaced rings-images/ring-24.png with the new download successfully!")

# 3. Update version query parameter in malana-collection/malana-collection.html for cache busting
html_path = 'malana-collection/malana-collection.html'
content = open(html_path, encoding='utf-8').read()

old_str = 'src="/rings-images/ring-24.png?v=2026"'
new_str = 'src="/rings-images/ring-24.png?v=2030"'

if old_str in content:
    content = content.replace(old_str, new_str)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Updated ring-24 version query parameter in malana-collection.html successfully.")
else:
    # Try alternate spacing/quotes
    old_str_alt = 'src="/rings-images/ring-24.png"'
    new_str_alt = 'src="/rings-images/ring-24.png?v=2030"'
    if old_str_alt in content:
        content = content.replace(old_str_alt, new_str_alt)
        open(html_path, 'w', encoding='utf-8').write(content)
        print("Updated ring-24 version query parameter (no previous token).")
    else:
        print("Could not find ring-24 tag in malana-collection.html!")
