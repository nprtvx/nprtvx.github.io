from src.page import Page
from src.style import Style

css = f"""
	.landing-poster {{
	        margin-top: 8rem;
	}}

	#landing-poster-heading {{
		font-size: 26px;
		letter-spacing: 2.6px;
		padding-left: 2em;
	}}

"""
style = Style(extra_css=css)

# include all these in landing poster


landing_poster = f"""
	<div class="landing-poster">
	        <h1 id="landing-poster-heading">welcome to neon monkey</h1>
	</div>
"""

body = f"""
	{landing_poster}
"""

page = Page(
    title="Home",
    body=body,
    links=[("About", "/about/"), ("Contact", "/contact/")],
    style=style,
    filename="index.html"
)

page.body = """
	<div id='App'></div>
"""
import src.neonmonkey as neonmonkey

# page.body += f"<h1 id='title'>{neonmonkey.title}</h1>"

# page.body += f
"""
	<div id='logo-nm'>
		{neonmonkey.title}
	</div>
	<style>
		#logo-nm {{
			position: absolute;
			left: 48px;
			top: 150px;
			width: 300px;
			height: 100px;
		}}
	</style>
"""

# page.body += f
"""
	<svg xmlns="https://www.w3.org/2000/svg/" viewBox="0 0 100 100" width='100px'>
		<polygon points="16,92 8,52 8,8 26,8 50,50 68,8 84,8 92,8 92,52 84,92 50,50 16,16 16,92" fill="#892"></polygon>
		<polygon points="50,50 76,16 84,16 84,52 76,68 50,50" fill="#900"></polygon>
	</svg>
"""

from src.cars import vrzerozerom as vroom

home.body = vroom.body