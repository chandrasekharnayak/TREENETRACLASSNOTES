from playwright.sync_api import sync_playwright

def laogin_facebook(email,password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.facebook.com/login/')

        page.fill("//input[@id='email']",email)
        page.fill("//input[@id='pass']",password)

        page.click("//button[@id='loginbutton']")


        #screenshot
        page.screenshot(path='fblogin.png')

        page.wait_for_timeout(5000)
        browser.close()



laogin_facebook('k.csnayak108@gmail.com','fvyjhftydty')


loctaer
iframe
windows
actions
mouse
keyboard
auto wait
dropdowns


7pm