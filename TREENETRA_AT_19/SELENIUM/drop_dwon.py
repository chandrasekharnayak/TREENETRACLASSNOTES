#two types dropdown
'''
1.selective drop
2.Auto suggestive dropdown


'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

select_locater = Select(driver.find_element(By.ID,'dropdown-class-example'))
# select_locater.select_by_index(3)
# select_locater.select_by_value('option2')
select_locater.select_by_visible_text('Option1')

time.sleep(3)
#select the all option and its depends webpage to webpage
# select_locater.all_selected_options()

# select_locater.deselect_by_index(1)


time.sleep(3)

driver.close()'''




#auto-seletive

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

input_box = driver.find_element(By.ID,'autocomplete')
input_box.send_keys('ind')

# values = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li")

time.sleep(2)
ul_tag = driver.find_element(By.XPATH,"//ul[@id='ui-id-1']")
values = ul_tag.find_elements(By.XPATH,"li")


for value in values:
    if value.text =='India':
        value.click()


time.sleep(3)

driver.close()