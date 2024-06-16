import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TensorAboutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.PAGE_URL = 'https://tensor.ru/about'
        self.DIV_WORK_BLOCK = (By.XPATH, '//div[div[h2[text()="Работаем"]]]')

    def is_work_block_present(self):
        with allure.step('Block "Работаем" is present on the page'):
            self.wait.until(EC.presence_of_element_located(self.DIV_WORK_BLOCK))

    def check_images_size(self):
        with allure.step('Checking images size'):
            element = self.find(self.DIV_WORK_BLOCK)
            images_list = element.find_elements(By.TAG_NAME, 'img')
            first_image = images_list[0]
            first_image_width = first_image.size['width']
            first_image_height = first_image.size['height']

            for image in images_list[1:]:
                width = image.size['width']
                height = image.size['height']
                # print(f'width: {width}')
                # print(f'height: {height}')
                assert width == first_image_width and height == first_image_height, 'Images sizes are different'
