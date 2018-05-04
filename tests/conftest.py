import os

import pytest
from selenium.webdriver import Chrome, DesiredCapabilities, Firefox, Remote
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver():
    """
    Set the following env vars:

    TST_DRIVER: name of the driver "chrome", "firefox"
    TST_SELENIUM: url to the Selenium Grid Hub

    :return: driver
    """
    # choose between Remote or local or Headless Chrome, Firefox
    driver = get_browser_driver()
    driver.set_window_size(1200, 1000)  # set default screen size

    yield driver
    # close the browser
    driver.quit()


def get_browser_driver():
    """
    Get web-driver
    :return: driver instance object
    """
    conf_driver = get_config('driver')
    remote_selenium = get_config('selenium')
    capabilities = dict(getattr(DesiredCapabilities, conf_driver.upper()))

    if remote_selenium:
        browser_driver = Remote(remote_selenium, capabilities)
    elif conf_driver.lower() == 'chrome':
        chrome_options = Options()

        # update path ENV variable if necessary
        if "usr/local/bin:" not in os.environ["PATH"]:
            os.environ["PATH"] += ":/usr/local/bin"

        if get_config('headless'):
            chrome_options.set_headless()
        browser_driver = Chrome(
            desired_capabilities=capabilities, chrome_options=chrome_options)

    elif conf_driver.lower() == 'firefox':
        browser_driver = Firefox(capabilities=capabilities)
    else:
        raise Exception('Unknown/unsupported driver selected: ' + conf_driver)

    return browser_driver


def get_config(key):
    """
    Get the config from ENV vars
    :param key: the key of the config to get
    :return: string containing the requested config
    """
    value = os.environ.get("TST_" + key.upper())

    return value


@pytest.fixture(scope="session")
def base_url():
    """
    Set the base url using the env var: TST_BASE_URL
    :return: string containing the base url to use
    """
    return get_config("base_url")
