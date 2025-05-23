from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome()

url = 'http://localhost:63342/TREENETRABATCH/BatchCodeData/TREENETRA_AT_15/Selenium/test.html?_ijt=h9crmhr0ejo3671t89sk1apbdc&_ij_reload=RELOAD_ON_SAVE'

driver.get(url)

# first_name =driver.find_element(By.ID,'fname')
# first_name.send_keys('Himanshu')


time.sleep(10)


driver.close()