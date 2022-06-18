from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv(dotenv_path=Path("env/.env"))

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

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
