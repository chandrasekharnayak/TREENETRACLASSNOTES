from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)

open_new_window = driver.find_element(By.ID,"openwindow").click()

driver.switch_to.window(driver.window_handles[1])

click_cource = driver.find_element(By.LINK_TEXT,"Courses").click()

fetch_text = driver.find_element(By.XPATH,"//h1[text()='QA Click Academy']").text
print(fetch_text)

driver.switch_to.window(driver.window_handles[0])

main_page_title = driver.title
print(main_page_title)


time.sleep(3)
driver.quit()