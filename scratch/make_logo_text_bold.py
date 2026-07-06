import os

html_path = 'index.html'

if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # We find the style block boundaries
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    
    si = content.find(start_marker)
    ei = content.find(end_marker)
    
    if si != -1 and ei != -1:
        override_block = content[si:ei]
        
        # Replace the rule for .kavita-khosla to make the font-weight bold (700)
        old_weight_rule = "      font-weight: 400 !important;"
        new_weight_rule = "      font-weight: 700 !important; /* Bold */"
        
        if old_weight_rule in override_block:
            override_block = override_block.replace(old_weight_rule, new_weight_rule)
            new_content = content[:si] + override_block + content[ei:]
            open(html_path, 'w', encoding='utf-8').write(new_content)
            print("Successfully made the logo text bold (font-weight: 700).")
        else:
            print("Error: Could not locate the font-weight rule in style override block.")
    else:
        print("Error: Could not locate overrides style block in index.html.")
else:
    print("index.html not found!")
