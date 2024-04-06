from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
username_element=driver.find_element(By.ID,"user-name").send_keys("secret_sauce")
time.sleep(3)
password_element=driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
login_element=driver.find_element(By.ID,"login-button").click()
time.sleep(3)
driver.quit()