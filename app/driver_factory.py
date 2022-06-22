import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import BaseWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from browsers import Browsers


class DriverFactory:

    logger = logging.getLogger()


    @classmethod
    def create(cls, browser: Browsers) -> BaseWebDriver:
        match browser:
            case Browsers.FIREFOX.name:
                cls.logger.info("Creating Firefox driver")
                driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

            case Browsers.EDGE.name:
                cls.logger.info("Creating Edge driver")
                options = EdgeOptions()
                # options.accept_insecure_certs = True
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

            case Browsers.CHROME.name:
                cls.logger.info("Creating Chrome driver")
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

            case other:
                # Should not get here, but just in case
                cls.logger.error("Browser not supported.")
                raise Exception("Browser not supported.")

        cls.logger.info("Driver created successfully")
        return driver
