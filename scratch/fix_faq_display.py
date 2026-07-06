import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

ACCORDION_CSS_OLD = """  /* FAQ Accordion Styling */
  .we-specialize-exclusively, .we-specialize-exclusively2 {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.3s ease, padding 0.3s ease;
    opacity: 0;
    margin-top: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }"""

ACCORDION_CSS_NEW = """  /* FAQ Accordion Styling */
  .we-specialize-exclusively, .we-specialize-exclusively2 {
    display: block !important;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.3s ease, padding 0.3s ease;
    opacity: 0;
    margin-top: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }"""

if ACCORDION_CSS_OLD in content:
    content = content.replace(ACCORDION_CSS_OLD, ACCORDION_CSS_NEW)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Successfully updated FAQ CSS with display: block !important.")
else:
    print("Could not find the old CSS block!")
