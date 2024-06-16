import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SbisContactsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.PAGE_URL = 'https://sbis.ru/contacts'
        self.TENSOR_BANNER = (By.XPATH, '(//a[@title="tensor.ru"]//img)[1]')
        self.REGION = (By.XPATH, '//div[div[h1[text()="Контакты"]]]//span/span')
        self.PARTNER_LIST = (By.ID, 'city-id-2')
        self.REGION_LIST_DATA_QA = (By.XPATH, '//div[contains(@data-qa,"controls-Render__field")]')
        self.NEW_REGION_LINK = 'span.sbis_ru-link[title*="{}"]'


    def click_to_tensor_banner(self):
        with allure.step('Click to Tensor banner'):
            self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()


    def is_region_selected(self, region):
        with allure.step(f'region is selected: {region}'):
            self.wait.until(EC.text_to_be_present_in_element(self.REGION, region))

    def is_partner_list(self):
        with allure.step('Partner list is presented'):
            self.wait.until(EC.presence_of_element_located(self.PARTNER_LIST))

    def change_region_click(self):
        with allure.step('Clicked to change region'):
            self.wait.until(EC.element_to_be_clickable(self.REGION)).click()

    def is_regions_list_opened(self):
        with allure.step('Region list is opened'):
            self.wait.until(EC.presence_of_all_elements_located(self.REGION_LIST_DATA_QA))

    def click_new_region(self, new_region):
        with allure.step(f'Select and click new region: {new_region}'):
            self.wait.until(EC.presence_of_all_elements_located(self.REGION_LIST_DATA_QA))
            new_region_link = (By.CSS_SELECTOR, self.NEW_REGION_LINK.format(new_region))
            self.wait.until(EC.element_to_be_clickable(new_region_link)).click()

    def check_url(self, new_region):
        with allure.step('Page URL contains new region'):
            self.wait.until(EC.url_contains(new_region))

    def check_title(self, new_region):
        with allure.step('Page title contains new region'):
            self.wait.until(EC.title_contains(new_region))

