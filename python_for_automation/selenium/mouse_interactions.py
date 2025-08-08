# ActionChains(driver)
# click_and_hold()  for long press
# context_click() # right click
# double_click()
# drag_and_drop()
# move_to_element().perform()
# for all the above methods at the end you have to use perform()
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class MouseInteractions:

    def __init__(self, chrome_driver, url):
        self.chrome_driver = chrome_driver
        self.url = url

    def page_opening(self):
        self.chrome_driver.get(self.url)
        print(self.chrome_driver.title)
        self.chrome_driver.maximize_window()

    def mouse_interaction(self):
       mouse_actions = ActionChains(self.chrome_driver)
       mouse_actions.move_to_element(self.chrome_driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
       mouse_actions.move_to_element(self.chrome_driver.find_element(By.LINK_TEXT, "Top")).click().perform()
       time.sleep(5)
chrome_driver = webdriver.Chrome()
chrome_driver.implicitly_wait(10)
url = "https://rahulshettyacademy.com/AutomationPractice/"
mouse_interactions_object = MouseInteractions(chrome_driver, url)
mouse_interactions_object.page_opening()
mouse_interactions_object.mouse_interaction()




















































