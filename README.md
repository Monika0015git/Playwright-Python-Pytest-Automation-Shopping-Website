# Playwright Python Pytest Automation - Shopping Website

## Project Overview

This project is a Python-based web automation framework built using Playwright and pytest.

The project follows the Page Object Model (POM) design pattern to keep page locators and page-specific actions organized and reusable.

The automation covers an end-to-end shopping workflow on the Automation Exercise website.

## Tech Stack

- Python
- Playwright
- pytest
- pytest-html
- Page Object Model (POM)
- Git and GitHub

## Automation Flow

The end-to-end test covers the following workflow:

1. Open the Automation Exercise website
2. Verify the home page logo
3. Verify the Signup / Login link
4. Navigate to the Login page
5. Verify the Login section
6. Enter login credentials
7. Login to the application
8. Verify the Products link
9. Navigate to the Products page
10. Verify the Products section
11. Select a product
12. Navigate to Product Details
13. Add the product to the cart
14. Verify that the product was added to the cart
15. Open the cart
16. Verify the product in the cart
17. Proceed to checkout
18. Verify the Checkout page
19. Verify delivery address details
20. Verify billing address details
21. Enter an order comment
22. Place the order
23. Get order placed confirmation message
24. Navigate to the Home page
25. Log out from the application

## Project Structure

```text
playwright-vs-code-automation/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── product_details_page.py
│   ├── view_cart_page.py
│   ├── checkout_page.py
│   └── payment_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_end_to_end.py
│
├── utils/
│   └── __init__.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Features

### 1. Page Object Model

Each application page has its own page object containing:

* Page locators
* Page actions
* Page-specific validations

A common `BasePage` is used as the parent class for the page objects.

### 2. Pytest

pytest is used as the test framework for:

* Test execution
* Assertions
* Fixtures
* Test configuration

### 3. Playwright

Playwright is used for browser automation and web element interactions.

The browser runs in headed mode so the automation steps can be visually observed during execution.

### 4. Assertions

Assertions are used to verify important application behavior and page states.

### 5. Logging

Python logging is used to record useful information during test execution, such as:

* Application URL
* Page title
* Navigation
* Element visibility
* User actions

### 6. HTML Reporting

pytest-html is used to generate an HTML test execution report.

## Prerequisites

Make sure the following are installed:

* Python
* pip
* Git

## Installation

Clone the repository:

```bash
git clone https://github.com/Monika0015git/Playwright-Python-Pytest-Automation-Shopping-Website.git
```

Navigate to the project directory:

```bash
cd Playwright-Python-Pytest-Automation-Shopping-Website
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## How to Run Tests

Run the complete test suite:

```bash
pytest
```

Run tests with console output visible:

```bash
pytest -s
```

Generate an HTML report:

```bash
pytest -s --html=reports/report.html --self-contained-html
```

## Test Reports and Logging

The project is configured to:

* Display test logs in the terminal
* Store logs in `reports/test.log`
* Generate HTML test reports in the `reports` directory

The `reports` directory is excluded from Git using `.gitignore`.

## Page Object Model

The framework follows a simple Page Object Model structure.

```text
BasePage
   │
   ├── HomePage
   ├── LoginPage
   ├── ProductsPage
   ├── ProductDetailsPage
   ├── ViewCartPage
   └── CheckoutPage
```

The test class interacts with the page objects rather than directly locating elements inside the test.

This keeps the test scenario easier to read and makes page-specific code easier to maintain.

## Future Enhancements

Possible future improvements include:

* Add more test scenarios
* Add parameterized test data
* Improve test data management
* Add screenshots for failed tests
* Add payment page automation
* Add CI/CD integration using GitHub Actions
* Improve reporting
