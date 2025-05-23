from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://rahulshettyacademy.com/dropdownsPractise/'
driver.get(url)

driver.implicitly_wait(5)

input_box = driver.find_element(By.ID,'autosuggest').send_keys('ind')

fetch_list = driver.find_elements(By.XPATH,"//li[@role='presentation']/a")

for i in fetch_list:
    if i.text =='India':
        i.click()

time.sleep(5)
driver.quit()

