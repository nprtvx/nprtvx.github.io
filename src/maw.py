from src.page import Page
from src.style import Style

css = f"""
	#maw-img {{
		position: absolute;
		width: 250px;
		height: 420px;
		border-radius: 2rem;
		padding: 2.6px;
		background: #0004;
	}}
"""
style = Style(extra_css=css)

body = f"""
	<div id='maw-img'>
		<img src='https://www.canva.com/content-partner/?utm_medium=acquisitions&utm_source=pexels&utm_campaign=predownload%20button&utm_content=edit%20in%20canva&external-id=792222&image-url=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F792222%2Fpexels-photo-792222.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26w%3D8000%26h%3D8000%26fit%3Dmax' alt='profile-image' />
	</div>
	<div id='profile-details>
		<ul id='maw-details'>
			<li class='profile-details' id='fullname'></li>
			<li class='profile-details' id='email'></li>
			<li class='profile-details' id='phone'></li>
		</ul>
	</div>
"""

page = Page(
    title="MaW",
    body=body,
    links=[],
    style=style,
    filename="maw/index.html"
)
