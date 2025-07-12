from src.BaseClassesForNM import Page, Style

css = f"""
    #profile {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 1rem 0;
        list-style: none;
    }}
    #fullname {{
        color: #29e;
        font-size: 26px;
        margin: 1rem 0;
        text-transform: capitalize;
    }}
    #email {{
        color: #29e;
        font-size: 26px;
        margin: 1rem 0;
    }}
    h2 {{
        padding-left: 2rem;
        font-size: 26px;
        text-transform: uppercase;
        color: #954;
    }}
    p {{
        padding: 0 1rem;
        font-size: 21px;
    }}
    #logo {{
        display: flex;
        align-items: center;
        justify-content: center;
        color: #aaa;
        font-family: emoji;
        font-size: 8rem;
        background-color: #954;
        border-radius: 2rem;
        width: content-width;
        padding: 2rem;
    }}
"""
style = Style(extra_css=css)

body = f"""
    <h2>profile</h2>
    <p>strong, independent dentist from india working in the usa as a full time lead co-ordinator at "soul dental" west</p>
    <ul id='profile'>
        <li id='fullname'>tejitha yenupuri</li>
        <li id='email'>ytejita95@gmail.com</li>
    </ul>
    <div id='logo'>
        ][v|_
    </div>
"""

page = Page(
    title="MaW",
    body=body,
    links=[],
    style=style,
    filename="maw/index.html"
)