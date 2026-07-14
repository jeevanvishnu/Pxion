import os
import re

with open('c:/Users/jeeva/OneDrive/Documents/Bebright/projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all src attributes from images and videos
paths = re.findall(r'src="([^"]+)"', content)

print(f"Checking {len(paths)} paths in projects.html:")
broken = 0
for path in paths:
    # Only check relative paths to assets/assetss
    if path.startswith('http') or path.startswith('https'):
        continue
    full_path = os.path.join('c:/Users/jeeva/OneDrive/Documents/Bebright', path)
    # clean up slashes
    full_path = os.path.abspath(full_path)
    if not os.path.exists(full_path):
        print(f"Broken path: {path} (Resolved to: {full_path})")
        broken += 1
    else:
        # print first few as check
        pass

print(f"Check complete. Staged/broken paths: {broken}")
