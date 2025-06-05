'''

dummy url create a resource server on application.
help of flask we will create onw api application---mvc (model -view - controller)
create auth token (jwt/outh2.0)
validate the response based on user

'''

import requests

# url = 'https://jsonplaceholder.typicode.com/posts'
#
# #auth
#
# #payload --- sending the data(json)
#
# payload = {
#     "userId": 1,
#     "title": "create a user",
#     "body": "create user auth"
#   },
#
# #post
#
# for i in range(1,11):
#
#     response = requests.post(url,json=payload)
#
#     print(response.status_code)
#     print(response.json())

#own api call in flask

# url = 'http://127.0.0.1:5000/posts'
#
# payload = {'title':'qwerty',
#            'body':'anagram'}
#
# response = requests.post(url,json=payload)
#
# # print(response.status_code)
# # print(response.json())
#
# response1 = requests.get(url)
#
# print(response1.status_code)
# print(response1.json())

#spesific id call

url = 'http://127.0.0.1:5000/posts/3'

response = requests.get(url)

print(response.json())

