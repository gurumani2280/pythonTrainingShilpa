import pytest
import time


from Pages.login_page import LoginPage


@pytest.mark.usefixtures("init")
class TestLogin3():
    def test_login3(self):
        lp = LoginPage(self.driver)
        lp.login("standard_user","secret_sauce")

        time.sleep(5)