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
driver.get(r'C:\Users\TREENETRA\PycharmProjects\TREENETRAProject\TREENETRA_AT_12\Selenium\sibling.html')  # Replace with your local HTML file path


# 3. Auto Suggestive Dropdown
auto_suggestion = driver.find_element(By.XPATH,"//input[@id='search']").send_keys('am')
time.sleep(3)

fetch_datas = driver.find_elements(By.XPATH,"//div[@id='suggestions']/div")

for i in fetch_datas:
    if i.text == 'Amela':
        i.click()

time.sleep(3)
driver.quit()