""""""
from selenium import webdriver
from python_for_automation.selenium.functional_testing import AddToCart as addtocart
from selenium.webdriver.common.by import By


class Testcase_2_verify_total_amount:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url






driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = "https://rahulshettyacademy.com/seleniumPractise/"
test_2_object = Testcase_2_verify_total_amount(driver, url)
test_2_object.coming_to_cart()
test_2_object.checking_total_amount()