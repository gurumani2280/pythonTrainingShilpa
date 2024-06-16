import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Demo_listbox:
    def chklist(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.NAME,"UserTitle")
        var1 = Select(dropdown)
        var1.select_by_index(4)
        time.sleep(4)
        var1.select_by_visible_text("Marketing / PR Manager")
        time.sleep(4)
        var1.select_by_value("Customer_Service_Manager_ANZ")
        time.sleep(4)


obj1 = Demo_listbox()
obj1.chklist()
