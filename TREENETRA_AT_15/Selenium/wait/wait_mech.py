#wait mechanisim
'''
implict wait
explicit wait
Fulient wait


implict wait :-
Applies to all element globally
its comes directly webdriver . driver.implict_wait
less fixiable
static wait

explicit wait :-
Applies to specific elements or condition
WebDriverWait
Cutomizable with various condition
dynamic wait--- complex element, complec senario
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://rahulshettyacademy.com/seleniumPractise/#/'

driver.get(url)

driver.implicitly_wait(5)

search_bar = driver.find_element(By.XPATH,"//input[@type='search']")
search_bar.send_keys('ber')

time.sleep(2)
add_cart_click = driver.find_elements(By.XPATH,"//button[text()='ADD TO CART']")
for i in add_cart_click:
    i.click()

cart_click = driver.find_element(By.XPATH,"//img[@alt='Cart']")
cart_click.click()

procced_to_checkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")
procced_to_checkout.click()

promo_code = driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']")
promo_code.send_keys('qwertyu')

click_apply = driver.find_element(By.XPATH,"//button[text()='Apply']")
click_apply.click()

invalid_code = driver.find_element(By.XPATH,"//span[text()='Invalid code ..!']").text

assert invalid_code == 'Invalid code ..!'





time.sleep(2)
driver.close()


















