from src.BaseClassesForNM import Style, Page

body = """
	<div id="animated-bouncing-ball" style="
    position: absolute;
    left: 50px;
"></div>
	<div id="cards-for-quotes">
		<div id="card-for-quote"></div>
	</div>
	<div id="cards-for-quotes">
		
	<div id="card-for-quote">
    <div class="card-heading" style="
    /* position: static; */
    font-size: 3em;
    padding: 1%;
    /* background: whitesmoke; */
    opacity: 0.3;
    border-radius: 1em;
">quote name</div>
</div><div id="card-for-quote">
    <div class="card-heading" style="
    /* position: static; */
    font-size: 3em;
    padding: 1%;
    /* background: whitesmoke; */
    opacity: 0.3;
    border-radius: 1em;
">quote name</div>
</div><div id="card-for-quote">
    <div class="card-heading" style="
    /* position: static; */
    font-size: 3em;
    padding: 1%;
    /* background: whitesmoke; */
    opacity: 0.3;
    border-radius: 1em;
">quote name</div>
</div></div>
"""

style = Style()

# Page object for the Popeye page
page = Page( title="Black & White", body=body, links=None, style=style, 
    filename="blackNwhite/index.html"
)

page.style.extra_css = page.style.extra_css + """
	footer, navbar {
		display: none;
	}
	body {
		background-color: #000000a8;
		color: a2a2a2a2;
	}

	#cards-for-quotes {
		display: flex;
		align-items: space-evenly;
		justify-content: space-evenly;
		height: 100vmin;
		background-color: #000000a4;
	}

	#card-for-quote {
		width: 250px;
		height: 250px;
		border-radius: 26px;
		box-shadow: 0 0 8px #a2a2a2a2;
	}

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
