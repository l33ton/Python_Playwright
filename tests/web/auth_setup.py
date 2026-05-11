import pytest
from playwright.sync_api import expect
from constants import TEST_VALID_USERS, MY_DETAILS_LOCATOR, LOGIN_URL
from env_config import COMMON_PASSWORD



@pytest.mark.skip_auth
def test_save_auth_state(base_url, page, context):
    context.clear_cookies()
    page.goto(base_url)
    page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); }")

    page.goto(base_url + LOGIN_URL)

    employee = TEST_VALID_USERS["employee"]
    page.fill("#login-username", employee["username"])
    page.fill("#login-password", COMMON_PASSWORD)
    page.click("button[type='submit']")

    expect(page.locator(MY_DETAILS_LOCATOR)).to_be_visible()

    context.storage_state(path="auth.json")
    context.close()