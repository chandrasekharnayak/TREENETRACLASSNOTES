import pytest
from selenium.webdriver.common.by import By
import time


'''def test_facebook_title(set_browser):
    time.sleep(10)
    assert 'Facebook' in set_browser.title
'''

@pytest.mark.usefixtures("browser_per_class")
class TestFacebookClass:

    def test_login_page_title(self,browser_per_class):
        time.sleep(30)
        assert "Facebook" in browser_per_class.title

