from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json

driver = webdriver.Chrome()

file_path = os.path.abspath('ecom.html')

driver.get(file_path)

#json file handel in test data activities

with open('test_data.json','r') as file:
    data = file.read()
    excepted_result = json.loads(data)




# total row count of web table

'''actual_total_rows = driver.find_elements(By.XPATH,"//tbody[@id='ecom-data-body']/tr")

assert  excepted_result['row_count']  == len(actual_total_rows),f'{len(actual_total_rows)} not equal to {excepted_result['row_count']}'

time.sleep(3)'''


#2

'''name = 'Bob'
products = driver.find_elements(By.XPATH,f"//tr/td[text()='{name}']/following-sibling::td[2]")
products_name = [i.text for i in products]
print(products_name)
print(products)


#price
price = driver.find_elements(By.XPATH,f"//tr/td[text()='{name}']/following-sibling::td[4]")

all_price_list = [eval(i.text) for i in price]
print(sum(all_price_list))'''



#3
dates = driver.find_elements(By.XPATH,'//tr/td[4]')

for i in dates:
    dd = int(i.text[-2::])



driver.close()


# assert
# total row count of web table
# check how may product buy a indivisual customer and price ,prpduct_name:- provide customer name
# cehck the sell between 1st 15days and last 15days, and compare growth and loss,
# provide a indivisual date , thyen given the total product sell and product owner n

