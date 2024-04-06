from selenium import webdriver
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
title=driver.title
print("Page Title : ",title)
time.sleep(2)
current_URL=driver.current_url
print("URL : ",current_URL)
time.sleep(2)
HTML_Page_Source=driver.page_source
print("Page Source is : ",HTML_Page_Source)
time.sleep(2)
driver.quit()
