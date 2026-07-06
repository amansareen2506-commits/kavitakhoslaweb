import os
import shutil

src = r"C:\Users\HP\Downloads\ChatGPT Image Jul 3, 2026, 12_22_53 AM.png"
dest = "image-31@2x.86c8359a.png"

# 1. Backup original
bak = dest + ".bak"
if os.path.exists(dest) and not os.path.exists(bak):
    shutil.copy2(dest, bak)
    print(f"Backed up: {dest} to {bak}")

# 2. Replace image
shutil.copy2(src, dest)
print("Replaced second banner image with new ChatGPT image successfully!")

# 3. Add CSS rule to hide dynamic text on the second banner
html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

HIDE_TEXT_CSS = """
  /* Hide dynamic HTML text overlay on the second banner since the text is baked into the new image */
  .image-3-group .frame-parent5 {
    display: none !important;
  }
"""

style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + HIDE_TEXT_CSS + content[style_end:]
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Added HIDE_TEXT_CSS for second banner to index.html successfully.")
else:
    print("Could not find </style> tag in index.html!")
