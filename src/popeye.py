from src.page import Page
from src.style import Style


css = f"""
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
	#vroom {{
		background-color: #8926;
		width: 100px;
		height: 100px;
		border-radius: 50vmin;
	}}
"""
style = Style(extra_css=css)

vr0000m = " vroooom ".upper();

body = f"""
    <div id="vroom">{vr0000m}</div>
"""


page = Page(title="Home", body=body, style=style, filename='index.html')

page.body += body

