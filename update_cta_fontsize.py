import os
import glob

path = 'c:/Users/jeeva/OneDrive/Documents/Bebright'
files = glob.glob(os.path.join(path, '*.html'))

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    updated = False
    
    old_h2 = '<h2 style="color: #ffffff; font-size: clamp(28px, 4vw, 42px);'
    new_h2 = '<h2 style="color: #ffffff; font-size: clamp(20px, 2.8vw, 30px);'
    
    old_div = '<div class="container" style="position: relative; z-index: 2; max-width: 800px;">'
    new_div = '<div class="container" style="position: relative; z-index: 2; max-width: 1000px;">'
    
    if old_h2 in content:
        content = content.replace(old_h2, new_h2)
        updated = True
        
    if old_div in content:
        content = content.replace(old_div, new_div)
        updated = True
        
    if updated:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated font size in {os.path.basename(f)}")
