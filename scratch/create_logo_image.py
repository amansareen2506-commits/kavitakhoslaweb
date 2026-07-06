"""
Create a pixel-perfect 'Kavita Khosla' logo image using Playfair Display Bold.
Downloads the font directly from Google Fonts CSS API.
"""
import os
import re
import urllib.request
from PIL import Image, ImageDraw, ImageFont

# 1. Download Playfair Display Bold font directly
FONT_CSS_URL = "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap"
FONT_FILE = "PlayfairDisplay-Bold.ttf"

if not os.path.exists(FONT_FILE):
    print("Fetching font CSS to get TTF URL...")
    req = urllib.request.Request(FONT_CSS_URL, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    css_content = urllib.request.urlopen(req).read().decode('utf-8')
    
    # Extract the font URL from the CSS
    urls = re.findall(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', css_content)
    if urls:
        font_url = urls[0]
        print(f"Downloading font from: {font_url}")
        urllib.request.urlretrieve(font_url, FONT_FILE)
        print("Font downloaded.")
    else:
        print("Error: Could not find font URL in CSS response.")
        print("CSS content:", css_content[:500])
        exit(1)

print(f"Using font file: {FONT_FILE}")

# 2. Render the text
TEXT = "Kavita Khosla"
FONT_SIZE = 72  # Render at 2x for crisp retina display
COLOR = (61, 21, 53)  # #3d1535 dark plum
BG_COLOR = (255, 255, 255)  # White

font = ImageFont.truetype(FONT_FILE, FONT_SIZE)

# Measure text bounding box
dummy_img = Image.new('RGB', (1, 1))
dummy_draw = ImageDraw.Draw(dummy_img)
bbox = dummy_draw.textbbox((0, 0), TEXT, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Create image with padding
pad_x = 60
pad_y = 40
img_width = text_width + 2 * pad_x
img_height = text_height + 2 * pad_y

img = Image.new('RGB', (img_width, img_height), BG_COLOR)
draw = ImageDraw.Draw(img)

# Center text
x = (img_width - text_width) // 2 - bbox[0]
y = (img_height - text_height) // 2 - bbox[1]
draw.text((x, y), TEXT, fill=COLOR, font=font)

# 3. Save the image
output_path = 'kavita-khosla-logo.png'
img.save(output_path, 'PNG')
print(f"Logo saved to: {output_path}")
print(f"Image size: {img_width}x{img_height}")

# Clean up font file
os.remove(FONT_FILE)
print("Cleaned up font file.")
