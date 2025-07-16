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
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}}

		body {{
				background-color: {self.body_bg};
				color: {self.text_color};
				overflow: hidden;
		}}

		#whole-package {{
			position: absolute;
			top: 0;
			right: 0;
			bottom: 0;
			left: 0;
		}}

		#navbar {{
			display: flex;
			align-items: center;
			justify-content: space-between;
			padding: 1rem 2rem;
		}}

		#logo {{
			display: flex;
			align-items: center;
			
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
        title = str('ne0NM0NkEy'.title())
	title = title.strip()
	title = ' '.join(title)
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
        self.body_html = f"""
		<body>
			<div id='whole-package'>
				<div id="navbar">
					<a class="logo" id="logo" href="/">
						<svg xmlns="https://www.w3.org/2000/svg/" viewBox="0 0 100 100" width="39px" id="logo-svg-nm">
							<polygon points="16,92 8,52 8,8 26,8 50,50 68,8 84,8 92,8 92,52 84,92 50,50 16,16 16,92" fill="#8926"></polygon>
							<polygon points="50,50 76,16 84,16 84,52 76,68 50,50" fill="#9006"></polygon>
						</svg>
						{title}
					</a>
					<div class="menu" id="menu-lines">
						<span id="menu-line"></span>
						<span id="menu-line"></span>
						<span id="menu-line"></span>
					</div>
				</div>
				{self.body}
				<div id='copy-right'>
					&copy; {title} {datetime.datetime.now().year}
				</div>
			</div>
		</body>
	"""

        return f"""
		<!DOCTYPE html>
		<html lang="en">
			{self.head_html}
			{self.body_html}
		</html>
	"""

    def write(self, directory="templates"):
        path = os.path.join(directory, self.filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure parent directories exist
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
            print(f"Wrote {path}")
