import re

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

# Match the exact Discover the Set button element
pattern = r'\s*<button class=cta-primary>\s*<div class=explore-now>DISCOVER THE SET</div>\s*</button>'
new_content, count = re.subn(pattern, "", content, flags=re.IGNORECASE)

open(html_path, 'w', encoding='utf-8').write(new_content)
print(f"Successfully removed {count} DISCOVER THE SET buttons from index.html.")
