import os
import glob
import re

old_block = """          <div class="nav-item-dropdown">
            <a href="solutions.html" class="nav-link dropdown-toggle">Services</a>
            <div class="simple-dropdown">
              <ul>
                <li><a href="installation.html">Installation & configuration</a></li>
                <li><a href="indoor.html">Indoor led screen</a></li>
                <li><a href="outdoor.html">Outdoor led screen</a></li>
                <li><a href="rental.html">Rental led screen</a></li>
                <li><a href="av-solutions.html">AV solutions</a></li>
              </ul>
            </div>
          </div>"""

# Find the new block that was injected. It might have varying spacing, so let's use regex
# to find the nav-item-dropdown for Services and replace it completely.
pattern = re.compile(
    r'<div class="nav-item-dropdown">\s*<a href="solutions\.html"[^>]*>Services</a>\s*<div class="mega-menu services-menu">.*?</svg>\s*</span>\s*<span class="promo-cta-text">Book Service</span>\s*</a>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>',
    re.DOTALL
)

def update_all_html_files():
    html_files = glob.glob("*.html")
    updated_count = 0
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, count = pattern.subn(old_block, content)
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reverted {file}")
            updated_count += 1
            
    print(f"Total reverted: {updated_count}")

if __name__ == "__main__":
    update_all_html_files()
