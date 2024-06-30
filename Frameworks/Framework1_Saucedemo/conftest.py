import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    request.cls.driver = driver
    yield
    driver.quit()


