import pytest

from tests.constants import LOGIN_URL, COMMON_PASSWORD, TEST_VALID_USERS, PROFILE_URL, NEW_PASSWORD
from tests.pages.dashboard_page import DashboardPage
from tests.pages.login_page import LoginPage

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
    page.goto(base_url + PROFILE_URL)
    yield DashboardPage(page)
@pytest.fixture
def change_to_original_name(dashboard_page):
    yield
    dashboard_page.change_first_and_last_name(first_name="Alex", last_name="Rider")
@pytest.fixture
def change_password_to_common(dashboard_page):
    yield
    dashboard_page.change_password(NEW_PASSWORD, COMMON_PASSWORD)

