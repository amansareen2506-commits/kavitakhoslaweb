import os
import re

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
    gap: 12px !important;
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
    font-weight: 500 !important;
  }
  .footer-nav a:hover, .footer-nav2 a:hover,
  .about-us:hover, .about-us2:hover, .about-us3:hover, .about-us4:hover, .about-us5:hover, .about-us6:hover, .about-us7:hover, .about-us9:hover, .about-us10:hover, .about-us11:hover, .about-us12:hover {
    opacity: 1 !important;
    color: #b3a66c !important;
  }
  
  /* Footer copyright and social media links styled exactly like the screenshot */
  .kavita-khosla2 {
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    opacity: 0.7 !important;
    width: auto !important;
    max-width: 60% !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    white-space: nowrap !important;
    display: inline-block !important;
    position: static !important;
  }
  .instagram, .instagram2, .instagram3 {
    font-size: 11px !important;
    color: #ffffff !important;
    opacity: 0.8 !important;
    text-decoration: none !important;
    white-space: nowrap !important;
    display: inline-block !important;
    position: static !important;
    width: auto !important;
    height: auto !important;
    font-weight: 600 !important;
    transition: opacity 0.2s ease, color 0.2s ease !important;
  }
  .instagram:hover, .instagram2:hover, .instagram3:hover {
    opacity: 1 !important;
    color: #b3a66c !important;
  }
  .social-media-handle-nav-parent {
    gap: 24px !important;
  }
"""

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        
        # 1. Update HTML content of collections: replace the two natural diamonds and solitaires links with one merged link
        old_diamonds_solitaire_block = """                  <div class=footer-nav2>
                  <a class=about-us5 href=/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html>NATURAL DIAMONDS</a>
                </div>
                  <div class=footer-nav2>
                  <a class=about-us6 href=/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html>SOLITAIRES</a>
                </div>"""
        
        old_diamonds_solitaire_block_alt = """                  <div class=footer-nav2>
                  <a class=about-us5 href=/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html>NATURAL DIAMONDS</a>
                </div>
                  <div class=footer-nav2>
                  <a class=about-us6 href=/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html>SOLITAIRES</a>
                </div>"""
        
        new_diamonds_solitaire_block = """                  <div class=footer-nav2>
                  <a class=about-us5 href=/natural-solitaire-and-diamonds/natural-solitaire-and-diamonds.html>NATURAL DIAMOND AND SOLITAIRES</a>
                </div>"""
        
        if old_diamonds_solitaire_block in content:
            content = content.replace(old_diamonds_solitaire_block, new_diamonds_solitaire_block)
        elif old_diamonds_solitaire_block_alt in content:
            content = content.replace(old_diamonds_solitaire_block_alt, new_diamonds_solitaire_block)
        else:
            # Let's do a regex replacement for robustness
            content = re.sub(
                r'<\s*div\s+class\s*=\s*footer-nav2\s*>\s*<\s*a\s+class\s*=\s*about-us5[^>]*>NATURAL DIAMONDS</a>\s*</div>\s*<\s*div\s+class\s*=\s*footer-nav2\s*>\s*<\s*a\s+class\s*=\s*about-us6[^>]*>SOLITAIRES</a>\s*</div>',
                new_diamonds_solitaire_block,
                content,
                flags=re.IGNORECASE
            )
            
        # 2. Update GST text to be all uppercase
        content = re.sub(
            r'©\s*2026\s*\|\s*gst\s*nO\.\s*06AJAPK5493J1Z0',
            '© 2026 | GST NO. 06AJAPK5493J1Z0',
            content,
            flags=re.IGNORECASE
        )

        # 3. Inject CSS styles
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
        print(f"Successfully updated footer contents and CSS in: {page}")
    else:
        print(f"File not found: {page}")
