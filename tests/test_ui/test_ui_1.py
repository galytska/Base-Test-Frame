from page_wrappers.home_page.home_page import HomePage
from tests.base_test import BaseTest


class TestUi1(BaseTest):
    """
    Test case description
    """
    def test_home_page(self, driver, base_url):
        expected = 'Demoqa | Just another WordPress site'
        home = HomePage(driver)

        driver.get(base_url+'/about-us/')
        home.click_home_page_logo()
        actual_title = driver.title
        assert actual_title == expected
