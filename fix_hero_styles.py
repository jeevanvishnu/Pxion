import os
import re

directory = r'c:\Users\jeeva\OneDrive\Documents\Bebright'

h1_pattern = re.compile(r'<h1\b([^>]*\bclass=[\'"][^\'"]*\b(?:hero-title|gallery-hero-title)\b[^\'"]*[\'"][^>]*)>', re.IGNORECASE)
style_pattern = re.compile(r'style=[\'"]([^\'"]*)[\'"]', re.IGNORECASE)

target_style = 'style="font-size: clamp(32px, 4.5vw, 52px); margin-bottom: 16px;"'

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        enc = 'utf-8'
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()
        enc = 'cp1252'

    def replace_h1(match):
        inner_content = match.group(1)
        if style_pattern.search(inner_content):
            new_inner = style_pattern.sub(target_style, inner_content)
        else:
            new_inner = inner_content + ' ' + target_style
        return f'<h1{new_inner}>'

    new_content = h1_pattern.sub(replace_h1, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding=enc) as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Done!")
