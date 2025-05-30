from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # Go to the homepage
    # page.goto("https://the-internet.herokuapp.com/")
    # print("Title:", page.title())

    # --- Viewport Resize ---
    # print("Resizing viewport...")
    # page.set_viewport_size({"width": 12800, "height": 7200})
    # time.sleep(3)
    # --- Scroll to bottom ---
    # print("Scrolling down...")
    # time.sleep(3)
    # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    # time.sleep(3)

    # --- Dropdown ---
    # print("Handling dropdown...")
    # page.goto("https://the-internet.herokuapp.com/dropdown")
    # dropdown = page.locator("#dropdown")
    # time.sleep(3)
    # dropdown.select_option("2")  # Select option with value "2"
    # time.sleep(3)
    # selected = dropdown.input_value()
    # print(f"Selected dropdown value: {selected}")

    # --- Alerts & Dialogs ---
    # print("Handling alerts...")
    # page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    #
    # time.sleep(3)
    # def handle_dialog(dialog):
    #     print(f"Dialog message: {dialog.message}")
    #     time.sleep(3)
    #     dialog.accept()
    # page.on("dialog", handle_dialog)
    # page.click("text=Click for JS Alert")  # Trigger alert, automatically accepted

    # --- File Upload ---
    # print("Uploading file...")
    # page.goto("https://the-internet.herokuapp.com/upload")
    # file_input = page.locator('input#file-upload')
    # file_path = "playwright.txt"  # Create this file before running or use your own path
    # time.sleep(3)
    # with open(file_path, "w") as f:
    #     f.write("Hello Playwright file upload test!")
    # file_input.set_input_files(file_path)
    # time.sleep(3)
    # page.click("input#file-submit")
    # print("File uploaded. Result:", page.locator("div#uploaded-files").text_content())

    # --- Popup (New Tab) ---
    # print("Handling popup (new tab)...")
    # page.goto("https://the-internet.herokuapp.com/windows")
    # time.sleep(3)
    # with page.expect_popup() as popup_info:
    #     page.click("text=Click Here")  # Opens new tab
    # popup = popup_info.value
    # print("Popup URL:", popup.url)
    # popup.close()

    # --- File Download (Demonstration) ---
    # The site itself doesn't offer a direct downloadable file,
    # so let's simulate with a dummy example.
    # print("Simulating file download...")
    # page.goto("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
    # with page.expect_download() as download_info:
    #     # Click first download button for PDF example
    #     page.click("a.btn.btn-orange.btn-outline.btn-xl")
    # download = download_info.value
    # download.save_as("sample_downloaded_file.pdf")
    # print("File downloaded:", download.suggested_filename)

    # browser.close()

with sync_playwright() as playwright:
    run(playwright)
