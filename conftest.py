import os
import pytest

from constants import LOGIN_URL, TEST_VALID_USERS, PROFILE_URL, NEW_PASSWORD, VEHICLE_URL
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from env_config import COMMON_PASSWORD
from pages.vehicles_page import VehiclesPage


@pytest.fixture
def login_page(base_url, page):
    page.goto(base_url + LOGIN_URL)

    yield LoginPage(page)

@pytest.fixture
def dashboard_page(page, base_url):
    target_url = f"{base_url}{PROFILE_URL}"
    page.goto(target_url)
    yield DashboardPage(page)

@pytest.fixture
def vehicles_page(page, base_url):
    page.goto(base_url + VEHICLE_URL)
    yield VehiclesPage(page)

@pytest.fixture
def change_to_original_name(dashboard_page, page, base_url):

    yield
    target_url = f"{base_url}{PROFILE_URL}"
    page.goto(target_url)

    try:
        page.goto(target_url, wait_until="networkidle")

        temporary_dashboard = DashboardPage(page)
        if temporary_dashboard.edit_info_button_locator.is_visible(timeout=3000):
            temporary_dashboard.change_first_and_last_name(first_name="George", last_name="Hill", base_url=base_url)
            print("You have successfully change first and last name")
        else:
            print("You dont have permission to change first and last name")
    except Exception as e:
        print(f"Couldn't find the edit button on this url: {target_url}{e}")

@pytest.fixture
def change_password_to_common(page, base_url, dashboard_page, new_password):
    yield
    target_url = f"{base_url}{PROFILE_URL}"
    page.goto(target_url)

    try:
        page.goto(target_url, wait_until="networkidle")

        temporary_dashboard = DashboardPage(page)

        if temporary_dashboard.change_password_button_locator.is_visible():
            temporary_dashboard.change_password(new_password, COMMON_PASSWORD)
            print("Password is changed to common")
        else:
            print("Oops, you don't have permission to change the password")
    except Exception as e:
        print(f"Couldn't find the edit button on this url: {target_url}{e}")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, request):
    if "auth_setup" in request.node.nodeid:
        return {**browser_context_args, "storage_state": None}

    auth_path = os.path.join(os.getcwd(), "auth.json")

    if os.path.exists(auth_path):
        return {**browser_context_args, "storage_state": auth_path}

    return browser_context_args