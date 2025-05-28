from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demoblaze.com/')

    time.sleep(3)

    #Click Login Button
    page.click("a#login2")

    #Explicit wait -- selector # attched, detached , visible, hidden
    page.wait_for_selector("div#logInModal" , state='visible')

    #Fill in the logincredential

    page.fill('input#loginusername','treenetra')
    page.fill('input#loginpassword','treenetra')

    #click login
    page.click("button[onclick='logIn()']")

    # page.wait_for_timeout() Wait for specific amount of time (in miloisec),

    # page.wait_for_function() Wait for a java scripts function

    # page.wait_for_load_state()  network, domconentent

    page.wait_for_selector("a#logout2",state='visible')

    assert page.is_visible('a#logout2'),'Login failed'

    time.sleep(2)

    title = page.title()

    assert title == 'STORE','Login in unsucessful'

    page.click('a#logout2')

    time.sleep(3)

    browser.close()