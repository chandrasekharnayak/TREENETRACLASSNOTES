from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj =  Service('C:\\ChromeDriverPath\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.facebook.com/login/')

time.sleep(5)

driver.quit()



