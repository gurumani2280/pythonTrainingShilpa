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
username_element.send_keys("standard_user")
time.sleep(2)
password_element=driver.find_element(By.ID,"password")
password_element.send_keys("secret_sauce")
time.sleep(2)
login=driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
driver.quit()
