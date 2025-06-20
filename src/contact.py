from src.BaseClassesForNM import Page, Style

css = """
    h1 { text-transform: uppercase; }
"""

style = Style(extra_css=css)

body = """
    <p>Email us at <a href='mailto:info@example.com'>info@example.com</a>.</p>
"""

page = Page(
    title="Contact",
    body=body,
    links=[("Home", "/"), ("About", "/about/")],
    style=style,
    filename="contact/index.html"
)
