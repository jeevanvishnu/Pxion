const fs = require('fs');
const path = require('path');

const dir = 'c:/Users/jeeva/OneDrive/Documents/Bebright';
const files = fs.readdirSync(dir);

let count = 0;
files.forEach(file => {
    if (file.endsWith('.html')) {
        const filePath = path.join(dir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        
        const regex = /<!-- Mobile Menu -->\s*<nav[^>]*id="mobile-menu"[^>]*>\s*<ul class="mobile-nav">/;
        
        if (regex.test(content) && !content.includes('mobile-menu-header')) {
            const match = content.match(regex)[0];
            const replaced = match.replace('<ul class="mobile-nav">', `<div class="mobile-menu-header">
            <span class="mobile-menu-title">Menu</span>
            <button class="mobile-menu-close" aria-label="Close menu" id="mobile-menu-close-btn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                   <path d="M18 6L6 18M6 6l12 12"></path>
                </svg>
            </button>
        </div>
        <ul class="mobile-nav">`);
            content = content.replace(regex, replaced);
            fs.writeFileSync(filePath, content, 'utf8');
            count++;
            console.log('Updated ' + file);
        }
    }
});

console.log('Total files updated: ' + count);
