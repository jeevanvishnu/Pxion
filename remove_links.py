import os
import re
import glob

def remove_links_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for indoor customised led (desktop & mobile)
    # This regex looks for <li>...indoor-customised-led.html...</li> across multiple lines
    p_indoor = re.compile(r'<li[^>]*>\s*<a[^>]*href=["\']indoor-customised-led\.html["\'][^>]*>.*?</a>\s*</li>', re.IGNORECASE | re.DOTALL)
    
    # Pattern for outdoor customised led (desktop & mobile)
    p_outdoor = re.compile(r'<li[^>]*>\s*<a[^>]*href=["\']outdoor-customised-led\.html["\'][^>]*>.*?</a>\s*</li>', re.IGNORECASE | re.DOTALL)
    
    # Pattern for video wall (desktop & mobile)
    p_video_wall = re.compile(r'<li[^>]*>\s*<a[^>]*href=["\']video-wall\.html["\'][^>]*>.*?</a>\s*</li>', re.IGNORECASE | re.DOTALL)

    new_content = p_indoor.sub('', content)
    new_content = p_outdoor.sub('', new_content)
    new_content = p_video_wall.sub('', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = glob.glob('*.html')
changed = 0
for f in html_files:
    if remove_links_from_file(f):
        print(f"Updated {f}")
        changed += 1

print(f"Total files updated: {changed}")
