import os

class Style:
    def __init__(self, body_bg="#000000", text_color="#abcdef", extra_css=""):
        self.body_bg = body_bg
        self.text_color = text_color
        self.extra_css = extra_css

    def render(self):
        return f"""
	* {{
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}}
        body {{
            background-color: {self.body_bg};
            color: {self.text_color};
            font-family: Arial, sans-serif;
        }}
	#nm-navbar {{
		position: sticky;
		top: 0;
		padding: 8px 26px;
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		background-color: #abcdef;
	}}
	#nm-logo-img {{
		width: 100px;
		height: 100px;
		border-radius: 0.8rem;
	}}
	h1 {{
		color: #261192;
		font-size: xxx-large;
	}}
        {self.extra_css}
	#nm-footer {{
		background-color: #abcdef;
		padding-top: 2em;
	}}
	h2 {{
		color: #261192;
		font-size: xx-large;
		padding-bottom: 10px;
	}}
	#nm-footer-copy {{
		color: #000000;
		padding: 2em 0;
	}}
        """

class Page:
    def __init__(self, title, body, links=None, style=None, filename="page.html"):
        self.title = title
        self.body = body
        self.links = links or []
        self.style = style or Style()
        self.filename = filename

    def render(self):
        links_html = " | ".join(
            f'<a href="{href}">{text}</a>' for text, href in self.links
        )
        return f"""<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="UTF-8">
				<title>{str('neon monkey'.title()) +" | "+ self.title if self.title != "Home" else str('neon monkey'.title())}</title>
				<link rel="icon" href="assets/icons/favicon.ico">
				<style>
					{self.style.render()}
				</style>
			</head>
			<body>
				<div id="nm-navbar">
					<img src="assets/landing-logo.PNG" id="nm-logo-img" alt="LOGO-NM">
					<h1>{str('neon monkey'.upper())}</h1>
					<ul>
						<li><a href="/about/">about</a></li>
						<li><a href="/contact/">contact</a></li>
						<li><a href="/popeye/">popeye</a></li>
					</ul>
				</div>
				{self.body}
				<div id='nm-footer'>
					<h2>{str('neon monkey'.upper())}</h2>
					<div id='nm-footer-copy'>&copy 2025 {str('neon monkey'.upper())}</div>
				</div>
			</body>
		</html>
	"""

    def write(self, directory="templates"):
        path = os.path.join(directory, self.filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure parent directories exist
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
            print(f"Wrote {path}")
