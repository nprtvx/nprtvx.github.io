from src.BaseClassesForNM import Page, Style

css = f"""
	h1 {
		font-size: 8em;
		padding: 26px;
	}
	div {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 2.6em;
		flex-direction: column;
	}
	p {
		font-size: 48px;
	}
	a {
		text-decoration: none;
		color: #66baab;
	}
	a:hover {
		color: #261192;
		background-color: #66baab;
	}
"""
style = Style(extra_css=css)

body = f"""
	<div>
		<h1>404</h1>
		<p>wanna go home? <a href="/">click here</a></p>
	</div
"""

page = Page(
    title="404",
    body=body,
    style=style,
    filename="404/index.html"
)
