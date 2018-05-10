from page_wrappers.base_page import BasePage


class DataTypePage(BasePage):
    """
    e.g. '/portal/data/type/view or /portal/data/type/add'
    """

    def click_add_new_data_type(self):
        """
        Click add data type plus '+' button
        :return:
        """
        add_btn = self.wait.until_element_presence_by_xpath(
            '//section[@class="content"]//td[@class="view-table-actions-cell"]//a')
        add_btn.click()

    def fill_in_mandatory_data_type(self, test_type):
        """
        Fill in mandatory data type fields
        Validate new data
        Return validate success or empty list
        :param test_type: str
        :return: WebElement or []
        """
        name_input = self.wait.until_element_presence_by_xpath(
            '//input[@name="name"]')
        name_input.send_keys(test_type)
        validate_btn = self.driver.find_element_by_class_name('btn-warning')
        validate_btn.click()
        valid_success = self.wait.until_elements_visible_by_xpath(
            '//li[contains(@class, "list-group-item-success")]')
        return valid_success

    def submit_new_data_type(self):
        """
        Click submit data types button
        :return:
        """
        self.driver.find_element_by_xpath(
            '//button[@type="submit"]').click()

    def find_data_type_names(self):
        """
        Search for all data types names on page
        :return: lst of str e.g. ['Copy of Passport', 'Email Address']
        """
        types = self.wait.until_elements_visible_by_class_name(
            'view-rows-table-main-row-title')
        types_txt = [type_name.text.strip() for type_name in types]
        return types_txt

    def get_data_type_id_by_name(self, dt_name):
        """
        Search for new data type by name
        Return data type id
        :param dt_name: str
        :return: str
        """
        types = self.driver.find_elements_by_class_name(
            'view-rows-table')
        new_types = [t for t in types if dt_name in t.text]
        if new_types:
            new_id = new_types[0].text.split()[-1]
        return new_id
