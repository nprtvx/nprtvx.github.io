from src.page import Page
from src.style import Style

style = Style()

page = Page(title="popeye", body="", style=style, filename='index.html')


vr0000m = " vroooom ".capitalize();

page.body += f"""
    <div id="vroom">{vr0000m}</div>
"""

if __name__=="__main__":
    popeye = page
