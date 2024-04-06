from selenium import webdriver

import time
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
time.sleep(2)
username_element=driver.find_element(By.NAME,"username").send_keys("sadheeshshilpa")
time.sleep(3)
password_element=driver.find_element(By.NAME,"password").send_keys("123456")
time.sleep(3)
ln_element=driver.find_element(By.ID,"lastname").send_keys("Sadheesh")
time.sleep(3)
addr_element=driver.find_element(By.ID,"address").send_keys("Ecity,bangalore")
time.sleep(3)
gender_element=driver.find_element(By.XPATH,"//input[@value='f']").click()
time.sleep(3)
dob_element=driver.find_element(By.NAME,"dob").send_keys("15/05/2000")
time.sleep(3)
driver.quit()