# Create a DataFrame to store the manual test cases for the Login Page in the required format
login_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Username Field',
        'Verify Password Field',
        'Verify Login Button Functionality',
        'Verify Forgot Password Link',
        'Verify Login with Valid Credentials',
        'Verify Login with Invalid Username',
        'Verify Login with Invalid Password',
        'Verify Error Message for Empty Fields'
    ],
    'Module / Feature': ['Login Page'] * 8,
    'Test Case Description': [
        'Verify the username field accepts valid input.',
        'Verify the password field masks the entered password.',
        'Verify the login button is functional and submits credentials.',
        'Verify the forgot password link redirects to the reset password page.',
        'Verify login with valid username and password.',
        'Verify login with an invalid username.',
        'Verify login with an invalid password.',
        'Verify error messages appear when the username and password fields are left empty.'
    ],
    'Pre-Conditions': ['User is on the login page.'] * 8,
    'Test Steps': [
        '1. Open the Login page.\n2. Enter a valid username.',
        '1. Open the Login page.\n2. Enter any password and ensure it is masked.',
        '1. Open the Login page.\n2. Enter valid credentials.\n3. Click the login button.',
        '1. Open the Login page.\n2. Click on the "Forgot Password" link.',
        '1. Open the Login page.\n2. Enter a valid username and password.\n3. Click the login button.',
        '1. Open the Login page.\n2. Enter an invalid username and valid password.\n3. Click the login button.',
        '1. Open the Login page.\n2. Enter a valid username and invalid password.\n3. Click the login button.',
        '1. Open the Login page.\n2. Leave the username and password fields empty.\n3. Click the login button.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Username is accepted and moves to the next field.',
        'Password is masked and not visible.',
        'Login button is functional and submits credentials for authentication.',
        '"Forgot Password" link redirects to the password reset page.',
        'User is logged in successfully and redirected to the CRM system.',
        'An error message is displayed for invalid username.',
        'An error message is displayed for invalid password.',
        'Error messages are displayed for empty username and password fields.'
    ],
    'Actual Result': [''] * 8,
    'Status (Pass/Fail)': [''] * 8,
    'Priority': ['High'] * 8,
    'Severity': ['Critical'] * 8,
    'Test Environment': ['Web Browser'] * 8,
    'Test Type': ['Functional'] * 8,
    'Assigned To': [''] * 8,
    'Test Execution Date': [''] * 8,
    'Defect ID (if applicable)': [''] * 8,
    'Comments / Notes': [''] * 8,
    'Automation Status': [''] * 8,
    'Requirements ID / Traceability': [''] * 8
})

# Display the new test cases for the login page
tools.display_dataframe_to_user(name="Login Page Test Cases", dataframe=login_test_cases)
