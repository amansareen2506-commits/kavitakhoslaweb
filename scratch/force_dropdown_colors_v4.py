import os

pages = [
    'pierre-collection/pierre-collection.html',
    'pierre-collection/pendants.html',
    'pierre-collection/necklaces.html',
    'pierre-collection/solitaire-pendants.html',
]

# Definitive visibility CSS override (pure white color)
FIX_CSS = """
  /* === Fix: override compiled CSS that hides nested dropdown === */
  /* 1. Parent .pierre-collection has overflow-x:hidden clipping the flyout */
  .pierre-collection {
    overflow-x: visible !important;
    overflow: visible !important;
  }
  /* 2. Ensure dropdown-content doesn't clip nested flyout */
  .dropdown-content {
    overflow: visible !important;
  }
  /* 3. Ensure frame-wrapper2 and header don't clip */
  .frame-wrapper2,
  .header-nav-group,
  .frame-header,
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

        # Now let's check if the BODY_STYLE_BLOCK is already in the file
        if "<!-- Body level style block" not in new_content:
            # Append it right before </html>
            html_end = new_content.rfind('</html>')
            if html_end != -1:
                new_content = new_content[:html_end] + BODY_STYLE_BLOCK + new_content[html_end:]
        else:
            # Replace the existing body style block
            body_start = new_content.find("<!-- Body level style block")
            body_end = new_content.find("</style>", body_start) + len("</style>")
            if body_start != -1 and body_end != -1:
                new_content = new_content[:body_start] + BODY_STYLE_BLOCK + new_content[body_end:]

        open(page, 'w', encoding='utf-8').write(new_content)
        print(f'Successfully updated: {page}')
    else:
        print(f'File not found: {page}')
