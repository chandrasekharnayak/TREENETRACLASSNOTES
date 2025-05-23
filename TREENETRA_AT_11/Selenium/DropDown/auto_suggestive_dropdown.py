from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')#opening url/heat url

input_data = driver.find_element(By.ID,"autosuggest").send_keys('Ind')
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//li[@role='presentation']/a")
for i in countries:
    if i.text == 'India':
        i.click()


time.sleep(5)

driver.quit() # single web application
