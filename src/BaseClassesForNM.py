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
		background-color: #66baab;
		height: 8vmin;
		position: sticky;
		z-axis: 999;
	}}
        {self.extra_css}
	#nm-footer {{
		background-color: #66baab;
		padding-top: 2em;
	}}
	#nm-footer h1 {{
		color: #261192;
		font-size: 2.6rem;
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
				<style>
					{self.style.render()}
				</style>
			</head>
			<body>
				<div id='nm-navbar'>
					<img src='assets/landing-poster.jpg' id='nm-logo-img' alt={'logo nm'.upper()} >
				</div>
				{self.body}
				<div id='nm-footer'>
					<h2>{str('neon monkey'.title())}</h2>
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
