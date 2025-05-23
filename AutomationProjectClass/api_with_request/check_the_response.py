import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    print(f'sucessful:- {response.status_code}')
    data = response.json()
    print(data)
else:
    print(f'failed:- {response.status_code}')