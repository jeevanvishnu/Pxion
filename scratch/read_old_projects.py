import subprocess
import re

try:
    out = subprocess.check_output(['git', 'show', '0a01670:projects.html'], encoding='utf-8')
    # Find all divs with class "gallery-item" or "project-gallery-card"
    items = re.findall(r'<div class="gallery-item.*?>.*?</div>\s*</div>\s*</div>', out, re.DOTALL)
    if not items:
        # Try finding any gallery items
        items = re.findall(r'<div class="gallery-item.*?>.*?</div>', out, re.DOTALL)
    
    print(f"Found {len(items)} items")
    for i, item in enumerate(items):
        print(f"--- Item {i} ---")
        print(item)
except Exception as e:
    print("Error:", e)
