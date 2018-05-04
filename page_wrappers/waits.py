from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config.config import UI_MAX_RESPONSE_TIME


class Waits:
    def __init__(self, driver):
        self.wait_element = WebDriverWait(
            driver,
            UI_MAX_RESPONSE_TIME,
            ignored_exceptions=WebDriverException
        )

    def until_elements_presence_by_xpath(self, element, message=None):
        """
        wait until web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is present returns web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: web element/elements
        """
        return self.wait_element.until(
            ec.presence_of_all_elements_located((By.XPATH, element)), message)
