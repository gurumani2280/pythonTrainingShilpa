from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
driver.quit()