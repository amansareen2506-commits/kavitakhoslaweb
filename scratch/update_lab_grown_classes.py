import os

html_path = 'lab-grown-diamonds/lab-grown-diamonds.html'
content = open(html_path, encoding='utf-8').read()

# Let's replace:
# class=frame-child51 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030"
# with:
# class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030"
content = content.replace(
    'class=frame-child51 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030"',
    'class=frame-child49 loading=lazy alt="Lab Grown" src="/lab-grown-diamonds-images/lab-grown-2.png?v=2030"'
)

open(html_path, 'w', encoding='utf-8').write(content)
print("Updated HTML image classes for matching sizes successfully.")
