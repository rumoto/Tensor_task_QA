from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    #Windows 7
    # service = Service(executable_path='./chromedriver.exe')
    # options = webdriver.ChromeOptions()
    # chrome_browser = webdriver.Chrome(service=service, options=options)
    #Windows 10
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()





