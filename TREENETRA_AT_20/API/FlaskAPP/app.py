from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'jwtsecretkey'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
jwt = JWTManager(app)

database = []  # list of dictionaries

@app.route('/')
def index():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        user = {
            "id": str(uuid.uuid4()),
            "firstname": data['firstname'],
            "lastname": data['lastname'],
            "email": data['email'],
            "phone": data['phone'],
            "password": data['password'],
            "service": "",
            "months": 0
        }
        database.append(user)
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in database:
            if user['email'] == username and user['password'] == password:
                access_token = create_access_token(identity=username)
                return redirect(url_for('dashboard', token=access_token))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/dashboard')
@jwt_required()
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/user', methods=['GET'])
@jwt_required()
def get_user():
    return jsonify(database), 200

@app.route('/api/user', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    data['id'] = str(uuid.uuid4())
    database.append(data)
    return jsonify({"msg": "User added", "data": data}), 201

@app.route('/api/user/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    for user in database:
        if user['id'] == user_id:
            user.update(data)
            return jsonify({"msg": "User updated", "data": user}), 200
    return jsonify({"msg": "User not found"}), 404

@app.route('/api/user/<user_id>', methods=['PATCH'])
@jwt_required()
def patch_user(user_id):
    data = request.get_json()
    for user in database:
        if user['id'] == user_id:
            user.update(data)
            return jsonify({"msg": "User patched", "data": user}), 200
    return jsonify({"msg": "User not found"}), 404

@app.route('/api/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    global database
    database = [user for user in database if user['id'] != user_id]
    return jsonify({"msg": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
