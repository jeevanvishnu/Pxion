import re, glob
for file in glob.glob('*.html'):
    if file == 'indoor-led-screen.html':
        continue # skip as it was properly set manually

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'bento-title' not in content:
        continue
    
    # Extract the true product name from <title>
    m1 = re.search(r'<title>(.*?) — PIXON TECHNOLOGIES</title>', content)
    title = 'LED Screen'
    if m1:
        title = m1.group(1).strip()
    
    # Unescape HTML entities like &amp; just in case, but keep it clean
    title = title.replace('&amp;', '&')
    
    # Replace all bento-titles with the correct title
    new_content = re.sub(r'<h3 class="bento-title">.*?</h3>', f'<h3 class="bento-title">{title}</h3>', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed titles in {file} -> {title}")
