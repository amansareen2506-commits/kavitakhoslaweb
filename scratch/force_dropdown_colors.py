import os

pages = [
    'pierre-collection/pierre-collection.html',
    'pierre-collection/pendants.html',
    'pierre-collection/necklaces.html',
    'pierre-collection/solitaire-pendants.html',
]

# Definitive visibility CSS override
FIX_CSS = """
  /* === Fix: override compiled CSS that hides nested dropdown === */
  /* 1. Compiled CSS sets ALL `a` tags to dark color — override for nested dropdown */
  .nested-dropdown-content a,
  .dropdown-content .nested-dropdown-content a,
  .pierre-collection .nested-dropdown-content a,
  .frame-header .nested-dropdown-content a {
    color: #ffffffb8 !important;
    background-color: transparent !important;
    font-size: 12px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  .nested-dropdown-content a:hover,
  .dropdown-content .nested-dropdown-content a:hover {
    background-color: #0c2921 !important;
    color: #b3a66c !important;
  }
  /* 2. Parent .pierre-collection has overflow-x:hidden clipping the flyout */
  .pierre-collection {
    overflow-x: visible !important;
    overflow: visible !important;
  }
  /* 3. Ensure dropdown-content doesn't clip nested flyout */
  .dropdown-content {
    overflow: visible !important;
  }
  /* 4. Ensure frame-wrapper2 and header don't clip */
  .frame-wrapper2,
  .header-nav-group,
  .frame-header,
  header {
    overflow: visible !important;
  }

  /* 5. Force ALL first-level and second-level dropdown links to be light off-white color */
  .dropdown-content a,
  .dropdown-content div a,
  .dropdown-content div div a,
  .dropdown-content .nested-dropdown a,
  .dropdown-content .nested-dropdown-content a,
  .nested-dropdown-content a {
    color: #ffffffb8 !important;
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

for page in pages:
    if os.path.exists(page):
        content = open(page, encoding='utf-8').read()
        # Find the start of our previous fix block
        start_marker = '  /* === Fix: override compiled CSS that hides nested dropdown === */'
        end_marker = '</style><body>'
        
        si = content.find(start_marker)
        ei = content.find(end_marker)
        
        if si != -1 and ei != -1:
            # Replace the entire previous fix block with the new one
            new_content = content[:si] + FIX_CSS + content[ei:]
            open(page, 'w', encoding='utf-8').write(new_content)
            print(f'Successfully updated: {page}')
        else:
            # If start marker is not found, try to inject it before </style><body>
            idx = content.find('</style><body>')
            if idx != -1:
                new_content = content[:idx] + FIX_CSS + content[idx:]
                open(page, 'w', encoding='utf-8').write(new_content)
                print(f'Injected new fix block: {page}')
            else:
                print(f'Could not find style block to inject in: {page}')
    else:
        print(f'File not found: {page}')
