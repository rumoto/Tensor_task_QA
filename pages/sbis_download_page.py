import allure
import requests
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SbisDownloadPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.PAGE_URL = 'https://sbis.ru/download'
        self.WINDOWS_TAB = (By.XPATH, '//div[@data-id="default"][//span[text()="Windows"]]')
        self.PLUGIN_TAB = (By.XPATH, '//div[@data-id="plugin"]')
        self.WEB_INSTALLER_LINK = (By.XPATH, '//a[contains(text(),"Скачать (Exe 7.22 МБ)")]')


    def is_windows_tab_opened(self):
        with allure.step('Windows tab is opened'):
            self.wait.until(EC.text_to_be_present_in_element_attribute(
                self.WINDOWS_TAB, 'class', 'controls-Checked__checked')
            )

    def is_plugin_tab_opened(self):
        with allure.step('Plugin tab is opened'):
            self.wait.until(EC.text_to_be_present_in_element_attribute(
                self.PLUGIN_TAB, 'class', 'controls-Checked__checked')
            )

    def download_web_installer(self):
        with allure.step('Download web-installer'):
            element = self.wait.until(EC.element_to_be_clickable(self.WEB_INSTALLER_LINK))
            file_url = element.get_attribute('href')
            filename = file_url.split('/')[-1]
            response = requests.get(file_url)
            response.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(response.content)
            download_path = f'{os.getcwd()}/{filename}'
            return download_path

    def is_file_size_correct(self, path):
        with allure.step('Checking the file size to be correct'):
            file_size_bytes = os.path.getsize(path)
            assert file_size_bytes == 7570584, 'Размер файла отличается от исходного'

