import logging
import sys


class BaseTest:
    """
    Base class to initialize the base test class and driver.
    Also it uses as storage for common test methods
    """

    def init(self):
        """
        Log test class description
        """
        self.log.info(self.__class__.__doc__)

    @property
    def log(self):
        """
        Uses for test logs
        With following format of displaying(e.g: INFO:Test1.test_get_url::: <message>)
        :return: logger instance object
        """
        logger = logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name + "::")
        return logger
