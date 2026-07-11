import os
import glob
import re

directory = r"c:\Users\jeeva\OneDrive\Documents\Bebright"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for the <a> tag version without <li>
    pattern_a = re.compile(
        r'(<a href="installation\.html">Installation & Configuration</a>\s*'
        r'<a href="indoor\.html">Indoor LED Screen</a>\s*'
        r'<a href="outdoor\.html">Outdoor LED Screen</a>\s*'
        r'<a href="rental\.html">Rental LED Screen</a>\s*'
        r'<a href="av-solutions\.html">AV Solutions</a>)'
    )
    
    if pattern_a.search(content):
        def replacement_a(match):
            original = match.group(1)
            lines = original.split('\n')
            last_line = lines[-1]
            indent_match = re.match(r'(\s*)', last_line)
            indent = indent_match.group(1) if indent_match else '                            '
            
            new_items = (
                f'\n{indent}<a href="retail-display.html">Retail Display Solution</a>'
                f'\n{indent}<a href="customized-led-screens.html">Customized LED Screens</a>'
                f'\n{indent}<a href="immersive-projection.html">Immersive Projection</a>'
            )
            return original + new_items

        new_content = pattern_a.sub(replacement_a, content)
        
        if "retail-display.html" not in content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated (<a> format) {os.path.basename(file_path)}")
        else:
            print(f"Skipped {os.path.basename(file_path)} - already updated")
    else:
        # no match
        pass

print("Done!")
