import os

html_path = 'index.html'

if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # 1. Restore the Google Fonts link to import Kalnia web font
    old_fonts = 'https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&amp;family=Cormorant+Garamond:ital,wght@0,300..700;1,300..700&amp;display=swap'
    new_fonts = 'https://fonts.googleapis.com/css2?family=Kalnia:wght@300;400;500;600;700&amp;display=swap'
    
    if old_fonts in content:
        content = content.replace(old_fonts, new_fonts)
        print("Restored Google Font import for Kalnia in <head>.")
    else:
        print("Warning: Playfair/Cormorant font import link not found in head.")
        
    # 2. Rebuild the clean header overrides block with original Kalnia typography styles
    REBUILT_HEADER_CSS = """
  /* === Centered Two-Row Desktop Header Overrides === */
  @media screen and (min-width: 769px) {
    /* 1. Header wrapper container: 2px solid black border box, white bg */
    body header.frame-parent {
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
      background-color: #ffffff !important;
      border: 2px solid #000000 !important;
      padding: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      position: relative !important;
      height: auto !important;
    }
    
    /* 2. Top-left corner decorative box outline */
    .header-corner-box {
      display: block !important;
      position: absolute !important;
      top: 14px !important;
      left: 14px !important;
      width: 14px !important;
      height: 14px !important;
      border: 1px solid #d3d3d3 !important;
      background-color: transparent !important;
      border-radius: 2px !important;
      pointer-events: none !important;
      z-index: 100 !important;
    }
    
    /* Hide mobile menu checkbox and hamburger button on desktop */
    .menu-toggle-chk,
    .hamburger-btn {
      display: none !important;
    }
    
    /* 3. Logo Row - Centered with vertical padding */
    body header .kavita-khosla-parent {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      margin: 0 !important;
      padding: 24px 0 16px 0 !important; /* ~24px top, ~16px bottom padding */
      position: relative !important;
      height: auto !important;
      float: none !important;
      border-bottom: 1px solid #e5e5e5 !important; /* Divider line separating logo from nav */
    }
    
    /* Logo text - Original Kalnia font, ~32px, dark plum/maroon */
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
    }
    
    /* Hide the image logo */
    body header img.brand-name-and-style-1 {
      display: none !important;
    }
    
    /* 4. Nav Row Wrapper */
    body header .link {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      margin: 0 !important;
      height: auto !important;
      position: static !important;
    }
    
    body header .link2 {
      display: flex !important;
      flex-direction: row !important;
      justify-content: center !important;
      align-items: center !important;
      gap: 45px !important; /* ~40-50px gaps between nav items */
      width: 100% !important;
      height: auto !important;
      position: static !important;
      border-top: none !important;
      padding: 14px 0 !important; /* Vertical padding ~14px */
    }
    
    /* Normalize link wrappers */
    body header .header-nav,
    body header .dropdown {
      width: auto !important;
      height: auto !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      position: relative !important;
    }
    
    /* 5. Nav Link Styling - Original Kalnia font, uppercase, ~12px, dark green/black */
    body header a.home,
    body header a.home2,
    body header a.home3,
    body header .dropdown div.home,
    body header .dropdown div.home2 {
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 12px !important;
      text-transform: uppercase !important;
      color: #08201a !important; /* Theme original color */
      font-weight: 500 !important;
      letter-spacing: 0.04em !important;
      text-decoration: none !important;
      opacity: 0.9 !important;
      transition: opacity 0.2s ease, color 0.2s ease !important;
    }
    
    body header a.home:hover,
    body header a.home2:hover,
    body header a.home3:hover,
    body header .dropdown:hover div.home,
    body header .dropdown:hover div.home2 {
      opacity: 1 !important;
      color: #b3a66c !important;
    }
    
    /* Dropdown caret indicator */
    body header .dropdown::after {
      content: " ▾" !important;
      color: #08201a !important;
      opacity: 0.9 !important;
      margin-left: 6px !important;
      font-size: 10px !important;
    }
  }
  
  /* Mobile styling overrides for header (hamburger and border box) */
  @media screen and (max-width: 768px) {
    body header.frame-parent {
      border: 2px solid #000000 !important;
      background-color: #ffffff !important;
      box-sizing: border-box !important;
    }
    .header-corner-box {
      display: block !important;
      position: absolute !important;
      top: 14px !important;
      left: 14px !important;
      width: 14px !important;
      height: 14px !important;
      border: 1px solid #d3d3d3 !important;
      border-radius: 2px !important;
      pointer-events: none !important;
    }
  }
"""

    # We replace everything from the first occurrence of the start marker to the end marker
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    
    si = content.find(start_marker)
    ei = content.find(end_marker)
    
    if si != -1 and ei != -1:
        new_content = content[:si] + REBUILT_HEADER_CSS + content[ei:]
        open(html_path, 'w', encoding='utf-8').write(new_content)
        print("Successfully replaced header overrides block with original Kalnia font styles and cleaned duplicates.")
    else:
        print("Error: Could not locate the desktop overrides style block boundaries.")
        
else:
    print("index.html not found!")
