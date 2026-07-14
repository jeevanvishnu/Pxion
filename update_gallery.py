import os

html_path = r'c:\Users\jeeva\OneDrive\Documents\Bebright\retail-display.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

images = [
    'imgi_121_6895746445931.jpg',
    'imgi_122_6895746442731.jpg',
    'imgi_164_6895723590ea6.jpg',
    'imgi_168_67fdcd3f878a1.jpg',
    'imgi_209_66d012b34a7d4.png',
    'imgi_211_66d013891036e.png',
    'imgi_22_6840f982781e5.jpg',
    'imgi_30_DS042Q-8-1-e1732778188113.jpg',
    'imgi_72_68afbe8f53a50.jpg'
]

cards = []
for i, img in enumerate(images):
    card = f'''                    <div class="product-card reveal">
                        <div class="product-visual" style="height: 250px; background: transparent; padding: 20px;">
                            <img src="assetss/Retails/{img}" alt="Retail Display Model {i+1}" style="max-height: 100%; max-width: 100%; object-fit: contain; border-radius: 8px;">
                        </div>
                        <div class="product-content" style="padding: 20px;">
                            <div class="product-type" style="font-size: 12px; color: #00D9FF; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">Display Series</div>
                            <h3 class="product-name" style="font-size: 18px; margin-bottom: 10px;">Smart Retail Terminal</h3>
                        </div>
                    </div>'''
    cards.append(card)

grid_html = '<div class="showcase-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">\n' + '\n'.join(cards) + '\n                </div>'

start_marker = '<div class="showcase-grid"'
end_marker = '<!-- Functions & Capabilities -->'

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = end_marker + content.split(end_marker)[1]
    
    new_content = pre + grid_html + '\n            </div>\n        </section>\n\n        ' + post
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated successfully to 9 cards.')
else:
    print('Markers not found.')
