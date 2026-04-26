from playwright.sync_api import expect

from constants import USERNAME_INPUT_LOCATOR, PASSWORD_INPUT_LOCATOR, PROFILE_URL, LOGIN_FORM_LOCATOR, \
    FORGOT_PASSWORD_LOCATOR, LOGIN_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input_locator = page.locator(USERNAME_INPUT_LOCATOR)
        self.password_input_locator = page.locator(PASSWORD_INPUT_LOCATOR)
        self.login_button_locator = page.locator(LOGIN_FORM_LOCATOR).get_by_text("Login")

    def login(self, username, password):
        self.username_input_locator.fill(username)
        self.password_input_locator.fill(password)
        self.login_button_locator.click()

    def expect_login_form_to_be_visible_and_have_same_url(self, base_url):
        expect(self.page.locator(LOGIN_FORM_LOCATOR)).to_be_visible()
        expect(self.page.locator(FORGOT_PASSWORD_LOCATOR)).to_be_visible()
        expect(self.page.locator(USERNAME_INPUT_LOCATOR)).to_be_visible()
        expect(self.page.locator(PASSWORD_INPUT_LOCATOR)).to_be_visible()
        expect(self.page).to_have_url(f"{base_url}{LOGIN_URL}")