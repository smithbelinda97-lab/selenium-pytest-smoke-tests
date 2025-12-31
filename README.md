# Selenium Pytest Automation Framework

This project is a complete Selenium automation framework built using Python and Pytest.
It follows the Page Object Model and includes smoke tests, login validation,
cart operations, checkout flows, menu verification, and reset app state scenarios.


---

## 🔧 Tech Stack
- Python 3.13
- Selenium WebDriver
- Pytest
- WebDriverManager
- Git & GitHub
- Visual Studio Code

---

## 📂 Project Structure
🔹 Complete Project Structure section

selenium-pytest-automation-framework/
│
├── pages/                  # Page Object Model classes
│   ├── base_page.py         # Common reusable methods (waits, screenshots, etc.)
│   ├── login_page.py        # Login page actions and locators
│   ├── home_page.py         # Product, cart, menu actions
│   └── checkout_page.py     # Checkout and order completion actions
│
├── tests/                  # Test cases
│   ├── smoke/               # Smoke tests
│   │   └── test_smoke.py
│   ├── test_login_001.py
│   ├── test_invalid_login_002.py
│   ├── test_checkout_003.py
│   ├── test_multi_product_checkout_004.py
│   └── test_cart_menu_sort_reset_005.py
│
├── utils/                  # Utilities
│   └── driver_factory.py   # WebDriver setup and browser configuration
│
├── reports/                # HTML test reports (generated at runtime)
│
├── conftest.py              # Pytest fixtures and hooks
├── .gitignore
├── README.md
└── Test_Plan.md

---

## ✅ Test Scenarios
- Smoke test to verify application launch
- Valid login and logout
- Invalid login error validation
- Add products to cart
- Remove products and verify cart count
- Sort products by price (Low to High)
- Complete checkout flow (single and multiple products)
- Verify hamburger menu options
- Reset application state and validate cart reset
---

## ▶️ How to Run the Tests

### 1. Create and activate virtual environment
```bash
python -m venv venv
Windows

venv\Scripts\activate

2. Install dependencies
pip install selenium pytest webdriver-manager
3. Run tests
pytest

---

### 🔹 Add Learning Outcomes section (VERY GOOD FOR RECRUITERS)
```markdown
---

## 🧠 What This Project Demonstrates
- Selenium automation using Python
- Pytest test discovery and execution
- WebDriverManager for browser setup
- Proper use of virtual environments
- Clean Git repository management
🔹 Add Future Enhancements
---

## 🚀 Future Enhancements
- Page Object Model (POM)
- Explicit waits for better stability
- Login automation flows
- HTML test reports
- CI/CD integration
🔹 Author section (optional but nice)
---

## 👩‍💻 Author
Belinda Smith
