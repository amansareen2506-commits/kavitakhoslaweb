import os
import re

# 1. Update index.html: Center two-row desktop header with PLUM text logo and bottom border
index_path = 'index.html'
if os.path.exists(index_path):
    content = open(index_path, encoding='utf-8').read()
    
    # We will replace the centered header overrides block with the plum & border version
    HEADER_FIX_CSS_INDEX = """
  /* === Centered Two-Row Desktop Header Overrides === */
  @media screen and (min-width: 769px) {
    /* 1. Header wrapper: column flex, white background, centered */
    body header.frame-parent {
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
      border-bottom: 1px solid #f2f2f2 !important; /* Separator line below nav bar */
    }
    
    /* Hide the mobile checkbox toggle on desktop */
    .menu-toggle-chk,
    .hamburger-btn {
      display: none !important;
    }
    
    /* 2. Centered Logo Row */
    body header .kavita-khosla-parent {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      margin: 0 0 12px 0 !important;
      position: static !important;
      height: auto !important;
      float: none !important;
    }
    
    /* Show and style the text logo in the center in PLUM color */
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
    }
    
    /* Hide the image logo completely */
    body header img.brand-name-and-style-1 {
      display: none !important;
    }
    
    /* 3. Centered Navigation Row */
    body header .link {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
      max-width: 1200px !important;
      margin: 0 auto !important;
      height: auto !important;
      position: static !important;
    }
    
    body header .link2 {
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
    body header .dropdown div.home,
    body header .dropdown div.home2 {
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
    body header .dropdown:hover div.home,
    body header .dropdown:hover div.home2 {
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

    # We find and replace the Centered header override block inside style
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    
    si = content.find(start_marker)
    ei = content.find(end_marker)
    
    if si != -1 and ei != -1:
        new_content = content[:si] + HEADER_FIX_CSS_INDEX + content[ei:]
        open(index_path, 'w', encoding='utf-8').write(new_content)
        print("Updated homepage header with Centered Plum Text & Bottom Border Overrides.")
    else:
        # If block is missing (e.g. because we deleted it or changed it), let's inject it before </style><body>
        idx = content.find('</style><body>')
        if idx != -1:
            new_content = content[:idx] + HEADER_FIX_CSS_INDEX + content[idx:]
            open(index_path, 'w', encoding='utf-8').write(new_content)
            print("Injected Centered Plum Text & Bottom Border Overrides into index.html.")
        else:
            print("Error: </style><body> not found in index.html!")

# 2. Update about-us.html: Revert completely to the default Locofy single-row layout
about_path = 'about-us/about-us.html'
if os.path.exists(about_path):
    content = open(about_path, encoding='utf-8').read()
    
    # Removecentered overrides
    pattern = r'\s*/\* === Centered Two-Row Desktop Header Overrides === \*/\s*@media screen and \(min-width: 769px\) \{.*?\}\s*\}'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Fallback string replace
    start_marker = '  /* === Centered Two-Row Desktop Header Overrides === */'
    end_marker = '</style><body>'
    si = content.find(start_marker)
    ei = content.find(end_marker)
    if si != -1 and ei != -1:
        content = content[:si] + content[ei:]
        
    # Revert HTML texts back to default
    content = content.replace('Kavita Khosla', 'KAVITA KHOSLA')
    content = content.replace('>HOME</a>', '>Home</a>')
    
    open(about_path, 'w', encoding='utf-8').write(content)
    print("Reverted about-us.html header to the default single-row layout.")
