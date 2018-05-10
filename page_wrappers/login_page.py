from page_wrappers.base_page import BasePage


class LoginPage(BasePage):
    def login_to_account(self, username, password):
        """
        Login to the account
        with provided username and password
        :param username: str
        :param password: str
        :return:
        """
        username_field = self.wait.until_element_visible_by_id('login-page-username')
        username_field.send_keys(username)
        pass_field = self.wait.until_element_visible_by_id('login-page-password')
        pass_field.send_keys(password)

        login_form = self.wait.until_element_visible_by_id('login-form')
        login_form.submit()
