import pandas as pd

# Create a DataFrame to store the manual test cases in the required format
test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08', 'TC09', 'TC10', 'TC11', 'TC12', 'TC13'],
    'Test Case Title / Name': [
        'Verify Username Field',
        'Verify Email Field for Empty Input',
        'Verify Email Format Validation',
        'Verify Email Uniqueness Validation',
        'Verify Auto User ID Generation',
        'Verify Age Field Only Accepts Numeric Input',
        'Verify Age Field for Empty Input',
        'Verify Age Range Validation',
        'Verify Password and Confirm Password Fields',
        'Verify Password and Confirm Password Match',
        'Verify Password Strength Validation',
        'Verify Form Submission with Valid Data',
        'Verify Form Submission with Empty Fields'
    ],
    'Module / Feature': ['Signup Page'] * 13,
    'Test Case Description': [
        'Verify the username field accepts valid input.',
        'Verify the email field does not accept empty input.',
        'Verify the email field accepts valid email format only.',
        'Verify the system checks for unique emails.',
        'Verify that the system generates a unique user ID automatically.',
        'Verify the age field only accepts numeric input.',
        'Verify the age field does not accept empty input.',
        'Verify that age input is within the valid range (e.g., 18-99).',
        'Verify password and confirm password fields accept valid input.',
        'Verify that the password and confirm password fields match.',
        'Verify that the password meets minimum strength criteria (e.g., 8 characters).',
        'Verify successful form submission with valid data.',
        'Verify form submission displays errors when required fields are empty.'
    ],
    'Pre-Conditions': ['User is on the signup page.'] * 13,
    'Test Steps': [
        '1. Open the Signup page.\n2. Enter a valid username and move to the next field.',
        '1. Open the Signup page.\n2. Leave the email field empty and attempt to submit.',
        '1. Open the Signup page.\n2. Enter an invalid email format and attempt to submit.',
        '1. Open the Signup page.\n2. Enter an email that already exists in the system.',
        '1. Open the Signup page.\n2. Fill all fields and submit the form.',
        '1. Open the Signup page.\n2. Enter non-numeric characters in the Age field and attempt to submit.',
        '1. Open the Signup page.\n2. Leave the Age field empty and attempt to submit.',
        '1. Open the Signup page.\n2. Enter an age below 18 or above 99 and submit.',
        '1. Open the Signup page.\n2. Enter a valid password and confirm password.',
        '1. Open the Signup page.\n2. Enter different passwords in Password and Confirm Password fields.',
        '1. Open the Signup page.\n2. Enter a weak password (less than 8 characters) and submit.',
        '1. Open the Signup page.\n2. Fill all fields with valid data and submit the form.',
        '1. Open the Signup page.\n2. Leave required fields empty and submit the form.'
    ],
    'Test Data': [''] * 13,
    'Expected Result': [
        'Username is accepted and moves to the next field.',
        'Error message for empty email field is displayed.',
        'Error message for invalid email format is displayed.',
        'Error message for duplicate email is displayed.',
        'A unique auto-generated User ID is created.',
        'Error message for non-numeric characters in the Age field is displayed.',
        'Error message for empty Age field is displayed.',
        'Error message for invalid age is displayed.',
        'Password and Confirm Password fields accept valid input.',
        'Error message for mismatched passwords is displayed.',
        'Error message for weak password is displayed.',
        'Form is submitted successfully.',
        'Error messages for empty required fields are displayed.'
    ],
    'Actual Result': [''] * 13,
    'Status (Pass/Fail)': [''] * 13,
    'Priority': ['High'] * 13,
    'Severity': ['Critical'] * 13,
    'Test Environment': ['Web Browser'] * 13,
    'Test Type': ['Functional'] * 13,
    'Assigned To': [''] * 13,
    'Test Execution Date': [''] * 13,
    'Defect ID (if applicable)': [''] * 13,
    'Comments / Notes': [''] * 13,
    'Automation Status': [''] * 13,
    'Requirements ID / Traceability': [''] * 13
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Signup Page Test Cases", dataframe=test_cases)
