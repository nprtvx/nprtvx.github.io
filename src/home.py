from src.page import Page
from src.style import Style

css = f"""
"""
style = Style(extra_css=css)

body = f"""
	{landing_poster}
"""

page = Page(
    title="Home",
    body=body,
    links=[("About", "/about/"), ("Contact", "/contact/")],
    style=style,
    filename="index.html"
)


page.body = """
	<div id='App'></div>
"""
import src.neonmonkey as neonmonkey


### EoF




