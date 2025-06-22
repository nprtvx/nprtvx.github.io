from src.BaseClassesForNM import Style, Page

# CSS styles for the Popeye page
CSS_STYLES = """
    #popeye-nahnothing {
        display: flex;
        font-size: 48px;
        align-items: center;
        justify-content: center;
        background-color: #26119226;
        border-radius: 26px;
        box-shadow: 5px 10px 18px #66b88b;
        padding: 2em;
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    .animated-box {
        width: 100px;
        height: 100px;
        background-color: #ff6347;
        margin: 20px;
        animation: bounce 2s infinite;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-30px);
        }
        60% {
            transform: translateY(-15px);
        }
    }
"""

# HTML body for the Popeye page
HTML_BODY = """
    <div id='popeye-nahnothing'>
        nah! nothing here
    </div>
    <div class='animated-box'>
        Animated Box
    </div>
"""

# Style object for the Popeye page
style = Style(extra_css=CSS_STYLES)

# Page object for the Popeye page
page = Page(
    title="Popeye",
    body=HTML_BODY,
    links=None,
    style=style,
    filename="popeye/index.html"
)