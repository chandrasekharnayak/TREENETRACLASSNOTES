# Create a DataFrame to store the manual test cases for the Billing Page in the required format
billing_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Billing History Display',
        'Verify Payment Method Management',
        'Verify Pay Now Button Functionality',
        'Verify Download Bill Functionality',
        'Verify Payment Method Update',
        'Verify Bill Due Date Display',
        'Verify Graph/Chart of Spending Trends',
        'Verify Navigation Links for Billing'
    ],
    'Module / Feature': ['Billing Page'] * 8,
    'Test Case Description': [
        'Verify that the billing history displays past and current bills with accurate due dates and amounts.',
        'Verify that users can add or edit payment methods such as credit cards or bank accounts.',
        'Verify that the Pay Now button allows the user to make an immediate payment.',
        'Verify that the Download Bill button allows the user to download the bill in PDF format.',
        'Verify that payment methods can be successfully updated or changed.',
        'Verify that the bill due date is displayed correctly next to each bill.',
        'Verify that the spending trends graph/chart displays accurate data over time.',
        'Verify that all navigation links (Billing History, Payment Options, Bill Settings) are functional and redirect to the correct sections.'
    ],
    'Pre-Conditions': ['User is logged in and on the Billing page.'] * 8,
    'Test Steps': [
        '1. Open the Billing page.\n2. Review the billing history for past and current bills.',
        '1. Open the Billing page.\n2. Click on the Payment Method section.\n3. Add or edit a payment method.',
        '1. Open the Billing page.\n2. Click on the Pay Now button next to a bill and follow the steps to make a payment.',
        '1. Open the Billing page.\n2. Click on the Download Bill button for any bill and save the file.',
        '1. Open the Billing page.\n2. Navigate to the Payment Method section.\n3. Update an existing payment method.',
        '1. Open the Billing page.\n2. Verify the due dates displayed next to each bill.',
        '1. Open the Billing page.\n2. Check the graph/chart section for spending trends over time.',
        '1. Open the Billing page.\n2. Click on each navigation link (Billing History, Payment Options, Bill Settings) and verify redirection.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Billing history displays accurate information for each bill with correct due dates and amounts.',
        'User is able to successfully add or edit payment methods.',
        'Pay Now button allows the user to make a payment, and a confirmation is displayed.',
        'Download Bill button successfully downloads the bill in PDF format.',
        'Payment method is successfully updated and saved.',
        'Bill due dates are displayed accurately next to each bill.',
        'Spending trends graph/chart shows correct and updated data over time.',
        'All navigation links work as expected and redirect to the correct sections.'
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

# Display the new test cases for the Billing page
tools.display_dataframe_to_user(name="Billing Page Test Cases", dataframe=billing_test_cases)
