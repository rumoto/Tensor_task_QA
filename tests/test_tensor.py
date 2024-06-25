import time
import pytest
import allure
#from pages.base_page import BasePage
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorHomePage
from pages.tensor_about_page import TensorAboutPage
from pages.sbis_download_page import SbisDownloadPage

@allure.feature('Task #1')
@allure.title('Testing images size')
def test_task_1(driver):
    sbis_main_page = SbisMainPage(driver)
    sbis_main_page.open()
    sbis_main_page.is_page_opened()
    sbis_main_page.click_contact_link()
    sbis_contact_page = SbisContactsPage(driver)
    sbis_contact_page.is_page_opened()
    sbis_contact_page.click_to_tensor_banner()
    tensor_main_page = TensorHomePage(driver)
    tensor_driver = driver.window_handles[1]
    driver.switch_to.window(tensor_driver)
    tensor_main_page.is_page_opened()
    tensor_main_page.click_to_more_details_link()
    tensor_about_page = TensorAboutPage(driver)
    tensor_about_page.is_page_opened()
    tensor_about_page.is_work_block_present()
    tensor_about_page.check_images_size()

@allure.feature('Task #2')
@allure.title('Changing region')
def test_task_2(driver):
    sbis_main_page = SbisMainPage(driver)
    sbis_main_page.open()
    sbis_main_page.is_page_opened()
    sbis_main_page.click_contact_link()
    sbis_contact_page = SbisContactsPage(driver)
    sbis_contact_page.is_page_opened()
    sbis_contact_page.is_region_selected('Ярославская обл.')
    sbis_contact_page.is_partner_list()
    # Запоминаем первый город в списке партнеров моего региона
    my_region_partner_list = sbis_contact_page.find(sbis_contact_page.PARTNER_LIST).text
    sbis_contact_page.change_region_click()
    sbis_contact_page.is_regions_list_opened()
    sbis_contact_page.click_new_region('Камчатский край')
    sbis_contact_page.is_region_selected('Камчатский край')
    sbis_contact_page.is_partner_list()
    # Запоминаем первый город в списке партнеров после изменения региона
    new_region_partner_list = sbis_contact_page.find(sbis_contact_page.PARTNER_LIST).text
    # Проверяем, что город-партнер изменился
    with allure.step('Partner city changed'):
        assert my_region_partner_list != new_region_partner_list
    sbis_contact_page.check_url('41-kamchatskij-kraj')
    sbis_contact_page.check_title('Камчатский край')

@allure.feature('Task #3')
@allure.title('Download file')
def test_task_3(driver):
    sbis_main_page = SbisMainPage(driver)
    sbis_main_page.open()
    sbis_main_page.is_page_opened()
    sbis_main_page.click_footer_download_link()
    sbis_download_page = SbisDownloadPage(driver)
    sbis_download_page.is_page_opened()
    sbis_download_page.is_plugin_tab_opened()
    sbis_download_page.is_windows_tab_opened()
    download_path = sbis_download_page.download_web_installer()
    sbis_download_page.is_file_size_correct(download_path)
