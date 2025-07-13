import os
from datetime import datetime

current_year = datetime.now().year

class Style:
    def __init__(self, body_bg="#000000", text_color="#8926", extra_css=""):
        self.body_bg = body_bg
        self.text_color = text_color
        self.extra_css = extra_css

    def render(self):
        self.defaultstyle = f"""
		* {{
			margin: o;
			padding: 0;
			box-sizing: border-box;
		}}

		@import url('https://fonts.googleapis.com/css2?family=Bitcount+Grid+Double:wght@100..900&family=Manufacturing+Consent&display=swap');

		body {{
			background-color: {self.body_bg};
			color: {self.text_color};
			font-family: monospace;
		}}

		#logo {{
			position: absolute;
			top: 2.6px;
			padding: 2rem;
		}}

		#menu-lines {{
			position: absolute;
			top: 2.6px;
			right: 2.6px;
			margin: 2rem;
		}}

		#menu-line {{
			padding: 0 1rem;
			background-color: #8926;
		}}
	"""

class Page:
    def __init__(self, title, body, links=None, style=None, filename="page.html", logo=None):
        self.title = title
        self.logo = logo
        self.body = body
        self.links = links or []
        self.style = style or Style()
        self.filename = filename

    def render(self):
        title = str('neon monkey'.title())
        links_html = " | ".join(
            f'<a href="{href}">{text}</a>' for text, href in self.links
        )

        self.head_html = f"""
		<head>
			<meta charset="UTF-8">
			<title>{title +" | "+ self.title if self.title != "Home" else str('neon monkey'.title())}</title>
			<link rel="icon" href="/assets/favicon.ico">
			<style>
				{self.style.render()}
			</style>
		</head>
        """

        return f"""<!DOCTYPE html>
		<html lang="en">
			{self.head_html}
			<body>
				<div class='logo' id='logo'>{title}</div>
				<div class='menu' id='menu-lines'>
					<span id='menu-line'></span>
					<span id='menu-line'></span>
					<span id='menu-line'></span>
				</div>

				{self.body}

				<div id='copy-right'>
					&copy; {title} {current_year}
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
