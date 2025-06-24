from src.BaseClassesForNM import Style, Page

# Page object for the Popeye page
page = Page( title="Popeye", body=HTML_BODY, links=None, style=style, 
    filename="popeye/index.html"
)

page.body = page.body + """ <div id="animated-bouncing-ball">
		animated bouncing ball
	</div> """ + page.style.extra_css = page.style.extra_css + """
	#animated-bouncing-ball {
		width: 25px; height: 25px; background-color: #26119287; 
		animation: bounce 8s infinite;
	}

"""
