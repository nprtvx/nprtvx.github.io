from src.page import Page
from src.style import Style
print('popeye in src after imports')
style = Style()

vr0000m = " vroooom ".capitalize();
print('popeye page ', vr0000m)

body = f"""
    <div id="vroom">{vr0000m}</div>
"""
print(body)

page = Page(title="popeye", body=body, style=style, filename='index.html')
