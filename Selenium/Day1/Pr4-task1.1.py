from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)
username_element=driver.find_element(By.NAME,"username")
username_element.send_keys("abcd")
time.sleep(2)
password_element=driver.find_element(By.NAME,"password")
password_element.send_keys("1234")
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
time.sleep(2)
driver.quit()