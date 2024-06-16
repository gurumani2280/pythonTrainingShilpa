import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetAttr:
    def getvalue(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        value1 = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack']").get_attribute("data-trackvalue")
        print(value1)


obj1 = GetAttr()
obj1.getvalue()
