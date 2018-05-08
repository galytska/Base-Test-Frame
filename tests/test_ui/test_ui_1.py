from page_wrappers.login_page import LoginPage
from tests.base_test import BaseTest


class TestUi1(BaseTest):
    """
    Test case description
    """

    def test_home_page(self, driver, base_url):
        login_page = LoginPage(driver)
        test_path = '/portal/login'

        driver.get(base_url + test_path)
        login_page.login_to_account(
            username='test_admin',
            password='BELQDJd6Y6')

        # assert '/portal/dashboard' in driver.current_url
        login_page.select_data_model('Data Types')
        login_page.click_add_new_data_type()
        login_page.fill_in_mandatory_data_type('test')
        types = login_page.find_data_type_by_name('test')
        assert 'test' in types, driver.get_screenshot_as_file('screenshot')