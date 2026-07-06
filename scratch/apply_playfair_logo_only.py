import os

html_path = 'index.html'

if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # 1. Update font link to include both Kalnia and Playfair Display
    old_fonts = 'https://fonts.googleapis.com/css2?family=Kalnia:wght@300;400;500;600;700&amp;display=swap'
    new_fonts = 'https://fonts.googleapis.com/css2?family=Kalnia:wght@300;400;500;600;700&amp;family=Playfair+Display:ital,wght@0,400..900;1,400..900&amp;display=swap'
    
    if old_fonts in content:
        content = content.replace(old_fonts, new_fonts)
        print("Updated font link to load both Kalnia and Playfair Display.")
    else:
        # Fallback if it's already there or slightly different
        if new_fonts not in content:
            print("Warning: Could not find Kalnia-only link to replace, checking if Playfair is already loaded.")
            
    # 2. Update the style overrides block for .kavita-khosla logo text
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    
    si = content.find(start_marker)
    ei = content.find(end_marker)
    
    if si != -1 and ei != -1:
        override_block = content[si:ei]
        
        # Replace logo text styles inside override block
        old_logo_rule = """    /* Show and style the text logo in the center in PLUM color and Kalnia font */
    body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 32px !important;
      color: #4b1e3e !important; /* Dark plum/purple */
      font-weight: 700 !important; /* Bold */
      text-transform: none !important; /* Title Case 'Kavita Khosla' */
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
        
        new_logo_rule = """    /* Show and style the text logo in the center in PLUM color and Playfair Display font */
    body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: 40px !important;
      color: #4b1e3e !important; /* Dark plum/purple */
      font-weight: 600 !important; /* Medium-bold */
      text-transform: none !important; /* Title Case 'Kavita Khosla' */
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
        
        if old_logo_rule in override_block:
            override_block = override_block.replace(old_logo_rule, new_logo_rule)
            new_content = content[:si] + override_block + content[ei:]
            open(html_path, 'w', encoding='utf-8').write(new_content)
            print("Successfully updated the Kavita Khosla logo text style to Playfair Display (#4b1e3e, 40px, semi-bold).")
        else:
            # Try a partial string replace for the properties inside .kavita-khosla rule
            print("Warning: exact old_logo_rule match not found. Attempting regex or fallback replace.")
            # Let's do a fallback replacement
            import re
            pattern = r'body header \.kavita-khosla-parent \.kavita-khosla \{[^}]*\}'
            match = re.search(pattern, override_block)
            if match:
                replacement_rule = """body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: 40px !important;
      color: #4b1e3e !important;
      font-weight: 600 !important;
      text-transform: none !important;
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
                override_block = re.sub(pattern, replacement_rule, override_block)
                new_content = content[:si] + override_block + content[ei:]
                open(html_path, 'w', encoding='utf-8').write(new_content)
                print("Successfully updated the Kavita Khosla logo text style via regex fallback.")
            else:
                print("Error: Could not find logo styles rule.")
    else:
         print("Error: Overrides style block not found in index.html.")
else:
    print("index.html not found!")
