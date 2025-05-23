from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.facebook.com/?stype=lo&deoia=1&jlou=AfdtvQaBVV1bAj0lwXklSS5qr4izinhQ289IMOf-NrXqU-tTQl21vtBkpd_hodUlSelZXiOiOsJZAlMuZvfo8W4OnDrPJuO8h32656uVWsB10Q&smuh=17725&lh=Ac9mqtumYbTF4A_5KRg')#opening url/heat url

#id
# email = driver.find_element(By.ID,'email').send_keys('qwerty@108')
email = driver.find_element(By.CSS_SELECTOR,'#email').send_keys('djhk')
#name
# email = driver.find_element(By.NAME,'email').send_keys('querty@108')
#classname
# email = driver.find_element(By.CLASS_NAME,'inputtext').send_keys('qwerty@108')
#
# password = driver.find_element(By.CLASS_NAME,'_9npi').send_keys('password@108')
#
# submit = driver.find_element(By.NAME,'login').click()


#LINKTEXT and PARTIALLINKTEXT

#linktext
# forget_password = driver.find_element(By.LINK_TEXT,'Forgotten password?').click()

#Partial_link_text
# forget_password = driver.find_element(By.PARTIAL_LINK_TEXT,'Forgotten').click()

time.sleep(5)
driver.quit()