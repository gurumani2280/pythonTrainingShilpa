from selenium.webdriver.common.by import By

class ProductPageLocator:
    menu_locator = (By.CSS_SELECTOR,".bm-burger-button")
    logout_locator = (By.ID,"logout_sidebar_link")