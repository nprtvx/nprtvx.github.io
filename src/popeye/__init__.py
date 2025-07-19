from src.page import Page
from src.style import Style
from src.cars import gallery

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
  		color: #199b;
    		background: transparent;
      		border: 4px solid;
		border-radius: 1em;
  		padding: 1rem 2rem;
    		margin: 0.5rem 0;
      		width: 100%;
		text-align: center;
    	}}
     	#greetinglinks {{
      		display: flex;
		align-items: center;
  		justify-content: space-evenly;
    	}}
     	#greeting {{
      		font-size: 4rem;
		color: #199b;
  	}}
   * {{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}}

.hero {{
	width: 100%;
	height: 100vh;
	background-image: linear-gradient(rgba(12, 3, 51, 0.3), rgba(12, 3, 51, 0.3));
	position: relative;
	padding: 0 5%;
	display: flex;
	align-items: center;
	justify-content: center;
}}

nav {{
	width: 100%;
	position: absolute;
	top: 0;
	left: 0;
	padding: 20px 8%;
	display: flex;
	align-items: center;
	justify-content: space-between;
}}

nav .logo {{
	width: 80px;
}}

nav ul li {{
	list-style: none;
	display: inline-block;
	margin-left: 40px;

}}

nav ul li a {{
	text-decoration: none;
	color: #fff;
	font-size: 17px;
}}

.content {{
	text-align: center;
}}

.content h1 {{
	font-size: 160px;
	color: #fff;
	font-weight: 800;
	transition: 0.5s;
}}

.content h1:hover {{
	-webkit-text-stroke: 2px #fff;
	color: transparent;
	transition: 0.5s;
}}

.content a {{
	text-decoration: none;
	display: inline-block;
	color: #fff;
	font-size: 24px;
	border: 2px solid;
	padding: 14px 70px;
	border-radius: 50px;
	margin-top: 20px;
}}

.back-video {{
	position: absolute;
	right: 0;
	bottom: 0;
	z-index: -1;
}}

@media (min-aspect-ratio: 16/9) {{
	.bck-video {{
		width: 100%;
		height: auto;
	}}
}}

@media (max-aspect-ratio: 16/9) {{
	.back-video {{
		width: auto;
		height: 100%;
	}}
}}
"""
style = Style(extra_css=css)

vr0000m = " vroooom ".upper();

#body = "<div id='popeye'></div>"

page = Page(title="Home", body="", style=style, filename='index.html')

def create_element(tag: str, id: str):
	return f"const {id} = document.createElement('{tag}');{id}.setAttribute('id', '{id}');"

scripts = [
	"const popeye = document.getElementById('popeye');",
	f"{create_element('h2', 'greeting')}",
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
	"popeye.append(greeting);",
	"popeye.append(greetinglinks);",
	"loginlink.addEventListener('click', () => {{ popeye.remove(greeting, greetinglinks); popeye.append(login); }});",
	"signuplink.addEventListener('click', () => {{ popeye.remove(greeting, greetinglinks); popeye.append(signup); }});",
	"////popeye.appendChild(vr00m);"
]

page.body += f"""
<div class="hero">

			<video autoplay loop muted plays-inline class="back-video">
				<source src="https://videos.pexels.com/video-files/855433/855433-hd_1864_1048_25fps.mp4" type="video/mp4">
			</video>

			<nav class="navbar">
				<img src="https://images.pexels.com/photos/248539/pexels-photo-248539.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="logo">
				<ul class="menu">
					<li><a href="#">HOME</a></li>
					<li><a href="#">DASHBOARD</a></li>
					<li><a href="#">ABOUT</a></li>
					<li><a href="#">CONTACT</a></li>
				</ul>
			</nav>

			<div class="content">
				<h1>coffee shop</h1>
				<a href="#">explore</a>
			</div>
		</div>
  <div>
  {''.join(gallery.image_elements)}
  </div>
  """

#page.body += f"""<script>{''.join(scripts)}</script>"""

# eof
