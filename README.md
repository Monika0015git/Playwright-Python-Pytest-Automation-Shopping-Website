# 🛒 Playwright Python Pytest Automation Framework

A beginner-friendly **end-to-end web automation framework** built using **Python, Playwright, and pytest**, following the **Page Object Model (POM)** design pattern.

The framework automates an e-commerce shopping workflow including login, product selection, cart validation, checkout, and order placement.

---

## 🌐 Application Under Test

**Website:** [Automation Exercise](https://www.automationexercise.com/)

The project uses the **Automation Exercise** website as the application under test for practicing real-world web UI automation scenarios.

---

## 🎯 Project Objective

The objective of this project is to build a structured and maintainable UI automation framework using Python and Playwright while applying common QA automation practices such as:

* Page Object Model (POM)
* Reusable page methods
* pytest fixtures
* Assertions and validations
* Browser automation
* Logging
* HTML test reporting
* End-to-end test execution

---

## 🛠️ Tech Stack

| Technology        | Purpose                  |
| ----------------- | ------------------------ |
| Python            | Programming language     |
| Playwright        | Web UI automation        |
| pytest            | Test framework           |
| pytest-html       | HTML test reporting      |
| Page Object Model | Framework design pattern |
| Git               | Version control          |
| GitHub            | Source code repository   |

---

## 🧪 Test Coverage

The end-to-end automation covers the following areas:

| Module          | Scenarios Covered                                       |
| --------------- | ------------------------------------------------------- |
| Home Page       | Logo validation, Login navigation, Products navigation  |
| Login           | Login page validation, credential entry, authentication |
| Products        | Products page validation, product selection             |
| Product Details | Product details validation, Add to Cart                 |
| Cart            | Cart navigation and product validation                  |
| Checkout        | Checkout page, delivery address, billing address        |
| Order           | Order comment, order placement, confirmation            |
| Logout          | Navigation and logout                                   |

---

## 🔄 End-to-End Automation Flow

The main test scenario follows this workflow:

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
23. Verify the order confirmation message
24. Navigate to the Home page
25. Log out from the application

---

## 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern.

```text
                    Test Layer
                        │
                        ▼
               test_end_to_end.py
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
    HomePage        LoginPage       ProductsPage
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                ProductDetailsPage
                        │
                        ▼
                   ViewCartPage
                        │
                        ▼
                   CheckoutPage
                        │
                        ▼
                    BasePage
                        │
                        ▼
                    Playwright
```

### Page Object Responsibilities

Each page object contains:

* Page locators
* Page-specific actions
* Page-specific validations
* Reusable methods

The test layer interacts with page objects instead of directly locating elements inside the test.

This keeps the test flow readable and makes page-specific code easier to maintain.

---

## 📂 Project Structure

```text
Playwright-Python-Pytest-Automation-Shopping-Website/
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
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔑 Key Framework Features

### 1. Page Object Model

Each application page has its own page object containing:

* Locators
* Page actions
* Page-specific validations

A common `BasePage` is used as the parent class for page objects.

### 2. pytest

pytest is used for:

* Test execution
* Assertions
* Fixtures
* Test configuration

### 3. Playwright

Playwright is used for:

* Browser automation
* Element interaction
* Page navigation
* Locator handling
* Assertions and validations

The browser is launched in **headed mode** so the automation steps can be visually observed during execution.

### 4. Assertions

Assertions are used to validate important application states and expected behavior throughout the end-to-end workflow.

### 5. Logging

Python logging is used to record useful information during execution, including:

* Application URL
* Page title
* Navigation
* Element visibility
* User actions

### 6. HTML Reporting

`pytest-html` is used to generate an HTML test execution report.

---

## ⚙️ Prerequisites

Make sure the following are installed:

* Python
* pip
* Git

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Monika0015git/Playwright-Python-Pytest-Automation-Shopping-Website.git
```

### 2. Navigate to the project directory

```bash
cd Playwright-Python-Pytest-Automation-Shopping-Website
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running the Tests

### Run the complete test suite

```bash
pytest
```

### Run tests with console output

```bash
pytest -s
```

### Generate an HTML report

```bash
pytest -s --html=reports/report.html --self-contained-html
```

---

## 📊 Test Reports & Logging

The framework is configured to:

* Display test logs in the terminal
* Store logs in `reports/test.log`
* Generate HTML reports in the `reports` directory

The generated reports are excluded from Git using `.gitignore`.

---

## 📸 Screenshots

Screenshots can be stored in the `screenshots` directory to document:

* Test execution
* Application workflow
* Failed test scenarios
* HTML test reports

---

## 🧩 Why Page Object Model?

Page Object Model is used to separate **test logic** from **page-specific locators and actions**.

This provides:

* Better code organization
* Reusable page methods
* Easier maintenance
* Reduced locator duplication
* More readable test cases

---

## 🚀 Future Enhancements

Possible improvements for the framework include:

* Add more positive and negative test scenarios
* Add parameterized test data using pytest
* Improve test data management
* Add automatic screenshots on test failure
* Expand checkout and payment automation
* Add cross-browser execution
* Add CI/CD integration using GitHub Actions
* Improve test reporting

---

## 👩‍💻 Author

**Monika Rani Bilung**

Junior QA Engineer | Manual Testing | Test Automation

**GitHub:**
https://github.com/Monika0015git

**LinkedIn:**
http://www.linkedin.com/in/monika-bilung-060201274

---

## 🔗 Repository

**GitHub Repository:**
https://github.com/Monika0015git/Playwright-Python-Pytest-Automation-Shopping-Website

<img width="1365" height="723" alt="image" src="https://github.com/user-attachments/assets/a35c68bb-995e-4a68-ac20-56910aaffa94" />
<img width="808" height="1257" alt="test execution report" src="https://github.com/user-attachments/assets/a8854203-6255-484f-be6c-bc7bf9c52e64" />


