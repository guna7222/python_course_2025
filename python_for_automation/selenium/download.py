from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

url = "https://rahulshettyacademy.com/upload-download-test/index.html"
driver.get(url)

# implicitly wait
driver.implicitly_wait(10)

# download the file
driver.find_element(By.ID, "downloadButton").click()

# upload the file
upload = driver.find_element(By.CSS_SELECTOR, "#fileinput")
file_path = "C:\\Users\\dilli\\Downloads\\download.xlsx"

try:
    upload.send_keys(file_path)
except Exception as e:
    print("file not found")

# explict wait
wait = WebDriverWait(driver, 10)
toast_locator = (By.XPATH, "//div[@class='Toastify__toast-body']/div[2]")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
success_message = driver.find_element(*toast_locator).text
print(success_message)

