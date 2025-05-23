'''
there are two types of dropdown avl
1.selective
2.autosuggestive
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver= webdriver.Chrome()

url = 'https://rahulshettyacademy.com/client'

driver.get(url)

click_hyperlink =driver.find_element(By.LINK_TEXT,"Register here")
click_hyperlink.click()

selective_dropdown = Select(driver.find_element(By.XPATH,"//select[@formcontrolname='occupation']"))
# selective_dropdown.select_by_visible_text('Engineer')
# selective_dropdown.select_by_value('4: Scientist')
# selective_dropdown.select_by_index(3)


time.sleep(3)
driver.close()

