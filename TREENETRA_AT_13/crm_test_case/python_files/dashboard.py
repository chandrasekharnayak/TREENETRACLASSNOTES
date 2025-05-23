# Create a DataFrame to store the manual test cases for the Dashboard/Home Page in the required format
dashboard_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Account Overview Section Display',
        'Verify Quick Links Section Functionality',
        'Verify Navigation Menu Links',
        'Verify Display of Account Balance',
        'Verify Current Plan Information',
        'Verify Recent Transactions Display',
        'Verify Service Status Information',
        'Verify Navigation Menu Redirection'
    ],
    'Module / Feature': ['Dashboard/Home Page'] * 8,
    'Test Case Description': [
        'Verify that the Account Overview section displays correct account information.',
        'Verify that the Quick Links section provides access to essential functions such as viewing bills, managing plans, or checking service requests.',
        'Verify that all links in the Navigation Menu on the left panel redirect to the correct sections.',
        'Verify that the Account Balance is displayed correctly in the Account Overview section.',
        'Verify that the Current Plan information is displayed accurately in the Account Overview section.',
        'Verify that recent transactions or service requests are displayed in the right panel.',
        'Verify that the Service Status section accurately reflects the user\'s current service status.',
        'Verify that each link in the Navigation Menu redirects to the correct pages (Plans, Billing, Service Requests).'
    ],
    'Pre-Conditions': ['User is logged in and on the dashboard/home page.'] * 8,
    'Test Steps': [
        '1. Open the Dashboard/Home page.\n2. Check the Account Overview section for correct account details.',
        '1. Open the Dashboard/Home page.\n2. Click on each link in the Quick Links section.',
        '1. Open the Dashboard/Home page.\n2. Click on each link in the Navigation Menu.',
        '1. Open the Dashboard/Home page.\n2. Check the Account Balance section for correct balance display.',
        '1. Open the Dashboard/Home page.\n2. Check the Current Plan section for accurate plan details.',
        '1. Open the Dashboard/Home page.\n2. Review the Recent Transactions section for correct information.',
        '1. Open the Dashboard/Home page.\n2. Check the Service Status section for current service information.',
        '1. Open the Dashboard/Home page.\n2. Click on each Navigation Menu link and verify redirection to correct sections.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Account Overview section displays correct account details including balance, plan, and pending actions.',
        'All Quick Links are functional and redirect to the appropriate sections (e.g., View Bills, Manage Plans, etc.).',
        'All Navigation Menu links are functional and redirect to the correct sections (e.g., Plans, Billing, Services, etc.).',
        'Account Balance is displayed accurately.',
        'Current Plan information is displayed accurately.',
        'Recent Transactions or Requests are displayed correctly.',
        'Service Status is displayed accurately based on the user\'s current services.',
        'Each Navigation Menu link redirects to the correct section.'
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

# Display the new test cases for the dashboard/home page
tools.display_dataframe_to_user(name="Dashboard/Home Page Test Cases", dataframe=dashboard_test_cases)
