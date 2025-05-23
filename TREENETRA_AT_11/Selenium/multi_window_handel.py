from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.amazon.in/')

time.sleep(2)
#open new tab
driver.execute_script("window.open('','_blank');")

time.sleep(2)
#window switch one to another
driver.switch_to.window(driver.window_handles[1])

driver.get('https://treenetra.in/')



time.sleep(5)
driver.quit()