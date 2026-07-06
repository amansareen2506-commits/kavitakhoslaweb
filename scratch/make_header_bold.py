import os

html_path = 'index.html'

if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # 1. Update the Google Fonts link for Kalnia to include weights 300 to 700
    old_font_link = 'https://fonts.googleapis.com/css2?family=Kalnia:wght@300;400&amp;display=swap'
    new_font_link = 'https://fonts.googleapis.com/css2?family=Kalnia:wght@300;400;500;600;700&amp;display=swap'
    
    content = content.replace(old_font_link, new_font_link)
    
    # 2. Update the style overrides inside the Centered Desktop Header block
    # We will search for the font-size/font-weight rules for .kavita-khosla and update them to match the thick/bold second image
    old_css_rules = """    /* Show and style the text logo in the center in PLUM color */
    body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 32px !important;
      color: #4d1741 !important; /* Plum color from the screenshot */
      font-weight: 400 !important;
      text-transform: none !important; /* Preserve Title Case 'Kavita Khosla' */
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
    
    new_css_rules = """    /* Show and style the text logo in the center in PLUM color (Bold & Premium) */
    body header .kavita-khosla-parent .kavita-khosla {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: 'Kalnia', var(--font-kalnia), Kalnia, serif !important;
      font-size: 40px !important; /* Larger and more prominent */
      color: #4d1741 !important; /* Exact rich plum color */
      font-weight: 600 !important; /* Thicker bold strokes matching the second image */
      text-transform: none !important; /* Preserve Title Case */
      letter-spacing: -0.01em !important; /* Snug tracking for premium typography */
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }"""
    
    if old_css_rules in content:
        content = content.replace(old_css_rules, new_css_rules)
        print("Updated desktop header CSS overrides to make the Kavita Khosla text bold, thick, and rich plum color.")
    else:
        print("Could not find the exact old CSS rules in index.html!")
        
    open(html_path, 'w', encoding='utf-8').write(content)
else:
    print("index.html not found!")
