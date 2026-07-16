import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update style.css to style.css?v=2 to bust cache
    new_content = content.replace('<link href="style.css" rel="stylesheet"/>', '<link href="style.css?v=2" rel="stylesheet"/>')
    new_content = new_content.replace('<link rel="stylesheet" href="style.css">', '<link rel="stylesheet" href="style.css?v=2">')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated cache buster in {file}")
print("Cache buster applied.")
