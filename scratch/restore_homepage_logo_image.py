import os

html_path = 'index.html'

if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # 1. Update style block: hide text logo, show image logo
    # We find the style block boundaries
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    
    si = content.find(start_marker)
    ei = content.find(end_marker)
    
    if si != -1 and ei != -1:
        # We will extract the current block and replace the logo styling rules inside it
        override_block = content[si:ei]
        
        # Replace the rule for .kavita-khosla to hide it
        old_logo_text_rule = """    /* Logo text - Original Kalnia font, ~32px, dark plum/maroon */
    body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 32px !important;
      color: #4B1E3E !important; /* Dark plum/maroon */
      font-weight: 500 !important;
      text-transform: none !important; /* Title Case */
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
    
        new_logo_text_rule = """    /* Hide HTML logo text on desktop */
    body header .kavita-khosla-parent .kavita-khosla {
      display: none !important;
    }"""
    
        # Replace the rule for img.brand-name-and-style-1 to show it
        old_logo_img_rule = """    /* Hide the image logo */
    body header img.brand-name-and-style-1 {
      display: none !important;
    }"""
    
        new_logo_img_rule = """    /* Show and center original image logo */
    body header img.brand-name-and-style-1 {
      display: block !important;
      width: 208px !important;
      height: 46px !important;
      object-fit: contain !important;
      margin: 0 auto !important;
      position: static !important;
    }"""
    
        if old_logo_text_rule in override_block:
            override_block = override_block.replace(old_logo_text_rule, new_logo_text_rule)
        else:
            print("Warning: old_logo_text_rule not found in block.")
            
        if old_logo_img_rule in override_block:
            override_block = override_block.replace(old_logo_img_rule, new_logo_img_rule)
        else:
            print("Warning: old_logo_img_rule not found in block.")
            
        new_content = content[:si] + override_block + content[ei:]
        open(html_path, 'w', encoding='utf-8').write(new_content)
        print("Successfully updated style override block in index.html to restore image logo.")
    else:
        print("Error: Could not locate overrides style block in index.html.")
else:
    print("index.html not found!")
