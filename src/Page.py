import os
import datetime

class Page:
    def __init__(self, title, body, links=None, style=None, filename="page.html", logo=None):
        self.title = title
        self.logo = logo
        self.body = body
        self.links = links or []
        self.style = style or Style()
        self.filename = filename

    def render(self):
        title = str('Ne0NM0NkEy')
        title = title.strip()
        title = f"{title[:3]} {title[3:7]} {title[7:]}"
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
