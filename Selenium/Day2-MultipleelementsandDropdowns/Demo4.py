#Write test in all the input text box of that page

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
time.sleep(2)
input_textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
print(type(input_textboxes)) #<class 'list'>
time.sleep(3)
for textbox in input_textboxes:
    if textbox.is_enabled():
        textbox.send_keys("test")
time.sleep(3)
for textbox in input_textboxes:
    if textbox.is_enabled():
        textbox.clear()


time.sleep(3)
driver.quit()