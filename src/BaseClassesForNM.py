import os

class Style:
    def __init__(self, body_bg="#001126", text_color="#abcdef", extra_css=""):
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
            }}

            h1 {{
        		color: #261192;
        		font-size: xxx-large;
        	}}
        """

        self.logo_img = f"""
            #nm-logo-img {{
                width: 100px;
                height: 100px;
                border-radius: 0.8rem;
            }}
        """

        self.nm_menu_item = f"""
            #nm-menu-item {{
        		text-decoration: none;
        		font-size: xx-large;
        		text-transform: capitalize;
        	}}
        """

        self.navbar_menu_nm = f"""
            #navbar-menu-nm {{
        		display: flex;
        		align-items: center;
        		justify-content: space-evenly;
        		width: 50%;
        		list-style: none;
        	}}

            {self.nm_menu_item}
        """

        self.navbar = f"""
            #nm-navbar {{
                position: sticky;
                top: 0;
                padding: 8px 26px;
                display: flex;
                align-items: center;
                justify-content: space-between;
		box-shadow = 0 0 8em 0 #261192 inset;
            }}

            {self.logo_img}
            {self.navbar_menu_nm}
        """

        self.footer_nm = f"""
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
					<img src="assets/logo.png" id="nm-logo-img" alt="LOGO-NM">
					<div id="nm-logo-img">
						{self.logo}
					</div>
					<ul id="navbar-menu-nm">
						<li><a href="/about/" id="nm-menu-item">about</a></li>
						<li><a href="/contact/" id="nm-menu-item">contact</a></li>
						<li><a href="/404/" id="nm-menu-item">404</a></li>
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
