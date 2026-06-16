import os
import glob

replacements = {
    'href="products.html#indoor-led"': 'href="indoor-led-screen.html"',
    'href="products.html#oled-series"': 'href="oled-series.html"',
    'href="products.html#indoor-cob"': 'href="indoor-cob.html"',
    'href="products.html#indoor-custom"': 'href="indoor-customised-led.html"',

    'href="products.html#outdoor-led"': 'href="outdoor-led-screen.html"',
    'href="products.html#outdoor-mesh"': 'href="outdoor-mesh-screen.html"',
    'href="products.html#outdoor-flexible"': 'href="outdoor-flexible-led.html"',
    'href="products.html#outdoor-custom"': 'href="outdoor-customised-led.html"',

    'href="products.html#smart-classroom"': 'href="smart-classroom-led.html"',
    'href="products.html#interactive-conference"': 'href="interactive-conference-led.html"',
    'href="products.html#kinetic-led"': 'href="kinetic-led-screen.html"',
    'href="products.html#spherical-led"': 'href="spherical-led-screen.html"',
    'href="products.html#transparent-glass"': 'href="transparent-glass-led.html"',
    'href="products.html#transparent-film"': 'href="transparent-film-led.html"',

    'href="products.html#kiosk-poster"': 'href="kiosk-poster.html"',
    'href="products.html#video-wall"': 'href="video-wall.html"'
}

def update_all_html_files():
    html_files = glob.glob("*.html")
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated links in {file}")

if __name__ == "__main__":
    update_all_html_files()
