import os
import pytest
from constants import TEST_VALID_USERS
from dotenv import load_dotenv

@pytest.mark.skip_auth
def test_save_auth_state(login_page, context):
    customer = TEST_VALID_USERS["customer"]
    load_dotenv()
    common_password = os.getenv("COMMON_PASSWORD")
    login_page.login(customer["username"], common_password)
    context.storage_state(path="auth.json")