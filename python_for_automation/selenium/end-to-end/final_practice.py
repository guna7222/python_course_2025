from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Shopping:

    def __init__(self, driver, url, mobile, country):
        self.driver = driver
        self.url = url
        self.mobile = mobile
        self.country = country

    def opening_browser(self):
        self.driver.get(self.url)

    def clicking_on_shop_link(self):
        self.driver.find_element(By.LINK_TEXT, "Shop").click()

    def shop(self):
        #loop the mobiles see if any mobile is matching with given mobile if yes add to cart
        parent_element = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for x in parent_element:
            print(x.find_element(By.XPATH, "div/h4/a").text)
            if x.find_element(By.XPATH, "div/h4/a").text == self.mobile:
                x.find_element(By.XPATH, "div/button").click()

    def checkout(self):
        # click on checkout button
        self.driver.find_element(By.CSS_SELECTOR, 'div[id="navbarResponsive"] ul li a').click()

    def final_checkout(self):
        checkout = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        checkout.click()

    def delivery_location(self):
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys(self.country)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions ul li a")))
        self.driver.find_element(By.CSS_SELECTOR, ".suggestions ul li a").click()
        label = self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']")
        label.click()
        print(label.is_selected())
        self.driver.find_element(By.CSS_SELECTOR, 'form[class="ng-untouched ng-pristine ng-valid"] input').click()

    def success_message_for_checkout(self):
        success_message = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        print(success_message)
        assert "Success!" in success_message


url = "https://rahulshettyacademy.com/angularpractice/"
driver = webdriver.Chrome()
mobile = "Samsung Note 8"
country = "india"
driver.implicitly_wait(10)
chrome = Shopping(driver, url, mobile, country)
chrome.opening_browser()
chrome.clicking_on_shop_link()
chrome.shop()
chrome.checkout()
chrome.final_checkout()
chrome.delivery_location()
chrome.success_message_for_checkout()