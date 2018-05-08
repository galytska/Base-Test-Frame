from page_wrappers.base_page import BasePage
from selenium.webdriver.support.select import Select


class LoginPage(BasePage):
    def login_to_account(self, username, password):
        username_field = self.wait.until_element_visible_by_id('login-page-username')
        username_field.send_keys(username)
        pass_field =self.wait.until_element_visible_by_id('login-page-password')
        pass_field.send_keys(password)

        login_form = self.wait.until_element_visible_by_id('login-form')
        login_form.submit()

    def get_login_failed_msg(self, expected_msg):
        login_failed_msg = \
            self.wait.until_elements_presence_by_xpath(
                '//li[contains(text(), "{}")]'.format(expected_msg))
        return login_failed_msg

    def select_data_model(self, item):
        sidebar = self.wait.until_element_visible_by_class_name('sidebar')
        sidebar.find_element_by_xpath('//span[.="Data Models"]').click()
        data_models_item = self.wait.until_element_visible_by_xpath(
            '//span[.="{}"]'.format(item))
        data_models_item.click()
        title = self.wait.until_elements_presence_by_xpath(
            '//nav[@class="navbar navbar-static-top"]//span[.="Data Type"]')
        return title

    def click_add_new_data_type(self):
        add_btn = self.wait.until_element_presence_by_xpath(
            '//section[@class="content"]//td[@class="view-table-actions-cell"]//a')
        add_btn.click()

    def fill_in_mandatory_data_type(self, test_type):
        name_input = self.wait.until_element_presence_by_xpath(
            '//input[@name="name"]')
        name_input.send_keys(test_type)
        validate_btn = self.driver.find_element_by_class_name('btn-warning')
        validate_btn.click()
        self.wait.until_element_visible_by_xpath(
            '//li[contains(@class, "list-group-item-success")]')
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

    def find_data_type_by_name(self, type_name):
        self.wait.until_elements_visible_by_class_name(
            'view-rows-table-main-row-title')

        types = self.wait.until_elements_visible_by_class_name(
            'view-rows-table-main-row-title')
        types_txt = [type_name.text for type_name in types]
        return types_txt
