# Create a DataFrame to store the manual test cases for the Service Requests/Ticketing Page in the required format
ticketing_test_cases = pd.DataFrame({
    'Test Case ID': ['TC01', 'TC02', 'TC03', 'TC04', 'TC05', 'TC06', 'TC07', 'TC08'],
    'Test Case Title / Name': [
        'Verify Request ID Display',
        'Verify Status Field Functionality',
        'Verify Details View for Service Requests',
        'Verify Submit New Request Button Functionality',
        'Verify Service Request Creation',
        'Verify Status Update for Service Requests',
        'Verify Request ID Uniqueness',
        'Verify List/Filter of Service Requests'
    ],
    'Module / Feature': ['Service Requests/Ticketing Page'] * 8,
    'Test Case Description': [
        'Verify that the Request ID is displayed correctly for each service request.',
        'Verify that the status of the service request is displayed correctly (e.g., Open, In Progress, Closed).',
        'Verify that clicking on "View Details" displays the detailed information of the service request.',
        'Verify that the "Submit New Request" button is functional and allows users to create a new service request.',
        'Verify that a new service request can be successfully created by entering all the required details.',
        'Verify that the status of a service request can be updated and reflects the correct progress (Open, In Progress, Closed).',
        'Verify that each Request ID is unique and not duplicated.',
        'Verify that the list of service requests can be filtered or sorted by status, date, or request type.'
    ],
    'Pre-Conditions': ['User is logged in and on the Service Requests/Ticketing page.'] * 8,
    'Test Steps': [
        '1. Open the Service Requests/Ticketing page.\n2. Review the Request ID for each service request in the list.',
        '1. Open the Service Requests/Ticketing page.\n2. Check the status field for each request and ensure it is accurate.',
        '1. Open the Service Requests/Ticketing page.\n2. Click on "View Details" for any service request.\n3. Verify the displayed details.',
        '1. Open the Service Requests/Ticketing page.\n2. Click on the "Submit New Request" button.\n3. Enter details for a new request.',
        '1. Open the Service Requests/Ticketing page.\n2. Use the "Submit New Request" button to create a new service request.\n3. Submit the request.',
        '1. Open the Service Requests/Ticketing page.\n2. Change the status of any service request and verify the update.',
        '1. Open the Service Requests/Ticketing page.\n2. Review the list of requests to ensure that each request has a unique Request ID.',
        '1. Open the Service Requests/Ticketing page.\n2. Use the filters or sorting options to view the service requests by status, date, or request type.'
    ],
    'Test Data': [''] * 8,
    'Expected Result': [
        'Request ID is displayed correctly for each service request.',
        'Status field accurately reflects the current status of the service request.',
        '"View Details" displays the complete and correct information of the selected service request.',
        '"Submit New Request" button allows the user to create a new service request without issues.',
        'New service request is successfully created and displayed in the list.',
        'Status of the service request is updated and reflected correctly on the page.',
        'Each Request ID is unique and no duplicates are found.',
        'List of service requests is filtered or sorted correctly based on the selected criteria.'
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

# Display the new test cases for the Service Requests/Ticketing page
tools.display_dataframe_to_user(name="Service Requests/Ticketing Page Test Cases", dataframe=ticketing_test_cases)
