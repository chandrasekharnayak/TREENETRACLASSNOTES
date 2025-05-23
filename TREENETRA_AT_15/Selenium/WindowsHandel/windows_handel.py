from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

#open a new tab
driver.execute_script("window.open('','_blank');")

time.sleep(2)
#jump one window to another
driver.switch_to.window(driver.window_handles[1])

driver.get('https://treenetraeducation.com/')

time.sleep(3)
#return default window
driver.switch_to.window(driver.window_handles[0])


time.sleep(3)
driver.quit()
