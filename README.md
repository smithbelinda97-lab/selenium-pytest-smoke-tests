# Selenium Pytest Automation Framework

This project is a complete Selenium automation framework built using **Python** and **Pytest**.
It follows the **Page Object Model (POM)** and includes smoke tests, login validation,
cart operations, checkout flows, menu verification, and reset app state scenarios.

---

## 🔧 Tech Stack
- Python 3.13
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Git & GitHub
- Visual Studio Code

---

## 📂 Project Structure

selenium-pytest-automation-framework/
│
├── pages/ # Page Object Model classes
│ ├── base_page.py # Common reusable methods (waits, screenshots, etc.)
│ ├── login_page.py # Login page actions and locators
│ ├── home_page.py # Product, cart, menu actions
│ └── checkout_page.py # Checkout and order completion actions
│
├── tests/ # Test cases
│ ├── smoke/
│ │ └── test_smoke.py
│ ├── test_login_001.py
│ ├── test_invalid_login_002.py
│ ├── test_checkout_003.py
│ ├── test_multi_product_checkout_004.py
│ └── test_cart_menu_sort_reset_005.py
│
├── utils/ # Utilities
│ └── driver_factory.py # WebDriver setup and browser configuration
│
├── reports/ # HTML test reports (generated at runtime)
│
├── conftest.py # Pytest fixtures and hooks
├── .gitignore
├── README.md
└── Test_Plan.md

yaml
Copy code

---

## ✅ Test Scenarios Covered
- Smoke test to verify application launch
- Valid login and logout
- Invalid login error validation
- Add products to cart
- Remove products and verify cart count
- Sort products by price (Low to High)
- Complete checkout flow (single and multiple products)
- Purchase multiple products
- Verify hamburger menu options
- Reset application state and validate cart reset

---

## ▶️ How to Run the Tests

### 1️⃣ Create and activate virtual environment
```bash
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
2️⃣ Install dependencies
bash
Copy code
pip install selenium pytest webdriver-manager
3️⃣ Run all tests
bash
Copy code
pytest
4️⃣ Run tests with HTML report
bash
Copy code
pytest -v --html=reports/report.html --self-contained-html

