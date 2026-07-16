import os
import glob
import re

html_files = glob.glob('*.html')
# Exclude indoor-led-screen.html as it is already updated
if 'indoor-led-screen.html' in html_files:
    html_files.remove('indoor-led-screen.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<div class="gallery-grid">' not in content:
        continue

    # Extract the title from the h2 before it
    title_match = re.search(r'<h2 class="section-title">(.*?)<span.*?>(.*?)</span></h2>', content)
    title_text = "LED Screen"
    if title_match:
        # e.g. "Outdoor LED Screen " + "References" -> we just want "Outdoor LED Screen"
        title_text = title_match.group(1).strip()
    
    # We want to replace the whole <div class="gallery-grid"> block up to its closing </div>
    # The structure is:
    # <div class="gallery-grid">
    #   <!-- Gallery Image X -->
    #   <div class="gallery-item reveal...">
    #     <div class="gallery-image">
    #       <img alt="..." src="..."/>
    #     </div>
    #   </div>
    #   ...
    # </div>
    
    # Let's just do a regex replace for the gallery grid items
    
    # 1. Change gallery-grid to bento-gallery
    new_content = content.replace('<div class="gallery-grid">', '<div class="bento-gallery">')
    
    # 2. Change gallery-item to bento-item
    new_content = new_content.replace('gallery-item', 'bento-item')
    
    # 3. We need to replace the <div class="gallery-image"> \n <img ...> \n </div>
    # with: <img ...> \n <div class="bento-overlay"></div> \n <h3 class="bento-title">Title</h3>
    
    pattern = r'<div class="gallery-image">\s*(<img.*?>)\s*</div>'
    replacement = r'\1\n<div class="bento-overlay"></div>\n<h3 class="bento-title">' + title_text + r'</h3>'
    
    new_content = re.sub(pattern, replacement, new_content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

print("Done updating galleries via regex.")
