from page_wrappers.base_page import BasePage


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

