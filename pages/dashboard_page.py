from constants import *
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.edit_info_button_locator = page.locator(EDIT_INFO_BUTTON_LOCATOR)
        self.first_name_input_locator = page.locator(FIRST_NAME_INPUT_LOCATOR)
        self.last_name_input_locator = page.locator(LAST_NAME_INPUT_LOCATOR)
        self.save_info_button_locator = page.locator(SAVE_INFO_BUTTON_LOCATOR)
        self.change_password_button_locator = page.get_by_role("link", name="Change Password")
        self.old_password_input_locator = page.locator(OLD_PASSWORD_INPUT_LOCATOR)
        self.new_password_input_locator = page.locator(NEW_PASSWORD_INPUT_LOCATOR)
        self.confirm_password_input_locator = page.locator(CONFIRM_PASSWORD_INPUT_LOCATOR)
        self.save_password_button_locator = page.get_by_role("button", name= "Save")

    def navigate_to_profile(self, base_url):
        self.page.goto(f"{base_url}")

    def change_first_and_last_name(self, first_name, last_name):
        self.edit_info_button_locator.click()
        self.first_name_input_locator.fill(first_name)
        self.last_name_input_locator.fill(last_name)
        self.save_info_button_locator.click()

    def change_password(self, old_password, new_password):
        self.change_password_button_locator.click()
        self.old_password_input_locator.fill(old_password)
        self.new_password_input_locator.fill(new_password)
        self.confirm_password_input_locator.fill(new_password)
        self.save_password_button_locator.click()