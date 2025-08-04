import requests

username = 'popeye'
response = requests.post(f'https:////nprtvx.github.io//account//users//{username}',
    data={"text": username})
if response.status_code == 200:
    print('success')
else:
    print('enter username')
print(response.text)