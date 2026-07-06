import os

pages = [
    'index.html',
    'about-us/about-us.html',
]

HEADER_FIX_CSS = """
  /* === Centered Two-Row Desktop Header Overrides === */
  @media screen and (min-width: 769px) {
    /* 1. Header wrapper: column flex, white background, centered */
    header.frame-parent,
    header.frame-header {
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
      background-color: #ffffff !important;
      padding: 20px 0 15px 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      height: auto !important;
      position: static !important;
      border-bottom: 1px solid #f2f2f2 !important;
    }
    
    /* Hide the mobile checkbox toggle on desktop */
    .menu-toggle-chk,
    .hamburger-btn {
      display: none !important;
    }
    
    /* 2. Centered Logo Row */
    .kavita-khosla-parent,
    .kavita-khosla-group {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      margin: 0 0 16px 0 !important;
      position: static !important;
      height: auto !important;
      float: none !important;
    }
    
    /* Hide duplicate text logo label */
    .kavita-khosla,
    .kavita-khosla4 {
      display: none !important;
    }
    
    /* Center logo image and size it beautifully */
    header img.brand-name-and-style-1,
    header img.brand-name-and-style-12 {
      width: 180px !important;
      height: auto !important;
      display: block !important;
      margin: 0 auto !important;
      object-fit: contain !important;
      object-position: center !important;
      position: static !important;
    }
    
    /* 3. Centered Navigation Row */
    header .link,
    header .frame-wrapper3 {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      max-width: 1200px !important;
      margin: 0 auto !important;
      height: auto !important;
      position: static !important;
    }
    
    header .link2,
    header .header-nav-parent {
      display: flex !important;
      flex-direction: row !important;
      justify-content: center !important;
      align-items: center !important;
      gap: 32px !important; /* Elegant spacing between nav links */
      width: 100% !important;
      height: auto !important;
      position: static !important;
      border-top: 1px solid #f2f2f2 !important;
      padding-top: 15px !important;
    }
    
    /* Normalize link wrapper divs */
    header .header-nav,
    header .header-nav7,
    header .dropdown {
      width: auto !important;
      height: auto !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      position: relative !important;
    }
    
    /* 4. Link Styling (Black, Kalnia font, uppercase) */
    header a.home,
    header a.home2,
    header a.home3,
    header a.home7,
    header a.home9,
    header .dropdown div.home,
    header .dropdown div.home2,
    header .dropdown div.home7 {
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 12px !important;
      text-transform: uppercase !important;
      color: #08201a !important;
      font-weight: 500 !important;
      letter-spacing: 0.04em !important;
      text-decoration: none !important;
      opacity: 0.85 !important;
      transition: opacity 0.2s ease, color 0.2s ease !important;
    }
    
    header a.home:hover,
    header a.home2:hover,
    header a.home3:hover,
    header a.home7:hover,
    header a.home9:hover,
    header .dropdown:hover div.home,
    header .dropdown:hover div.home2,
    header .dropdown:hover div.home7 {
      opacity: 1 !important;
      color: #b3a66c !important;
    }
    
    /* Style Collections dropdown down caret */
    header .dropdown::after {
      color: #08201a !important;
      opacity: 0.85 !important;
      margin-left: 6px !important;
      font-size: 9px !important;
    }
  }
"""

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        
        # We will inject the HEADER_FIX_CSS inside the <style> block, right before </style><body>
        start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
        end_marker = '</style><body>'
        
        si = content.find(start_marker)
        ei = content.find(end_marker)
        
        if si != -1 and ei != -1:
            new_content = content[:si] + HEADER_FIX_CSS + content[ei:]
        else:
            idx = content.find('</style><body>')
            if idx != -1:
                new_content = content[:idx] + HEADER_FIX_CSS + content[idx:]
            else:
                new_content = content
                print(f"Warning: </style><body> not found in {page}!")

        open(page, 'w', encoding='utf-8').write(new_content)
        print(f"Successfully updated desktop header layout in: {page}")
    else:
        print(f"File not found: {page}")
