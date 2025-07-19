from src.page import Page
from src.style import Style


css = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}
    body {{
        background-color: #000d;
    }}
    #popeye {{
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: center;
        flex-direction: column;
    }}
"""
style = Style(extra_css=css)

vr0000m = " vroooom ".capitalize();

body = f"""
    <div id="vroom">{vr0000m}</div>
    <style>
	#vroom {{
		background-color: #8926;
		width: 100px;
		height: 100px;
		border-radius: 50vmin;
	}}
    </style>
"""


page = Page(title="home", body=body, style=style, filename='index.html')

page.body += body

