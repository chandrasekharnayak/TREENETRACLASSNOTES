#class fixture

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def browser_per_class():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/login/')
    driver.maximize_window()

    # login

    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')
    login_button = driver.find_element(By.ID, 'loginbutton')

    username_field.send_keys('7008379108')
    password_field.send_keys('Agastya@108**')

    login_button.click()
    yield driver
    #postcondition logout