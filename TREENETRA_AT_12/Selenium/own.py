# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.options import Options
#
# # Set up Chrome options for headless mode
# chrome_options = Options()
# chrome_options.headless = True
#
# # Initialize the WebDriver
# driver = webdriver.Chrome(options=chrome_options)
#
# # Load the webpage
# driver.get("file:///C:/Users/TREENETRA/PycharmProjects/TREENETRAProject/TREENETRA_AT_12/Selenium/own.html")
#
# # 1. Handle the iframes, jump between them and assert text
# driver.switch_to.frame("iframe1")
# iframe1_text = driver.find_element(By.TAG_NAME, "body").text
# print(iframe1_text)
# # assert "This is iframe 1" in iframe1_text
#
# driver.switch_to.default_content()  # Back to main frame
#
# driver.switch_to.frame("iframe2")
# iframe2_text = driver.find_element(By.TAG_NAME, "body").text
# # assert "This is iframe 2" in iframe2_text
#
# driver.switch_to.default_content()  # Back to main frame
#
# # 2. Handle the multi-windows and assert text
# main_window = driver.current_window_handle
# driver.find_element(By.CLASS_NAME, "new-window-button").click()
#
# # Switch to new window
# for handle in driver.window_handles:
#     if handle != main_window:
#         driver.switch_to.window(handle)
#         break
#
# new_window_text = driver.find_element(By.TAG_NAME, "h1").text
# assert "This is a new window" in new_window_text
# driver.close()
#
# driver.switch_to.window(main_window)  # Back to the main window
#
# # 3. Handle the mouse hover with ActionChains
# menu = driver.find_element(By.LINK_TEXT, "Services")
# submenu = driver.find_element(By.LINK_TEXT, "Service 1")
#
# actions = ActionChains(driver)
# actions.move_to_element(menu).perform()
# actions.click(submenu).perform()
#
# # 4. Perform a double click
# actions.double_click(driver.find_element(By.LINK_TEXT, "Home")).perform()
#
# # 5. Scroll up and down
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down
# driver.execute_script("window.scrollTo(0, 0);")  # Scroll up
#
# # 6. Take a screenshot
# driver.save_screenshot("screenshot.png")
#
# # 7. Handle cross-browser testing
# # - Cross-browser testing involves running this script with different drivers, like Firefox's geckodriver, or Edge's msedgedriver.
#
# # 8. Handle headless mode
# # - Headless mode is already enabled in this script via `chrome_options.headless = True`.
#
# # 9. Handle the dynamic web table
# # Find all columns
# columns = driver.find_elements(By.XPATH, "//table[@class='dynamic-table']//th")
# for col in columns:
#     print(col.text)
#
# # Find the first three rows
# rows = driver.find_elements(By.XPATH, "//table[@class='dynamic-table']//tr[position() <= 3]")
# for row in rows:
#     print([cell.text for cell in row.find_elements(By.TAG_NAME, "td")])
#
# # Find the last row's last data
# last_row_last_data = driver.find_element(By.XPATH, "//table[@class='dynamic-table']//tr[last()]/td[last()]").text
# print(f"Last row's last data: {last_row_last_data}")
#
# # Clean up
# driver.quit()
