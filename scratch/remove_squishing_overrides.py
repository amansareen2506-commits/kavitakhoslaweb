import os
import re

# 1. Update index.html
html_path = 'index.html'
if os.path.exists(html_path):
    content = open(html_path, encoding='utf-8').read()
    
    # We will remove the centering override CSS block
    pattern = r'/\* Footer columns centering override for desktop \*/\s*@media screen and \(min-width: 769px\) \{\s*body \.homepage \.frame-parent18 \.frame-parent19 \{\s*display: flex !important;\s*width: max-content !important;\s*max-width: 100% !important;\s*margin: 0 auto !important;\s*gap: 80px !important;\s*padding-left: 75px !important;\s*\}\s*body \.homepage \.frame-parent18 \.frame-parent19 \.about-parent \{\s*flex: 0 0 300px !important;\s*max-width: 300px !important;\s*margin: 0 !important;\s*\}\s*\}'
    
    content = re.sub(pattern, '', content)
    
    # Let's do a fallback replace just in case the spacing is slightly different
    old_str = """/* Footer columns centering override for desktop */
@media screen and (min-width: 769px) {
  body .homepage .frame-parent18 .frame-parent19 {
    display: flex !important;
    width: max-content !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    gap: 80px !important;
    padding-left: 75px !important;
  }
  body .homepage .frame-parent18 .frame-parent19 .about-parent {
    flex: 0 0 300px !important;
    max-width: 300px !important;
    margin: 0 !important;
  }
}"""
    content = content.replace(old_str, "")
    
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Successfully removed footer columns squishing override from index.html.")

# 2. Update about-us/about-us.html
about_path = 'about-us/about-us.html'
if os.path.exists(about_path):
    content = open(about_path, encoding='utf-8').read()
    
    pattern = r'/\* Footer columns centering override for desktop \*/\s*@media screen and \(min-width: 769px\) \{\s*body \.about-us13 \.frame-parent30 \.frame-parent31 \{\s*display: flex !important;\s*width: max-content !important;\s*max-width: 100% !important;\s*margin: 0 auto !important;\s*gap: 80px !important;\s*padding-left: 75px !important;\s*\}\s*body \.about-us13 \.frame-parent30 \.frame-parent31 \.about-group \{\s*flex: 0 0 300px !important;\s*max-width: 300px !important;\s*margin: 0 !important;\s*\}\s*\}'
    
    content = re.sub(pattern, '', content)
    
    old_str_about = """/* Footer columns centering override for desktop */
@media screen and (min-width: 769px) {
  body .about-us13 .frame-parent30 .frame-parent31 {
    display: flex !important;
    width: max-content !important;
    max-width: 100% !important;
    margin: 0 auto !important;
    gap: 80px !important;
    padding-left: 75px !important;
  }
  body .about-us13 .frame-parent30 .frame-parent31 .about-group {
    flex: 0 0 300px !important;
    max-width: 300px !important;
    margin: 0 !important;
  }
}"""
    content = content.replace(old_str_about, "")
    
    open(about_path, 'w', encoding='utf-8').write(content)
    print("Successfully removed footer columns squishing override from about-us.html.")
