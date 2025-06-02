from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #goto the navigation url

    page.goto('https://the-internet.herokuapp.com/iframe')

    #handel frame and locate the element
    frame = page.frame(name="mce_0_ifr")

    #access and intracting with element inside the frame
    text_area = frame.locator("#tinymce")
    print(text_area.inner_text())

    #take screenshot
    page.screenshot(path="iframe_screnshot.png")


    browser.close()