import os
import re

files_to_update = [
    "installation.html",
    "indoor.html",
    "outdoor.html",
    "rental.html",
    "av-solutions.html"
]

search_pattern = r'<div class="section-label">Ready to Start\?</div>\s*<h2 class="section-title" style="margin-bottom: 20px;">\s*Enquire <span class="hero-title-accent">Now</span>\s*</h2>\s*<p class="about-story-text" style="color: var\(--text-secondary\); margin-bottom: 30px;">\s*Get in touch with our experts to discuss your requirements, request a quote, or schedule a consultation\. We are here to bring your vision to life\.\s*</p>'

replacement_content = """<div class="section-label">Get Started</div>
                            <h2 class="section-title" style="margin-bottom: 20px;">
                                Let's Build Your Next <br /><span class="hero-title-accent">Display Experience</span>
                            </h2>
                            <p class="about-story-text" style="color: var(--text-secondary); margin-bottom: 30px;">
                                From custom kinetic screens to massive commercial outdoor LED installations, our display engineers are ready to elevate your visual environment.
                            </p>"""

for filename in files_to_update:
    filepath = os.path.join(r"c:\Users\jeeva\OneDrive\Documents\Bebright", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = re.sub(search_pattern, replacement_content, content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Missing {filename}")
