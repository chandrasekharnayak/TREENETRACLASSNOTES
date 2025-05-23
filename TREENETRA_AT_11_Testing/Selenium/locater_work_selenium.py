from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj =  Service('C:\\ChromeDriverPath\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.facebook.com/login/')

#id
email = driver.find_element(By.ID,'email')
email.send_keys('chandrasekhar108@gmail.com')

#name
password = driver.find_element(By.NAME,'pass')
password.send_keys('qwerty@1234')

#link text and partial link text
time.sleep(2)
#link text
# driver.find_element(By.LINK_TEXT,'Forgotten account?').click()

#partial link text

# driver.find_element(By.PARTIAL_LINK_TEXT,'Sign up').click()


#tagname
elemenmts = driver.find_elements(By.TAG_NAME,'input')
# print(type(elemenmts))

for i in elemenmts:
    print(i.get_attribute('name'))



time.sleep(5)

driver.quit()



