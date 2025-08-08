import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/java/linked-list-in-java/")

driver.maximize_window()
print(driver.title)
url_from_browser = driver.current_url
print(url_from_browser)
time.sleep(2)