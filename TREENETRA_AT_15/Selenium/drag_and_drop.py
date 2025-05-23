from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()



driver.get('https://www.globalsqa.com/demo-site/draganddrop/#google_vignette')

driver.maximize_window()

driver.implicitly_wait(5)
source = driver.find_element(By.XPATH,"(//h5[text()='High Tatras']/following-sibling::img)[1]")
target = driver.find_element(By.ID,'trash')

#perform drag and drop

action = ActionChains(driver)
action.drag_and_drop(source,target).perform()

time.sleep(3)
driver.quit()