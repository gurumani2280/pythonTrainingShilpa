from Pages.login_page_locator import LoginPageLocator


class LoginPage(LoginPageLocator):
    def __init__(self,driver):
        self.driver=driver
    def get_username(self):
        return self.driver.find_element(*self.username_locator)
    def get_password(self):
        return self.driver.find_element(*self.password_locator)
    def get_login(self):
        return self.driver.find_element(*self.login_locator)

    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_login().click()

