import os
import datetime

class Style:
    def __init__(self, body_bg="#000000", text_color="#8926", extra_css=""):
        self.body_bg = body_bg
        self.text_color = text_color
        self.extra_css = extra_css

    def render(self):
        self.default_style = f"""
		* {{
			margin: o;
			padding: 0;
			box-sizing: border-box;
		}}

		body {{
			background-color: {self.body_bg};
			color: {self.text_color};
			font-family: monospace;
		}}

		#logo {{
			position: absolute;
			top: 2rem;
			left: 2rem;
			font-size: 48px;
			font-family: "Bitcount Grid Double", system-ui;
			font-optical-sizing: auto;
			font-weight: 500;
			font-style: normal;
			font-variation-settings:
				"slnt" 0,
				"CRSV" 0.5,
				"ELSH" 0,
				"ELXP" 0;
		}}

		#menu-lines {{
			position: absolute;
			right: 2rem;
			top: 2rem;
			display: flex;
			align-items: center;
			justify-content: space-evenly;
			flex-direction: column;
		}}

		#menu-line {{
			padding: 2.6px 14px;
			background-color: #8926;
			border-radius: 1rem;
			margin: 4px;
		}}

		#copy-right {{
			font-size: 26px;
			position: absolute;
			bottom: 2rem;
			left: 2rem;
			text-transform: uppercase;
			font-family: 'Bitcount Grid Double', system-ui;
		}}
	"""
        return f"""
		{self.default_style}
		{self.extra_css}
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
				@import url('https://fonts.googleapis.com/css2?family=Bitcount+Grid+Double:wght@100..900&family=Permanent+Marker&display=swap');
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
					&copy; {title} {datetime.datetime.now().year}
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
