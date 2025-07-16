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
			text-decoration: none;
			justify-content: space-evenly;
			font-size: 63px;
			color: #8926;
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
			padding: 3px 36px;
			background-color: #8926;
			border-radius: 1rem;
			margin: 8px;
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
