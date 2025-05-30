#uploading file,Handeling dropdown, Alerts, popup. Dialogs, scrooling and view port Resizing, download the file

from playwright.sync_api import sync_playwright
import time

def run_application(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to the homepage
    # page.goto('https://the-internet.herokuapp.com/')
    # print('Title:-',page.title())

    #view port Resizing
    # print('Resizeing view port')
    # page.set_viewport_size({"width":12800,"height":7200})
    # time.sleep(3)

    #Scroll
    # print("scroll down")
    # time.sleep(2)
    # page.evaluate("window.scrollTo(0,document.body.scrollHeight);")
    # time.sleep(2)

    # Dropdown
    # print('handeling dropdown')
    # page.goto('https://the-internet.herokuapp.com/dropdown')
    # dropdown = page.locator("#dropdown")
    # time.sleep(3)
    # dropdown.select_option("2")# select option with value "2"
    # selected = dropdown.input_value()
    # print(f"selected dropdown value:-{selected}")
    # time.sleep(3)
    #
    # assert selected=='2','not matched'


    #alert
    # page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    #
    # def handel_dialog(dialog):
    #     print(f"dialog messgage:-{dialog.message}")
    #     time.sleep(3)
    #     dialog.accept()
    # page.on("dialog",handel_dialog)
    # page.click("text=Click for JS Alert")

    #File upload
    print("uploading a file")
    page.goto("https://the-internet.herokuapp.com/upload")
    file_input = page.locator("input#file-upload")
    time.sleep(2)
    file_path = r"C:\Users\TREENETRA\PycharmProjects\TREENETRADAILY\TREENETRA_AT_19\Playwright\dj.txt"

    with open(file_path,'w') as file:
        file.write('hello dj')
    file_input.set_input_files(file_path)
    page.click("input#file-submit")
    time.sleep(3)
    print(page.locator("div#uploaded-files").text_content().strip())


#download-- download, and read file name
# https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/
with sync_playwright() as playwright:
    run_application(playwright)