from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5000"

LOGIN_DATA = {
    "username": "k.csnayak108@gmail.com",
    "password": "Password@123"
}


def run(playwright):
    request_context = playwright.request.new_context()

    # 1. Login to get JWT token
    login_response = request_context.post(f"{BASE_URL}/login", data=LOGIN_DATA)
    assert login_response.status == 302, "Login failed"

    redirect_url = login_response.headers.get("location", "")
    token = redirect_url.split("token=")[1] if "token=" in redirect_url else None
    assert token, "Token not found"
    print("[+] JWT token obtained.")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # 2. GET Request
    get_res = request_context.get(f"{BASE_URL}/api/user", headers=headers)
    print("GET Response:", get_res.status, get_res.json())

    # 3. POST Request
    post_data = {
        "firstname": "Jane",
        "lastname": "Smith",
        "email": "jane@example.com",
        "phone": "1231231234",
        "password": "test123",
        "service": "prepaid",
        "months": 2
    }
    post_res = request_context.post(f"{BASE_URL}/api/user", headers=headers, data=post_data)
    print("POST Response:", post_res.status, post_res.json())
    user_id = post_res.json().get("data", {}).get("id")

    # 4. PUT Request
    put_data = {
        "firstname": "UpdatedJane",
        "months": 3
    }
    put_res = request_context.put(f"{BASE_URL}/api/user/{user_id}", headers=headers, data=put_data)
    print("PUT Response:", put_res.status, put_res.json())

    # 5. PATCH Request
    patch_data = {
        "lastname": "PatchedSmith"
    }
    patch_res = request_context.patch(f"{BASE_URL}/api/user/{user_id}", headers=headers, data=patch_data)
    print("PATCH Response:", patch_res.status, patch_res.json())

    # 6. DELETE Request
    delete_res = request_context.delete(f"{BASE_URL}/api/user/{user_id}", headers=headers)
    print("DELETE Response:", delete_res.status, delete_res.json())

    request_context.dispose()


with sync_playwright() as playwright:
    run(playwright)
