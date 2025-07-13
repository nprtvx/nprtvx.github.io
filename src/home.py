from src.BaseClassesForNM import Page, Style

css = f"""
	.landing-poster {{
		position: absolute;
		
	        margin: 2em;
        	padding: 2em 0;
		border-radius: 2em;
	        box-shadow: 0 0 1em #29eaea inset;
	}}

	#landing-poster-heading {{
		font-size: xxx-large;
		color: #3692;
		text-shadow: 0 0 8px #abcdef;
		letter-spacing: 18px;
		padding: 0 2em;
		text-align: center;
	}}

	.card-div {{
		background-color: #29eaea87;
		padding: 1px 0;
		margin: 0 8em;
	}}
"""
style = Style(extra_css=css)

landing_poster = f"""
	<div class="landing-poster">
	        <h1 id="landing-poster-heading">welcome to neon monkey</h1>
	</div>
"""

after_landing_poster = f"""
	<div id="after-landing-poster">
		<div class="card-div"></div>
	</div>
"""

body = f"""
	{landing_poster}
	{after_landing_poster}
"""

page = Page(
    title="Home",
    body=body,
    links=[("About", "/about/"), ("Contact", "/contact/")],
    style=style,
    filename="index.html"
)

page.body = page.body + """
	<div id="adivelement">
		a div element to disaply some text
		To-Do:
			change it to a new version
			new implementation
	</div>
	<style>
		#adivelement {
			width: 48%;
			height: 26%;
			background-color: #489429;
			border-radius: 2rem;
			box-shadow: 0 0 0.5rem 0 inset;
		}
	</style>
"""
