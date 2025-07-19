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
		justify-content: center;
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

body = "<div id='popeye'></div>"

page = Page(title="Home", body=body, style=style, filename='index.html')

def create_element(tag: str, id: str):
	return f'const {id} = document.createElement({tag});{id}.setAttribute('id', {id});'

scripts = [
	"const popeye = document.getElementById('popeye');",
	f"{create_element('div', 'greeting')}",
	f"{create_element('a', 'login')}",
	f"{create_element('a', 'signup')}",
	"greeting.append(login)",
	"greeting.append(signup)",
	"popeye.append(greeting),
	"////popeye.appendChild(vr00m);"
]

page.body += f"""<script>{''.join(scripts)}</script>"""

# eof
