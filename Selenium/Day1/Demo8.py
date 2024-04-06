from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
username_element=driver.find_element(By.ID,"user-name")
username_element.send_keys("xyz")
time.sleep(2)
driver.quit()