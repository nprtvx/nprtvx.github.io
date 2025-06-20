from src.BaseClassesForNM import Style, Page

# css styles
css = ""

# get style for popeye page
style = Style(extra_css=css)

# body for popeye page
body = "
   ello mastaru
"
# create page for popeye
page = Page(
    title="Popeye",
    body="",
    links=None,
    style=style,
    filename="popeye/index.html"
)
