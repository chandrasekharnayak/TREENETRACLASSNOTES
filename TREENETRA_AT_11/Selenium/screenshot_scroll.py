from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)

#top to buttom scroll
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

# fix place
driver.execute_script('window.scrollBy(0,300)')

#screen shot

driver.get_screenshot_as_file('screenshot1.png')


time.sleep(2)
driver.quit()

