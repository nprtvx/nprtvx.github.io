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

	"""
        return f"""
            {self.default_style}
            {self.extra_css}
	"""
