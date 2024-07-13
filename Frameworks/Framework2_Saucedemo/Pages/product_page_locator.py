from selenium.webdriver.common.by import By

class ProductPageLocator:
    menu_locator = (By.CSS_SELECTOR,".bm-burger-button")
    logout_locator = (By.ID,"logout_sidebar_link")
    addtocart_locator1 = (By.ID, "add-to-cart-sauce-labs-backpack")
    addtocart_locator2 = (By.ID, "add-to-cart-sauce-labs-bike-light")