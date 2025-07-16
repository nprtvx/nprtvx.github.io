

title = str("neonmonkey").title()


title = title.strip('')
TITLE =''
for letter in title:
	if letter.lower() in ['n', 'm', 'e']:
		TITLE += letter.upper()
	elif letter == 'o':
		TITLE += '0'
	else:
		TITLE += letter
title = ' '.join(TITLE)
