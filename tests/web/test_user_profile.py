import pytest
from playwright.sync_api import expect
from constants import *

@pytest.mark.skip_auth
def test_if_navigate_to_my_profile_works(logged_in, dashboard_page):
    # Arrange
    # Our arrangement is the dashboard_page fixture
    # Act
    # Dashboard_page fixture is navigating to profile_url
    # Assert
    expect(dashboard_page.page).to_have_url(EXPECTED_PROFILE_URL)
    expect(dashboard_page.page.locator(EDIT_INFO_BUTTON_LOCATOR)).to_be_visible()

@pytest.mark.parametrize("first_name, last_name", [
    ("Ivan", "Georgiev"),
    ("VeryLongNameThatMightBreakTheUI", "Test"),
    ("O'Neil", "D-r")])
@pytest.mark.skip_auth
def test_if_changing_name_works(logged_in, dashboard_page, first_name, last_name, change_to_original_name):
    # Arrange
    expected_result = f"Full name: {first_name} {last_name}"
    # Act
    dashboard_page.change_first_and_last_name(first_name, last_name)
    # Assert
    expect(dashboard_page.page.locator(FULL_NAME_LOCATOR)).to_contain_text(expected_result)
    # Cleanup - we are cleaning with a fixture called "change_to_original_name"
@pytest.mark.skip_auth
@pytest.mark.parametrize("new_password", [
    "JaKeTheDog1!",
    "Adventuretime1*",
    "FinnTheHuman2+"])
def test_if_changing_password_works_with_valid_data(logged_in, dashboard_page, new_password, change_password_to_common):
    # Arrange
    # Our arrangement is mark.parametrize
    # Act
    dashboard_page.change_password(COMMON_PASSWORD, new_password)
    # Assert
    expect(dashboard_page.page).to_have_url(EXPECTED_PROFILE_URL)
    # Cleanup - we are cleaning with a fixture called "change_password_to_common" and password is changed to the original one
@pytest.mark.skip_auth
@pytest.mark.parametrize("new_password", [
    "JaKeTheDog1",
    "Jake333",
    "A",
    "Jake!t1"])
def test_if_changing_password_shows_error_with_invalid_data(dashboard_page, new_password):
    # Arrange
    error_message = dashboard_page.page.get_by_text(ERROR_MESSAGE).first
    # Arrangement is the same as the previous test
    # Act
    dashboard_page.change_password(COMMON_PASSWORD, new_password)
    # Assert
    expect(error_message).to_be_visible()