import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Testexample:
    global driver
    def element_interactions(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
        driver.find_element(By.XPATH, "//label[normalize-space()='Default Checked']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//label[normalize-space()='Click on this check box']").click()
        time.sleep(3)
        var1 = driver.find_element(By.XPATH,"//div[@id='txtAge']").text
        print(var1)
        driver.find_element(By.XPATH, "//label[normalize-space()='Default Checked']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='check1']").click()
        time.sleep(3)



obj1=Testexample()


obj1.element_interactions()
