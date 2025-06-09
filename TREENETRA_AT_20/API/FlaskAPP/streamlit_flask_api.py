import streamlit as st
import uuid
import jwt
import datetime

# Secret key for JWT
JWT_SECRET = 'jwtsecretkey'

# In-memory "database"
if "users" not in st.session_state:
    st.session_state.users = []

if "token" not in st.session_state:
    st.session_state.token = None

# ---------------- JWT Utilities ----------------
def create_token(username):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def decode_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return None

# ---------------- Pages ----------------
def signup_page():
    st.title("Signup Page")
    with st.form("signup_form"):
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        cpassword = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Signup")
        if submitted:
            if password != cpassword:
                st.error("Passwords do not match.")
            else:
                st.session_state.users.append({
                    "id": str(uuid.uuid4()),
                    "firstname": fname,
                    "lastname": lname,
                    "email": email,
                    "phone": phone,
                    "password": password,
                    "service": "",
                    "months": 0
                })
                st.success("Signup successful. Please login.")

def login_page():
    st.title("Login Page")
    with st.form("login_form"):
        username = st.text_input("Username (email)")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            for user in st.session_state.users:
                if user['email'] == username and user['password'] == password:
                    token = create_token(username)
                    st.session_state.token = token
                    st.success("Login successful.")
                    st.experimental_rerun()
                    return
            st.error("Invalid credentials.")

def dashboard_page():
    st.title("Dashboard")

    token = st.session_state.get("token", "")
    user = decode_token(token)
    if not user:
        st.error("Invalid or expired token. Please login again.")
        return

    st.success(f"Welcome {user['sub']}!")

    plan_type = st.radio("Select Plan Type", ["Prepaid", "Postpaid"])
    if plan_type == "Prepaid":
        option = st.selectbox("Select Plan", ["199 - 1 Month", "299 - 2 Months", "399 - 3 Months"])
    else:
        option = st.selectbox("Select Plan", ["499 - 1 Month", "599 - 2 Months", "699 - 3 Months"])

    if st.button("Submit Plan"):
        months = int(option.split("-")[1].strip().split()[0]) // 100
        for user in st.session_state.users:
            if user['email'] == user['sub'] or user['email'] == user['email']:
                user['service'] = plan_type.lower()
                user['months'] = months
                st.success("Plan updated.")

    st.subheader("Current Users")
    st.json(st.session_state.users)

    # Admin-like actions for demonstration
    st.subheader("Modify User Data")
    user_id = st.selectbox("Select user by ID", [u["id"] for u in st.session_state.users])
    if user_id:
        if st.button("Delete User"):
            st.session_state.users = [u for u in st.session_state.users if u["id"] != user_id]
            st.success("User deleted.")
            st.experimental_rerun()

# ---------------- Main App ----------------
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Signup", "Login", "Dashboard"])

    if page == "Signup":
        signup_page()
    elif page == "Login":
        login_page()
    elif page == "Dashboard":
        dashboard_page()

if __name__ == "__main__":
    main()
