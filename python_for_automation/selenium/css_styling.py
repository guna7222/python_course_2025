from selenium.webdriver.common.by import By
from selenium import webdriver

class VerifyLoginHeadingStyles:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def verify_login_heading_styles(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".login-title")
        font_size = element.value_of_css_property("font-size")
        actual_font_size = "30px"
        assert font_size == actual_font_size

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/client/#/auth/login"
object1 = VerifyLoginHeadingStyles(driver, url)
object1.open_page()
object1.verify_login_heading_styles()