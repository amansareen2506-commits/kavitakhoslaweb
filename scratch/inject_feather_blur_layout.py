import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# Define the HTML blocks to inject
col1_addition = """            <div class=rectangle-parent14>
              <img class=frame-child57 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-small-1.png?v=2030">

              <img class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-small-2.png?v=2030">
            </div>
          </div>"""

col2_addition = """            <div class=rectangle-parent17>
              <img class=frame-child56 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-small-3.png?v=2030">
            </div>
          </div>"""

# Targets for injection
target_col1_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-84@2x.d0389893.png?v=2030>
            </div>
          </div>"""

target_col2_end = """              <img class=frame-child51 loading=lazy alt src=/Rectangle-83@2x.58e9e4e6.png?v=2030>
            </div>
          </div>"""

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
print("Updated HTML with feather-blurred-padded images.")
