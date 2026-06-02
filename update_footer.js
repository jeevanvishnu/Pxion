const fs = require('fs');

const contactColumn = `                <!-- Contact Us -->
                <div>
                    <div class="footer-col-title">Contact Us</div>
                    <div style="color: rgba(255, 255, 255, 0.7); font-size: 0.95rem; margin-bottom: 12px; display: flex; flex-direction: column; gap: 10px;">
                        <a href="mailto:info@pixontechnologies.com" style="color: inherit; text-decoration: none; display: flex; align-items: center; gap: 8px; transition: color 0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='inherit'">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                            info@pixontechnologies.com
                        </a>
                        <a href="tel:+971504037863" style="color: inherit; text-decoration: none; display: flex; align-items: center; gap: 8px; transition: color 0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='inherit'">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                            +971 50 403 7863
                        </a>
                    </div>
                    <div style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); margin-top: 15px;">
                        <iframe 
                            width="100%" 
                            height="100%" 
                            frameborder="0" 
                            scrolling="no" 
                            marginheight="0" 
                            marginwidth="0" 
                            src="https://maps.google.com/maps?q=Naif,%20Deira%20Dubai,%20United%20Arab%20Emirates&t=&z=13&ie=UTF8&iwloc=&output=embed"
                            style="display: block; width: 100%; border: none;">
                        </iframe>
                    </div>
                </div>`;

const files = fs.readdirSync('.').filter(f => f.endsWith('.html') && f !== 'contact.html');
files.forEach(f => {
    let content = fs.readFileSync(f, 'utf8');
    if (!content.includes('<!-- Contact Us -->')) {
        const regex = /(<!-- Services -->[\s\S]*?<\/nav>\s*<\/div>)/;
        if (regex.test(content)) {
            content = content.replace(regex, '$1\n' + contactColumn);
            fs.writeFileSync(f, content);
            console.log('Updated HTML file: ' + f);
        } else {
            console.log('Failed to match in ' + f);
        }
    }
});

let css = fs.readFileSync('style.css', 'utf8');
if (css.includes('1.5fr 1fr 1fr;')) {
    css = css.replace(/1\.5fr\s+1fr\s+1fr;/g, '1.5fr 1fr 1fr 1.2fr;');
    fs.writeFileSync('style.css', css);
    console.log('Updated style.css');
}
