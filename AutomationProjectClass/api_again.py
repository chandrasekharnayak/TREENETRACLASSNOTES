import requests
import json

#get

'''base_url = 'https://reqres.in/'
get_end_point= 'api/users?page=2'

response = requests.get(f'{base_url}{get_end_point}')

if response.status_code == 200:
    data = response.json()
    id = int(input('Enter the id number:-'))
    result = data['data']
    for i in result:
        if i['id']==id:
            print(i['email'])'''


base_url = 'https://reqres.in/'
post_end_point= 'api/users'

data = {
    "name": "morpheus",
    "job": "leader"
}

json_data = json.dumps(data)
response = requests.post(f'{base_url}{post_end_point}',data=json_data)

if response.status_code == 201:
    print(response.status_code)
    print(response.json())
else:
    print(response.status_code)