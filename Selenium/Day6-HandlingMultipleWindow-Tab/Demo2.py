import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
parent_window_handle = driver.current_window_handle
print("parent_window_handle ======", parent_window_handle)
print("type(parent_window_handle) ======", type(parent_window_handle))

all_window_handles = driver.window_handles
print("all_window_handles ======", all_window_handles)
print("typpe of all_window_handles ======", type(all_window_handles))


time.sleep(2)


driver.find_element(By.XPATH, '//div[@id="Tabbed"]/a/button').click()
time.sleep(2)

driver.quit()
