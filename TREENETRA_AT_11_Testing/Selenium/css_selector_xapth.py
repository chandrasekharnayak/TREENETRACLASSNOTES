from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj =  Service('C:\\ChromeDriverPath\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.flipkart.com/')

'''serach_box = driver.find_element(By.XPATH,"//div/form/div/div/input")
serach_box.send_keys('samsung mobiles')'''

#gro

gro = driver.find_element(By.XPATH,"(//div/div/div/div/div/a/div/div/span/span)[1]")
gro.click()


time.sleep(5)

driver.quit()
