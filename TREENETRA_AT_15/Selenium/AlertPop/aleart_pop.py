from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

#handel alerts
alreat_click = driver.find_element(By.ID,"alertbtn").click()

time.sleep(3)
alert = driver.switch_to.alert
alert.accept()


#pop up

input_box = driver.find_element(By.ID,'name')
input_box.send_keys('manas')

confir = driver.find_element(By.ID,'confirmbtn')
confir.click()

popup_switch = driver.switch_to.alert
# popup_switch.accept()
popup_switch.dismiss()

time.sleep(3)
driver.quit()
