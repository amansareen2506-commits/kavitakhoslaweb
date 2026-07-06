import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

# CSS rule to hide the dynamic HTML text overlay on the first banner since the text is already baked into the new image.
HIDE_TEXT_CSS = """
  /* Hide dynamic HTML text overlay on the first banner since the text is baked into the new image */
  .image-3-parent .frame-parent3 {
    display: none !important;
  }
"""

style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + HIDE_TEXT_CSS + content[style_end:]
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Successfully added HIDE_TEXT_CSS to index.html.")
else:
    print("Could not find </style> tag in index.html!")
