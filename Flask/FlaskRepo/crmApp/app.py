from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Dummy user data for login
users = {
    "admin": "password123"
}

# Dummy employee data
employee_data = [
    {
        "id": 1,
        "name": "John Doe",
        "salary": 50000,
        "designation": "Software Engineer",
        "manager": "Jane Smith"
    },
    {
        "id": 2,
        "name": "Emily Johnson",
        "salary": 70000,
        "designation": "Product Manager",
        "manager": "Robert Brown"
    },
    {
        "id": 3,
        "name": "Michael Williams",
        "salary": 60000,
        "designation": "Data Analyst",
        "manager": "Emma Davis"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/api/employee_data', methods=['GET'])
def get_employee_data():
    return jsonify(employee_data)

if __name__ == '__main__':
    app.run(debug=True)
