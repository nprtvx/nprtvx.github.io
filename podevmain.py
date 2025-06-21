from os import system
import sys

def pomain():

	message = [msg for msg in sys.argv if msg != 'podevmain.py']
	print(message)
	message = ''.join(message)
	print(message)

	if message != '':
		system('git add .')
		system(f'git commit -m {message}')
		system(f'git push origin dev-main')
	else:
		print('arguments: '.upper(), sys.argv)
pomain()
