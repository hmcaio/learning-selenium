import argparse
import enum
import logging
import logging.config
from pathlib import Path

import yaml
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# with open('logging.yml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

logger = logging.getLogger()

load_dotenv(dotenv_path=Path("env/.env"))


class Browsers(enum.Enum):
    FIREFOX = 0
    EDGE = 1


def create_driver(browser):
    match browser:
        case Browsers.FIREFOX.name:
            logger.info("Using Firefox browser")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case Browsers.EDGE.name:
            logger.info("Using Edge browser")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        case other:
            # Should not get here since browser valid values are limited by argparse, but just in case
            logger.error("Browser not supported.")
            raise Exception("Browser not supported.")

    logger.info("Driver created successfully")
    return driver


def run(browser):
    driver = create_driver(browser)

    # driver.implicitly_wait(time_to_wait=5)

    driver.get("https://google.com")

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_box.submit()
    # search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"

    input("Press any key to continue")

    driver.quit()


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser(description="Demo Selenium script")
    
    arg_parse.add_argument("--browser", choices=Browsers._member_names_, default=Browsers.FIREFOX.name, help="Browser to use")
    
    args = arg_parse.parse_args()

    run(args.browser)
