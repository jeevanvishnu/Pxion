import os
import glob
import re

html_files = glob.glob('*.html')
added_count = 0

addition = """<li><a href="retail-display.html" class="mobile-submenu-link">Retail Display Solution</a></li>
{indent}<li><a href="customized-led-screens.html" class="mobile-submenu-link">Customized LED Screens</a></li>
{indent}<li><a href="immersive-projection.html" class="mobile-submenu-link">Immersive Projection</a></li>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the mobile submenu for services. It usually ends with AV Solutions or Immersive Projection
    # If Immersive Projection is already there, skip.
    if 'href="immersive-projection.html" class="mobile-submenu-link"' in content:
        continue

    # Let's find the AV Solutions link inside the mobile menu
    # The AV Solutions link in mobile menu looks like: <a href="av-solutions.html" class="mobile-submenu-link">AV Solutions</a>
    pattern = r'([ \t]*)<li><a href="av-solutions\.html" class="mobile-submenu-link">AV Solutions</a></li>'
    
    match = re.search(pattern, content)
    if match:
        indent = match.group(1)
        replacement = match.group(0) + '\n' + indent + addition.format(indent=indent)
        
        # We need to make sure we only replace this specific instance inside the mobile menu
        new_content = content.replace(match.group(0), replacement)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        added_count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {added_count}")
