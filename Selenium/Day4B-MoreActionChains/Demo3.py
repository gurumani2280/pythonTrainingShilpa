import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
# get geeksforgeeks.org
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/index.html")
block1 = driver.find_element(By.XPATH, "//h1[normalize-space()='Block 1']")

block3 = driver.find_element(By.XPATH, "//h1[normalize-space()='Block 3']")
time.sleep(3)
action = ActionChains(driver)
action.drag_and_drop(block1,block3).perform()
time.sleep(3)

driver.quit()