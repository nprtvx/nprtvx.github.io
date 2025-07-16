from src.page import Page
from src.style import Style

style = Style()

vr0000m = " vroooom ".capitalize();

body = f"""
    <div id="vroom">{vr0000m}</div>
"""

page = Page(title="popeye", body=body, style=style, filename='index.html')

