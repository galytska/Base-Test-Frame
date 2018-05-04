from page_wrappers.waits import Waits


class BasePage:
    """
    BasePage should contain all common site-page functionality
    """

    def __init__(self, driver):
        self.driver = driver

    @property
    def wait(self):
        """
        Init class Waits(selenium waits).
        (e.g: self.wait.until....)
        :return:
        """
        return Waits(self.driver)
