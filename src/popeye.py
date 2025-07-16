from src.page import Page
from src.style import Style
print('popeye in src after imports')
style = Style()

vr0000m = " vroooom ".capitalize();
print('popeye page ', vr0000m)

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
print(body)

page = Page(title="popeye", body=body, style=style, filename='index.html')

page.body += body
