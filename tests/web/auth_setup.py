import pytest
from playwright.sync_api import expect

from constants import TEST_VALID_USERS, MY_DETAILS_LOCATOR
from env_config import COMMON_PASSWORD
from pages.login_page import LoginPage


@pytest.mark.skip_auth
def test_save_auth_state(page, login_page, context):
    login_pg = LoginPage(page)

    employee = TEST_VALID_USERS["employee"]
    login_pg.login(employee["username"], COMMON_PASSWORD)

    expect(login_page.page.locator(MY_DETAILS_LOCATOR)).to_be_visible()

    context.storage_state(path="auth.json")
    context.close()