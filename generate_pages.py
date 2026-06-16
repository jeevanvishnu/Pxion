import os
import re

base_file = "indoor-products.html"

pages = [
    {"file": "indoor-led-screen.html", "title": "Indoor LED Screen", "badge": "INDOOR PRODUCTS"},
    {"file": "oled-series.html", "title": "OLED Series", "badge": "INDOOR PRODUCTS"},
    {"file": "indoor-cob.html", "title": "Indoor COB (Chip-On-Board)", "badge": "INDOOR PRODUCTS"},
    {"file": "indoor-customised-led.html", "title": "Indoor Customised LED Screen", "badge": "INDOOR PRODUCTS"},

    {"file": "outdoor-led-screen.html", "title": "Outdoor LED Screen", "badge": "OUTDOOR PRODUCTS"},
    {"file": "outdoor-mesh-screen.html", "title": "Outdoor Mesh Screen", "badge": "OUTDOOR PRODUCTS"},
    {"file": "outdoor-flexible-led.html", "title": "Outdoor Flexible LED", "badge": "OUTDOOR PRODUCTS"},
    {"file": "outdoor-customised-led.html", "title": "Outdoor Customised LED Screen", "badge": "OUTDOOR PRODUCTS"},

    {"file": "smart-classroom-led.html", "title": "Smart Classroom LED System", "badge": "INNOVATIVE SCREENS"},
    {"file": "interactive-conference-led.html", "title": "Interactive Conference LED", "badge": "INNOVATIVE SCREENS"},
    {"file": "kinetic-led-screen.html", "title": "Kinetic LED Screen", "badge": "INNOVATIVE SCREENS"},
    {"file": "spherical-led-screen.html", "title": "Spherical LED Screen", "badge": "INNOVATIVE SCREENS"},
    {"file": "transparent-glass-led.html", "title": "Transparent Glass LED Screen", "badge": "INNOVATIVE SCREENS"},
    {"file": "transparent-film-led.html", "title": "Transparent Film LED Screen", "badge": "INNOVATIVE SCREENS"},

    {"file": "kiosk-poster.html", "title": "Kiosk & Poster Screen", "badge": "LCD & KIOSK"},
    {"file": "video-wall.html", "title": "Video Wall", "badge": "LCD & KIOSK"},
]

def generate():
    with open(base_file, "r", encoding="utf-8") as f:
        content = f.read()

    for p in pages:
        new_content = content
        
        # Replace Title
        new_content = re.sub(
            r"<title>.*? — PIXON TECHNOLOGIES</title>", 
            f"<title>{p['title']} — PIXON TECHNOLOGIES</title>", 
            new_content
        )
        
        # Replace Badge
        new_content = re.sub(
            r"(<div class=\"hero-badge\".*?>\s*<span.*?</span>\s*)[A-Z\s]+(\s*</div>)",
            rf"\g<1>{p['badge']}\g<2>",
            new_content,
            flags=re.DOTALL
        )
        
        # Replace H1
        new_content = re.sub(
            r"(<h1 class=\"hero-title\".*?>\s*).*?(\s*</h1>)",
            rf"\g<1>{p['title']}\g<2>",
            new_content,
            flags=re.DOTALL
        )
        
        # Replace description in main section
        new_content = re.sub(
            r"features for .*?\.",
            f"features for {p['title']}.",
            new_content
        )
        
        with open(p['file'], "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"Generated {p['file']}")

if __name__ == "__main__":
    generate()
