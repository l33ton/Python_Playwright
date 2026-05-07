```text
TECHNICAL DOCUMENTATION: PYTHON PLAYWRIGHT AUTOMATION FRAMEWORK

1. OVERVIEW
This project is an automated end-to-end testing framework designed for web applications. It utilizes Python, Pytest, and Playwright. The architecture follows the Page Object Model (POM) design pattern to ensure code reusability, easy maintenance, and scalability.

2. PROJECT STRUCTURE
Python_Playwright/
  pages/
    base_page.py        - Parent class with common browser interactions
    dashboard_page.py   - Post-login landing page logic
    login_page.py       - Authentication UI elements and actions
    vehicles_page.py    - Vehicle management module logic
  tests/
    web/
      auth_setup.py     - Session persistence and global login setup
      test_auth.py      - Login and logout test cases
      test_user_profile.py - User data verification tests
      test_vehicles.py  - Vehicle-related business logic tests
  utils/
    data_generator.py   - Randomized test data generation
  .gitignore            - Files and folders to be ignored by Git
  conftest.py           - Pytest fixtures and CLI arguments
  constants.py          - Global constants and configuration variables
  env_config.py         - Environment-specific settings
  pytest.ini            - Global configuration for the pytest runner

3. KEY FEATURES
- Page Object Model (POM): Separation of test logic from UI locators.
- Environment Switching: Supports multiple environments (Stage, Prod).
- Authentication Management: Uses storage_state to skip login steps.
- Automated Data Generation: Employs Faker for unique test data.

4. SETUP AND INSTALLATION
- Prerequisites: Python 3.8+ and pip.
- Install packages: pip install -r requirements.txt
- Install browsers: playwright install

5. EXECUTION COMMANDS
- Run all tests: pytest
- Run for a specific environment: pytest --env=stage
- Run in headed mode: pytest --headed

6. BEST PRACTICES
- Timeouts are managed globally in constants.py.
- Detailed logs and settings are defined in pytest.ini.
- Sensitive files are excluded from Git via .gitignore.
```
