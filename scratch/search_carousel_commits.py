import subprocess
import re

try:
    # Get all commit hashes for projects.html
    hashes = subprocess.check_output(['git', 'log', '--format=%H', '--', 'projects.html'], encoding='utf-8').strip().split('\n')
    for h in hashes:
        out = subprocess.check_output(['git', 'show', f'{h}:projects.html'], encoding='utf-8')
        if 'carousel-item' in out:
            print(f"Commit {h} has carousel-item")
            items = re.findall(r'<div class="carousel-item"[^>]*data-src="([^"]+)"[^>]*data-type="([^"]+)"', out)
            print(f"Found {len(items)} items:")
            for src, t in items:
                print(f"  {src} ({t})")
            break
except Exception as e:
    print("Error:", e)
