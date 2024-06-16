import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Demofindelementsbyid():
    def element_by_id(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)
        driver.find_element(By.ID,"login-input").send_keys("abc")
        time.sleep(6)


find1=Demofindelementsbyid()
find1.element_by_id()