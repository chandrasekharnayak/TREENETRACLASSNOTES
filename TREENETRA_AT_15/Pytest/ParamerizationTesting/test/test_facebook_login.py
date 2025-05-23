import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize("username,password,expected_result",[
    ("7008379108","Agastya@108**","pass"),#positive testcase
    ("7008379108",'kjbhjkbj','fail'),#negetive testcase
    ('jkbhjkbh','Agastya@108**','fail'),#negetive testcase
    ('7008379108','','fail'),#negetive testcase
    ('','','fail'),#negetive testcase
    ('', 'Agastya@108**', 'fail'),  # negetive testcase
])
def test_facebook_login(username,password,expected_result):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get('https://www.facebook.com/login/')

        username_field = driver.find_element(By.ID,'email')
        password_field = driver.find_element(By.ID,'pass')
        login_button = driver.find_element(By.ID,'loginbutton')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()

        time.sleep(5)

        if expected_result =='pass':
            assert 'https://www.facebook.com/' in driver.current_url
        else:
            error_message = driver.find_element(By.XPATH,"//div[@class='_9ay7']")
            assert error_message.is_displayed()


    finally:
        driver.quit()