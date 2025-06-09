import requests


BASE_URL = 'http://127.0.0.1:5000'

LOGIN_DATA = {
    'username':'k.csnayak108@gmail.com',
    'password':'Password@123'
}

def get_jwt_token():
    response = requests.post(f'{BASE_URL}/login',data=LOGIN_DATA,allow_redirects=False)
    if response.status_code==302 and "token=" in response.headers.get("Location",""):
        token = response.headers["Location"].split("token=")[1]
        print("jwt token get",token)
        return token
    else:
        print('Login falied',response.status_code)
        return None

token = get_jwt_token()

# def get_all_user(token):
#     headers = {"Authorization":f"Bearer {token}"}
#     response = requests.get(f"{BASE_URL}/api/user",headers=headers)
#     print("GET Response :-")
#     print(response.status_code)
#     print(response.json())
#
# get_all_user(token)

def post_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "firstname":"sankar prasad",
        "lastname":"padhi",
        "email":"sankar@gmail.com",
        "phone":"1234567890",
        "password":"Password@123"
    }

    response = requests.post(f"{BASE_URL}/api/user",json=data,headers=headers)
    print('Post Response:-')
    print(response.status_code)
    print(response.json())

post_user(token)







