import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TensorHomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.PAGE_URL = 'https://tensor.ru'
        self.DIV_POWER = (By.XPATH, '//div[p[text()="Сила в людях"]]')
        self.MORE_DETAILED_LINK = (By.XPATH, "//div[p[text()='Сила в людях']]//a[text()='Подробнее']")

    def is_power_div_present(self):
        with allure.step('Block "Сила в людях" is present on the page'):
            self.wait.until(EC.presence_of_element_located(self.DIV_POWER))

    def click_to_more_details_link(self):
        with allure.step('Click on "Подробнее" link'):
            element = self.wait.until(EC.element_to_be_clickable(self.MORE_DETAILED_LINK))
            self.driver.execute_script('arguments[0].scrollIntoView(true)', element)
            self.driver.execute_script('arguments[0].click()', element)
