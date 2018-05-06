from page_wrappers.home_page.home_page import HomePage
from page_wrappers.login_page import LoginPage
from tests.base_test import BaseTest


class TestUi1(BaseTest):
    """
    Test case description
    """
    def test_home_page(self, driver, base_url):
        login_page = LoginPage(driver)
        test_path = '/portal/login'
        expected_msg = 'Login Failed'

        driver.get(base_url + test_path)
        login_page.login_to_account(
            username='test_admin',
            password='BELQDJd6Y6')
        actual_msg = login_page.get_login_failed_msg(expected_msg)
        assert actual_msg
