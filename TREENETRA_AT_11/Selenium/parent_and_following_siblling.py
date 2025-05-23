from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG')

driver.implicitly_wait(5)
#parent sibling/ preceding-sibling
click_4_gb_checkbox = driver.find_element(By.XPATH,"//div[text()='4 GB']/preceding-sibling::div").click()


click_realme_checkbox = driver.find_element(By.XPATH,"//div[@title='realme']/div/label/input/following-sibling::div[1]").click()
time.sleep(2)

driver.quit()


iframe
popup and alret

pytest
robo
api
project

