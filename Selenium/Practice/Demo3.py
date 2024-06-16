import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Gettext:
    def find_text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        text = driver.find_element(By.LINK_TEXT, "Yatra for Business").text
        print(text)


obj1 = Gettext()
obj1.find_text()
