import time
from importlib import invalidate_caches
from selenium.webdriver.support.ui import WebDriverWait
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class AddToCart:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # opening page
    def opening_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # def search_items_and_add_to_card(self):
    #     self.driver.find_element(By.CSS_SELECTOR, 'input[class="search-keyword"]').send_keys("ber")
    #     ber_items = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
    #     # assert len(ber_items) > 0
    #     items_added_to_cart = []
    #     for items in ber_items:
    #         # chaining concept
    #         items.find_element(By.XPATH, "div/button").click()
    #         items_added_to_cart.append(items.find_element(By.CSS_SELECTOR, "h4.product-name").text)
    #     print(items_added_to_cart)

    def filter_on_search_with_ber(self):
        excepted_items = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        self.driver.find_element(By.CSS_SELECTOR, 'input[class="search-keyword"]').send_keys("ber")
        ber_items = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        # assert len(ber_items) > 0
        items_added_to_cart = []
        for items in ber_items:
            # chaining concept
            items.find_element(By.XPATH, "div/button").click()
            items_added_to_cart.append(items.find_element(By.CSS_SELECTOR, "h4.product-name").text)
        assert Counter(excepted_items) == Counter(items_added_to_cart)

    def click_on_cart_icon(self):
        self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()

    def click_on_proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, '//button[contains(text(), "PROCEED TO CHECKOUT")]').click()

    def checking_total_amount(self):
        table = self.driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
        sum = 0
        for t in table:
            sum += int(t.text)
        print(sum)
        total_amount_to_be_paid = self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
        convertion = int(total_amount_to_be_paid)
        print(convertion)
        assert sum == convertion

    def enter_promo_code(self):
        self.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")


    def apply_promo_code(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        # implicit wait
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

    def discount(self):
        without_discount = self.driver.find_element(By.CSS_SELECTOR, ".totAmt").text
        with_discount = self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
        # int_without_discount = int(without_discount)
        # int_with_discount = int(with_discount)
        # assert int_without_discount < int_with_discount
        print(type(without_discount))
        print(type(with_discount))

        float_type_without_discount = float(without_discount)
        float_type_with_discount = float(with_discount)
        if float_type_with_discount < float_type_without_discount:
            print(True)
        else:
            print(False)

    # def invalid_promo_code(self):
    #     invalid_promo_code_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Invalid code ..!')]").text
    #     print(invalid_promo_code_text)
    #     return invalid_promo_code_text

    def discount_percentage(self):
        discount_percentage = self.driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
        print(discount_percentage)
        return discount_percentage

    # if invalid promo code then discount should be 0 percent
    def negative_test_case_for_invalid_promo_code_percentage(self):
        if self.invalid_promo_code() == "Invalid code ..!":
            assert self.discount_percentage() == "0%"
        else:
            raise Exception("Test case failed")


driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = "https://rahulshettyacademy.com/seleniumPractise/"
add_to_cart = AddToCart(driver, url)
add_to_cart.opening_page()
# add_to_cart.search_items_and_add_to_card()
add_to_cart.click_on_cart_icon()
add_to_cart.click_on_proceed_to_checkout()
add_to_cart.checking_total_amount()
add_to_cart.enter_promo_code()
add_to_cart.apply_promo_code()
# add_to_cart.invalid_promo_code()
add_to_cart.discount()
# add_to_cart.discount_percentage()
# add_to_cart.negative_test_case_for_invalid_promo_code_percentage()