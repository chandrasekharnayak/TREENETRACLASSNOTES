#lunching browser :- chromium , firefox and webkit

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    #chromium
    browser = p.chromium.launch(headless=False)

    #firefox
    # browser = p.firefox.launch(headless=False)

    #webkit
    # browser = p.webkit.launch(headless=False)


    #opening a new  context and page
    context = browser.new_context()

    #new page
    page = context.new_page()

    #navigate to a website

    url = ''
    page.goto(url)

    #locating element

    #css selector
    page.locator("input#username").fill('value')
    page.locator("css").click

    # Xpath


    #Role text and custom

    page.get_by_role("button", name='Log in').click()
    page.get_by_text('log in').fill()

    #type()
    page.locater('css,xpath').type('admin123',delay=100)

    #check()
    #checkbox and radio button
    page.locator('').check()

    #uncheck() :- checkbox , check to uncheck


    #select_option()

    page.locator("select#country").select_option('IN')
    page.locator("select#country").select_option(label='India')
    page.locator("select#country").select_option(index=2)
    page.locator("select#country").select_option(['python','java'])








    browser.close()
