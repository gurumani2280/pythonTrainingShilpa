import pytest
from selenium import webdriver

import time
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def launch_browser2():
    global driver
    driver = webdriver.Edge()
    time.sleep(2)
    print("Edge browser opened")
    yield
    driver.quit()
    print("Closing the Edge browser")


def test_checkbox3(launch_browser2):
    print("Working on Edge browser launched in fixture")
    driver.maximize_window()
    time.sleep(2)
    driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@value='selenium']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@value='testing']").click()
    time.sleep(3)
    java_checkbox = driver.find_element(By.XPATH, "//input[@value='java']")
    print(type(java_checkbox))  # <class 'selenium.webdriver.remote.webelement.WebElement'>
    java_checkbox.click()
    time.sleep(3)


