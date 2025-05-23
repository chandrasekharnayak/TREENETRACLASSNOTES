from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.maximize_window()

def action_chain():
    hover_element = driver.find_element(By.ID,'mousehover')
    actions = ActionChains(driver)
    return actions.move_to_element(hover_element).perform()

# action_chain()
# top_option = driver.find_element(By.XPATH,"//a[text()='Top']")
# time.sleep(2)
# top_option.click()
# #
#
# action_chain()
# reload = driver.find_element(By.XPATH,"//a[text()='Reload']")
# time.sleep(2)
# reload.click()

#dobule click
'''find_element = driver.find_element(By.Locater,'value')
action = ActionChains(driver)
action.double_click(find_element).perform()'''

#drag and down




time.sleep(3)
driver.quit()