import pytest

@pytest.mark.usefixtures("browser_instance") #  Just run the fixture (no return)
class TestPlacingOrder:

   def test_browser(self, browser_instance):
       driver = browser_instance
       url = "https://rahulshettyacademy.com/angularpractice/"
       driver.get(url)
       print(driver.title)