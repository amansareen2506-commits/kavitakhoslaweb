import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# Let's revert the previous HTML additions first to start clean
# Column 1 original end target
target_col1_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
            </div>
          </div>"""

# Column 2 original end target
target_col2_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
            </div>
          </div>"""

# Let's read the file again to find where they are
# We will do a robust regex replace to return to original state before appending
import re
# Remove any custom lab-grown divs we added in our last step
content = re.sub(r'\s*<div class=rectangle-parent14>\s*<img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png\?v=2030">.*?</div>\s*</div>', '\n          </div>', content, flags=re.DOTALL)
content = re.sub(r'\s*<div class=rectangle-parent17>\s*<img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png\?v=2030">.*?</div>\s*</div>', '\n          </div>', content, flags=re.DOTALL)

# Let's verify by checking if the source matches the original structure
# Let's write the fresh balanced layout with height: 384px (classes frame-child57, frame-child51, frame-child56)
# Column 1 (Left) will get lab-grown-1 and lab-grown-2
col1_addition = """            <div class=rectangle-parent14>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-1.png?v=2030">

              <img class=frame-child51 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030">
            </div>
          </div>"""

# Column 2 (Right) will get lab-grown-3
col2_addition = """            <div class=rectangle-parent17>
              <img class=frame-child56 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-3.png?v=2030">
            </div>
          </div>"""

# Let's replace the column endings
idx1 = content.find(target_col1_end)
if idx1 != -1:
    content = content[:idx1 + len(target_col1_end) - 6] + col1_addition + content[idx1 + len(target_col1_end):]
    print("Injected Column 1.")
else:
    print("Could not find Column 1 end!")

idx2 = content.find(target_col2_end)
if idx2 != -1:
    content = content[:idx2 + len(target_col2_end) - 6] + col2_addition + content[idx2 + len(target_col2_end):]
    print("Injected Column 2.")
else:
    print("Could not find Column 2 end!")

open(html_path, 'w', encoding='utf-8').write(content)
print("File successfully updated with compact balanced layout!")
