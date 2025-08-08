from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/upload-download-test/index.html"

driver.get(url)


fruit_name = "apple"


finding_price = driver.find_element(By.XPATH, "/div[contains(text(), 'price')]").get_attribute('data-column-id')
print(finding_price)

driver.find_element(By.XPATH, f"//div[contains(text(), {fruit_name})]/parent::div/parent::div/div[@id='cell-"+finding_price+"-undefined']").text
