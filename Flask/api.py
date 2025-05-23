import requests

url = 'http://172.105.54.198:5000/api/users'

response = requests.get(url)

data = response.json()
for i in data:
	if i['first_name'] =='ishwari':
		print(i)




# payload = {
# 	'confirm_password': 'qwerty',
# 	'email_id': 's.csnayak108@gmail.com',
# 	'first_name': 'Krishna',
# 	'last_name': 'Nayak',
# 	'manager_name': 'SDFGH',
# 	'password': 'qwerty',
# 	'phone_no': '2345678'
# }
#
# response = requests.post(url,data=payload)
#
# print(response.status_code)