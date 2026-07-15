import os
import urllib.parse
from bs4 import BeautifulSoup

html_file = 'c:/Users/jeeva/OneDrive/Documents/Bebright/customized-led-products.html'
with open(html_file, 'r', encoding='windows-1252', errors='replace') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the main tag
main_tag = soup.find('main')
if not main_tag:
    print('Main tag not found')
    exit(1)

# Find the products-showcase section
showcase = soup.find('section', class_='products-showcase')

# We will create new HTML to replace the showcase section.
# First, let's get images for Indoor
indoor_dir = 'c:/Users/jeeva/OneDrive/Documents/Bebright/assetss/Indoor Customised LED Screen'
indoor_images = os.listdir(indoor_dir)

# Second, for Outdoor
outdoor_dir = 'c:/Users/jeeva/OneDrive/Documents/Bebright/assetss/Outdoor Products/Outdoor Customised LED Screen'
outdoor_images = os.listdir(outdoor_dir)

indoor_gallery_html = '<div class="image-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin-top: 40px;">'
for img in indoor_images:
    src = f'assetss/Indoor%20Customised%20LED%20Screen/{urllib.parse.quote(img)}'
    indoor_gallery_html += f'''
    <div style="border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); aspect-ratio: 4/3;">
        <img src="{src}" alt="Indoor Customised LED" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
    </div>'''
indoor_gallery_html += '</div>'

outdoor_gallery_html = '<div class="image-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; margin-top: 40px;">'
for img in outdoor_images:
    src = f'assetss/Outdoor%20Products/Outdoor%20Customised%20LED%20Screen/{urllib.parse.quote(img)}'
    outdoor_gallery_html += f'''
    <div style="border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); aspect-ratio: 4/3;">
        <img src="{src}" alt="Outdoor Customised LED" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
    </div>'''
outdoor_gallery_html += '</div>'

new_sections_html = f'''
<section class="section" id="indoor-details" style="padding: 80px 0; background: var(--dark-bg);">
    <div class="container">
        <div class="section-header text-center" style="margin-bottom: 50px;">
            <div class="section-label" style="color: var(--orange); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Indoor Solutions</div>
            <h2 class="section-title" style="margin-top: 10px;">Indoor Customised LED Screen</h2>
            <p class="section-sub" style="max-width: 700px; margin: 15px auto 0;">Flexible, high-resolution bespoke LED screens that perfectly integrate into architectural indoor spaces. Motorized kinetic systems, spherical formats, and bespoke flexible modules.</p>
        </div>
        
        {indoor_gallery_html}
        
        <div style="margin-top: 50px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">Dynamic Movement</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Motorized kinetic systems allow screens to physically move, separate, and reassemble.</p>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">360-Degree Viewing</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Spherical and cylindrical formats provide complete, omnidirectional visual coverage.</p>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">Custom PCB Design</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Bespoke flexible modules can be mapped to virtually any architectural shape or curve.</p>
            </div>
        </div>
    </div>
</section>

<section class="section" id="outdoor-details" style="padding: 80px 0; background: rgba(3,7,18,0.95);">
    <div class="container">
        <div class="section-header text-center" style="margin-bottom: 50px;">
            <div class="section-label" style="color: var(--orange); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Outdoor Solutions</div>
            <h2 class="section-title" style="margin-top: 10px;">Outdoor Customised LED Screen</h2>
            <p class="section-sub" style="max-width: 700px; margin: 15px auto 0;">High-brightness, weather-resistant customized LED displays designed to stand out in any outdoor environment. Extreme brightness, IP68 weatherproofing, and smart thermal management.</p>
        </div>
        
        {outdoor_gallery_html}
        
        <div style="margin-top: 50px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">Extreme Brightness</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Up to 10,000 nits output ensures content slices through the harshest direct sunlight.</p>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">IP68 Weatherproofing</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Fully sealed cabinets resist torrential rain, dust storms, and coastal salt spray.</p>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
                <h3 style="color: var(--accent-cyan); font-size: 1.25rem; margin-bottom: 15px;">Freeform Modularity</h3>
                <p style="color: rgba(255,255,255,0.7); line-height: 1.6;">Build custom shapes, giant 3D installations, and letters limited only by imagination.</p>
            </div>
        </div>
    </div>
</section>
'''

new_soup = BeautifulSoup(new_sections_html, 'html.parser')
showcase.replace_with(new_soup)

with open(html_file, 'w', encoding='windows-1252') as f:
    f.write(str(soup))
print('Successfully updated customized-led-products.html')
