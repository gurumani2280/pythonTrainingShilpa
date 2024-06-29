import pytest
from selenium import webdriver

import time


@pytest.fixture(scope="function")
def launch_browser6():
    #global driver
    driver = webdriver.Edge()
    time.sleep(2)
    print("Edge browser opened launch_browser4")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()
    print("Closing the Edge browser launch_browser4")