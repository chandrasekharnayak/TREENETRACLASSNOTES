from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    print(dir(p))
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #navigate to the webpage

    page.goto('https://www.tutorialspoint.com/whiteboard.htm')

    page.pause()

    browser.close()
#
#
# x = 10 --- simple var
# _x = 10 ---- private var
#
# __x = 10 --- protected


