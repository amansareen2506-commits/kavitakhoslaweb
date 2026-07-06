import os

pages = [
    'pierre-collection/pierre-collection.html',
    'pierre-collection/pendants.html',
    'pierre-collection/necklaces.html',
    'pierre-collection/solitaire-pendants.html',
]

# Ultra-specific visibility CSS override to override any possible compiled CSS or browser styling
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

  /* 4. Ultra-high specificity overrides to force dropdown links to be visible and white/gold */
  html body div.pierre-collection header.frame-header div.frame-wrapper2 div.header-nav-group div.dropdown.header-nav7 div.dropdown-content a,
  html body div.pierre-collection header.frame-header div.frame-wrapper2 div.header-nav-group div.dropdown.header-nav7 div.dropdown-content div.nested-dropdown div.nested-dropdown-content a,
  .dropdown-content a,
  .nested-dropdown-content a {
    color: #ffffffb8 !important;
    background-color: transparent !important;
    font-size: 12px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  html body div.pierre-collection header.frame-header div.frame-wrapper2 div.header-nav-group div.dropdown.header-nav7 div.dropdown-content a:hover,
  html body div.pierre-collection header.frame-header div.frame-wrapper2 div.header-nav-group div.dropdown.header-nav7 div.dropdown-content div.nested-dropdown div.nested-dropdown-content a:hover,
  .dropdown-content a:hover,
  .nested-dropdown-content a:hover {
    background-color: #0c2921 !important;
    color: #b3a66c !important;
  }
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
            open(page, 'w', encoding='utf-8').write(new_content)
            print(f'Successfully updated: {page}')
        else:
            idx = content.find('</style><body>')
            if idx != -1:
                new_content = content[:idx] + FIX_CSS + content[idx:]
                open(page, 'w', encoding='utf-8').write(new_content)
                print(f'Injected new fix block: {page}')
            else:
                print(f'Could not find style block to inject in: {page}')
    else:
        print(f'File not found: {page}')
