import os
import re

pages = [
    'index.html',
    'about-us/about-us.html',
]

HEADER_FIX_CSS = """
  /* === Centered Two-Row Desktop Header Overrides === */
  @media screen and (min-width: 769px) {
    /* 1. Header wrapper: column flex, white background, centered */
    body header.frame-parent,
    body header.frame-header {
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
      border-bottom: none !important; /* Removed black line below nav bar */
    }
    
    /* Hide the mobile checkbox toggle on desktop */
    .menu-toggle-chk,
    .hamburger-btn {
      display: none !important;
    }
    
    /* 2. Centered Logo Row */
    body header .kavita-khosla-parent,
    body header .kavita-khosla-group {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      margin: 0 0 12px 0 !important;
      position: static !important;
      height: auto !important;
      float: none !important;
    }
    
    /* Show and style the text logo in the center in BLACK color */
    body header .kavita-khosla-parent .kavita-khosla,
    body header .kavita-khosla-group .kavita-khosla4 {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
      font-family: var(--font-kalnia), Kalnia, serif !important;
      font-size: 32px !important;
      color: #000000 !important; /* Black color */
      font-weight: 400 !important;
      text-transform: none !important; /* Preserve Title Case 'Kavita Khosla' */
      letter-spacing: 0.02em !important;
      text-align: center !important;
      width: auto !important;
      height: auto !important;
      position: static !important;
    }
    
    /* Hide the image logo completely */
    body header img.brand-name-and-style-1,
    body header img.brand-name-and-style-12 {
      display: none !important;
    }
    
    /* 3. Centered Navigation Row */
    body header .link,
    body header .frame-wrapper3 {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      max-width: 1200px !important;
      margin: 0 auto !important;
      height: auto !important;
      position: static !important;
    }
    
    body header .link2,
    body header .header-nav-parent {
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
    body header .header-nav,
    body header .header-nav7,
    body header .dropdown {
      width: auto !important;
      height: auto !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      position: relative !important;
    }
    
    /* 4. Link Styling (Black, Kalnia font, uppercase) */
    body header a.home,
    body header a.home2,
    body header a.home3,
    body header a.home7,
    body header a.home9,
    body header .dropdown div.home,
    body header .dropdown div.home2,
    body header .dropdown div.home7 {
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
    
    body header a.home:hover,
    body header a.home2:hover,
    body header a.home3:hover,
    body header a.home7:hover,
    body header a.home9:hover,
    body header .dropdown:hover div.home,
    body header .dropdown:hover div.home2,
    body header .dropdown:hover div.home7 {
      opacity: 1 !important;
      color: #b3a66c !important;
    }
    
    /* Style Collections dropdown down caret */
    body header .dropdown::after {
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
        
        # 1. Update text logo to Title Case 'Kavita Khosla'
        content = content.replace('KAVITA KHOSLA', 'Kavita Khosla')
        
        # 2. Update Home link to all-caps HOME
        content = content.replace('>Home</a>', '>HOME</a>')
        
        # 3. Inject CSS styles right before </style><body>
        idx = content.find('</style><body>')
        if idx != -1:
            content = content[:idx] + HEADER_FIX_CSS + content[idx:]
            print(f"Successfully injected header overrides into {page}.")
        else:
            print(f"Error: </style><body> not found in {page}!")
            
        open(page, 'w', encoding='utf-8').write(content)
    else:
        print(f"File not found: {page}")
