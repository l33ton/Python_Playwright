import pytest
from playwright.sync_api import expect

from constants import TEST_VALID_USERS, MY_DETAILS_LOCATOR
from env_config import COMMON_PASSWORD

@pytest.mark.skip_auth
def test_save_auth_state(login_page, context):
    employee = TEST_VALID_USERS["employee"]
    login_page.login(employee["username"], COMMON_PASSWORD)
    context.storage_state(path="auth.json")

    expect(login_page.page.locator(MY_DETAILS_LOCATOR)).to_be_visible()