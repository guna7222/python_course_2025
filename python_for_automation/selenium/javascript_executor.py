
# driver.execute_script("window.scrollBy(0, 500)")
# driver.get_screenshot_as_file("screen1.png")

# headless mode - invisible mode (fast)
# head mode - visible mode

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)

driver.execute_script("window.scrollBy(0, 500")
driver.get_screenshot_as_file("screenshot.png")