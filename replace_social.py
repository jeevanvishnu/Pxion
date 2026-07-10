import os
import re

dir_path = r"c:\Users\jeeva\OneDrive\Documents\Bebright"

pattern = re.compile(r'^(\s*)<a href="#" class="social-btn" aria-label="Instagram">in</a>\s*$', re.MULTILINE)

replacement = r'''\1<a href="https://www.linkedin.com/company/pixonglobal/" class="social-btn" aria-label="LinkedIn">in</a>
\1<a href="https://www.instagram.com/pixonglobal?utm_source=qr" class="social-btn" aria-label="Instagram">ig</a>'''

count = 0
for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content, num_subs = pattern.subn(replacement, content)
        
        if num_subs > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
