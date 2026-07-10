const fs = require('fs');
const path = require('path');

const baseDir = __dirname;
const files = [
    'indoor-cob.html',
    'indoor-customised-led.html',
    'indoor-led-screen.html',
    'interactive-conference-led.html',
    'kinetic-led-screen.html',
    'kiosk-poster.html',
    'oled-series.html',
    'outdoor-customised-led.html',
    'outdoor-flexible-led.html',
    'outdoor-led-screen.html',
    'outdoor-mesh-screen.html',
    'smart-classroom-led.html',
    'spherical-led-screen.html',
    'transparent-film-led.html',
    'transparent-glass-led.html',
    'video-wall.html'
];

files.forEach(file => {
    const filePath = path.join(baseDir, file);
    if (!fs.existsSync(filePath)) return;
    
    let content = fs.readFileSync(filePath, 'utf8');

    // The subtext added previously was:
    // <p class="section-sub">Explore our [name] reference images from real-world deployments</p>
    // We will match it and remove it entirely.
    
    // We need to account for possible whitespace/newline variations
    const regex = /\s*<p class="section-sub">Explore our .*? reference images from real-world deployments<\/p>/g;

    if (regex.test(content)) {
        const updatedContent = content.replace(regex, '');
        fs.writeFileSync(filePath, updatedContent);
        console.log("Removed subtext in", file);
    } else {
        console.log("Subtext not found in", file);
    }
});
