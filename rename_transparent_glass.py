import os
import re

directory = r'c:\Users\jeeva\OneDrive\Documents\Bebright'

# 1. Rename directory if exists
old_dir = os.path.join(directory, 'assetss', 'innovative led screens', 'Transparent Glass LED Screen')
new_dir = os.path.join(directory, 'assetss', 'innovative led screens', 'Glass Transparent Display Solutions')

if os.path.exists(old_dir):
    os.rename(old_dir, new_dir)
    print(f"Renamed directory: {old_dir} -> {new_dir}")

# 2. Rename HTML file if exists
old_html = os.path.join(directory, 'transparent-glass-led.html')
new_html = os.path.join(directory, 'glass-transparent-display-solutions.html')

if os.path.exists(old_html):
    os.rename(old_html, new_html)
    print(f"Renamed file: {old_html} -> {new_html}")

# 3. Process all HTML files
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    if filename == 'transparent-glass-led.html':
        continue # Processed or renamed
    
    # If the file was renamed, we should open the new file
    filepath = os.path.join(directory, filename)
    if filename == 'glass-transparent-display-solutions.html':
        pass
    elif not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # Replacements
    content = content.replace('transparent-glass-led.html', 'glass-transparent-display-solutions.html')
    content = content.replace('assetss/innovative led screens/Transparent Glass LED Screen', 'assetss/innovative led screens/Glass Transparent Display Solutions')
    
    # Regex replacements for text (handling newlines)
    # 1. "Transparent Glass LED Screen" -> "Glass Transparent Display Solutions"
    content = re.sub(r'Transparent\s+Glass\s+LED\s+Screen', 'Glass Transparent Display Solutions', content)
    
    # 2. "Transparent Glass LED" -> "Glass Transparent Display Solutions" (where it wasn't already caught by above)
    content = re.sub(r'Transparent\s+Glass\s+LED', 'Glass Transparent Display Solutions', content)
    
    # 3. "Transparent Glass\n\s*LED Screen"
    content = re.sub(r'Transparent\s+Glass\s*\n\s*LED\s+Screen', 'Glass Transparent Display Solutions', content)
    
    # 4. "Transparent Glass\n\s*LED"
    content = re.sub(r'Transparent\s+Glass\s*\n\s*LED', 'Glass Transparent Display Solutions', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated content in {filename}")

# Process the new_html if it was renamed
if os.path.exists(new_html):
    with open(new_html, 'r', encoding='utf-8') as f:
        content = f.read()
    original_content = content
    
    content = content.replace('transparent-glass-led.html', 'glass-transparent-display-solutions.html')
    content = content.replace('assetss/innovative led screens/Transparent Glass LED Screen', 'assetss/innovative led screens/Glass Transparent Display Solutions')
    content = re.sub(r'Transparent\s+Glass\s+LED\s+Screen', 'Glass Transparent Display Solutions', content)
    content = re.sub(r'Transparent\s+Glass\s+LED', 'Glass Transparent Display Solutions', content)
    content = re.sub(r'Transparent\s+Glass\s*\n\s*LED\s+Screen', 'Glass Transparent Display Solutions', content)
    content = re.sub(r'Transparent\s+Glass\s*\n\s*LED', 'Glass Transparent Display Solutions', content)
    
    if content != original_content:
        with open(new_html, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated content in glass-transparent-display-solutions.html")

print("Done.")
