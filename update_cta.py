import os
import glob
import re

path = 'c:/Users/jeeva/OneDrive/Documents/Bebright'
files = glob.glob(os.path.join(path, '*.html'))

new_cta = """    <!-- ============================================================
         SECTION 7: CTA
         ============================================================ -->
    <section class="section cta-section" id="get-started" style="padding: 0;">
        <div style="background: linear-gradient(135deg, #0A3DFF 0%, #00D9FF 100%); padding: 100px 20px; position: relative; overflow: hidden; display: flex; justify-content: center; align-items: center; text-align: center;">
            
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

            <div class="container" style="position: relative; z-index: 2; max-width: 800px;">
                <h2 style="color: #ffffff; font-size: clamp(28px, 4vw, 42px); font-weight: 500; margin-bottom: 20px; font-family: 'Inter', sans-serif;">Ready to Transform Your Space?</h2>
                <p style="color: rgba(255, 255, 255, 0.95); font-size: 1.1rem; line-height: 1.6; margin-bottom: 40px; font-weight: 400; max-width: 650px; margin-left: auto; margin-right: auto;">
                    Our Customised LED Screen solutions are designed to deliver exceptional results. Get a free consultation today to learn how we can meet your specific needs.
                </p>
                <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                    <a href="contact.html" class="cta-btn-solid">
                        Get Free Consultation
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                    <a href="projects.html" class="cta-btn-outline">
                        View Projects
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>"""

for f in files:
    # Skip solutions pages since they have slightly different wording and layout that we already did manually
    if "solutions.html" in f:
        continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try replacing with the comment block first
    pattern1 = re.compile(r'<!--\s*={50,}\s*SECTION \d+: CTA\s*={50,}\s*-->\s*<section class="section cta-section".*?</section>', re.DOTALL)
    if pattern1.search(content):
        new_content = pattern1.sub(new_cta, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {os.path.basename(f)}")
        continue
        
    pattern2 = re.compile(r'<section class="section cta-section".*?</section>', re.DOTALL)
    if pattern2.search(content):
        new_content = pattern2.sub(new_cta, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {os.path.basename(f)} (no comments)")
