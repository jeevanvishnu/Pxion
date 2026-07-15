import os
import glob
import re

path = 'c:/Users/jeeva/OneDrive/Documents/Bebright'
files = glob.glob(os.path.join(path, '*.html'))

new_cta = """<section aria-labelledby="cta-heading" class="section cta-section" id="contact" style="padding: 0;">
    <div style="background: transparent; padding: 100px 20px; position: relative; overflow: hidden; display: flex; justify-content: center; align-items: center; text-align: center;">
        
        <!-- Left curved lines -->
        <svg width="300" height="100%" viewBox="0 0 300 400" preserveAspectRatio="none" style="position: absolute; left: 0; top: 0; opacity: 0.5; pointer-events: none;">
            <path d="M0,0 C120,80 150,250 0,400" fill="none" stroke="#ffffff" stroke-width="1.5"/>
            <path d="M0,0 C160,100 190,270 0,400" fill="none" stroke="#ffffff" stroke-width="1"/>
            <path d="M0,0 C200,120 230,290 0,400" fill="none" stroke="#ffffff" stroke-width="0.5"/>
        </svg>

        <!-- Right curved lines -->
        <svg width="300" height="100%" viewBox="0 0 300 400" preserveAspectRatio="none" style="position: absolute; right: 0; bottom: 0; opacity: 0.5; pointer-events: none;">
            <path d="M300,400 C180,320 150,150 300,0" fill="none" stroke="#ffffff" stroke-width="1.5"/>
            <path d="M300,400 C140,300 110,130 300,0" fill="none" stroke="#ffffff" stroke-width="1"/>
            <path d="M300,400 C100,280 70,110 300,0" fill="none" stroke="#ffffff" stroke-width="0.5"/>
        </svg>

        <div class="container" style="position: relative; z-index: 2; max-width: 1000px;">
            <div class="cta-label" style="color: rgba(255,255,255,0.8); text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 700; margin-bottom: 15px;">&mdash; UPGRADE TODAY &mdash;</div>
            <h2 id="cta-heading" style="color: #ffffff; font-size: clamp(20px, 2.8vw, 30px); font-weight: 500; margin-bottom: 20px; font-family: 'Inter', sans-serif;">Ready To Upgrade Your Display Experience?</h2>
            <p style="color: rgba(255, 255, 255, 0.95); font-size: 1.1rem; line-height: 1.6; margin-bottom: 40px; font-weight: 400; max-width: 650px; margin-left: auto; margin-right: auto;">
                From precise LED module calibrations to massive commercial LED meshes, PIXON TECHNOLOGIES's engineering team is ready to design and calibrate your layout.
            </p>
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                <a href="contact.html" class="cta-btn-solid">
                    Contact Our Team
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </a>
                <a href="contact.html" class="cta-btn-outline">
                    Schedule Consultation
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </a>
            </div>
        </div>
    </div>
</section>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Just replace the section tag to the end of the section
    # Use re.DOTALL to allow .*? to match across newlines
    pattern = re.compile(r'<section[^>]*class="[^"]*cta-section[^"]*"[^>]*>.*?</section>', re.DOTALL)
    
    # Check how many matches to ensure we don't accidentally match too much
    matches = pattern.findall(content)
    
    if len(matches) > 0:
        new_content = pattern.sub(new_cta, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {os.path.basename(f)} (Replaced {len(matches)} sections)")
    else:
        print(f"No cta-section found in {os.path.basename(f)}")
