from selenium import webdriver
import time

driver =webdriver.Chrome()

url = 'https://www.facebook.com/login/'

driver.get(url)

time.sleep(3)


driver.close()