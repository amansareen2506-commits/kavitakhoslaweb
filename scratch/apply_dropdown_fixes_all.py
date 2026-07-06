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

# Definitive visibility CSS override (pure white color)
FIX_CSS = """
  /* === Fix: override compiled CSS that hides nested dropdown === */
  /* 1. Parent collection containers have overflow-x:hidden clipping the flyout */
  .pierre-collection, .thia-collection, .malana-collection, .onzee-collection, .homepage, .about-us13, .contact-us, .lab-grown-diamonds, .natural-diamond-solitaire, .our-policies {
    overflow-x: visible !important;
    overflow: visible !important;
  }
  /* 2. Ensure dropdown-content doesn't clip nested flyout */
  .dropdown-content {
    overflow: visible !important;
  }
  /* 3. Ensure frame-wrapper and header don't clip */
  .frame-wrapper2, .frame-wrapper4, .frame-wrapper,
  .header-nav-group, .header-nav-container, .header-nav-parent,
  .frame-header, .frame-parent, .frame-parent9,
  header {
    overflow: visible !important;
  }

  /* 4. Force ALL first-level and second-level dropdown links to be pure white color */
  .dropdown-content a,
  .dropdown-content div a,
  .dropdown-content div div a,
  .dropdown-content .nested-dropdown a,
  .dropdown-content .nested-dropdown-content a,
  .nested-dropdown-content a {
    color: #ffffff !important;
    background-color: transparent !important;
    font-size: 12px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  .dropdown-content a:hover,
  .dropdown-content div a:hover,
  .dropdown-content .nested-dropdown-content a:hover,
  .nested-dropdown-content a:hover {
    background-color: #0c2921 !important;
    color: #b3a66c !important;
  }
"""

# Let's also append a duplicate style block at the end of the body for absolute priority
BODY_STYLE_BLOCK = """
<!-- Body level style block to override any dynamic styles or late-loading compiled CSS -->
<style>
  .dropdown-content a,
  .dropdown-content div a,
  .dropdown-content div div a,
  .dropdown-content .nested-dropdown a,
  .dropdown-content .nested-dropdown-content a,
  .nested-dropdown-content a {
    color: #ffffff !important;
    background-color: transparent !important;
    font-size: 12px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  .dropdown-content a:hover,
  .dropdown-content div a:hover,
  .dropdown-content .nested-dropdown-content a:hover,
  .nested-dropdown-content a:hover {
    background-color: #0c2921 !important;
    color: #b3a66c !important;
  }
</style>
"""

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        start_marker = '  /* === Fix: override compiled CSS that hides nested dropdown === */'
        end_marker = '</style><body>'
        
        si = content.find(start_marker)
        ei = content.find(end_marker)
        
        if si != -1 and ei != -1:
            new_content = content[:si] + FIX_CSS + content[ei:]
        else:
            idx = content.find('</style><body>')
            if idx != -1:
                new_content = content[:idx] + FIX_CSS + content[idx:]
            else:
                new_content = content

        # Append or replace the BODY_STYLE_BLOCK right before </html>
        if "<!-- Body level style block" not in new_content:
            html_end = new_content.rfind('</html>')
            if html_end != -1:
                new_content = new_content[:html_end] + BODY_STYLE_BLOCK + new_content[html_end:]
        else:
            body_start = new_content.find("<!-- Body level style block")
            body_end = new_content.find("</style>", body_start) + len("</style>")
            if body_start != -1 and body_end != -1:
                new_content = new_content[:body_start] + BODY_STYLE_BLOCK + new_content[body_end:]

        open(page, 'w', encoding='utf-8').write(new_content)
        print(f'Successfully updated: {page}')
    else:
        print(f'File not found: {page}')
