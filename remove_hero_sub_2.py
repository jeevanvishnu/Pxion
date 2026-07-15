import os
import re

directory = r'c:\Users\jeeva\OneDrive\Documents\Bebright'

target_style = 'style="margin-bottom: 36px; max-width: 720px; margin-left: auto; margin-right: auto;"'

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        enc = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
        enc = 'cp1252'

    # Find the hero section paragraphs
    match = re.search(r'(class="hero-title"[^>]*>.*?</h1>\s*)(<p\s+class="hero-sub"[^>]*>.*?</p>\s*)(<p[^>]*>.*?</p>)', content, re.DOTALL | re.IGNORECASE)
    if match:
        before_paras = match.group(1)
        para1 = match.group(2)
        para2 = match.group(3)
        
        # Extract content of para2
        p2_match = re.match(r'<p[^>]*>(.*?)</p>', para2, re.DOTALL | re.IGNORECASE)
        if p2_match:
            p2_content = p2_match.group(1)
            
            # Clean up the typo "centerswhere" or similar
            p2_content = re.sub(r'centers[^\w\s]?where', 'centers where', p2_content)
            
            new_para2 = f'<p class="hero-sub" {target_style}>{p2_content}</p>'
            
            # Replace the old paragraphs with the new one
            new_content = content.replace(para1 + para2, new_para2)
            
            with open(filepath, 'w', encoding=enc) as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Done!")
