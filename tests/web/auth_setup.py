from constants import TEST_VALID_USERS, COMMON_PASSWORD


def test_save_auth_state(login_page, context):
    customer = TEST_VALID_USERS["customer"]
    login_page.login(customer["username"], COMMON_PASSWORD)
    context.storage_state(path="auth.json")