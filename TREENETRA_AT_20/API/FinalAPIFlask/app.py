from flask import Flask,redirect,url_for,request,render_template,jsonify
from flask_jwt_extended import JWTManager, create_access_token,jwt_required,get_jwt_identity #jwt token creation and access
from datetime import timedelta # create time spam
import uuid # create the user id


app = Flask(__name__) # application creation
app.secret_key = 'supersecretkey' # create secret key for jet token
app.config['JWT_SECRET_KEY']='jwtsecretkey' # confiog jwt secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES']= timedelta(minutes=30) # create the expires time for jwt token
jwt = JWTManager(app) # create the jwt token


database = []

@app.route('/')
def index():
    return redirect(url_for('signup'))


@app.route('/signup',methods= ['GET','POST'])
def signup():
    if request.method =='POST': # if request is post then data will created
        data = request.form # this line use for accepting the data from ui
        user = {
            "id":str(uuid.uuid4()),
            "firstname":data["firstname"],
            "lastname":data["lastname"],
            "email":data["email"],
            "phone":data["phone"],
            "password":data["password"]
        }

        database.append(user)
        return redirect(url_for("login"))
    return render_template('signup.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        for user in database:
            if user['email']==username and user['password']==password:
                access_token = create_access_token(identity=username)
                return redirect(url_for('dashboard',token=access_token))
            return 'Invalid credentials'
    return render_template('login.html')


@app.route('/dashboard')
@jwt_required()
def dashboard():
    return render_template('dashboard.html')


#------------------------------------------------------backend data enter---------------------------------------------------------
@app.route('/api/user',methods=['GET'])
@jwt_required()
def get_user():
    return jsonify(database),200


@app.route('/api/user',methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    data['id']=str(uuid.uuid4())
    database.append(data)
    return jsonify({"msg":"user added","data":data}),201


if __name__ == '__main__':
    app.run(debug=True)

