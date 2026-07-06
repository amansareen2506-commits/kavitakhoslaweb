import os

pages = [
    'index.html',
    'about-us/about-us.html',
    'contact-us/contact-us.html',
    'lab-grown-diamonds/lab-grown-diamonds.html',
    'malana-collection/malana-collection.html',
    'natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html',
    'onzee-collection/onzee-collection.html',
    'our-policies/our-policies.html',
    'pierre-collection/pierre-collection.html',
    'pierre-collection/pendants.html',
    'pierre-collection/necklaces.html',
    'pierre-collection/solitaire-pendants.html',
    'thia-collection/thia-collection.html',
]

FOOTER_FIX_CSS = """
  /* === Clean and tidy footer navigation overrides === */
  .footer-nav, .footer-nav2 {
    width: auto !important;
    height: auto !important;
    display: block !important;
    position: static !important;
  }
  .footer-nav-parent {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 10px !important;
    width: 100% !important;
  }
  .footer-nav a, .footer-nav2 a,
  .about-us, .about-us2, .about-us3, .about-us4, .about-us5, .about-us6, .about-us7, .about-us9, .about-us10, .about-us11, .about-us12 {
    font-size: 11px !important;
    line-height: 1.4 !important;
    color: #ffffff !important;
    opacity: 0.7 !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    display: inline-block !important;
    position: static !important;
    width: auto !important;
    height: auto !important;
    text-align: left !important;
    transition: opacity 0.2s ease, color 0.2s ease !important;
  }
  .footer-nav a:hover, .footer-nav2 a:hover,
  .about-us:hover, .about-us2:hover, .about-us3:hover, .about-us4:hover, .about-us5:hover, .about-us6:hover, .about-us7:hover, .about-us9:hover, .about-us10:hover, .about-us11:hover, .about-us12:hover {
    opacity: 1 !important;
    color: #b3a66c !important;
  }
"""

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        
        # We will inject the FOOTER_FIX_CSS inside the <style> block, right before </style><body>
        # (This is where our other overrides are injected, so it is extremely safe)
        start_marker = '  /* === Clean and tidy footer navigation overrides === */'
        end_marker = '</style><body>'
        
        si = content.find(start_marker)
        ei = content.find(end_marker)
        
        if si != -1 and ei != -1:
            new_content = content[:si] + FOOTER_FIX_CSS + content[ei:]
        else:
            idx = content.find('</style><body>')
            if idx != -1:
                new_content = content[:idx] + FOOTER_FIX_CSS + content[idx:]
            else:
                new_content = content
                print(f"Warning: </style><body> not found in {page}!")

        open(page, 'w', encoding='utf-8').write(new_content)
        print(f"Successfully updated footer layout in: {page}")
    else:
        print(f"File not found: {page}")
