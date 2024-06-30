import pytest
import time


from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


@pytest.mark.usefixtures("init")
class TestLogout1():
    def test_logout1(self):
        lp = LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")
        time.sleep(5)
        pp = ProductPage(self.driver)
        pp.logout()
        time.sleep(6)
