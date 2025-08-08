from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/AutomationPractice/"

def radio_button_selection():
    chrome_driver.get(url)
    chrome_driver.maximize_window()
    radio_buttons = chrome_driver.find_elements(By.XPATH, "//input[@name='radioButton']")
    selected_radio_button_count = 0
    for x in radio_buttons:
        if x.get_attribute('value') == "radio2":
            x.click()
            break


    for index, value in enumerate(radio_buttons):
        if value.is_selected():
            selected_radio_button_count += 1
            print("selected", selected_radio_button_count)
        else:
            print("Not selected")
    return selected_radio_button_count

assert radio_button_selection() == 1, f"Expected 1 radio button, found {radio_button_selection()}"
