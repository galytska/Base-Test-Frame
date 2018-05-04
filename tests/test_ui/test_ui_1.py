from tests.base_test import BaseTest


class TestUi1(BaseTest):
    """
    Test case description
    """
    def test_home_page(self, driver, base_url):
        expected = 'Demoqa | Just another WordPress site'

        driver.get(base_url)
        actual_title = driver.title
        assert actual_title == expected
