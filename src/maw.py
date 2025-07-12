from src.BaseClassesForNM import Page, Style

css = f"""
    #profile {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 1rem 0;
    }}
    #fullname {{
        color: #29e;
        background-color: #000d;
        font-size: 26px;
        margin: 1rem 0;
    }}
    #email {{
        color: #29e;
        background-color: #000d;
        font-size: 26px;
        margin: 1rem 0;
    }}
"""
style = Style(extra_css=css)

body = f"""
    <h2>profile</h2>
    <p>strong, independent dentist from india working in the usa as a full time lead co-ordinator at "soul dental" west</p>
    <ul id='profile'>
        <li id='fullname'>tejitha yenupuri</li>
        <li id='fullname'>ytejita95@gmail.com</li>
    </ul>
"""

page = Page(
    title="MaW",
    body=body,
    links=[],
    style=style,
    filename="maw/index.html"
)