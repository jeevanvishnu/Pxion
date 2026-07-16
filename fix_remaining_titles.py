import re

files_to_fix = {
    'oled-series.html': 'OLED Series',
    'spherical-led-screen.html': 'Spherical LED Screen',
    'transparent-film-led.html': 'Transparent Film LED',
    'video-wall.html': 'Video Wall'
}

for filename, correct_title in files_to_fix.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the incorrectly set title
        new_content = re.sub(r'<h3 class="bento-title">LED Screen</h3>', f'<h3 class="bento-title">{correct_title}</h3>', content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename} -> {correct_title}")
        else:
            print(f"No changes needed for {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
