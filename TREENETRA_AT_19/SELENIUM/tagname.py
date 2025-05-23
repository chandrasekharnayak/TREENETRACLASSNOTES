from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=1d77edae-dc60-4bb6-8540-305bfcc4402f&as-searchtext=mo')


tags = driver.find_element(By.TAG_NAME,'aa')
print(tags)
print(len(tags))

for i in tags:
    print(i.text)

# driver.quit()# close all
driver.close()#close the current window