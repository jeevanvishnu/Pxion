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

    # Pattern to find hero-sub followed by hero-desc
    pattern = re.compile(
        r'<p\s+class="hero-sub"[^>]*>.*?</p>\s*(.*?)\s*<p\s+class="hero-desc"[^>]*>(.*?)</p>',
        re.DOTALL | re.IGNORECASE
    )

    def replace_func(match):
        between = match.group(1)
        desc_content = match.group(2)
        
        # Clean up the typo "centerswhere" or similar
        desc_content = re.sub(r'centers[^\w\s]?where', 'centers where', desc_content)
        
        return f'{between}<p class="hero-sub" {target_style}>{desc_content}</p>'

    new_content, count = pattern.subn(replace_func, content)
    
    if count > 0:
        with open(filepath, 'w', encoding=enc) as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Done!")
