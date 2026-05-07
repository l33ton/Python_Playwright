TECHNICAL DOCUMENTATION: PYTHON PLAYWRIGHT AUTOMATION FRAMEWORK

1. OVERVIEW
This project is an automated end-to-end testing framework designed for web applications. 
It utilizes Python, Pytest, and Playwright. The architecture follows the Page Object 
Model (POM) design pattern to ensure code reusability, easy maintenance, and scalability.

2. PROJECT STRUCTURE
Python_Playwright/
├── pages/
│   ├── base_page.py        # Parent class with common browser interactions
│   ├── dashboard_page.py   # Post-login landing page logic
│   ├── login_page.py       # Authentication UI elements and actions
│   └── vehicles_page.py    # Vehicle management module logic
├── tests/
│   └── web/
│       ├── auth_setup.py    # Session persistence and global login setup
│       ├── test_auth.py     # Login and logout test cases
│       ├── test_user_profile.py # User data verification tests
│       └── test_vehicles.py # Vehicle-related business logic tests
├── utils/
│   └── data_generator.py   # Randomized test data generation (Faker)
├── .gitignore              # Files and folders to be ignored by Git
├── conftest.py             # Pytest fixtures and CLI arguments
├── constants.py            # Global constants and configuration variables
├── env_config.py           # Environment-specific settings (URLs, credentials)
└── pytest.ini              # Global configuration for the pytest runner

3. KEY FEATURES

* Page Object Model (POM): Separation of test logic from UI locators. Each page 
  is represented by a class, reducing code duplication.
* Environment Switching: Supports multiple environments (Stage, Prod) via 
  command-line arguments.
* Authentication State Management: Uses Playwright's storage_state to save 
  session cookies, allowing tests to skip the login UI after the first run.
* Automated Data Generation: Uses the Faker library to generate unique data 
  for test inputs, preventing conflicts.

4. SETUP AND INSTALLATION

Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)

Installation Steps:
1. Clone the repository.
2. Install required packages:
   pip install -r requirements.txt
3. Install Playwright browsers:
   playwright install

5. EXECUTION COMMANDS

Run all tests:
pytest

Run for a specific environment:
pytest --env=stage

Run in headed mode (visible browser):
pytest --headed

Run specific test file:
pytest tests/web/test_vehicles.py

6. BEST PRACTICES
- Timeouts: Managed globally in constants.py.
- Reporting: Detailed logs are configured via pytest.ini.
- Security: Sensitive session data is excluded from version control via .gitignore.
