#json = java scripts object notation

# json --- validation, auth,data storaged

import json

# dumps,dump.loads.load

# json.dumps() -- convert the python object to json string
'''
di = {
    'Name':'Suvam',
    'Age':27,
    'Salary':67000
}

json_string = json.dumps(di)
print(json_string)

print(type(json_string))'''

#query

'''import requests

url = 'https://reqres.in/'
get= 'api/users?page=2'

response = requests.get(f'{url}{get}')

if response.status_code==200:
    data = response.json()

    json_dumps = json.dumps(data)
    print(type(json_dumps))'''


#json.loads()

''''import requests
import json
with open('json_file_data.json','r') as file:
    data = file.read()
    json_str_di = json.loads(data)

    url = 'https://reqres.in/api/users/2'
    data = {
        'name':'suryakanta',
        'job':'QA'
    }

    responce = requests.put(url,json=data)

    if responce.status_code==200:
        print(responce.json())
        print('Ok')

''''






















