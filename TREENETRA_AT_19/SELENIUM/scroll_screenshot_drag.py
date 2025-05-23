# from selenium import webdriver
# import time
#
#
# driver = webdriver.Chrome()
# driver.get('https://jqueryui.com/resizable/')
# driver.maximize_window()
#
# time.sleep(2)
#scroll down using js
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


#screenshot
# driver.save_screenshot(r"C:\Users\TREENETRA\OneDrive\Desktop\screenshot1.png")

# time.sleep(3)
# driver.close()


# js
'''
window-- class
scrollTo --- x,y
scrollUp -- down to up
scrollBy-- up to down'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')
driver.maximize_window()

driver.implicitly_wait(5)

time.sleep(2)



source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

actions = ActionChains(driver)
actions.drag_and_drop(source,target).perform()



time.sleep(3)
driver.close()



