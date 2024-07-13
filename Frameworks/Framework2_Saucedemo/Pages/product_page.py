from Pages.product_page_locator import ProductPageLocator


class ProductPage(ProductPageLocator):
    def __init__(self,driver):
        self.driver = driver

    def get_menu(self):
        return self.driver.find_element(*self.menu_locator)
    def get_logout(self):
        return self.driver.find_element(*self.logout_locator)

    def get_cart1(self):
        return self.driver.find_element(*self.addtocart_locator1)

    def get_cart2(self):
        return self.driver.find_element(*self.addtocart_locator2)

    def cart(self):
        self.get_cart1().click()
        self.get_cart2().click()

    def logout(self):
        self.get_menu().click()
        self.get_logout().click()