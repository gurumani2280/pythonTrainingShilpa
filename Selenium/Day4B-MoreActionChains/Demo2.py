import time

from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
# get geeksforgeeks.org
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
right_click_button = driver.find_element(By.XPATH, "//span[text()='right click me']")
action = ActionChains(driver)
action.context_click(right_click_button).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='Copy']").click()
time.sleep(3)
alert = driver.switch_to.alert
alert_text = alert.text
print("alert text == ", alert_text)
# Press the OK button
alert.accept()
time.sleep(3)
driver.quit()