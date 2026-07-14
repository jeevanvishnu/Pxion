import os

html_path = r'c:\Users\jeeva\OneDrive\Documents\Bebright\customized-led-screens.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

images = [
    ("imgi_10_圆柱屏430_0000_LED圆柱屏06-537203.png", "Cylindrical LED Display"),
    ("imgi_11_1688637909005328928.png", "Creative Tree Display"),
    ("imgi_12_旋转屏430_0002_旋转屏03-506097.png", "Rotating LED Display"),
    ("imgi_15_易拉罐430_0004_美国展会1-740435.png", "Can LED Display"),
    ("imgi_20_1724116069725785698.png", "Immersive Experience Display"),
    ("imgi_8_1688696624335939696.png", "Triangle / Custom Display")
]

cards = []
for filename, title in images:
    card = f'''                <div class="custom-model-card" style="background-color: #3e3e3e; padding: 40px 20px 25px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: space-between; border-radius: 4px; transition: transform 0.3s ease;">
                    <img src="assetss/cutomized/{filename}" alt="{title}" style="max-height: 220px; max-width: 100%; object-fit: contain; margin-bottom: 30px;">
                    <div>
                        <h3 style="color: #ffffff; font-size: 16px; font-weight: 800; margin-bottom: 8px;">{title}</h3>
                        <p style="color: #cccccc; font-size: 10px; font-weight: 700; letter-spacing: 1px; margin: 0; text-transform: uppercase;">P2 | P2.5 | P3 | P4</p>
                    </div>
                </div>'''
    cards.append(card)

gallery_section = f'''        <!-- Dark Product Gallery Matching User Reference -->
        <section id="custom-gallery" style="background-color: #2a2a2a; padding: 80px 0;">
            <div class="container" style="max-width: 1300px; margin: 0 auto; padding: 0 20px;">
                <div style="text-align: center; margin-bottom: 50px;">
                    <h2 style="color: #ffffff; font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; letter-spacing: -1px;">Creative Models Showcase</h2>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px;">
{chr(10).join(cards)}
                </div>
            </div>
        </section>
'''

start_marker = '<!-- Section 4: Get Started -->'
if start_marker in content:
    new_content = content.replace(start_marker, gallery_section + '\n        ' + start_marker)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Gallery added successfully.")
else:
    print("Could not find start marker.")
