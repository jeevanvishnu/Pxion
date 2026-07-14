import subprocess
import re

try:
    # Get the staged version of projects.html
    out = subprocess.check_output(['git', 'show', ':projects.html'], encoding='utf-8')
    # Find all divs containing WhatsApp or assetss/projects
    items = re.findall(r'(<div class="[^"]*"[^>]*onclick="openLightbox[^>]*>.*?</div>\s*</div>)', out, re.DOTALL)
    if not items:
        items = re.findall(r'(<div class="gallery-item.*?>.*?</div>)', out, re.DOTALL)
        
    print(f"Found {len(items)} items in staged version:")
    for i, item in enumerate(items):
        print(f"--- Item {i} ---")
        # print first 150 chars of item
        print(item.strip()[:300])
except Exception as e:
    print("Error:", e)
