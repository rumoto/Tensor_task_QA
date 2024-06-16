import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class SbisMainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.CONTACT_LINK_SELECTOR = (By.LINK_TEXT, 'Контакты')
        self.CHAT_BUTTON_XPATH = (By.XPATH, '//div[@title="Кнопка вызова"]')
        self.SBIS_FOOTER_DOWNLOAD_LINK = (By.LINK_TEXT, 'Скачать локальные версии')


    def is_page_opened(self):
        with allure.step('Sbis main page is opened'):
            try:
                chat_present = EC.presence_of_element_located(self.CHAT_BUTTON_XPATH)
                self.wait.until(chat_present)
            except TimeoutException:
                allure.attach('Message', 'Sbis main page can not be opened', allure.attachment_type.TEXT)

    def contact_link(self):
        return self.find(self.CONTACT_LINK_SELECTOR)

    def click_contact_link(self):
        with allure.step('Click on contact link'):
            self.contact_link().click()

    def click_footer_download_link(self):
        with allure.step('Open Sbis download page'):
            element = self.wait.until(EC.element_to_be_clickable(self.SBIS_FOOTER_DOWNLOAD_LINK))
            self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
            element.click()