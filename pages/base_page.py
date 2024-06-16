import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    PAGE_URL = 'https://sbis.ru'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        with allure.step('Open start page'):
            self.driver.get(self.PAGE_URL)

    def find(self, args):
        return self.driver.find_element(*args)

    def is_page_opened(self):
        with allure.step(f'Page is opened: {self.PAGE_URL}'):
            try:
                self.wait.until(EC.url_contains(self.PAGE_URL))
            except TimeoutException:
                allure.attach('Message', f'Page can not be opened: {self.PAGE_URL}', allure.attachment_type.TEXT)