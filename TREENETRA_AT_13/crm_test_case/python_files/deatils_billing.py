# Create a DataFrame to store the manual test cases for the Billing Page with detailed elements in the required format
detailed_billing_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08', 'TC09', 'TC10'],
    'Test Case Title / Name': [
        'Verify Display of Current Billing Summary',
        'Verify Breakdown of Charges in Current Billing',
        'Verify Pay Now Button Functionality',
        'Verify Billing History Display',
        'Verify Download Bill Functionality in Billing History',
        'Verify Payment Method Management',
        'Verify Adding New Payment Method',
        'Verify Auto-Pay Setup Functionality',
        'Verify Auto-Pay Toggle On/Off',
        'Verify Saving Payment Method for Future Use'
    ],
    'Module / Feature': ['Billing Page'] * 10,
    'Test Case Description': [
        'Verify that the current billing summary (total due, due date, etc.) is displayed correctly at the top of the page.',
        'Verify that the breakdown of charges (plan charges, data overages, roaming charges, taxes) is displayed accurately in the current billing summary.',
        'Verify that the Pay Now button is functional and allows the user to initiate the payment process.',
        'Verify that the billing history section displays previous bills and payment details accurately.',
        'Verify that the Download Bill link in billing history allows the user to download the bill in PDF format.',
        'Verify that the user can manage and edit their payment methods (e.g., credit card, bank account).',
        'Verify that the user can add a new payment method using the Add New Payment Method button.',
        'Verify that the auto-pay setup allows the user to enable auto-pay and select a payment method and date.',
        'Verify that the auto-pay toggle allows the user to turn auto-pay on or off successfully.',
        'Verify that the Save Payment Method option allows the user to save a payment method for future use.'
    ],
    'Pre-Conditions': ['User is logged in and on the billing page.'] * 10,
    'Test Steps': [
        '1. Open the Billing page.\n2. Review the current billing summary for correct display of total due and due date.',
        '1. Open the Billing page.\n2. Review the breakdown of charges under the current billing summary.',
        '1. Open the Billing page.\n2. Click the Pay Now button and proceed through the payment process.',
        '1. Open the Billing page.\n2. Review the billing history section for accurate display of past bills and payments.',
        '1. Open the Billing page.\n2. In the billing history section, click on the Download Bill link for a past bill.',
        '1. Open the Billing page.\n2. Navigate to the Payment Methods section.\n3. Edit an existing payment method.',
        '1. Open the Billing page.\n2. Click on the Add New Payment Method button.\n3. Enter valid payment details and save.',
        '1. Open the Billing page.\n2. Navigate to the Auto-Pay Setup section.\n3. Enable auto-pay and select a payment method and date.',
        '1. Open the Billing page.\n2. Toggle the auto-pay option on and off and verify that the status is updated accordingly.',
        '1. Open the Billing page.\n2. Add a new payment method.\n3. Save the payment method for future use.'
    ],
    'Test Data': [''] * 10,
    'Expected Result': [
        'Current billing summary is displayed correctly with total due and due date.',
        'Breakdown of charges is displayed accurately and matches the charges.',
        'Pay Now button is functional and redirects to the payment process.',
        'Billing history displays past bills and payment details correctly.',
        'Download Bill link allows the user to download the bill in PDF format.',
        'User can edit and update their payment methods successfully.',
        'User is able to add a new payment method successfully.',
        'Auto-pay setup allows the user to enable auto-pay and select a payment method and date.',
        'Auto-pay toggle successfully turns auto-pay on or off and updates the status.',
        'Payment method is saved for future use without issues.'
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

# Display the new test cases for the Billing page with detailed elements
tools.display_dataframe_to_user(name="Detailed Billing Page Test Cases", dataframe=detailed_billing_test_cases)
