import pytest
import requests
import json

from BatchCodeData.Flask.flask_api.api_test_file import response

#URL :- where data was stored
BASE_URL  = 'http://127.0.0.1:5000/employees_data'

#Test Data
valida_employee_data = {}

invalid_employee_data= {}

update_employee_data = {}

total_api = 5

def test_get_employee():
    ''' Test the GET method fetch all employees'''
    response = requests.get(BASE_URL)
    assert response.status_code==200
    assert isinstance(response.json(),dict)
    assert 'employees' in response.json()
    assert  total_api == len([int(i) for i in response.json()['employees']]),'data count is mismatch'
    with open('test_data/actutal_total_employee.json','r') as json_fil:
        actual_read_data = json.loads(json_fil.read())
        expected_data = response.json()
        actual_read_data_list = [(key1,value1['Name']) for key,value in actual_read_data.items() for key1,value1 in value.items()]
        expected_data_list = [(key1,value1['Name']) for key,value in expected_data.items() for key1,value1 in value.items()]
        assert actual_read_data_list == expected_data_list

