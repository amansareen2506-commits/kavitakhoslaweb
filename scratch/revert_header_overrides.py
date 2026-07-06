import os
import re

pages = [
    'index.html',
    'about-us/about-us.html',
]

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        
        # 1. Remove the centered header overrides CSS block completely
        # We look for the Centered Header Overrides block starting from our comment marker
        pattern = r'\s*/\* === Centered Two-Row Desktop Header Overrides === \*/\s*@media screen and \(min-width: 769px\) \{.*?\}\s*\}'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Fallback string replace in case of spacing difference
        start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
        end_marker = '</style><body>'
        si = content.find(start_marker)
        ei = content.find(end_marker)
        if si != -1 and ei != -1:
            content = content[:si] + content[ei:]
            
        # 2. Revert HTML text changes back to original
        content = content.replace('Kavita Khosla', 'KAVITA KHOSLA')
        content = content.replace('>HOME</a>', '>Home</a>')
        
        open(page, 'w', encoding='utf-8').write(content)
        print(f"Successfully reverted header overrides in: {page} to match default Locofy layout.")
    else:
        print(f"File not found: {page}")
