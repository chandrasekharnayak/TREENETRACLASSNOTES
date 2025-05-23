# Create a DataFrame to store the manual test cases for the Fulfillment/Customer Details Page in the required format
fulfillment_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Customer Name Field',
        'Verify Address Field Functionality',
        'Verify Contact Information Fields',
        'Verify Service Address Field',
        'Verify Service Start Date Field',
        'Verify Submit Button Functionality',
        'Verify Confirmation Box for Correct Details',
        'Verify Form Submission with Valid Data'
    ],
    'Module / Feature': ['Fulfillment/Customer Details Page'] * 8,
    'Test Case Description': [
        'Verify that the customer name field accepts valid input.',
        'Verify that the address field allows proper entry of customer address details.',
        'Verify that the email and phone number fields accept valid contact information.',
        'Verify that the service address field displays the correct format for the address.',
        'Verify that the service start date field allows selection of a valid future date.',
        'Verify that the submit button is functional and submits the form after entering valid details.',
        'Verify that the confirmation box appears after submitting the details and displays correct customer data.',
        'Verify that the form can be successfully submitted when all fields contain valid data.'
    ],
    'Pre-Conditions': ['User is on the fulfillment/customer details page.'] * 8,
    'Test Steps': [
        '1. Open the Fulfillment/Customer Details page.\n2. Enter a valid customer name in the Customer Name field.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter a valid address in the Address field.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter valid email and phone number in the respective fields.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter a valid service address.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter a future date in the Service Start Date field.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter valid data in all fields.\n3. Click on the Submit button.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter valid data in all fields.\n3. Submit the form.\n4. Verify the confirmation box displays correct details.',
        '1. Open the Fulfillment/Customer Details page.\n2. Enter valid data in all fields.\n3. Click on the Submit button to verify successful submission.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Customer name is accepted and moves to the next field.',
        'Address is entered successfully without errors.',
        'Email and phone number are accepted and validated.',
        'Service address is entered in the correct format without errors.',
        'Service start date is accepted and allows only future dates.',
        'Submit button is functional, and the form is submitted successfully.',
        'Confirmation box appears and displays correct details entered by the user.',
        'Form is submitted successfully when all fields are filled with valid data.'
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

# Display the new test cases for the Fulfillment/Customer Details page
tools.display_dataframe_to_user(name="Fulfillment/Customer Details Page Test Cases", dataframe=fulfillment_test_cases)
