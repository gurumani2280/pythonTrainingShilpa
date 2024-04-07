import pytest
from selenium import webdriver

import time
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def launch_browser5():
    global driver
    driver = webdriver.Edge()
    time.sleep(2)
    print("Edge browser opened launch_browser4")
    driver.maximize_window()
    time.sleep(2)
    yield
    driver.quit()
    print("Closing the Edge browser launch_browser4")


def test_checkbox5(launch_browser5):
    print("Working on Edge browser launched in fixture test_checkbox4")
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


def test_check_all_checkboxes5(launch_browser5):
    print("Working on Edge browser launched in fixture test_check_all_checkboxes")
    driver.get("file:///C:/PythonEmexo/pythonTrainingShilpa/Selenium/BasicHtmlElement.html")
    time.sleep(2)
    skill_checkboxes = driver.find_elements(By.NAME, "skill")
    print(type(skill_checkboxes))  # <class 'list'>
    time.sleep(3)
    for checkbox in skill_checkboxes:
        checkbox.click()
    time.sleep(3)
    for checkbox in skill_checkboxes:
        checkbox.click()
    time.sleep(3)

