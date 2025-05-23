# import json
# import os
#
# BASE_URL = "/employees_data"
#
# # Load test data from JSON files
# def load_json(file_name):
#     with open(os.path.join(os.path.dirname(__file__), "test_data", file_name)) as f:
#         return json.load(f)
#
# def test_get_employees(client):
#     """Test GET method - Fetch all employees"""
#     response = client.get(BASE_URL)
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "employees" in data
#     assert isinstance(data["employees"], dict)
#
# def test_post_employee_success(client):
#     """Test POST method - Add new employee (Valid data)"""
#     new_employee = load_json("test_post_data.json")
#     response = client.post(BASE_URL, json=new_employee)
#     assert response.status_code == 201
#     data = response.get_json()
#     assert "message" in data
#     assert data["message"] == "Employee added"
#     assert "id" in data
#
# def test_post_employee_failure(client):
#     """Test POST method - Add new employee (Missing fields)"""
#     invalid_employee = load_json("test_post_invalid.json")
#     response = client.post(BASE_URL, json=invalid_employee)
#     assert response.status_code == 400
#     data = response.get_json()
#     assert "error" in data
#
# def test_put_employee_success(client):
#     """Test PUT method - Update employee (Valid update)"""
#     emp_id = 1  # Assuming employee ID 1 exists
#     update_data = load_json("test_put_data.json")
#     response = client.put(f"{BASE_URL}/{emp_id}", json=update_data)
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "message" in data
#     assert data["message"] == "Employee updated"
#     assert "data" in data
#     assert data["data"]["Salary"] == 90000
#     assert data["data"]["Department"] == "Finance"
#
# def test_put_employee_failure(client):
#     """Test PUT method - Update employee (Invalid ID)"""
#     emp_id = 9999  # Assuming this ID does not exist
#     update_data = load_json("test_put_data.json")
#     response = client.put(f"{BASE_URL}/{emp_id}", json=update_data)
#     assert response.status_code == 404
#     data = response.get_json()
#     assert "error" in data
#
# def test_put_employee_invalid_data(client):
#     """Test PUT method - Update employee (Invalid data format)"""
#     emp_id = 1  # Assuming employee ID 1 exists
#     update_data = load_json("test_put_invalid.json")
#     response = client.put(f"{BASE_URL}/{emp_id}", json=update_data)
#     assert response.status_code == 200  # Should still pass but data is incorrect
#     data = response.get_json()
#     assert "message" in data



import json

BASE_URL = "http://127.0.0.1:5000/employees_data"

def test_get_employees(client):
    """Test GET method - Fetch all employees"""
    response = client.get(BASE_URL)
    assert response.status_code == 200
    data = response.get_json()
    assert "employees" in data
    assert isinstance(data["employees"], dict)

def test_post_employee_success(client):
    """Test POST method - Add new employee (Valid data)"""
    new_employee = {
        "Name": "Rahul",
        "Age": 30,
        "Department": "HR",
        "Salary": 70000,
        "Office": {"Location": "Mumbai", "Floor": 2}
    }
    response = client.post(BASE_URL, json=new_employee)
    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Employee added"
    assert "id" in data

def test_post_employee_failure(client):
    """Test POST method - Add new employee (Missing fields)"""
    invalid_employee = {
        "Name": "Sam",
        "Age": "Thirty",  # Invalid data type
        "Salary": 65000  # Missing Department & Office
    }
    response = client.post(BASE_URL, json=invalid_employee)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_put_employee_success(client):
    """Test PUT method - Update employee (Valid update)"""
    emp_id = 1  # Assuming employee ID 1 exists
    update_data = {"Salary": 90000, "Department": "Finance"}
    response = client.put(f"{BASE_URL}/{emp_id}", json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Employee updated"
    assert "data" in data
    assert data["data"]["Salary"] == 90000
    assert data["data"]["Department"] == "Finance"

def test_put_employee_failure(client):
    """Test PUT method - Update employee (Invalid ID)"""
    emp_id = 9999  # Assuming this ID does not exist
    update_data = {"Salary": 85000}
    response = client.put(f"{BASE_URL}/{emp_id}", json=update_data)
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

