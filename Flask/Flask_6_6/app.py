from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "super-secret-session"
app.config["JWT_SECRET_KEY"] = "super-secret-jwt"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

# jwt = JWTManager(app)

# Mock user store and data
users = [
    {'id':1,'title':'hello','body':'world'},
    {'id':2,'title':'Test','body':'framework'}
]
user_data = {
    "user1": {"profile": "Basic User", "notes": ["task1", "task2"]},
    "admin": {"profile": "Admin User", "logs": ["entry1", "entry2"]}
}

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            flash("User already exists!", "error")
            return redirect(url_for("signup"))
        users[username] = password
        flash("Signup successful. Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) != password:
            flash("Invalid credentials!", "error")
            return redirect(url_for("login"))
        # access_token = create_access_token(identity=username)
        # session["token"] = access_token
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    token = None
    if not token:
        return redirect(url_for("login"))
    try:
        # user = decode_token(token)["sub"]
        return render_template("dashboard.html", token=token)
    except:
        flash("Invalid or expired session.", "error")
        return redirect(url_for("login"))

@app.route("/api/data", methods=["GET","POST"])
# @jwt_required()
def protected_api():
    user =None
    data = request.json
    new_id = max(i['id'] for i in users)+1 if users else 1
    new_post = {'id': new_id, 'title': data['title'], 'body': data['body']}
    users.append(new_post)
    return jsonify({"user": user, "data":users})

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
