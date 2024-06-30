from Pages.product_page_locator import ProductPageLocator


class ProductPage(ProductPageLocator):
    def __init__(self,driver):
        self.driver = driver

    def get_menu(self):
        return self.driver.find_element(*self.menu_locator)
    def get_logout(self):
        return self.driver.find_element(*self.logout_locator)

    def logout(self):
        self.get_menu().click()
        self.get_logout().click()