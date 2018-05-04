import os

import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Chrome, Firefox, Remote
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver():
    """
    Set the following env vars:

    INQ_DRIVER: name of the driver "chrome", "firefox" or "phantomjs"
    INQ_SELENIUM: url to the Selenium Grid Hub e.g. http://comp1066.aws:8600/wd/hub

    :return: driver without proxy
    """
    # choose between Remote or local Chrome, Firefox or PhantomJS
    driver = get_browser_driver()

    yield driver
    # close the browser
    driver.quit()


def get_browser_driver():
    """
    Get web-driver. If bm(browser_proxy_mob) == True init with bm_proxy else without
    :param bm: bool
    :return: driver instance object
    """
    capabilities = dict(getattr(DesiredCapabilities, get_config('driver').upper()))
    proxy_server_client = None

    if get_config('selenium'):
        browser_driver = Remote(get_config('selenium'), capabilities)
    elif get_config('driver').lower() == 'chrome':
        chrome_options = Options()

        # Hack for Jordy
        if "usr/local/bin:" not in os.environ["PATH"]:
            os.environ["PATH"] += ":/usr/local/bin"

        if get_config('headless'):
            chrome_options.set_headless()
        browser_driver = Chrome(desired_capabilities=capabilities, chrome_options=chrome_options)

    elif get_config('driver').lower() == 'firefox':
        browser_driver = Firefox(capabilities=capabilities)
    else:
        raise Exception('Unknown/unsupported driver selected: ' + get_config('driver'))

    browser_driver.set_window_size(1200, 1000)  # set default screen size
    # browser_driver.implicitly_wait(
    #     implicit_wait())  # always wait max 7 seconds if an element is not immediately available

    return browser_driver


def get_config(key):
    """
    Get the config from ENV vars
    :param key: the key of the config to get
    :return: string containing the requested config
    """
    value = os.environ.get("INQ_" + key.upper(), None)

    # booleanize
    if value and value.lower() in ['0', 'false']:
        value = False

    return value
