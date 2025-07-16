from page import Page
from style import Style

css = """
    h1 { text-transform: uppercase; }
"""

style = Style(extra_css=css)

jsapp = """
    const app = document.querySelector("App");
    
"""

body = f"""
    <div id="App"></div>
    <script>{jsapp}</script>
"""

page = Page(
    title="About",
    body=body,
    links=[("Home", "/"), ("Contact", "/contact/")],
    style=style,
    filename="about/index.html"
)
