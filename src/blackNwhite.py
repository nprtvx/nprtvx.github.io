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
	@keyframes bounce {
		0% {
			background-color: #000000a8;
			width: 26px;
			height: 26px;
			border-radius: 26px 99px 36px 56px;
			box-shadow: 0 0 8px #a2a2a2a2 inset;
		}
		25% {
			background-color: #ff0000a8;
			width: 48px;
			height: 48px;
			border-radius: 26px 99px 36px 56px;
			box-shadow: 0 0 8px #a2a2a2a2 inset;
		}
		50% {
			background-color: #00ff00a8;
			width: 69px;
			height: 69px;
			border-radius: 26px 99px 36px 56px;
			box-shadow: 0 0 8px #a2a2a2a2 inset;
		}
		100% {
			background-color: #0000ffa8;
			width: 87px;
			height: 87px;
			border-radius: 26px 99px 36px 56px;
			box-shadow: 0 0 8px #a2a2a2a2 inset;
		}
	}
"""
