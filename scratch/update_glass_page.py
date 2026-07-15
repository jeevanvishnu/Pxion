import re
import os

file_path = r'c:\Users\jeeva\OneDrive\Documents\Bebright\glass-transparent-display-solutions.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer
header_match = re.search(r'(.*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<footer role="contentinfo">.*)', content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer.")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

new_body_html = """
    <!-- ============================================================
         SECTION 1: HERO
         ============================================================ -->
    <section class="hero-section" style="background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url('assetss/innovative led screens/Glass Transparent Display Solutions/imgi_35_maxresdefault.jpg'); background-size: cover; background-position: center; padding: 120px 0; color: white; text-align: center;">
        <div class="container">
            <h1 class="hero-title" style="font-size: 3.5rem; font-weight: 800; margin-bottom: 20px; line-height: 1.2;">See Through the Future:<br/><span class="hero-title-accent" style="color: var(--accent-cyan);">Glass Transparent Display Solutions</span></h1>
            <p class="hero-subtitle" style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 40px auto; opacity: 0.9;">Revolutionize your storefronts and architectural spaces with up to 85% transparency and stunning high-definition brightness. Attract customers without blocking the view.</p>
            <div class="hero-cta">
                <a href="contact.html" class="btn btn-primary" style="padding: 15px 30px; font-size: 1.1rem; border-radius: 30px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Request a Quote</a>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 2: CORE FEATURES (GRID)
         ============================================================ -->
    <section class="section">
        <div class="container">
            <div class="section-header text-center">
                <div class="section-label">Why Choose Transparent LED?</div>
                <h2 class="section-title">Redefining Visual <span class="hero-title-accent">Experiences</span></h2>
                <p class="section-sub">Experience the perfect blend of digital signage and architectural elegance.</p>
            </div>

            <div class="features-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; margin-top: 40px;">
                <!-- Feature 1 -->
                <div class="feature-card reveal" style="background: rgba(10, 25, 47, 0.5); padding: 40px 30px; border-radius: 12px; border: 1px solid rgba(0, 240, 255, 0.1); text-align: center; transition: transform 0.3s ease;">
                    <div class="feature-icon" style="margin-bottom: 20px;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2m0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"></path></svg>
                    </div>
                    <h3 class="feature-title" style="font-size: 1.3rem; margin-bottom: 15px; color: #fff;">Ultra-High Transparency</h3>
                    <p class="feature-desc" style="color: #a8b2d1; font-size: 0.95rem;">Achieve up to 85% transparency rate, ensuring natural sunlight and open sightlines are preserved.</p>
                </div>

                <!-- Feature 2 -->
                <div class="feature-card reveal reveal-delay-1" style="background: rgba(10, 25, 47, 0.5); padding: 40px 30px; border-radius: 12px; border: 1px solid rgba(0, 240, 255, 0.1); text-align: center; transition: transform 0.3s ease;">
                    <div class="feature-icon" style="margin-bottom: 20px;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                    </div>
                    <h3 class="feature-title" style="font-size: 1.3rem; margin-bottom: 15px; color: #fff;">High Brightness</h3>
                    <p class="feature-desc" style="color: #a8b2d1; font-size: 0.95rem;">Up to 5000-7000 nits of brightness guarantees crystal clear visibility even under direct sunlight.</p>
                </div>

                <!-- Feature 3 -->
                <div class="feature-card reveal reveal-delay-2" style="background: rgba(10, 25, 47, 0.5); padding: 40px 30px; border-radius: 12px; border: 1px solid rgba(0, 240, 255, 0.1); text-align: center; transition: transform 0.3s ease;">
                    <div class="feature-icon" style="margin-bottom: 20px;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line></svg>
                    </div>
                    <h3 class="feature-title" style="font-size: 1.3rem; margin-bottom: 15px; color: #fff;">Lightweight & Thin</h3>
                    <p class="feature-desc" style="color: #a8b2d1; font-size: 0.95rem;">Extremely lightweight die-cast aluminum cabinets weighing only 12kg/sqm for effortless installation.</p>
                </div>

                <!-- Feature 4 -->
                <div class="feature-card reveal reveal-delay-3" style="background: rgba(10, 25, 47, 0.5); padding: 40px 30px; border-radius: 12px; border: 1px solid rgba(0, 240, 255, 0.1); text-align: center; transition: transform 0.3s ease;">
                    <div class="feature-icon" style="margin-bottom: 20px;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                    </div>
                    <h3 class="feature-title" style="font-size: 1.3rem; margin-bottom: 15px; color: #fff;">Modular Maintenance</h3>
                    <p class="feature-desc" style="color: #a8b2d1; font-size: 0.95rem;">Front and rear maintenance options with easily replaceable LED strips ensure minimal downtime.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 3: HIGHLIGHT 1 (IMAGE + TEXT)
         ============================================================ -->
    <section class="section" style="background: rgba(2, 12, 27, 0.7); overflow: hidden;">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 50px;">
                <div class="reveal" style="flex: 1 1 500px;">
                    <img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_36_1000TOR-1.jpg" alt="Transparent Retail LED Display" style="width: 100%; border-radius: 12px; box-shadow: 0 20px 40px rgba(0, 240, 255, 0.1); object-fit: cover; border: 1px solid rgba(0, 240, 255, 0.2);" />
                </div>
                <div class="reveal reveal-delay-1" style="flex: 1 1 400px;">
                    <div class="section-label">Retail Excellence</div>
                    <h2 class="section-title" style="margin-top: 10px; margin-bottom: 20px; font-size: 2.2rem;">Transform Your <span class="hero-title-accent">Storefront</span></h2>
                    <p style="color: #a8b2d1; font-size: 1.1rem; line-height: 1.8; margin-bottom: 25px;">
                        Our Glass Transparent Displays are engineered specifically for modern retail environments. Traditional LED screens block natural light and obscure the view into your store. By utilizing our highly transparent micro-diodes, you can project high-definition video advertising directly on your glass facade while allowing pedestrians to see inside.
                    </p>
                    <ul style="list-style: none; padding: 0; color: #ccd6f6; font-size: 1.05rem;">
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Perfectly blends with architectural glass.</li>
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Zero impact on interior ambient lighting.</li>
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Easy plug-and-play media player integration.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 4: HIGHLIGHT 2 (TEXT + IMAGE)
         ============================================================ -->
    <section class="section" style="overflow: hidden;">
        <div class="container">
            <div style="display: flex; flex-wrap: wrap; flex-direction: row-reverse; align-items: center; gap: 50px;">
                <div class="reveal" style="flex: 1 1 500px;">
                    <img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_101_Outdoor-Rental-Transparent-LED-Screen-9.jpg" alt="Stage Rental Transparent LED Screen" style="width: 100%; border-radius: 12px; box-shadow: 0 20px 40px rgba(0, 240, 255, 0.1); object-fit: cover; border: 1px solid rgba(0, 240, 255, 0.2);" />
                </div>
                <div class="reveal reveal-delay-1" style="flex: 1 1 400px;">
                    <div class="section-label">Stage & Rental</div>
                    <h2 class="section-title" style="margin-top: 10px; margin-bottom: 20px; font-size: 2.2rem;">Unleash Creative <span class="hero-title-accent">Stage Designs</span></h2>
                    <p style="color: #a8b2d1; font-size: 1.1rem; line-height: 1.8; margin-bottom: 25px;">
                        Beyond fixed installations, our transparent series features robust rental cabinets designed for the demanding touring and event staging industry. The ability to overlay digital content while revealing performers and lighting fixtures behind the screen creates breathtaking depth and 3D visual effects.
                    </p>
                    <ul style="list-style: none; padding: 0; color: #ccd6f6; font-size: 1.05rem;">
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Fast-locking system for rapid setup and teardown.</li>
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> High refresh rate (>3840Hz) for flawless camera broadcasting.</li>
                        <li style="margin-bottom: 15px; display: flex; align-items: flex-start;"><svg style="margin-right: 15px; flex-shrink: 0;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Lightweight design significantly reduces truss load.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 5: SPECIFICATIONS TABLE
         ============================================================ -->
    <section class="section" style="background: rgba(2, 12, 27, 0.7);">
        <div class="container">
            <div class="section-header text-center">
                <div class="section-label">Technical Data</div>
                <h2 class="section-title">Product <span class="hero-title-accent">Specifications</span></h2>
            </div>
            
            <div class="reveal" style="overflow-x: auto; margin-top: 40px; border-radius: 12px; border: 1px solid rgba(0,240,255,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <table style="width: 100%; border-collapse: collapse; text-align: left; color: #ccd6f6; min-width: 600px;">
                    <thead>
                        <tr style="background: rgba(0, 240, 255, 0.1); border-bottom: 2px solid rgba(0,240,255,0.2);">
                            <th style="padding: 20px; font-weight: 600; font-size: 1.1rem; color: #fff;">Specification</th>
                            <th style="padding: 20px; font-weight: 600; font-size: 1.1rem; color: #fff;">P2.8-5.6</th>
                            <th style="padding: 20px; font-weight: 600; font-size: 1.1rem; color: #fff;">P3.9-7.8</th>
                            <th style="padding: 20px; font-weight: 600; font-size: 1.1rem; color: #fff;">P7.8-7.8</th>
                            <th style="padding: 20px; font-weight: 600; font-size: 1.1rem; color: #fff;">P10.4-10.4</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(255,255,255,0.02);">
                            <td style="padding: 15px 20px; font-weight: 500;">Pixel Pitch (mm)</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">2.8 × 5.6</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">3.9 × 7.8</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">7.8 × 7.8</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">10.4 × 10.4</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <td style="padding: 15px 20px; font-weight: 500;">Transparency Rate</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">~65%</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">~75%</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">~80%</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">~85%</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(255,255,255,0.02);">
                            <td style="padding: 15px 20px; font-weight: 500;">Brightness (nits)</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">4500 - 5000</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">4500 - 5500</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">5000 - 6000</td>
                            <td style="padding: 15px 20px; color: #a8b2d1;">5500 - 7000</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                            <td style="padding: 15px 20px; font-weight: 500;">Refresh Rate</td>
                            <td colspan="4" style="padding: 15px 20px; color: #a8b2d1; text-align: center;">≥ 3840 Hz</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); background: rgba(255,255,255,0.02);">
                            <td style="padding: 15px 20px; font-weight: 500;">Standard Cabinet Size</td>
                            <td colspan="4" style="padding: 15px 20px; color: #a8b2d1; text-align: center;">1000mm × 500mm / 1000mm × 1000mm</td>
                        </tr>
                        <tr>
                            <td style="padding: 15px 20px; font-weight: 500;">Maintenance</td>
                            <td colspan="4" style="padding: 15px 20px; color: #a8b2d1; text-align: center;">Front & Rear Access Available</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- ============================================================
         SECTION 6: GALLERY
         ============================================================ -->
    <section id="gallery" class="light-section section gallery-section">
        <div class="container">
            <div class="section-header text-center">
                <div class="section-label">Real World Success</div>
                <h2 class="section-title">Project <span class="hero-title-accent">Gallery</span></h2>
                <p class="section-sub">Explore our extensive portfolio of transparent display installations worldwide.</p>
            </div>

            <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 40px;">
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_216_1000TOR-4-2.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_220_1000TOR-3.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_224_1000TOR-5.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_228_1000TOR-6.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_232_1000TOR-7.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_236_1000TOR-8.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_102_Outdoor-Transparent-LED-Display.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
                <div class="gallery-item reveal"><div class="gallery-image"><img src="assetss/innovative led screens/Glass Transparent Display Solutions/imgi_37_1000TOR-2.jpg" alt="Transparent Screen Application" style="width:100%; height: 250px; object-fit: cover; border-radius: 8px;" /></div></div>
            </div>
            
            <div class="text-center" style="margin-top: 50px;">
                <a href="projects.html" class="btn btn-primary" style="padding: 12px 30px; font-size: 1.1rem; border-radius: 30px; font-weight: 600;">View All Projects</a>
            </div>
        </div>
    </section>

"""

# Combine header, new body, and footer
final_html = header_html + "\n" + new_body_html + "\n" + footer_html

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully replaced content.")
