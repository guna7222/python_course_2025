import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Task:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def opening_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def clicking_on_free_access_to_interview_ques_link(self):
        self.driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

    def opening_another_page_after_clicking_on_interview_ques_link(self):
        tabs = self.driver.window_handles
        # switching to another tab
        self.driver.switch_to.window(tabs[1])
        email = self.driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
        print(email)
        self.driver.close()
        self.driver.switch_to.window(tabs[0])
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456789")
        self.driver.find_element(By.NAME, "terms").click()
        self.driver.find_element(By.NAME, "signin").click()
        time.sleep(5)
        print(self.driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://rahulshettyacademy.com/loginpagePractise/"
task = Task(driver, url)
task.opening_page()
task.clicking_on_free_access_to_interview_ques_link()
task.opening_another_page_after_clicking_on_interview_ques_link()

# i frames
# driver.switch_to.frame("
# ")
# driver.switch_to.default_content()