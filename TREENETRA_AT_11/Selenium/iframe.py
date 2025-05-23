from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

iframe_element = driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")

driver.switch_to.frame(iframe_element)

screenshot = driver.get_screenshot_as_file('iframe.png')


time.sleep(3)
driver.quit()


