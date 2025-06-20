from src.BaseClassesForNM import Page, Style

css = """
    h1 { text-transform: uppercase; }
"""

style = Style(extra_css=css)

body = """
    <p>This site is generated by Python scripts. Enjoy browsing!</p>
"""

page = Page(
    title="About",
    body=body,
    links=[("Home", "/"), ("Contact", "/contact/")],
    style=style,
    filename="about/index.html"
)
