import re

with open('c:/Users/jeeva/OneDrive/Documents/Bebright/projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first gallery (indoor)
indoor_match = re.search(r'<div class="parallelogram-gallery">(.*?)</div>\s*<h2', content, re.DOTALL)
if indoor_match:
    indoor_html = indoor_match.group(1)
    # Extract images/videos from indoor_html
    media = re.findall(r'src="([^"]+)"', indoor_html)
    
    print("Top row 5 indices:")
    for i in range(16, min(20, len(media))):
        print(f"Index {i}: {media[i]}")
else:
    print('Indoor gallery not found')
