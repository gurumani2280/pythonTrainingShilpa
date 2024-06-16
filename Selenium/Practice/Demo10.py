# Do e2e checkout of items after adding to cart.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(4)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
time.sleep(3)

var1 = driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']").text
print(var1)
var2 = driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']").text
print(var2)
driver.find_element(By.ID, "checkout").click()
time.sleep(3)
print("Page title after Checkout of items : " + driver.title)
driver.find_element(By.ID, "first-name").send_keys("Shilpa")
time.sleep(4)
driver.find_element(By.ID, "last-name").send_keys("S")
time.sleep(4)
driver.find_element(By.ID, "postal-code").send_keys("560100")
time.sleep(4)
driver.find_element(By.ID, "continue").click()
time.sleep(4)
expected_message = "Added Items : Sauce Labs Backpack,Sauce Labs Bolt T-Shirt"
assert var1, var2 == expected_message
driver.find_element(By.ID, "finish").click()
time.sleep(4)
print("Page Title on Finish Page: ", driver.title)
driver.quit()

#Doubts:
#How to close the blue pop up
#Which function to use to inorder print the last message on finish