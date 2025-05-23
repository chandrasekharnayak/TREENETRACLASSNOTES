# Create a DataFrame to store the manual test cases for the Payment Gateway Page in the required format
payment_gateway_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08', 'TC09', 'TC10'],
    'Test Case Title / Name': [
        'Verify Display of Payment Amount',
        'Verify Payment Method Selection',
        'Verify Credit/Debit Card Details Entry',
        'Verify Billing Address Auto-Population',
        'Verify Pay Now Button Functionality',
        'Verify Payment Confirmation Display',
        'Verify Transaction ID and Payment Date on Confirmation',
        'Verify Payment Failure Scenario and Error Handling',
        'Verify Cancel Button Functionality',
        'Verify Download Receipt Button on Confirmation'
    ],
    'Module / Feature': ['Payment Gateway Page'] * 10,
    'Test Case Description': [
        'Verify that the payment amount is displayed correctly and is editable if partial payments are allowed.',
        'Verify that the user can select between saved payment methods or add a new method via the payment method drop-down.',
        'Verify that the user can enter valid credit/debit card details including cardholder name, card number, expiry date, and CVV.',
        'Verify that the billing address field is auto-populated with the customer’s address and can be edited if necessary.',
        'Verify that the Pay Now button is functional and submits the payment.',
        'Verify that the payment confirmation page is displayed with the correct details after successful payment.',
        'Verify that the Transaction ID, Date of Payment, and Amount Paid are displayed correctly on the confirmation page.',
        'Verify that if the payment fails (e.g., due to insufficient funds), an appropriate error message is displayed.',
        'Verify that the Cancel button allows the user to return to the previous page without making a payment.',
        'Verify that the Download Receipt button is functional and allows the user to download the receipt for a successful payment.'
    ],
    'Pre-Conditions': ['User has clicked Pay Now and is redirected to the Payment Gateway page.'] * 10,
    'Test Steps': [
        '1. Open the Payment Gateway page.\n2. Verify the payment amount displayed in the Amount to Pay field.',
        '1. Open the Payment Gateway page.\n2. Select a payment method from the drop-down menu or add a new one.',
        '1. Open the Payment Gateway page.\n2. Enter valid credit/debit card details in the respective fields.',
        '1. Open the Payment Gateway page.\n2. Verify that the billing address is auto-populated and can be edited.',
        '1. Open the Payment Gateway page.\n2. Fill in the required payment details.\n3. Click on the Pay Now button.',
        '1. Complete a payment.\n2. Verify the payment confirmation page is displayed after successful payment.',
        '1. Complete a payment.\n2. Review the confirmation page for correct Transaction ID, Date of Payment, and Amount Paid.',
        '1. Attempt a payment with insufficient funds or an invalid card.\n2. Verify that the correct error message is displayed.',
        '1. Open the Payment Gateway page.\n2. Click on the Cancel button.\n3. Verify that the user is returned to the previous page.',
        '1. Complete a successful payment.\n2. Click the Download Receipt button and verify the receipt is downloaded successfully.'
    ],
    'Test Data': [''] * 10,
    'Expected Result': [
        'Payment amount is displayed correctly and is editable if partial payments are allowed.',
        'User can select a payment method or add a new one without issues.',
        'Credit/debit card details are accepted and validated correctly.',
        'Billing address is auto-populated and can be edited if needed.',
        'Pay Now button submits the payment and redirects to the confirmation page.',
        'Payment confirmation page is displayed with correct details.',
        'Transaction ID, Date of Payment, and Amount Paid are displayed accurately.',
        'An appropriate error message is displayed if the payment fails due to insufficient funds or invalid card details.',
        'Cancel button works and returns the user to the previous page without processing a payment.',
        'Download Receipt button works and the receipt is downloaded successfully.'
    ],
    'Actual Result': [''] * 10,
    'Status (Pass/Fail)': [''] * 10,
    'Priority': ['High'] * 10,
    'Severity': ['Critical'] * 10,
    'Test Environment': ['Web Browser'] * 10,
    'Test Type': ['Functional'] * 10,
    'Assigned To': [''] * 10,
    'Test Execution Date': [''] * 10,
    'Defect ID (if applicable)': [''] * 10,
    'Comments / Notes': [''] * 10,
    'Automation Status': [''] * 10,
    'Requirements ID / Traceability': [''] * 10
})

# Display the new test cases for the Payment Gateway page
tools.display_dataframe_to_user(name="Payment Gateway Page Test Cases", dataframe=payment_gateway_test_cases)
