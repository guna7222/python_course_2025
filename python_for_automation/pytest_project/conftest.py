import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")

@pytest.fixture(scope="function")
def browser_instance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_name.lower() == "safari":
        driver = webdriver.Safari()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    else:
        print("please select available browsers [chrome, firefox, safari, edge]")

    driver.implicitly_wait(5)
    yield driver
    driver.close()