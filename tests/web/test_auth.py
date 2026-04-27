import pytest
import os
from playwright.sync_api import expect
from dotenv import load_dotenv
from constants import *

@pytest.mark.skip_auth
def test_login_with_valid_credentials(login_page, base_url):
    # Arrange
    customer = TEST_VALID_USERS["customer"]
    load_dotenv()
    common_password = os.getenv("COMMON_PASSWORD")
    # Act
    login_page.login(customer["username"], common_password)
    # Assert
    expect(login_page.page).to_have_url(base_url)
@pytest.mark.skip_auth
def test_login_with_invalid_credentials(login_page, base_url):
    # Arrange
    fake_customer = TEST_MOCK_USERS["mock_customer"]
    # Act
    login_page.login(fake_customer["username"], MOCK_PASSWORD)
    # Assert
    expect(login_page.page).not_to_have_url(base_url)
@pytest.mark.skip_auth
def test_login_without_username(login_page, base_url):
    # Arrange
    # Act
    login_page.login("", MOCK_PASSWORD)
    # Assert
    # Check if the login form is still visible, we are using helper method to avoid DRY.
    login_page.expect_login_form_to_be_visible_and_have_same_url(base_url)
@pytest.mark.skip_auth
def test_login_without_password(login_page, base_url):
    # Arrange
    fake_customer = TEST_MOCK_USERS["mock_customer"]
    # Act
    login_page.login(fake_customer["username"], "")
    # Assert
    login_page.expect_login_form_to_be_visible_and_have_same_url(base_url)
@pytest.mark.skip_auth
def test_login_with_empty_credentials(login_page, base_url):
    # Arrange
    # Act
    login_page.login("", "")
    # Arrange
    login_page.expect_login_form_to_be_visible_and_have_same_url(base_url)

