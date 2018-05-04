from tests.base_test import BaseTest


class TestUi1(BaseTest):




    def test_home_page(self, driver):
        expected = 'Demoqa | Just another WordPress site'
        driver.get('http://demoqa.com/')
        actual_title = driver.title
        assert actual_title == expected