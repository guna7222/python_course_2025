from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/client/#/auth/login")
chrome_driver.maximize_window()
chrome_driver.find_element(By.CLASS_NAME, 'forgot-password-link').click()
chrome_driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("demo@gmail.com")
chrome_driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Guna@7222")
chrome_driver.find_element(By.ID, "confirmPassword").send_keys("Guna@7222")
chrome_driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# xpath //form/div[1]/input
# css_selector form div:nth-child[2] input
# based on text xpath //button[text()="save button"]