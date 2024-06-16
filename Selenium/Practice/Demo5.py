import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Demo_checkenablement:
    def enablechk(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        chkenb = driver.find_element(By.XPATH,"//input[@id='login-button']").is_enabled()
        print(chkenb)


obj1 = Demo_checkenablement()
obj1.enablechk()
