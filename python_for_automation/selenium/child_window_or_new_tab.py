from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/windows"

# opening url
driver.get(url)

driver.find_element(By.LINK_TEXT, "Click Here").click()

# above line will open new tab we don't have control over that page
# to deal with child window or new tab we have to use
# window_handles property to get the tabs as list
tabs = driver.window_handles

# switching to new tab
driver.switch_to.window(tabs[1]) # new tab or child window
print(driver.find_element(By.TAG_NAME, "h3").text)
assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"
driver.close() # closing child window

# switching back to main window
driver.switch_to.window(tabs[0])
print(driver.find_element(By.TAG_NAME, "h3").text)