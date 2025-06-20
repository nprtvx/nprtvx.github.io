import os

class Style:
    def __init__(self, body_bg="#261192", text_color="#abcdef", extra_css=""):
        self.body_bg = body_bg
        self.text_color = text_color
        self.extra_css = extra_css

    def render(self):
        return f"""
        body {{
            background-color: {self.body_bg};
            color: {self.text_color};
            font-family: Arial, sans-serif;
        }}
        {self.extra_css}
        """

class Page:
    nonlocal __NAME_OF_THE_APP
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
  <h1>{self.title if self.title != "Home" else str('neon monkey'.title())}</h1>
  {self.body}
  <div>{links_html}</div>
</body>
</html>
"""

    def write(self, directory="templates"):
        os.makedirs(directory, exist_ok=True)
        path = os.path.join(directory, self.filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
        print(f"Wrote {path}")
