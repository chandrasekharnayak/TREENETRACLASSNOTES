from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.facebook.com/r.php?entry_point=login'
driver.get(url)

first_name = driver.find_element(By.NAME,'firstname')
first_name.send_keys('Vivek')

sure_name = driver.find_element(By.NAME,'lastname')
sure_name.send_keys('Das')

male = driver.find_element(By.XPATH,'//div/span/span[2]/label/input').click()


time.sleep(3)

driver.quit()




#locaters
# id
# name
# classname
# tagname
# link text
# partial link text
# xpath
# css selector


#xpath

# absolute:- node root(parent-child relation shjip)
# //div/span/span[2]/label/input
# relative xapth - dynamic location value
//tagname[@attribute='value'] --- very very high 6ways
//tagname[text()='text_name']
sibling :- following-sibling, preceding-sibling
//tagname[@attribute='value']/following-sibling::tagname
jump to parent
//tagname[@attribute='value']/parent::parent_tagname
#start-with, end-with, normalization-text, contains

https://rahulshettyacademy.com/AutomationPractice/