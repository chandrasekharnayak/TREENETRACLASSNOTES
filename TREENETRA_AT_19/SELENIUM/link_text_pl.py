from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

#intract with a hyper

# driver.find_element(By.ID,'u_0_6_l1').click()

# driver.find_element(By.LINK_TEXT,'Forgotten password').click()

driver.find_element(By.PARTIAL_LINK_TEXT,'password').click()

time.sleep(3)
driver.close()