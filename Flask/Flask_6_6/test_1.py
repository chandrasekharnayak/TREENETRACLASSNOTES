import unittest
import requests
import json


BASE_URL = "http://127.0.0.1:5000"
SINGNUP_URL = f"{BASE_URL}/signup"
LOGIN_URL = f"{BASE_URL}/login"
API_URL = f"{BASE_URL}/api/data"

class TestFlaskApi:

    @classmethod
    def setUpClass(cls):
        cls.username = 'testuser'
        cls.password = 'testpass'
        cls.token = None

        #Signup (If user exits,it will pass)
        requests.post(SINGNUP_URL,data={
            "username":cls.username,
            "password":cls.password
        })

        #Login and extract token
        login_response = requests.post(LOGIN_URL,data={
            "username":cls.username,
            "password":cls.password
        })

        #Parse token from response json

        # if 'application/json' in login_response.headers.get('Content-Type',''):
        #     try:
        #         data = login_response.json()
        #         print(data)
        #     except json.JSONDecodeError:
        #         print("Response content is no valid json")
        # else:
        #     print("Response is not json",login_response.text)

        # print(login_response.json())
        print(login_response.text)

        # print(login_response.json().get("access_token"))

        # assert cls.token is  None,'Token cloud not be retrieved'
        # print(cls.token)

        cls.header = {"Authorization":None}
        print(cls.header)

obj = TestFlaskApi
obj.setUpClass()