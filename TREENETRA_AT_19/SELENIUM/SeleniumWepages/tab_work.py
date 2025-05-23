from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# ..
# ..
# ..
# ..

time.sleep(3)
#open a new tab usingh js excuter

driver.execute_script("window.open('')")

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

driver.get('https://meet.google.com/landing?authuser=0')

time.sleep(2)

#return to main window

driver.switch_to.window(tabs[0])
print('back to main windows')

time.sleep(3)

driver.quit()