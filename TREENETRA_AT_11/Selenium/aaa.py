from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)
driver.get('file:///D:/TREENETRA/TelecomDomainProject/CodingPart/CRM/new.html')

first_name = driver.find_element(By.ID,'firstname').send_keys('Biswajit')
lastname = driver.find_element(By.ID,'lastname').send_keys('Biswal')
UID =driver.find_element(By.NAME,'uid').send_keys('535970')
gender_male= driver.find_element(By.XPATH,"//input[@value='male']").click()
# gender_female= driver.find_element(By.XPATH,"//input[@value='female']").click()
time.sleep(5)
driver.quit()