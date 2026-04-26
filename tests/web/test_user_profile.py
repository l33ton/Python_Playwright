import pytest
from playwright.sync_api import expect
from constants import *


def test_if_navigate_to_my_profile_works(dashboard_page):
    # Arrange

    # Act

    # Assert
    expect(dashboard_page.page).to_have_url(EXPECTED_PROFILE_URL)
@pytest.mark.parametrize("first_name, last_name", [
    ("Ivan", "Georgiev"),
    ("VeryLongNameThatMightBreakTheUI", "Test"),
    ("O'Neil", "D-r")])
def test_if_changing_name_works(dashboard_page, first_name, last_name, change_to_original_name):
    # Arrange
    expected_result = f"Full name: {first_name} {last_name}"
    # Act
    dashboard_page.change_first_and_last_name(first_name, last_name)
    # Assert
    expect(dashboard_page.page.locator(FULL_NAME_LOCATOR)).to_contain_text(expected_result)
    # Cleanup - we are cleaning with a fixture called "change_to_original_name"

def test_if_changing_password_works(dashboard_page, change_password_to_common):
    # Arrange

    # Act
    dashboard_page.change_password(COMMON_PASSWORD, NEW_PASSWORD)
    # Assert
    # Cleanup - we are cleaning with a fixture called "change_password_to_common" and password is changed to the original one
