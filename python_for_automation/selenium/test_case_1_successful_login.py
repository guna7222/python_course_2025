"""
Test Case 1: Successful Login
Launch the browser.
Navigate to the login page URL.
Verify that the login page is displayed successfully.
Enter Username: practice.
Enter Password: SuperSecretPassword!.
Click the Login button.
Verify that the user is redirected to the /secure page.
Confirm the success message "You logged into a secure area!" is visible.
Verify that a Logout button is displayed.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://practice.expandtesting.com/login")
    driver.maximize_window()

    login_header = driver.find_element(By.XPATH, "//button[contains(text(), 'Login'])")
    print(login_header)

    if login_header.is_displayed:
        print("displayed")
    else:
        print("not displayed")

    
except Exception as e:
    print(e)