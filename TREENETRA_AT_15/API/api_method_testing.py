import requests
import json


#URL :- where data was stored
BASE_URL  = 'http://127.0.0.1:5000/employees_data'

#1. Test GET Method
'''dict-- python --- server -- api--- json---
str --- type case -- dict

loads--- json string convert into python dict -- server to fetch the data in python env.
dumps -- python dict conver json string-- python data send to server'''

def get_employess():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        return data

print(get_employess())

#use for loop
#recursive function
#test_data --
#variable = [dict]
#2. Test Post method
'''def post_employee():
    payload = {
        "Name":"Abhay",
        "Age":27,
        "Department":"QA",
        "Salary":54000,
        "Office":{"Loacation":"Bhubaneswar","Floor":3}
    }

    headers = {"Content-Type":"application/json"}
    response = requests.post(BASE_URL,data=json.dumps(payload),headers=headers)

    if response.status_code == 201:
        print(response.json())
    return None

new_emp_id = post_employee()'''


#3. Test Put method
'''def put_method_test(emp_id):
    data = get_employess()
    list_emp_id = [int(i) for i in data['employees']]
    if emp_id not in list_emp_id:
        print('\n Skipping put test as no employee was created')
        return


    update_data = {
        "Salary":89000,
        "Office":{"Loaction":"CHN","Floor":1}
    }

    headers = {"Content-Type": "application/json"}
    response = requests.put(f'{BASE_URL}/{emp_id}',data = json.dumps(update_data),headers=headers)
    if response.status_code == 200:
        return response.json()

emp_id = None
print(put_method_test(1))'''