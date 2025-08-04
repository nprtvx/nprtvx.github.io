import requests

username = 'popeye'
response = requests.post(f'nprtvx.github.io//account//users//{username}',
    data={"text": username}) if _.status_code == 202 else 'enter username'
print(response.text)