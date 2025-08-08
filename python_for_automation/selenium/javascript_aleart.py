import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


class JavascriptAleart:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # opening page
    def opening_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # entering data on input element and click on aleart button
    def clicking_on_aleart_button(self):
        name = "rahul"
        self.driver.find_element(By.ID, "name").send_keys(name)
        entered_data = self.driver.find_element(By.ID, "name").get_attribute("value")
        print(entered_data)
        self.driver.find_element(By.ID, "alertbtn").click()
        time.sleep(4)
        # switching driver to aleart mode
        aleart_mode = self.driver.switch_to.alert
        aleart_msg = aleart_mode.text
        print(aleart_msg)
        assert name in aleart_msg
        pattern = rf"Hello.*\b{name}\b"
        assert re.search(pattern, aleart_msg)
        aleart_mode.accept()
        aleart_mode.dismiss()

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"
javascript_aleart_object = JavascriptAleart(driver, url)
javascript_aleart_object.opening_page()
javascript_aleart_object.clicking_on_aleart_button()
