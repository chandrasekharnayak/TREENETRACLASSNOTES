from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)
driver.get('https://www.naukri.com/registration/createAccount?othersrcp=22636')

# fullname
# -------------
# 1/id
fullname=driver.find_element(By.ID,'name').send_keys('Biswajit Biswal')
# 2/classname
# fullname = driver.find_element(By.CLASS_NAME,"formInput").send_keys('Biswajit Biswal')
time.sleep(2)

# email id
#1/id
# email = driver.find_element(By.ID,'email').send_keys('biswa58@gmail.com')
# 2/Name
# email=driver.find_element(By.NAME,'email').send_keys('biswa58@gmail.com')
#3/classname
email = driver.find_element(By.CLASS_NAME,'formInput').send_keys('biswa58@gmail.com')
time.sleep(2)

#password
# 1/id
# password = driver.find_element(By.ID,'password').send_keys('biswa5588')
# 2/classname
# email = driver.find_element(By.CLASS_NAME,'__input').send_keys('biswa5588')
# time.sleep(2)

# mobile number
# 1/id
mobile_number=driver.find_element(By.ID,'mobile').send_keys('7504639346')
time.sleep(2)

#linktext
# login
# login = driver.find_element(By.LINK_TEXT,'Login').click()

#Partial_link_text
# login
login= driver.find_element(By.PARTIAL_LINK_TEXT,'Login').click()
