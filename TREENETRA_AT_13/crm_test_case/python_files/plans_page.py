# Create a DataFrame to store the manual test cases for the Plans Page in the required format
plans_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Display of Current Plan',
        'Verify Available Plans Display',
        'Verify Plan Selection Functionality',
        'Verify Compare Plans Feature',
        'Verify Plan Upgrade Process',
        'Verify Plan Downgrade Process',
        'Verify Proceed Button Functionality',
        'Verify Price Display for Each Plan'
    ],
    'Module / Feature': ['Plans Page'] * 8,
    'Test Case Description': [
        'Verify that the current plan details are displayed correctly with options to upgrade or downgrade.',
        'Verify that all available plans (data-only, talk-time, bundled offers) are displayed with appropriate details.',
        'Verify that the "Select Plan" button works and allows the user to choose a plan.',
        'Verify that the "Compare Plans" feature allows side-by-side comparison of multiple plans.',
        'Verify the process of upgrading the plan from the current plan.',
        'Verify the process of downgrading the plan from the current plan.',
        'Verify that the "Proceed" button works correctly after selecting a plan.',
        'Verify that the price for each plan is displayed accurately.'
    ],
    'Pre-Conditions': ['User is logged in and on the Plans page.'] * 8,
    'Test Steps': [
        '1. Open the Plans page.\n2. Check the details of the current plan displayed.',
        '1. Open the Plans page.\n2. Review the list of available plans displayed on the page.',
        '1. Open the Plans page.\n2. Click on the "Select" button for any plan.\n3. Verify the plan selection process.',
        '1. Open the Plans page.\n2. Click on the "Compare Plans" option.\n3. Select multiple plans and verify the comparison table.',
        '1. Open the Plans page.\n2. Click on the upgrade option for the current plan.\n3. Follow the steps to complete the upgrade.',
        '1. Open the Plans page.\n2. Click on the downgrade option for the current plan.\n3. Follow the steps to complete the downgrade.',
        '1. Open the Plans page.\n2. Select any plan.\n3. Click on the "Proceed" button to confirm the selection.',
        '1. Open the Plans page.\n2. Verify the price of each plan displayed on the page.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Current plan details are displayed correctly with accurate information.',
        'All available plans are displayed with correct details including name, price, and features.',
        'Plan selection is successful, and the user is able to proceed to the confirmation step.',
        'Compare Plans feature works and displays the selected plans side by side with accurate details.',
        'Plan upgrade process is completed successfully with confirmation.',
        'Plan downgrade process is completed successfully with confirmation.',
        'Proceed button works and directs the user to the confirmation step after selecting a plan.',
        'Prices for all plans are displayed accurately on the page.'
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

# Display the new test cases for the Plans page
tools.display_dataframe_to_user(name="Plans Page Test Cases", dataframe=plans_test_cases)
