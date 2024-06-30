from selenium.webdriver.common.by import By
class LoginPageLocator:
    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_locator = (By.ID, "login-button")