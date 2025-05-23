from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/loginpagePractise/')

driver.find_element(By.ID,'username').send_keys('rahulshettyacademy')
driver.find_element(By.ID,'password').send_keys('learning')
driver.find_element(By.ID,'signInBtn').click()

expected_list = ['iphone X','Samsung Note 8', 'Nokia Edge', 'Blackberry']
elements = driver.find_elements(By.XPATH,"//h4[@class='card-title']")
# print(elements)
actual_list = []
#
for i in elements:
    data = i.text
    actual_list.append(data)
print(actual_list)
assert expected_list== actual_list