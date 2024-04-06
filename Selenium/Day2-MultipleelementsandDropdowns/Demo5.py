#Select Dropdown items
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
time.sleep(2)
dropdown_element=driver.find_element(By.NAME,"state")
dropdown_state=Select(dropdown_element)
print(type(dropdown_state))
dropdown_state.select_by_index(1)
time.sleep(2)
driver.quit()