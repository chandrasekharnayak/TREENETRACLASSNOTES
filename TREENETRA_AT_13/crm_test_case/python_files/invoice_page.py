# Create a DataFrame to store the manual test cases for the Invoice Page in the required format
invoice_page_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Invoice Header Information',
        'Verify Charges Breakdown Display',
        'Verify Data Overages and Roaming Charges',
        'Verify Discounts and Promotions',
        'Verify Total Amount Calculation',
        'Verify Download Invoice Button Functionality',
        'Verify Print Invoice Option',
        'Verify Payment History Display'
    ],
    'Module / Feature': ['Invoice Page'] * 8,
    'Test Case Description': [
        'Verify that the invoice header contains correct details such as invoice number, billing period, invoice date, due date, account number, and total amount due.',
        'Verify that the charges breakdown displays all relevant charges, including plan charges, usage charges, and other fees.',
        'Verify that data overages and roaming charges are displayed accurately under the usage charges section.',
        'Verify that any applicable discounts or promotions are displayed and deducted from the total amount.',
        'Verify that the total amount is calculated correctly by summing all charges and deducting any discounts.',
        'Verify that the Download Invoice button is functional and allows the user to download the invoice in PDF format.',
        'Verify that the Print Invoice option allows the user to print the invoice.',
        'Verify that the payment history, if displayed, accurately reflects previous payments applied to the account.'
    ],
    'Pre-Conditions': ['User is logged in and viewing the invoice page.'] * 8,
    'Test Steps': [
        '1. Open the Invoice page.\n2. Review the invoice header for correct display of invoice number, billing period, invoice date, due date, account number, and total amount due.',
        '1. Open the Invoice page.\n2. Review the charges breakdown section for plan charges, usage charges, and other fees.',
        '1. Open the Invoice page.\n2. Check the usage charges section for data overages and roaming charges.',
        '1. Open the Invoice page.\n2. Review the discounts and promotions section for any applicable deductions.',
        '1. Open the Invoice page.\n2. Verify that the total amount is calculated correctly based on the charges and discounts.',
        '1. Open the Invoice page.\n2. Click on the Download Invoice button and verify that the invoice is downloaded as a PDF.',
        '1. Open the Invoice page.\n2. Use the Print Invoice option to print the invoice.',
        '1. Open the Invoice page.\n2. Review the payment history section (if displayed) for accuracy of previous payments.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Invoice header displays correct information including invoice number, billing period, invoice date, due date, account number, and total amount due.',
        'Charges breakdown displays accurate information for plan charges, usage charges, and other fees.',
        'Data overages and roaming charges are displayed correctly in the usage charges section.',
        'Applicable discounts and promotions are displayed and deducted from the total amount.',
        'Total amount is calculated correctly by summing all charges and applying any discounts.',
        'Download Invoice button works and allows the user to download the invoice in PDF format.',
        'Print Invoice option works and the invoice is printed successfully.',
        'Payment history section accurately reflects previous payments applied to the account.'
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

# Display the new test cases for the Invoice Page
tools.display_dataframe_to_user(name="Invoice Page Test Cases", dataframe=invoice_page_test_cases)
