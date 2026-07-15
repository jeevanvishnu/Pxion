import sys
import re

file_path = r"C:\Users\jeeva\.gemini\antigravity-ide\brain\c495bc90-9356-4385-b2cd-91529910a4a2\.system_generated\steps\97\content.md"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract headings and bullet points using simple regex
    headings = re.findall(r'^(#{1,4})\s+(.+)$', content, re.MULTILINE)
    
    # Let's extract some text paragraphs that have keywords like feature, application, transparent
    paragraphs = content.split('\n\n')
    
    print("Headings:")
    for h in headings:
        print(f"{h[0]} {h[1].strip()}")
        
    print("\nRelevant Text Snippets:")
    count = 0
    for p in paragraphs:
        if 'transparent' in p.lower() and len(p.split()) > 10 and '<' not in p:
            print(f"- {p[:150]}...")
            count += 1
            if count > 10: break
            
except Exception as e:
    print("Error:", str(e))
