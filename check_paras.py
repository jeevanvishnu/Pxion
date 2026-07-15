import os
import re

directory = r'c:\Users\jeeva\OneDrive\Documents\Bebright'

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Extract hero section roughly
            match = re.search(r'class="hero-title"[^>]*>.*?</h1>(.*?</section>)', content, re.DOTALL | re.IGNORECASE)
            if match:
                hero_remainder = match.group(1)
                # Count paragraphs
                paragraphs = re.findall(r'<p[^>]*>.*?</p>', hero_remainder, re.DOTALL | re.IGNORECASE)
                if len(paragraphs) > 1:
                    print(f"File {file} has {len(paragraphs)} paragraphs after h1 in hero section.")
