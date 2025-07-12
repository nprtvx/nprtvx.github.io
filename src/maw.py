from src.BaseClassesForNM import Page, Style

css = f"""
	.landing-poster {{
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
    #maw-div {{
        color: #29e;
        background-color: #000d;
        font-size: 12rem;
        height: 100vmin;
        display: flex;
        aligin-items: center;
        justify-content: center;
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
    <div id='maw-div'>ello mawduuuu iduvu</div>
"""

page = Page(
    title="MaW",
    body=body,
    links=[],
    style=style,
    filename="index.html"
)