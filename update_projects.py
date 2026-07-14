import re

with open('c:/Users/jeeva/OneDrive/Documents/Bebright/projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all items
pattern = r'<div class="carousel-item" data-index="\d+" data-src="([^"]+)" data-type="([^"]+)">.*?</div>'
items = re.findall(pattern, content, re.DOTALL)

# Let's say first 20 are Indoor, remaining are Outdoor
indoor_items = items[:20]
outdoor_items = items[20:]

def generate_gallery_html(items, is_outdoor=False):
    html = '<div class="parallelogram-gallery">\n'
    for i, (src, type) in enumerate(items):
        
        media_html = ''
        if type == 'image':
            media_html = f'<img src="{src}" alt="Project View" loading="lazy" />'
        elif type == 'video':
            media_html = f'<video src="{src}" muted loop playsinline></video>\n            <div class="gallery-play-icon"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>'
            
        html += f'''    <div class="pg-item" onclick="openLightbox('{src}', '{type}')">
        <div class="pg-content">
            {media_html}
            <div class="pg-overlay"></div>
        </div>
    </div>\n'''
    html += '</div>\n'
    return html

indoor_html = generate_gallery_html(indoor_items)
outdoor_html = generate_gallery_html(outdoor_items, True)

new_section = f'''
        <!-- ======================== PARALLELOGRAM GALLERY ======================== -->
        <section class="gallery-section">
            <div class="container" style="max-width: 1400px; padding: 40px 20px;">
                <h2 class="gallery-title" style="text-align: center; margin-bottom: 40px; font-size: 2.5rem; color: #333; display: none;">Indoor Projects</h2>
                {indoor_html}
                
                <h2 class="gallery-title" style="text-align: center; margin: 80px 0 40px; font-size: 2rem; color: #040b4f; font-weight: 700;">Outdoor LED Projects</h2>
                {outdoor_html}
            </div>
        </section>
'''

# Replace the old section
# Find <section class="carousel-section"> ... </section>
start_idx = content.find('<section class="carousel-section">')
end_idx = content.find('</section>', start_idx) + len('</section>')

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_section.strip() + '\n' + content[end_idx:]
    with open('c:/Users/jeeva/OneDrive/Documents/Bebright/projects.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced carousel with parallelogram gallery.")
else:
    print("Could not find carousel-section.")
