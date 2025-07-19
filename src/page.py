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

        head_html = [
		"<meta charset='UTF-8'>",
		"<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
  		f"<title>{title +' | '+ self.title if self.title != 'Home' else str('neon monkey'.title())}</title>",
		"<link rel='icon' type='image/x-icon' href='/assets/favicon.ico'>",
   		f"<style>{self.style.render()}</style>"
  	]

        return f"""<!DOCTYPE html>
	<html lang="en">
		<head>{''.join(head_html)}</head>
  		<body>{self.body}</body>
	</html>
	"""

    def write(self, directory="templates"):
        #print('''writing files''')
        path = os.path.join(directory, self.filename)
        #print(path)
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure parent directories exist
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
            #print(f"Wrote {path}")
