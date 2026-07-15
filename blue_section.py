from bs4 import BeautifulSoup

file_path = 'c:/Users/jeeva/OneDrive/Documents/Bebright/customized-led-products.html'
with open(file_path, 'r', encoding='windows-1252', errors='replace') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

outdoor = soup.find('section', id='outdoor-details')
if outdoor:
    # Remove light-theme class
    classes = outdoor.get('class', [])
    if 'light-theme' in classes:
        classes.remove('light-theme')
    outdoor['class'] = classes
    
    # Change background to a premium deep blue gradient
    # Retain the padding style
    outdoor['style'] = "padding: 80px 0; background: linear-gradient(135deg, #001A4D 0%, #003399 100%);"
    
    # We might need to ensure the section subtitle is visible, because in dark theme it's usually var(--orange) which looks good.
    # The default text colors in feature cards are white, which will look perfect on this blue background.

with open(file_path, 'w', encoding='windows-1252') as f:
    f.write(str(soup))
print("Outdoor section updated to blue theme")
