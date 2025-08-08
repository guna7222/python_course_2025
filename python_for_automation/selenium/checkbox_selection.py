import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
print(driver.title)
assert driver.current_url == url
time.sleep(3)
all_checkboxes = driver.find_elements(By.XPATH, "//label/input[@type='checkbox']")

# checking all checkboxes
# for checkbox in all_checkboxes:
#     checkbox.click()

# checking specific checkbox
for checkbox1 in all_checkboxes:
    if checkbox1.get_attribute('value') == "option2":
        checkbox1.click()
        assert checkbox1.is_selected()
        break
