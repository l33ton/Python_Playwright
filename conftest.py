import os
import pytest

from constants import LOGIN_URL, TEST_VALID_USERS, PROFILE_URL, NEW_PASSWORD
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from env_config import COMMON_PASSWORD
@pytest.fixture
def login_page(base_url, page):
    page.goto(base_url + LOGIN_URL)

    yield LoginPage(page)
@pytest.fixture
def logged_in(login_page):
    customer = TEST_VALID_USERS["customer"]
    login_page.login(customer["username"], COMMON_PASSWORD)

    return login_page.page

@pytest.fixture
def dashboard_page(page, base_url):
    customer = TEST_VALID_USERS["customer"]
    profile_url = PROFILE_URL.format(account_id=customer["account_id"])
    page.goto(base_url + profile_url)
    yield DashboardPage(page)

@pytest.fixture
def change_to_original_name(dashboard_page):
    yield
    dashboard_page.change_first_and_last_name(first_name="Alex", last_name="Rider")

@pytest.fixture
def change_password_to_common(dashboard_page, new_password):
    yield
    dashboard_page.change_password(new_password, COMMON_PASSWORD)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request):
    if "skip_auth" in request.keywords:
        return browser_context_args

    auth_path = os.path.join(os.path.dirname(__file__), "auth.json")

    if os.path.exists(auth_path):
        return {
            **browser_context_args,
            "storage_state": auth_path
        }

    return browser_context_args
