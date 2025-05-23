from flask import Flask, jsonify, request

def create_app():
    """Creates and returns a Flask app instance"""
    app = Flask(__name__)

    # Sample employee data with nested dict structure
    employees = {
        1: {"Name": "Ajit", "Age": 28, "Department": "QC", "Salary": 78000, "Office": {"Location": "Mysur", "Floor": 3}},
        2: {"Name": "Sujit", "Age": 29, "Department": "Dev", "Salary": 82000, "Office": {"Location": "Mysur", "Floor": 2}},
        3: {"Name": "Manas", "Age": 26, "Department": "QA", "Salary": 76000, "Office": {"Location": "Pune", "Floor": 1}},
        4: {"Name": "Roshan", "Age": 26, "Department": "Prd", "Salary": 46000, "Office": {"Location": "Kolkata", "Floor": 1}},
        5: {"Name": "Satya", "Age": 28, "Department": "QA", "Salary": 87000, "Office": {"Location": "BLR", "Floor": 3}}
    }

    # Function to generate new employee ID
    def get_new_id():
        return max(employees.keys()) + 1 if employees else 1

    # GET method - Fetch employee data
    @app.route('/employees_data', methods=['GET'])
    def get_employee():
        return jsonify({'employees': employees}), 200

    # POST method - Create a new employee
    @app.route('/employees_data', methods=['POST'])
    def add_employee():
        data = request.json  # Get JSON payload from request
        new_id = get_new_id()

        # Validate required fields
        required_fields = ["Name", "Age", "Department", "Salary", "Office"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required field"}), 400

        employees[new_id] = {
            "Name": data["Name"],
            "Age": data["Age"],
            "Department": data["Department"],
            "Salary": data["Salary"],
            "Office": data["Office"]
        }

        return jsonify({"message": "Employee added", "id": new_id, "data": employees[new_id]}), 201

    # PUT method - Update employee details
    @app.route('/employees_data/<int:emp_id>', methods=['PUT'])
    def update_employees(emp_id):
        if emp_id not in employees:
            return jsonify({"error": "Employee not found"}), 404

        data = request.json  # Getting update payload
        employees[emp_id].update(data)

        return jsonify({"message": "Employee updated", "data": employees[emp_id]}), 200

    return app  # Return app instance

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

