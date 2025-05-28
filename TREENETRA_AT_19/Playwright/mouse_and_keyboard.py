from playwright.sync_api import sync_playwright
import time

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto('https://the-internet.herokuapp.com/context_menu')
#
#     time.sleep(3)
#
#     box = page.locator("div#hot-spot")
#     box.click(button='right')
#
#     alert = page.expect_event("dialog",lambda dialog : dialog.accept())
#     browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://the-internet.herokuapp.com/key_presses?')

    page.click("input#target")
    time.sleep(2)
    page.keyboard.press("Enter")

    time.sleep(3)

    page.keyboard.press('ArrowUp')

    browser.close()


#uploading file,Handeling dropdown, Alerts, popup. Dialogs, scrooling and view port Resizing, download the file


