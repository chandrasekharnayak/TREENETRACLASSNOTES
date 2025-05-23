'''
fixture
plugings-------
hookings

fixture :- 4 types of fixture
functional
class
session
module
'''

import pytest
from selenium import webdriver

#functional fixture
@pytest.fixture()
def browser():
    #setup:- precondition
    driver = webdriver.Chrome()
    yield driver
    #teardown:- postcondition
    driver.quit()

@pytest.fixture(scope='class')
def instgram_login_page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.instagram.com/')
    request.cls.driver = driver
    yield
    driver.close()




















