import Page, Style

css = """
	div#page-404 {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 2.6em;
		flex-direction: column;
	}
	h1 {
		font-size: 250px;
		color: #fff8;
		font-family: emoji;
	}
	p {
		font-size: 18px;
	}
	a {
		text-decoration: none;
		color: #66baab;
	}
	a:hover {
		color: #261192;
	}
"""
style = Style(extra_css=css)

body = f"""
	<div id='page-404'>
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
