import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Testexample:
    def element_interactions(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
        driver.find_element(By.NAME,"username").send_keys("Shilpa")
        driver.find_element(By.NAME,"password").send_keys("abcdef1")
        driver.find_element(By.NAME, "lastName").send_keys("Sadheesh")
        driver.find_element(By.NAME, "address").send_keys('''C 702 Smondo3 ''')

        time.sleep(4)


obj1=Testexample()
obj1.element_interactions()

