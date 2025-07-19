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
 	#login, #signup {{
		width: 400px;
  		height: 400px;
    		display: flex;
      		align-items: center;
		justify-content: center;
  	}}
   	#loginlink, #signuplink {{
		text-decoration: none;
  		color: #8926;
    		background: transparent;
      		border: 1px solid;
		border-radius: 1em;
  		padding: 1em;
    		margin: 1em;
    	}}
     	#greetinglinks {{
      		display: flex;
		align-items: center;
  		justify-content: space-evenly;
    	}}
"""
style = Style(extra_css=css)

vr0000m = " vroooom ".upper();

body = "<div id='popeye'></div>"

page = Page(title="Home", body=body, style=style, filename='index.html')

def create_element(tag: str, id: str):
	return f"const {id} = document.createElement('{tag}');{id}.setAttribute('id', '{id}');"

scripts = [
	"const popeye = document.getElementById('popeye');",
	f"{create_element('div', 'greeting')}",
	f"{create_element('a', 'loginlink')}",
	f"{create_element('a', 'signuplink')}",
	f"{create_element('form', 'login')}",
	f"{create_element('form', 'signup')}",
	f"{create_element('div', 'greetinglinks')}",
	"greeting.textContent = 'welcome';",
	"loginlink.textContent = 'login';",
	"signuplink.textContent = 'sign up';",
	"loginlink.setAttribute('href', '#login');",
	"signuplink.setAttribute('href', '#signup');",
	"greetinglinks.append(loginlink);",
	"greetinglinks.append(signuplink);",
	"greeting.append(greetinglinks);",
	"popeye.append(greeting);",
	"loginlink.addEventListener('click', () => {{ popeye.remove(greeting); popeye.append(login); }});",
	"signuplink.addEventListener('click', () => {{ popeye.remove(greeting); popeye.append(signup); }});",
	"////popeye.appendChild(vr00m);"
]

page.body += f"""<script>{''.join(scripts)}</script>"""

# eof
