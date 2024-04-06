from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
title=driver.title
print("Page Title",title)
Current_URL=driver.current_url
print("Current URL is :",Current_URL)
html_page_source=driver.page_source
print("HTML Page Source is :",html_page_source)
driver.quit()