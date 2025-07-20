


letterO = 'o'
doubleO = letterO*2

html = f"""
<div class='{doubleO}-div' id='{doubleO}-8'></div>
"""

script = f"""
const doubleO = document.getElementById('{doubleO}-8');
doubleO.textContent = {doubleO};
"""

style = f"""
.{doubleO}-div {{
color: #fff8;
background-color: #000d;
font-size: 32px;
animation: shadow-blink 2s infinite;
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

def get_doubleOshadow(html, style, script):
    page = Page(body=html+script, style=style, filename="doubleOshadow/index.html")

if __name__=="__main__":
    doubleOshadow = get_doubleOshadow()
    print(doubleOshadow)



# eof
# 