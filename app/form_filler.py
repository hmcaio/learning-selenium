from selenium.webdriver.common.by import By

from driver_factory import DriverFactory
from browsers import Browsers


class FormFiller:

    def __init__(self, browser: Browsers):
        self.driver = DriverFactory.create(browser)
    

    def run(self):
        # driver.implicitly_wait(time_to_wait=5)

        self.driver.get("https://google.com")

        title = self.driver.title
        assert title == "Google"

        self.driver.implicitly_wait(0.5)

        search_box = self.driver.find_element(by=By.NAME, value="q")
        search_button = self.driver.find_element(by=By.NAME, value="btnK")

        search_box.send_keys("Selenium")
        search_box.submit()
        # search_button.click()

        search_box = self.driver.find_element(by=By.NAME, value="q")
        value = search_box.get_attribute("value")
        assert value == "Selenium"

        input("Press any key to continue")

        self.driver.quit()
