import os
import re

dir_path = r"c:\Users\jeeva\OneDrive\Documents\Bebright"

pattern = re.compile(
    r'(<nav class="footer-links" aria-label="Services links">\s*<a href="products\.html" class="footer-link">Indoor LED Screens</a>\s*<a href="products\.html" class="footer-link">Outdoor LED Screens</a>\s*<a href="products\.html" class="footer-link">Custom Displays</a>\s*<a href="products\.html" class="footer-link">LCD &amp; Kiosks</a>\s*<a href="solutions\.html" class="footer-link">AV Integrations</a>\s*)(</nav>)',
    re.MULTILINE | re.DOTALL
)

def replace_func(match):
    prefix = match.group(1)
    suffix = match.group(2)
    # Adding the 3 items
    new_items = (
        '                        <a href="retail-display.html" class="footer-link">Retail Display Solution</a>\n'
        '                        <a href="customized-led-screens.html" class="footer-link">Customized LED Screens</a>\n'
        '                        <a href="immersive-projection.html" class="footer-link">Immersive Projection</a>\n'
        '                    '
    )
    return prefix + new_items + suffix

count = 0
for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content, num_subs = pattern.subn(replace_func, content)
        
        if num_subs > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")
        else:
            print(f"Skipped {filename} (no match)")

print(f"Total files updated: {count}")
