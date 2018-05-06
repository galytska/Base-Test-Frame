from page_wrappers.base_page import BasePage


class HomePage(BasePage):
    def click_home_page_logo(self):
        logo = self.wait.until_elements_presence_by_xpath(
            '//a[@class="site-anchor"]')[0]
        logo.click()