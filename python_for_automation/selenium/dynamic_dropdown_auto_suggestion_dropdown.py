import time

from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/dropdownsPractise/"
def web_page_is_up_down():
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return True
    else:
        return False

if web_page_is_up_down():
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.ID, "autosuggest").send_keys("ind")
    time.sleep(3)
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))
    print(countries)
    for country in countries:
        if country.text == "India":
            country.click()
            break



assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "india"
