from src.BaseClassesForNM import Page, Style

css = f"""
    h1 {{
        text-transform: uppercase;
    }}
    .landing-poster {{
        height: 120px;
        margin: 26px;
        padding: 26px;
        background: url("assets/landing-poster.jpg");
    }}
    #landing-poster-heading {{
        font-size: 48px;
        color: #261192;
    }}
"""
style = Style(extra_css=css)

body = f"""
    <section class="landing-poster">
        <h1 id="landing-poster-heading">welcome to neon monkey</h1>
    </section>
"""

page = Page(
    title="Home",
    body=body,
    links=[("About", "/about/"), ("Contact", "/contact/")],
    style=style,
    filename="index.html"
)
