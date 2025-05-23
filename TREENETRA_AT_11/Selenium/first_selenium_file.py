# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.
# import time
#
# service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service=service_object)
#
# driver.get('https://www.naukri.com/')#opening url/heat url
# driver.implicitly_wait(3)
#
#
# login = driver.find_element(By.XPATH,"//a[@id='login_Layer']")
# login.click()
#
# email = driver.find_element(By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']")
# email.send_keys('najayakumar24@gmail.com')
#
# password = driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
# password.send_keys('Dkams@54321')
#
# login = driver.find_element(By.XPATH,"//button[@type='submit']")
# login.click()
#
# view_profile = driver.find_element(By.XPATH,"//a[normalize-space()='View profile']")
# view_profile.click()
#
# '''Personal'''
#
# pen_link = driver.find_element(By.XPATH,"//em[@class='icon edit']")
# pen_link.click()
#
# name = driver.find_element(By.XPATH,"//input[@id='name']")
# name.send_keys('Ajay')
#
# experience = driver.find_element(By.XPATH,"//label[@for='exp-radio']")
# experience.click()
#
#
#
#
# time.sleep(3)
#
# driver.quit()