import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply inline styles
    content = content.replace('<h3 class="bento-title">', '<h3 class="bento-title" style="color: #ffffff !important; z-index: 999; text-shadow: 0 2px 4px rgba(0,0,0,0.9); position: absolute; bottom: 20px; left: 24px;">')
    
    content = content.replace('<div class="bento-overlay"></div>', '<div class="bento-overlay" style="position: absolute; inset: auto 0 0 0; height: 50%; background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%); pointer-events: none; z-index: 1;"></div>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Inline styles applied.")
