from src.BaseClassesForNM import Page, Style

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

page.body += f"<h1 id='title'>{neonmonkey.title}</h1>"

page.body += f"""
	<div id='logo-nm'>
		{neonmonkey.title}
	</div>
	<style>
		position: absolute;
		left: 48px;
		top: 150px;
		width: 300px;
		height: 100px;
	</style>
"""
