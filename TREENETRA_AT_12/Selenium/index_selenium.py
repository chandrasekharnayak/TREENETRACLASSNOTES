import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


# Set up the WebDriver
driver = webdriver.Chrome()
driver.get(r'C:\Users\TREENETRA\PycharmProjects\TREENETRAProject\TREENETRA_AT_12\Selenium\Calendar\index.html')

today = driver.find_element(By.XPATH,"//td[contains(@class,'today')]")
print(today.text)

previous_date = driver.find_element(By.XPATH,"(//td[contains(@class,'today')]/preceding-sibling::td)[2]")
print(previous_date.text)

next_date = driver.find_element(By.XPATH,"(//td[contains(@class,'today')]/following-sibling::td)[1]")
print(next_date.text)

# (//td[contains(@class,'today')]/../preceding-sibling::tr)[1]/td[text()='3']
# (//td[contains(@class,'today')]/../following-sibling::tr)[1]/td[text()='23']
time.sleep(3)
driver.close()



























# Implicit Wait
# driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be available

# Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # 1. Relatable and Parent Sibling
# parent_dropdown = driver.find_element(By.ID, 'parent')
# child_dropdown = driver.find_element(By.ID, 'child')
# parent_dropdown.click()
# parent_dropdown.find_element(By.XPATH, "//option[@value='2']").click()
# wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@data-parent='2']")))


# # 2. Selective Dropdown
# var = Select(driver.find_element(By.ID,'parent'))
# click_op = var.select_by_visible_text('Option 2')
#
#
# # 3. Auto Suggestive Dropdown
# auto_suggestion = driver.find_elements(By.XPATH,"//datalist[@id='suggestions']")
# print(len(auto_suggestion))

 # 4. Iframe
# iframe = driver.find_element(By.TAG_NAME, 'iframe')
# driver.switch_to.frame(iframe)
# Interact with iframe content here if needed
# driver.switch_to.default_content()

# 5. Handle Popup and Alert
# alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show Alert')]")
# alert_button.click()
# Alert(driver).accept()  # Accept the alert

# popup_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Open Popup')]")
# popup_button.click()

# 6. Mouse Hover
# hover_box = driver.find_element(By.ID, 'hover-box')
# actions = ActionChains(driver)
# actions.move_to_element(hover_box).perform()

# 7. Action Chain (Example: Mouse Hover and Click)
# actions.move_to_element(hover_box).click().perform()

# time.sleep(2)
# # Close the browser
# driver.quit()