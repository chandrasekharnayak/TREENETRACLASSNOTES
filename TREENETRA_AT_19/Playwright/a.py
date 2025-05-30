# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#
#     # Go to the iFrame page
#     page.goto("https://the-internet.herokuapp.com/iframe")
#
#     # Locate the frame by its name or selector
#     frame = page.frame(name="mce_0_ifr")
#
#     # Access and interact with elements inside the frame
#     text_area = frame.locator("#tinymce")
#     print("Existing Text:", text_area.inner_text())
#
#     # Clear and type new text
#     # text_area.fill("Hello from Playwright!")
#
#     # Take a screenshot of the frame
#     page.screenshot(path="iframe_screenshot.png")
#
#     browser.close()

'''Opening New Tabs/Windows'''

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     # Go to the page with multiple windows
#     page.goto("https://the-internet.herokuapp.com/windows")
#
#     # Click the link that opens a new window
#     with context.expect_page() as new_page_info:
#         page.click("a[href='/windows/new']")
#
#     # Get the new page (tab)
#     new_page = new_page_info.value
#
#     # Print titles of both pages
#     print("Original Page Title:", page.title())
#     print("New Page Title:", new_page.title())
#
#     # Interact with the new page
#     print("New Page Content:", new_page.content())
#
#     # Close the new page
#     new_page.close()
#
#     # Continue with the original page
#     print("Back to Original Page")
#
#     browser.close()


'''Switching Between Pages'''
#
# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page1 = context.new_page()
#
#     page1.goto("https://the-internet.herokuapp.com/windows")
#
#     # Open new tab
#     with context.expect_page() as new_page_info:
#         page1.click("a[href='/windows/new']")
#
#     page2 = new_page_info.value
#
#     # List all open pages
#     all_pages = context.pages
#     for idx, p in enumerate(all_pages):
#         print(f"Page {idx + 1} Title: {p.title()}")
#
#     # Switch back to page1
#     page1.bring_to_front()
#     print("Switched back to Page 1:", page1.url)
#
#     # Switch to page2
#     page2.bring_to_front()
#     print("Switched to Page 2:", page2.url)
#
#     browser.close()

'''Communicating Between Pages (Sharing Data)'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # Page 1: Set localStorage
    page1 = context.new_page()
    page1.goto("https://the-internet.herokuapp.com")
    page1.evaluate("localStorage.setItem('testKey', 'Hello from Page 1')")
    print("Data stored in localStorage on Page 1.")

    # Page 2: Access localStorage
    page2 = context.new_page()
    page2.goto("https://the-internet.herokuapp.com")
    value = page2.evaluate("localStorage.getItem('testKey')")
    print("Retrieved from localStorage on Page 2:", value)

    browser.close()
