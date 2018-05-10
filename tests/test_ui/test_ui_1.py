from helpers import file_operation
from page_wrappers.dashboard_page import DashboardPage
from page_wrappers.data_type_page import DataTypePage
from page_wrappers.login_page import LoginPage
from tests.base_test import BaseTest


class TestUi1(BaseTest):
    def test_home_page(self, driver, base_url):
        login_page = LoginPage(driver)
        data_type_page = DataTypePage(driver)
        dashboard_page = DashboardPage(driver)
        test_path = '/portal/login'
        test_type = 'Copy of {}'.format(self.fake.word().capitalize())

        driver.get(base_url + test_path)
        login_page.login_to_account(
            username='test_admin',
            password='BELQDJd6Y6')
        dashboard_page.select_data_model('Data Types')
        data_type_page.click_add_new_data_type()
        data_validated = data_type_page.fill_in_mandatory_data_type(test_type)
        assert data_validated, \
            'New data type "{}" did not pass validation'.format(test_type)
        data_type_page.submit_new_data_type()
        types = data_type_page.find_data_type_names()
        assert test_type in types, \
            'Could not find expected type "{}" in data types "{}"'.format(test_type, types)
        new_dt_id = data_type_page.get_data_type_id_by_name(test_type)
        file_operation.save_new_data_type(test_type, new_dt_id)
