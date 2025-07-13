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
    
    #try-diff-fonts {
            font-size: 180%;
            font-family: sans-serif;
            color: #abcd;
            height: 50vmin;
            background-color: #8365;
            box-shadow: 0 0 0.5rem 0;
            padding: 2rem;
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
	90% {
            transform: translateY(-20px);
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

page.body = page.body + """
	<div id="animated-bouncing-ball">
		animated bouncing ball
	</div>
"""

page.body = page.body + """
    <div id="try-diff-fonts">
        just a logo
    </div>
"""
page.style.extra_css = page.style.extra_css + """
	#animated-bouncing-ball {
		width: 25px;
		height: 25px;
		background-color: #26119287;
		animation: bounce 8s infinite;
	}
"""
