import requests

BASE_URL = "http://127.0.0.1:5000"

# Test user credentials
LOGIN_DATA = {
    "username": "k.csnayak108@gmail.com",
    "password": "Password@123"
}

def get_jwt_token():
    response = requests.post(f"{BASE_URL}/login", data=LOGIN_DATA, allow_redirects=False)
    if response.status_code == 302 and "token=" in response.headers.get("Location", ""):
        token = response.headers["Location"].split("token=")[1]
        print("[+] JWT token obtained.")
        print(token)
        return token
    else:
        print("[!] Login failed.",response.status_code)
        return None

get_jwt_token()
token = get_jwt_token()

# def get_all_users(token):
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(f"{BASE_URL}/api/user", headers=headers)
#     print("GET Response:", response.status_code, response.json())
#
# get_all_users(token)

# def post_user(token):
#     headers = {"Authorization": f"Bearer {token}"}
#     data = {
#         "firstname": "Jane",
#         "lastname": "Smith",
#         "email": "jane@example.com",
#         "phone": "1231231234",
#         "password": "test123",
#         "service": "prepaid",
#         "months": 2
#     }
#     response = requests.post(f"{BASE_URL}/api/user", json=data, headers=headers)
#     print("POST Response:", response.status_code, response.json())
#     return response.json().get("data", {}).get("id")
#
# post_user(token)

# def put_user(token, user_id):
#     headers = {"Authorization": f"Bearer {token}"}
#     data = {
#         "firstname": "UpdatedJane",
#         "months": 3
#     }
#     response = requests.put(f"{BASE_URL}/api/user/{user_id}", json=data, headers=headers)
#     print("PUT Response:", response.status_code, response.json())
#
# put_user(token,'db3dd682-d1b2-4373-8ebc-1c691e07c826')
#
# def patch_user(token, user_id):
#     headers = {"Authorization": f"Bearer {token}"}
#     data = {
#         "lastname": "PatchedSmith"
#     }
#     response = requests.patch(f"{BASE_URL}/api/user/{user_id}", json=data, headers=headers)
#     print("PATCH Response:", response.status_code, response.json())
#
# def delete_user(token, user_id):
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.delete(f"{BASE_URL}/api/user/{user_id}", headers=headers)
#     print("DELETE Response:", response.status_code, response.json())
#
# if __name__ == "__main__":
#     token = get_jwt_token()
#     if not token:
#         exit(1)
#
#     print("\n--- GET Request ---")
#     get_all_users(token)
#
#     print("\n--- POST Request ---")
#     new_user_id = post_user(token)
#
#     if new_user_id:
#         print("\n--- PUT Request ---")
#         put_user(token, new_user_id)
#
#         print("\n--- PATCH Request ---")
#         patch_user(token, new_user_id)
#
#         print("\n--- DELETE Request ---")
#         delete_user(token, new_user_id)
