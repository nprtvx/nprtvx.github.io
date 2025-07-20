

from src.page import Page
from src.style import Style

letterO = 'o'
doubleO = letterO*2

html = f"""
<div class='{doubleO}-div' id='{doubleO}-8'></div>
"""

script = f"""<script>
const {doubleO} = document.getElementById('{doubleO}-8');
{doubleO}.textContent = ` {doubleO} `;
</script>
"""

css = f"""
.{doubleO}-div {{
color: #fff8;
background-color: #000d;
font-size: 48vmin;
font-weight: 800;
--webkit-text-stroke: 2px #cdef;
animation: shadow-blink 2s infinite;
position: absolute;
top: 10vmin;
left: 10vmin;
width: 80vmin;
display: center;
align-items: center;
justify-content: center;
font-family: system-ui;
}}

@keyframes shadow-blink {{
.{doubleO}-div {{
from {{
text-shadow: 0 0 #fff;
}}
to {{
text-shadow: 0 26px #fff;
}}
}}
}}
"""

style = Style(extra_css=css)

def get_doubleOshadow(html, style, script):
    page = Page(title=f'{doubleO}', body=html+script, style=style, filename="doubleOshadow/index.html")
    return page


doubleOshadow = get_doubleOshadow(html,style, script)

# eof
# 