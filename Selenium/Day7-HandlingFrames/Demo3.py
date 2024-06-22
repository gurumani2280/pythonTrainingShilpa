
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://the-internet.herokuapp.com")
#to refresh the browser
driver.refresh()
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT,"Nested Frames").click()
# to switch to frame with frame name
driver.switch_to.frame("frame-bottom")
# to get the text inside the frame and print on console
print(driver.find_element(By.XPATH,"//body").text)
# to move out the current frame to the page level
driver.switch_to.default_content()
driver.switch_to.frame("frameset-middle")
driver.switch_to.frame("frame-middle")
print(driver.find_element(By.XPATH,"//div[@id='content']").text)
driver.switch_to.default_content()
#to close the browser
driver.quit()