import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init")
class TestLogin2():
    def test_login2(self):
        username_element = self.driver.find_element(By.ID, "user-name")
        username_element.send_keys("standard_user")
        time.sleep(2)
        password_element = self.driver.find_element(By.ID, "password")
        password_element.send_keys("secret_sauce")
        time.sleep(2)
        login = self. driver.find_element(By.ID, "login-button")
        login.click()
        time.sleep(15)