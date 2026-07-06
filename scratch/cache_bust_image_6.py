import os

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

old_str = "src=/image-6@2x.8c88ef1c.png?v=2030"
new_str = "src=/image-6@2x.8c88ef1c.png?v=2035"

if old_str in content:
    content = content.replace(old_str, new_str)
    open(html_path, 'w', encoding='utf-8').write(content)
    print("Updated image-6 cache-busting version token to v=2035 in index.html.")
else:
    # Try matching with quotes just in case
    old_str_quotes = 'src="/image-6@2x.8c88ef1c.png?v=2030"'
    new_str_quotes = 'src="/image-6@2x.8c88ef1c.png?v=2035"'
    if old_str_quotes in content:
        content = content.replace(old_str_quotes, new_str_quotes)
        open(html_path, 'w', encoding='utf-8').write(content)
        print("Updated image-6 cache-busting version token (with quotes) to v=2035.")
    else:
        print("Could not find image-6 tag in index.html!")
