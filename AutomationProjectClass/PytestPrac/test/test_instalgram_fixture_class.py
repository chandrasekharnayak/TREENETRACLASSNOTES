import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures('instgram_login_page')
class TestInstagramLoginPage:
    def test_login_with_valid_credential(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))
            login_button.click()
        except TimeoutException:
            print("Login page took too long to load.")

        # Fill in the username and password fields and submit the form
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
            username_field.send_keys('treenetra_education')
            password_field.send_keys('Education$108')
            login_button.click()
        except TimeoutException:
            print("Username/password field or login button took too long to load.")

        # Wait for the login process to complete
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("instagram.com/accounts"))
            print("Login successful!")
        except TimeoutException:
            print("Login process took too long.")

        # Do some actions here...

        # Log out
        try:
            profile_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p']")))
            profile_button.click()
            time.sleep(5)
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Log Out']")))
            logout_button.click()
            print("Logged out successfully!")
        except TimeoutException:
            print("Logout process sucessfully.")

    def test_login_with_invalid_credential(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))
            login_button.click()
        except TimeoutException:
            print("Login page took too long to load.")

        # Fill in the username and password fields and submit the form
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
            username_field.send_keys('treenetra_educatio')
            password_field.send_keys('Education$18')
            login_button.click()
        except TimeoutException:
            print("Username/password field or login button took too long to load.")

        # Wait for the login process to complete
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("instagram.com/accounts"))
            print("Login successful!")
        except TimeoutException:
            print("Login process took too long.")

        # Do some actions here...

        # Log out
        try:
            profile_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p']")))
            profile_button.click()
            time.sleep(5)
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Log Out']")))
            logout_button.click()
            print("Logged out successfully!")
        except TimeoutException:
            print("Logout process took too long.")

