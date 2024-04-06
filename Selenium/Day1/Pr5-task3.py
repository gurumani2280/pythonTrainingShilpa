from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://react-redux.realworld.io/#/login")
time.sleep(2)
username_element=driver.find_element(By.XPATH,"""//*[@id="main"]/div/div/div/div/div/form/fieldset/fieldset[1]/input""").send_keys("abc@gmail.com")
time.sleep(3)
password_element=driver.find_element(By.XPATH,"""//*[@id="main"]/div/div/div/div/div/form/fieldset/fieldset[2]/input""").send_keys("secret_sauce")
time.sleep(3)
login_element=driver.find_element(By.XPATH,"""//*[@id="main"]/div/div/div/div/div/form/fieldset/button""").click()
time.sleep(10)
driver.quit()