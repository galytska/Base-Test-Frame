from faker import Faker


class BaseTest:
    """
    Base class to initialize the base test class and driver.
    Also it uses as storage for common test methods
    """

    fake = Faker()
