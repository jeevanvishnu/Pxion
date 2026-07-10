import os
import re

# 1. Fix style.css hover effect
css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the specific hover effect rules
old_hover = """
.application-card:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 217, 255, 0.4);
    box-shadow: 0 20px 50px rgba(0, 217, 255, 0.15);
    background: rgba(255, 255, 255, 0.06);
}

.application-icon {
    width: 80px;
    height: 80px;
    border-radius: 20px;
    background: rgba(0, 217, 255, 0.08);
    border: 1px solid rgba(0, 217, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition);
}

.application-card:hover .application-icon {
    background: linear-gradient(135deg, #0A3DFF, #00D9FF);
    border-color: transparent;
    box-shadow: 0 12px 32px rgba(0, 217, 255, 0.3);
    transform: scale(1.15) rotate(5deg);
}
"""

new_hover = """
.application-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.08);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.application-icon {
    width: 80px;
    height: 80px;
    background: rgba(0, 217, 255, 0.05);
    border-radius: 20px;
    margin: 0 auto 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition);
}
"""

# Let's just do a rough replace if exact doesn't match
if ".application-card:hover" in css and "rotate(5deg)" in css:
    css = re.sub(r'\.application-card:hover\s*{[^}]*}\s*\.application-icon\s*{[^}]*}\s*\.application-card:hover\s*\.application-icon\s*{[^}]*}', new_hover, css, flags=re.DOTALL)
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Fix indoor-led-screen.html
def fix_indoor_page():
    fpath = 'indoor-led-screen.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove specs
    html = re.sub(r'<!--\s*=+\s*SECTION \d+: TECHNICAL SPECIFICATIONS\s*=+\s*-->\s*<section.*?</section>', '', html, flags=re.DOTALL)

    # Change gallery to light-section
    html = html.replace('<section class="section gallery-section">', '<section class="section gallery-section light-section" id="gallery">')
    
    # Change applications to NOT light-section
    # Look for "SECTION 3: APPLICATIONS"
    app_idx = html.find('SECTION 3: APPLICATIONS')
    if app_idx != -1:
        sec_start = html.find('<section class="section light-section">', app_idx)
        if sec_start != -1 and sec_start < app_idx + 300:
            html = html[:sec_start] + '<section class="section">' + html[sec_start + len('<section class="section light-section">'):]

    # Replace hero section
    hero_pattern = r'<section id="hero".*?</section>'
    new_hero = """<section id="hero" aria-label="Indoor LED Screen Hero Section"
            style="min-height: 70vh; padding-top: 140px; padding-bottom: 60px; position: relative; background-image: url('assets/product-bg.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
            <div style="position: absolute; inset: 0; background: rgba(3, 7, 18, 0.72); z-index: 0;"></div>
            <div class="hero-bg" style="position: absolute; inset: 0; z-index: 1;">
                <div class="hero-mesh"></div>
                <div class="orb orb-1" style="background: radial-gradient(circle, var(--accent-cyan) 0%, transparent 70%); top: -10%; left: 10%;"></div>
            </div>
            <div class="hero-content" style="position: relative; z-index: 2;">
                <div class="container">
                    <div style="max-width: 800px; margin: 0 auto; text-align: center;" class="animate-fade-in-up">
                        <div class="hero-badge" style="justify-content: center;">
                            <span class="hero-badge-dot" style="background: var(--accent-cyan); box-shadow: 0 0 8px var(--accent-cyan)"></span>
                            INDOOR PRODUCTS
                        </div>
                        <h1 class="hero-title" style="font-size: clamp(38px, 5vw, 64px); margin-bottom: 16px;">
                            Indoor <span class="hero-title-accent">LED Screen</span>
                        </h1>
                        <p class="hero-sub" style="margin-bottom: 20px; margin-left: auto; margin-right: auto;">
                            Stunning Visual Experiences for Indoor Spaces
                        </p>
                        <p class="hero-desc" style="margin-left: auto; margin-right: auto; margin-bottom: 40px; max-width: 600px;">
                            Transform your retail stores, corporate offices, shopping malls, auditoriums, and event venues with high-resolution indoor LED display solutions. Designed for exceptional image quality, vibrant colors, and seamless performance.
                        </p>
                        <div class="hero-actions" style="justify-content: center;">
                            <a href="#get-started" class="btn btn-primary">Get Consultation</a>
                            <a href="#features" class="btn btn-ghost">Learn More</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
    html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_indoor_page()
print("Restored indoor-led-screen.html and style.css successfully!")
