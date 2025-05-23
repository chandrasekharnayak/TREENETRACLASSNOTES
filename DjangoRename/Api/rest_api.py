# import requests
#
# end_point = int(input('enter the end point'))
#
# url = f'https://reqres.in/api/users?page={end_point}'
#
# response = requests.get(url)
#
#
# if end_point == 1:
#     if response.status_code == 200:
#         data = response.json()
#         ids = [i['id'] for i in data['data']]
#         print('these are ids number choce one of them:-',ids)
#         tell_me_id = int(input('Enter a id:-'))
#         res = [i['first_name'] for i in data['data'] if i['id']==tell_me_id]
#         print(res)
#
# elif end_point == 2:
#     if response.status_code == 200:
#         data = response.json()
#         ids = [i['id'] for i in data['data']]
#         print('these are ids number choce one of them:-', ids)
#         tell_me_id = int(input('Enter a id:-'))
#         res = [i['first_name'] for i in data['data'] if i['id'] == tell_me_id]
#         print(res)


# tell_me_id = int(input('Enter a id:-'))
# if response.status_code == 200:
#     data = response.json()
#     print(data)
    # res = [i['first_name'] for i in data['data'] if i['id']==tell_me_id]
    # print(res)

#post
'''import requests
import json

url = 'https://reqres.in/api/users'

payload = {'name': 'morpheus','job': 'leader'}
data = json.dumps(payload)

res = requests.post(url,data=data)

print(res.status_code)
print(res.json())'''


import requests
# url = 'https://reqres.in/api/users/2'
#
# data ={}
#
res = requests.put(url,data=data)
#
# print(res.status_code)














