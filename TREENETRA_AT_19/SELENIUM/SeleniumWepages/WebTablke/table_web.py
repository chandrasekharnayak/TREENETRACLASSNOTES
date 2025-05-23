from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

file_path = os.path.abspath('table.html')

driver.get(file_path)

expected_res = 4
'''thead = driver.find_elements(By.XPATH,'//thead/tr/th')

marks_index = 1
for i in thead:
    if i.text =='Marks':
        break
    marks_index=marks_index+1
# print(marks_index)

marks = driver.find_elements(By.XPATH,f"//tbody/tr/td[{marks_index}]")

total_sum = 0
for mark in marks:
    total_sum = total_sum +int(mark.text)'''

# print(total_sum)


count_canidates = driver.find_elements(By.XPATH,"//tbody//tr/td[1]")

actual_res = len(count_canidates)

# assert expected_res == actual_res,'failoed due to count mismatch'

if  expected_res == actual_res:
    print('pass')


time.sleep(4)
driver.close()


#create ecom web table
#more than 1000 rows
#name,address,product_name,date,price,month

# assert
# total row count of web table
# check how may product by a indivisual customer and price ,prpduct_name:- provide customer name
# cehck the sell between 1st 15days and last 15days, and compare growth and loss.
# provide a indivisual date , thyen given the total product sell and product owner name