import os

class Style:
    def __init__(self, body_bg="#000000", text_color="whitesmoke", extra_css=""):
        self.body_bg = body_bg
        self.text_color = text_color
        self.extra_css = extra_css

    def render(self):
        self.defaultstyle = f"""
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                background-color: {self.body_bg};
                color: {self.text_color};
                font-family: Arial, sans-serif;
		height: 100vh;
		width: 100vw;
            }}
        """

        self.logo_img = f"""
            #nm-logo-img {{
                width: 100%;
                height: 100%;
                border-radius: 1em;
            }}
            #img-link-logo {{
		opacity: 0.8;
		height: 150px;
		width: 250px;
            }}

        """

        self.nm_menu_item = f"""
		#nm-menu-item {{
        		text-decoration: none;
        		font-size: 1.5em;
        		text-transform: uppercase;
			letter-spacing: 0.2em;
			color: whitesmoke;
			opacity: 0.5;
			padding: 1em;
        	}}

		#nm-menu-item:hover {{
			padding: 1em;
			border: 1em #29eaea87;
			border-radius: 2em;
		}}
        """

        self.navbar_menu_nm = f"""
            #navbar-menu-nm {{
        		display: flex;
        		align-items: center;
        		justify-content: space-between;
        		list-style: none;
        	}}

            {self.nm_menu_item}
        """

        self.navbar = f"""
            #nm-navbar {{
                display: flex;
                align-items: center;
                justify-content: space-between;
		box-shadow: 0 0 2em 0 #fff8 inset;
                height: 10vh;
		position: sticky;
		top: 0;
            }}

            {self.logo_img}
            {self.navbar_menu_nm}
        """

        self.footer_nm = f"""
		#nm-footer {{
			box-shadow: 0 0 3em #fff8 inset;
			padding: 0 1em;
		}}
		#footer-copy {{
			text-shadow: 0 0 #0008;
			color: transparent;
			margin: 1em 0;
		}}
        """

        return f"""
            {self.defaultstyle}
            {self.navbar}
            {self.extra_css}
            {self.footer_nm}
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
			<link rel="icon" href="assets/icons/favicon.ico">
			<style>
				{self.style.render()}
			</style>
		</head>
        """

        return f"""<!DOCTYPE html>
		<html lang="en">
			{self.head_html}

			<body>
				<div id="nm-navbar">
					<a href="/" id="img-link-logo">
						<img src={self.logo} id="nm-logo-img" alt="LOGO-NM">
					</a>

					<ul id="navbar-menu-nm">
						<li id='li-menu-item'><a href="/about/" id="nm-menu-item">about</a></li>
						<li id='li-menu-item'><a href="/contact/" id="nm-menu-item">contact</a></li>
						<li id='li-menu-item'><a href="/404/" id="nm-menu-item">404</a></li>
					</ul>
				</div>

				{self.body}

				<div id='nm-footer'>
					<div id='footer-copy'>&copy 2025 {str('neon monkey'.upper())}</div>
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
