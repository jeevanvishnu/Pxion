const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const newSection = `
    <!-- ======================== WHY CHOOSE US ======================== -->
    <section id="why-choose" class="section" style="background: rgba(30, 136, 229, 0.02); border-top: 1px solid rgba(30, 136, 229, 0.08); padding-top: 80px; padding-bottom: 80px;">
      <div class="container">
        <header style="text-align: center; margin-bottom: 60px;">
          <div class="section-label reveal" style="justify-content: center; margin-bottom: 12px;">Our Advantage</div>
          <h2 class="section-title reveal reveal-delay-1">Why Choose Us</h2>
          <p class="section-sub reveal reveal-delay-2" style="margin: 16px auto 0;">Delivering specialized engineering integrations, professional setups, and dedicated support.</p>
        </header>

        <!-- Stats Counters Grid -->
        <div class="about-stats-grid reveal" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 24px; margin-bottom: 60px;">
          <div class="stat-glass-card" style="padding: 30px 24px; text-align: center; background: rgba(17, 25, 46, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; position: relative; overflow: hidden; backdrop-filter: blur(12px);">
            <div class="stat-num" style="font-size: 48px; font-weight: 800; color: var(--white);"><span class="counter" data-target="50">0</span><span style="color: var(--orange);">+</span></div>
            <div class="stat-label" style="font-size: 14px; font-weight: 600; color: rgba(255, 255, 255, 0.7); text-transform: uppercase; letter-spacing: 1px;">Projects Completed</div>
            <div class="stat-glow glow-blue" style="position: absolute; width: 100px; height: 100px; background: rgba(0, 188, 212, 0.3); filter: blur(40px); bottom: -30px; right: -30px; border-radius: 50%;"></div>
          </div>
          <div class="stat-glass-card reveal-delay-1" style="padding: 30px 24px; text-align: center; background: rgba(17, 25, 46, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; position: relative; overflow: hidden; backdrop-filter: blur(12px);">
            <div class="stat-num" style="font-size: 48px; font-weight: 800; color: var(--white);"><span class="counter" data-target="25">0</span><span style="color: var(--blue-accent);">+</span></div>
            <div class="stat-label" style="font-size: 14px; font-weight: 600; color: rgba(255, 255, 255, 0.7); text-transform: uppercase; letter-spacing: 1px;">Clients Served</div>
            <div class="stat-glow glow-orange" style="position: absolute; width: 100px; height: 100px; background: rgba(0, 188, 212, 0.3); filter: blur(40px); bottom: -30px; right: -30px; border-radius: 50%;"></div>
          </div>
          <div class="stat-glass-card reveal-delay-2" style="padding: 30px 24px; text-align: center; background: rgba(17, 25, 46, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; position: relative; overflow: hidden; backdrop-filter: blur(12px);">
            <div class="stat-num" style="font-size: 48px; font-weight: 800; color: var(--white);"><span class="counter" data-target="5">0</span><span style="color: var(--orange);">+</span></div>
            <div class="stat-label" style="font-size: 14px; font-weight: 600; color: rgba(255, 255, 255, 0.7); text-transform: uppercase; letter-spacing: 1px;">Countries Covered</div>
            <div class="stat-glow glow-blue" style="position: absolute; width: 100px; height: 100px; background: rgba(0, 188, 212, 0.3); filter: blur(40px); bottom: -30px; right: -30px; border-radius: 50%;"></div>
          </div>
          <div class="stat-glass-card reveal-delay-3" style="padding: 30px 24px; text-align: center; background: rgba(17, 25, 46, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; position: relative; overflow: hidden; backdrop-filter: blur(12px);">
            <div class="stat-num" style="font-size: 48px; font-weight: 800; color: var(--white);"><span class="counter" data-target="10">0</span><span style="color: var(--blue-accent);">+</span></div>
            <div class="stat-label" style="font-size: 14px; font-weight: 600; color: rgba(255, 255, 255, 0.7); text-transform: uppercase; letter-spacing: 1px;">Technology Categories</div>
            <div class="stat-glow glow-orange" style="position: absolute; width: 100px; height: 100px; background: rgba(0, 188, 212, 0.3); filter: blur(40px); bottom: -30px; right: -30px; border-radius: 50%;"></div>
          </div>
        </div>

        <!-- 8 Points Grid -->
        <div class="compact-services-grid">
          <!-- 1 -->
          <div class="compact-service-card reveal">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Experienced Technical Team</h4>
          </div>
          <!-- 2 -->
          <div class="compact-service-card reveal reveal-delay-1">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Customized Solutions</h4>
          </div>
          <!-- 3 -->
          <div class="compact-service-card reveal reveal-delay-2">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Competitive Pricing</h4>
          </div>
          <!-- 4 -->
          <div class="compact-service-card reveal reveal-delay-3">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Quality Products</h4>
          </div>
          <!-- 5 -->
          <div class="compact-service-card reveal">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Professional Installation</h4>
          </div>
          <!-- 6 -->
          <div class="compact-service-card reveal reveal-delay-1">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Fast Support</h4>
          </div>
          <!-- 7 -->
          <div class="compact-service-card reveal reveal-delay-2">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">After Sales Service</h4>
          </div>
          <!-- 8 -->
          <div class="compact-service-card reveal reveal-delay-3">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); color: #10B981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 12px rgba(16,185,129,0.3);">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" width="16" height="16"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h4 class="service-name-compact">Strong Execution Across Middle East</h4>
          </div>
        </div>
      </div>
    </section>
`;

if (html.includes('<!-- ======================== TESTIMONIALS ======================== -->')) {
    html = html.replace('<!-- ======================== TESTIMONIALS ======================== -->', newSection + '\n    <!-- ======================== TESTIMONIALS ======================== -->');
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('index.html updated successfully.');
} else {
    console.log('Could not find testimonials section.');
}

// Update script.js with counter animation
let js = fs.readFileSync('script.js', 'utf8');
if (!js.includes('.counter')) {
    const counterScript = `
// Animated Counters
document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.counter');
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const targetValue = parseInt(target.getAttribute('data-target'));
                let current = 0;
                const duration = 1500; // 1.5 seconds total
                const increment = targetValue / (duration / 16); // assuming 60fps (16ms per frame)
                
                const updateCounter = () => {
                    current += increment;
                    if (current < targetValue) {
                        target.innerText = Math.ceil(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        target.innerText = targetValue;
                    }
                };
                
                updateCounter();
                observer.unobserve(target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });
});
`;
    js += '\n' + counterScript;
    fs.writeFileSync('script.js', js, 'utf8');
    console.log('script.js updated successfully.');
}
