

from playwright.sync_api import  sync_playwright
import time

#opening new tab.window
'''with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # goto the navigation url

    page.goto('https://the-internet.herokuapp.com/windows')


    #click the link thet open a new window

    with context.expect_page() as new_page_info:
        page.click("a[href='/windows/new']")

    new_page = new_page_info.value
    print(new_page)


    print('first_page:-',page.title())
    print('second_apge:-', new_page.title())

    print('new page intraction:-',new_page.content())


    print(new_page.locator("//h3[text()='New Window']").text_content())

    new_page.close()

    browser.close()'''


#switching between pages

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()

    # goto the navigation url

    page1.goto('https://the-internet.herokuapp.com/windows')

    #opening new tab
    with context.expect_page() as new_page_info:
        page1.click("a[href='/windows/new']")

    page2 = new_page_info.value

    #list all open pages
    all_pages = context.pages

    for index,value in enumerate(all_pages):
        print(f"page number {index+1}:- {value}")

    #switch to page1
    page1.bring_to_front()
    print(page1.url)

    #switcg to page
    page2.bring_to_front()
    print(page2.url)
    browser.close()


