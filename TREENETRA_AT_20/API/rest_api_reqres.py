import requests

#get requests
# i want to send request to the server for a get request, and server response back a data

'''url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Failed :- {response.status_code}')

for each_data in data['data']:
    if each_data['id']==8:
        print(each_data)'''

#params

# url = 'https://reqres.in/api/users'
#
#
# for i in range(1,11):
#     params = {'page':i}
#
#     response = requests.get(url,params=params)
#     print(f'page_number {i}',response.status_code)
#
# # if response.status_code == 200:
# #     print(response.json())
# # else:
# #     print(f'Failed :- {response.json()}')


#post  -- create resource

url = 'https://reqres.in/api/users'

payload = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url,json=payload)

if response.status_code == 201:
    print(response.json())
else:
    print(f'Failed :- {response.status_code}')

















