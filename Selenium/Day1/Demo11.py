from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
time.sleep(2)
username_element=driver.find_element(By.NAME,"username")
username_element.send_keys("xyz")
time.sleep(2)
driver.quit()