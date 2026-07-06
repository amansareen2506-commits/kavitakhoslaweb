import os

# Overwrite Frame.033b85b4.svg and Frame1.ca451626.svg with a premium gold Chevron-Down arrow SVG
arrow_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="#b3a66c" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m6 9 6 6 6-6"/></svg>'

svg1 = 'Frame.033b85b4.svg'
svg2 = 'Frame1.ca451626.svg'

with open(svg1, 'w', encoding='utf-8') as f:
    f.write(arrow_svg)
print(f"Overwrote {svg1} with Chevron-Down SVG.")

with open(svg2, 'w', encoding='utf-8') as f:
    f.write(arrow_svg)
print(f"Overwrote {svg2} with Chevron-Down SVG.")
