from playwright.sync_api import expect
from constants import *


def test_if_navigate_to_my_profile_works(logged_in, dashboard_page):
    # Arrange
    # We are using the fixture logged_in, it removes repeating ourselves
    # Act
    # The fixture is navigating to our profile
    # Assert
    expect(dashboard_page.page).to_have_url(EXPECTED_PROFILE_URL)

def test_if_changing_name_works(dashboard_page, change_to_original_name):
    # Arrange
    expected_result = f"Full name: {TEST_FIRST_NAME} {TEST_LAST_NAME}"
    # Act
    dashboard_page.change_first_and_last_name(TEST_FIRST_NAME, TEST_LAST_NAME)
    # Assert
    expect(dashboard_page.page.locator(FULL_NAME_LOCATOR)).to_contain_text(expected_result)
    # Cleanup - we are cleaning with a fixture called "change_to_original_name"

def test_if_changing_password_works(logged_in, dashboard_page, change_password_to_common):
    # Arrange

    # Act
    dashboard_page.change_password(COMMON_PASSWORD, NEW_PASSWORD)
    # Assert
    # Cleanup - we are cleaning with a fixture called "change_password_to_common"