from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

#implicit wait
driver.implicitly_wait(3) # Global Wait

serach_bar = driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(2)
click_add_to_cart = driver.find_elements(By.XPATH,"//div[@class='products']/div")

for i in click_add_to_cart:
    if i.find_element(By.XPATH,"h4").text == 'Cucumber - 1 Kg':
        i.find_element(By.XPATH,"div/button").click()
    elif i.find_element(By.XPATH,"h4").text == 'Raspberry - 1/4 Kg':
        i.find_element(By.XPATH, "div/button").click()


driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('wertyuio')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()


#Explicit wait :- conditional wait
wait = WebDriverWait(driver,15) # create a wait
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo"))) # we used wait as condition level


time.sleep(5)
driver.quit()