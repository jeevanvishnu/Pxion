import os
import glob

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

new_block = """          <div class="nav-item-dropdown">
            <a href="solutions.html" class="nav-link dropdown-toggle">Services</a>
            <div class="mega-menu services-menu">
              <div class="mega-menu-grid services-grid">
                <!-- Installation -->
                <div class="mega-column">
                  <h4 class="mega-title">Installation</h4>
                  <ul class="mega-list">
                    <li><a href="installation.html">Installation & configuration</a></li>
                  </ul>
                </div>

                <!-- Indoor Solutions -->
                <div class="mega-column">
                  <h4 class="mega-title">Indoor Solutions</h4>
                  <ul class="mega-list">
                    <li><a href="indoor.html">Indoor led screen</a></li>
                  </ul>
                </div>

                <!-- Outdoor Solutions -->
                <div class="mega-column">
                  <h4 class="mega-title">Outdoor Solutions</h4>
                  <ul class="mega-list">
                    <li><a href="outdoor.html">Outdoor led screen</a></li>
                  </ul>
                </div>

                <!-- Specialized AV -->
                <div class="mega-column">
                  <h4 class="mega-title">Specialized AV</h4>
                  <ul class="mega-list">
                    <li><a href="rental.html">Rental led screen</a></li>
                    <li><a href="av-solutions.html">AV solutions</a></li>
                  </ul>
                </div>

                <!-- Right Promo Card -->
                <div class="mega-promo-card">
                  <div class="promo-content">
                    <div class="promo-logo">
                      <svg width="40" height="40" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M50 15 L85 35 L85 75 L50 95 L15 75 L15 35 Z" fill="url(#services-grad)" />
                        <defs>
                          <linearGradient id="services-grad" x1="15" y1="15" x2="85" y2="95" gradientUnits="userSpaceOnUse">
                            <stop offset="0%" stop-color="#8b5cf6" />
                            <stop offset="100%" stop-color="#3b82f6" />
                          </linearGradient>
                        </defs>
                      </svg>
                    </div>
                    <h3 class="promo-heading">Expert AV Installation & Maintenance Services</h3>
                    <div class="promo-arrow" style="margin-bottom: 24px;">
                      <svg width="70" height="50" viewBox="0 0 100 70" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10,10 C45,-10 65,40 35,50 C20,55 30,35 60,15 C70,10 85,25 70,45" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-linecap="round" fill="none" />
                        <path d="M60,40 L70,45 L75,35" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none" />
                      </svg>
                    </div>
                    <a href="contact.html" class="btn-promo-cta">
                      <span class="promo-cta-circle">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                          <line x1="5" y1="12" x2="19" y2="12" />
                          <polyline points="12 5 19 12 12 19" />
                        </svg>
                      </span>
                      <span class="promo-cta-text">Book Service</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>"""

def update_all_html_files():
    html_files = glob.glob("*.html")
    updated_count = 0
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We also need to be flexible with indentation if needed
        # Let's strip whitespace and do a flexible replace
        if old_block in content:
            new_content = content.replace(old_block, new_block)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            updated_count += 1
        else:
            # Let's try flexible search
            import re
            old_block_regex = re.sub(r'\s+', r'\\s+', old_block)
            match = re.search(old_block_regex, content)
            if match:
                # get original indentation of the first line
                start_index = match.start()
                # find newline before start_index
                nl_idx = content.rfind('\n', 0, start_index)
                indent = content[nl_idx+1:start_index]
                
                # Replace content
                new_content = content[:match.start()] + new_block + content[match.end():]
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file} (regex match)")
                updated_count += 1

    print(f"Total updated: {updated_count}")

if __name__ == "__main__":
    update_all_html_files()
