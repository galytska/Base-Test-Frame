from page_wrappers.base_page import BasePage


class DashboardPage(BasePage):
    """
    e.g. '/portal/dashboard'
    """

    def select_data_model(self, item):
        """
        Select provided item from the Data Models list
        :param item: Data model item e.g. Data Types
        :return: Data Type page title: WebElement
        """
        sidebar = self.wait.until_element_visible_by_class_name('sidebar')
        sidebar.find_element_by_xpath('//span[.="Data Models"]').click()
        data_models_item = self.wait.until_element_visible_by_xpath(
            '//span[.="{}"]'.format(item))
        data_models_item.click()
        title = self.wait.until_elements_presence_by_xpath(
            '//nav[@class="navbar navbar-static-top"]//span[.="Data Type"]')
        return title
