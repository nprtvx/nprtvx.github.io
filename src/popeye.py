from src.BaseClassesForNM import Style, Page

# css styles
css = """
   div {
      display: flex;
      font-size: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #26119226;
      border-radius: 26px;
      box-shadow: 5px 10px 18px #66b88b;
      padding: 2em;
   }
"""

# get style for popeye page
style = Style(extra_css=css)

# body for popeye page
body = """
   <div>
      nah! nothing here
   </div>
"""
# create page for popeye
page = Page(
    title="Popeye",
    body="",
    links=None,
    style=style,
    filename="popeye/index.html"
)
