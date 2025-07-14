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

        return f"""
		<!DOCTYPE html>
		<html lang="en">
			{self.head_html}
			<body>
				<div id='whole-package'>
					<div id='navbar'>
						<a class='logo' id='logo'>{title}</a>
						<div class='menu' id='menu-lines'>
							<span id='menu-line'></span>
							<span id='menu-line'></span>
							<span id='menu-line'></span>
						</div>
					</div>

					{self.body}

					<div id='copy-right'>
						&copy; {title} {datetime.datetime.now().year}
					</div>
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