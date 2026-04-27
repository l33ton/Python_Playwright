# LOGIN LOCATORS AND CONSTANTS

USERNAME_INPUT_LOCATOR = "#login-username"
PASSWORD_INPUT_LOCATOR = "#login-password"
LOGIN_URL = "auth/login"
LOGIN_FORM_LOCATOR = "#login-form"
FORGOT_PASSWORD_LOCATOR = ".nounderline"

TEST_VALID_USERS = {
    "customer": {"username": "alex_rider", "account_id": "1"},
    "employee": {"username": "felix_jackson"},
    "mechanic": {"username": "julia_grey"}
}
TEST_MOCK_USERS = {
    "mock_customer": {"username": "Wizardz"},
    "mock_without_username": {"username": ""}
}
MOCK_PASSWORD = "25252525A."

# PROFILE LOCATORS AND CONSTANTS
PROFILE_URL = "users/{account_id}/details"
EXPECTED_PROFILE_URL = "http://localhost:8081/users/1/details"
EDIT_INFO_BUTTON_LOCATOR = "#edit-info-button"
FIRST_NAME_INPUT_LOCATOR = "#first-name-input"
LAST_NAME_INPUT_LOCATOR = "#last-name-input"
SAVE_INFO_BUTTON_LOCATOR = "#save-info-button"
FULL_NAME_LOCATOR = "#full-name-text"
TEST_FIRST_NAME = "Jake"
TEST_LAST_NAME = "Jacobs"
OLD_PASSWORD_INPUT_LOCATOR = "#old-password"
NEW_PASSWORD_INPUT_LOCATOR = "#new-password"
CONFIRM_PASSWORD_INPUT_LOCATOR = "#confirm-password"
NEW_PASSWORD = "password132%D"
ERROR_MESSAGE_LOCATOR = ".error-message"
ERROR_MESSAGE = "Password must contain at least 8 characters, including one uppercase letter, one digit, and one special symbol (+, -, *, ^, etc.)"