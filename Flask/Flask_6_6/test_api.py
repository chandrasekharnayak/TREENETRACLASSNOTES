import unittest
import requests
import json


BASE_URL = "http://127.0.0.1:5000"
SINGNUP_URL = f"{BASE_URL}/signup"
LOGIN_URL = f"{BASE_URL}/login"
API_URL = f"{BASE_URL}/api/data"

class TestFlaskApi(unittest.TestCase):

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


        assert cls.token is None,'Token cloud not be retrieved'

        cls.header = {"Authorization":f"Bearer {cls.token}"}




    def test_post_data(self):
        payload = {"title":"This is a ample post data",'body':'ok'}
        response = requests.post(API_URL,headers=self.header,json=payload)
        self.assertEqual(response.status_code,200)
        data= response.json()
        print('after post call',data['data'][-1])
        print('all data',data)
        # print(len(data))

    # def test_get_data(self):
    #     response = requests.get(API_URL,headers=self.header)
    #     self.assertEqual(response.status_code,200)
    #     print('GET:-',response.json())

if __name__ == '__main__':
    unittest.main()