from flask import Flask,jsonify,request


app = Flask(__name__)

#get, post, put

#sample employee data with nested dict structure
employees = {
    1: {"Name":"Ajit","Age":28,"Department":"QC","Salary":78000,"Office":{"Location":"Mysur","Floor":3}},
    2: {"Name":"Sujit","Age":29,"Department":"Dev","Salary":82000,"Office":{"Location":"Mysur","Floor":2}},
    3: {"Name":"Manas","Age":26,"Department":"QA","Salary":76000,"Office":{"Location":"Pune","Floor":1}},
    4: {"Name":"Roshan","Age":26,"Department":"Prd","Salary":46000,"Office":{"Location":"Kolkata","Floor":1}},
    5: {"Name":"Satya","Age":28,"Department":"QA","Salary":87000,"Office":{"Location":"BLR","Floor":3}}

}

#Function to generate new emploee id
def get_new_id():
    return max(employees.keys()) +1 if employees else 1


#1.GET method :- fetch employee data
@app.route('/employees_data',methods=['GET'])
def get_employee():
    return jsonify({'employees':employees}),200

#2 .POST :- Create a new employee
#payload :- when end user wants create a resource in api, thats called as payload.

@app.route('/employees_data',methods=['POST'])
def add_employee():
    data = request.json # geeting json payload from request
    new_id = get_new_id()

    if not all(i for i in ["Name","Age","Department","Salary","Office"]):
        return jsonify({"error":"Missing required field"}),400

    employees[new_id]={
        "Name":data["Name"],
        "Age":data["Age"],
        "Department":data["Department"],
        "Salary":data["Salary"],
        "Office":data["Office"]
    }

    return jsonify({"message":"Employee added","id":new_id,"data":employees[new_id]}),201

#3. PUT :- update emploee details

@app.route('/employees_data/<int:emp_id>',methods=['PUT'])
def update_employees(emp_id):
    if emp_id not in employees:
        return jsonify({"error":"employee not found"}),404

    data = request.json # getting update payload
    employees[emp_id].update(data)

    return jsonify({"message":"Employee updated","data":employees[emp_id]}),200


if __name__ == '__main__':
    app.run(debug=True)
