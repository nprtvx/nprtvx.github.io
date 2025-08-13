from src.page import Page
from src.style import Style



body = f"""
<div class='bnw'>
<h1>black & white</h1>
<div class='hero'>
<h2>welcome</h2>
<ul>
<li><a href='/'>home</a></li>
<li><a href='/dOs'>OO</a></li>
<li><a href='#'></a></li>
<li><a href='#'></a></li>
</ul>
</div>
</div>
"""

css = f"""
.bnw {{
color: #000;
}}
.bnw h1 {{
font-size: 48px;

}}
.hero {{
display: flex;
align-items: center;
justify-content: center;
border-radius: 26px;
backgound: #8364;
}}
"""
style = Style(extra_css=css)

# Page object for the Popeye page
blackNwhite = Page( title="Black & White", body=body, links=None, style=style, 
    filename="blackNwhite/index.html"
)

bnw = blackNwhite

