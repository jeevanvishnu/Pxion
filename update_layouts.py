import os

files_to_update = [
    'rental.html',
    'installation.html',
    'indoor.html',
    'outdoor.html',
    'av-solutions.html'
]

for file_name in files_to_update:
    if not os.path.exists(file_name):
        print(f"Skipping {file_name}, does not exist")
        continue
    
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace plain <div class="about-split-layout">
    content = content.replace('<div class="about-split-layout">', '<div class="about-split-layout" style="align-items: stretch;">')
    
    # 2. Replace align-items: center in existing style
    content = content.replace('style="align-items: center; flex-direction: row-reverse;"', 'style="align-items: stretch; flex-direction: row-reverse;"')
    
    # 3. Replace aspect-ratio: 1/1; with height: 100%;
    content = content.replace('aspect-ratio: 1/1;', 'height: 100%;')
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated files successfully.")
