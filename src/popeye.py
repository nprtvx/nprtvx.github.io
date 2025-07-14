from src.BaseClassesForNM import Style, Page

# CSS styles for the Popeye page
CSS_STYLES = """
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    @keyframes something {
        0% {
            opacity: 0;
        }
        20% {
            opacity: 1;
        }
        40% {
            opacity: 0.4;
        }
        60% {
            opacity: 1;
        }
        80% {
            opacity: 0.8;
        }
        100% {
            opacity: 1;
        }
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
    
    #intro {
        font-size: 26px;
        padding-left: 2em;
    }
"""

# HTML body for the Popeye page
HTML_BODY = """
    <div id='intro'>
        popeye the sailor man
    </div>
    <div id='something-interesting'>
        let me know if you got anything interesting
	<input type='text' id='in-something-interesting' />
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
