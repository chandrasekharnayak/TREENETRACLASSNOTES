from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()

url = 'https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'

driver.get(url)

name = driver.find_element(By.ID,'name')
name.send_keys('Manas ranjan')

email = driver.find_element(By.NAME,"email")
email.send_keys('manas@gmail.com')

#absolute xpath
# gender_radio = driver.find_element(By.XPATH,"(//div/div/div/div[2]/input)[1]")
# gender_radio.click()

#relatable xpath
gender_radio = driver.find_element(By.XPATH,"(//input[@type='radio'])[2]")
gender_radio.click()


//input[@id='mobile']
(//div[@class='col-sm-3 text-left']/input)[5]
//textarea[@id='picture']

xpath

text
conatins
normalization_text
sibling
parent node
child node






time.sleep(3)


driver.close()