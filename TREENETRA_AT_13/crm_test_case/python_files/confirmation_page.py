# Create a DataFrame to store the manual test cases for the Confirmation Page in the required format
confirmation_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06'],
    'Test Case Title / Name': [
        'Verify Display of Confirmation Number',
        'Verify Summary of Action for Selected Plan',
        'Verify Download Receipt Button Functionality',
        'Verify Confirmation Page Layout and Content',
        'Verify Print Functionality for Confirmation',
        'Verify Confirmation Page After Payment/Plan Selection/Request'
    ],
    'Module / Feature': ['Confirmation Page'] * 6,
    'Test Case Description': [
        'Verify that the confirmation number is displayed correctly on the confirmation page.',
        'Verify that the summary of the action (e.g., selected plan, payment, service request) is displayed correctly on the confirmation page.',
        'Verify that the Download Receipt button is functional and allows the user to download the receipt.',
        'Verify that the confirmation page layout includes the "Thank You" message, confirmation number, summary, and receipt options.',
        'Verify that the user can print the confirmation page successfully.',
        'Verify that the confirmation page is displayed correctly after selecting a plan, making a payment, or raising a service request.'
    ],
    'Pre-Conditions': ['User has completed a transaction (plan selection, payment, or service request).'] * 6,
    'Test Steps': [
        '1. Complete a transaction (e.g., plan selection).\n2. Navigate to the confirmation page.\n3. Verify the confirmation number is displayed.',
        '1. Complete a transaction (e.g., plan selection).\n2. Navigate to the confirmation page.\n3. Check the summary of the action performed (e.g., plan details).',
        '1. Complete a transaction (e.g., plan selection).\n2. Navigate to the confirmation page.\n3. Click the Download Receipt button.',
        '1. Complete a transaction (e.g., plan selection).\n2. Verify the layout includes the Thank You message, confirmation number, summary, and receipt options.',
        '1. Complete a transaction (e.g., plan selection).\n2. Use the browser print functionality to print the confirmation page.',
        '1. Complete a transaction (e.g., plan selection, payment, or service request).\n2. Verify that the confirmation page displays the correct summary and confirmation number.'
    ],
    'Test Data': [''] * 6,
    'Expected Result': [
        'Confirmation number is displayed correctly.',
        'Summary of the action is displayed accurately, including details like plan name or payment amount.',
        'Download Receipt button works, and the receipt is downloaded successfully.',
        'Confirmation page layout is correct, with all required elements visible.',
        'Print functionality works and prints the confirmation page as expected.',
        'Confirmation page is displayed correctly with all relevant information after completing the transaction.'
    ],
    'Actual Result': [''] * 6,
    'Status (Pass/Fail)': [''] * 6,
    'Priority': ['High'] * 6,
    'Severity': ['Critical'] * 6,
    'Test Environment': ['Web Browser'] * 6,
    'Test Type': ['Functional'] * 6,
    'Assigned To': [''] * 6,
    'Test Execution Date': [''] * 6,
    'Defect ID (if applicable)': [''] * 6,
    'Comments / Notes': [''] * 6,
    'Automation Status': [''] * 6,
    'Requirements ID / Traceability': [''] * 6
})

# Display the new test cases for the Confirmation page
tools.display_dataframe_to_user(name="Confirmation Page Test Cases", dataframe=confirmation_test_cases)
