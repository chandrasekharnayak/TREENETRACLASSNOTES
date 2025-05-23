from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.maximize_window()

# scroll up and down
scroll_down = driver.execute_script("window.scrollBy(0,750);")

scroll_up = driver.execute_script("window.scrollBy(750,0);")



driver.switch_to.frame('courses-iframe')#either id or name

driver.save_screenshot('frame_screenshot.png') # screenshot

iframe_element = driver.find_element(By.XPATH,"//li[text()=' contact@rahulshettyacademy.com']")
print(iframe_element.text)

driver.switch_to.default_content() #return to main page

driver.find_element(By.ID,'alertbtn').click()

time.sleep(3)
driver.quit()

