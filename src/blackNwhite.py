from src.page import Page
from src.style import Style



body = """
<div class='bnw'>
<h1>black & white</h1>
<div class='hero'>
<h2>welcome</h2>
<ul>
<li><a href='#'></a></li>
<li><a href='#'></a></li>
<li><a href='#'></a></li>
<li><a href='#'></a></li>
</ul>
</div>
</div>
"""

css = """
.bnw {{
color: #000;
}}
.bnw h1 {{
font-size: 48px;

}}
"""
style = Style(extra_css=css)

# Page object for the Popeye page
blackNwhite = Page( title="Black & White", body=body, links=None, style=style, 
    filename="blackNwhite/index.html"
)

bnw = blackNwhite

