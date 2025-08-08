from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")

# ID, Xpath, CSS selectors, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hellow@gmail.com")
driver.find_element(By.NAME, "name").send_keys("Guna")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath //tagname[@attribute='value']
# input[@type='submit']
driver.find_element(By.XPATH,  "//input[@type='submit']").click()
success_msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_msg)

assert "success" in success_msg
# css selectors tagname[attribute='value']

# we can write css_selectors using #id and .class_name
# driver.find_element(By.CSS_SELECTOR, '#id').send_keys("Hey")
# chrome plugin selectors hub
# we can use index in xpath //tagname[@attribute='value'][2]

driver.find_element(By.CSS_SELECTOR, "label[for='inlineRadio1']").click()

# static dropdown
static_dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
static_dropdown.select_by_visible_text("Male")
static_dropdown.select_by_index(0)