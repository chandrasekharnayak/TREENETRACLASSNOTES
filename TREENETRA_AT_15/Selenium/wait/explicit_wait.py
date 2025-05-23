'''explict wait is a conditional wait. based on condition till wait a
perticular element to be net beforeintracting with a web element.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''print(dir(EC))
# visibility_of_element_located
visibility_of_any_elements_located
visibility_of_all_elements_located
visibility_of
# text_to_be_present_in_element_value
# text_to_be_present_in_element_attribute
# text_to_be_present_in_element
# presence_of_element_located
presence_of_all_elements_located
invisibility_of_element_located
# frame_to_be_available_and_switch_to_it
# element_to_be_selected
# element_to_be_clickable
element_selection_state_to_be
element_located_to_be_selected
element_located_selection_state_to_be
element_attribute_to_include'''


driver = webdriver.Chrome()

url = 'https://www.flipkart.com/black-friday-sale-store?param=72922&s_kwcid=AL!739!3!676201929245!b!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_exe_buyers_goog&gad_source=1&gclid=Cj0KCQiAo5u6BhDJARIsAAVoDWvS9buglx9k3P1chQB7ZgZ2sKJCDAwhZ4ZLLbuFGw65F0VP7kwxgwMaAqGLEALw_wcB'

driver.get(url)

search_bar = driver.find_element(By.XPATH,"//input[@name='q']")
search_bar.send_keys('Mobile',Keys.ENTER)

click_samsung_check_box = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[text()='SAMSUNG']/preceding-sibling::div")))
click_samsung_check_box.click()

time.sleep(1)
gb_select = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[text()='8 GB and Above']/preceding-sibling::div")))
gb_select.click()

# time.sleep(3)
# gb_select = driver.find_element(By.XPATH,"//div[text()='8 GB and Above']/preceding-sibling::div")
# gb_select.click()

#how to check the ancher tag using tagname

'''a_tag_check = driver.find_elements(By.TAG_NAME,'a')
print(a_tag_check)
print(len(a_tag_check))'''

#link text and partial link text

# link text :- wants the static text mentioned in the a tag, and it want a perfect data

'''click_became_a_seller = driver.find_element(By.LINK_TEXT,"Become a Seller")
click_became_a_seller.click()'''

#partial text :- paritially coorrect the text

click_became_a_seller = driver.find_element(By.PARTIAL_LINK_TEXT,"Become")
click_became_a_seller.click()


time.sleep(5)
driver.close()


# element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.Locater,'')))
'''
time.sleep(8)---dom element 3 sec---- 5sec
implicit_wait(8) --- do element 3 sec --- 5 sec not waste --- next element 
10--- 4 sec --- 6 sec -- next element

'''