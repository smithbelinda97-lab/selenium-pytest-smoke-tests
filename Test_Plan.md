# Test Plan – E-commerce Web Application

## 1. Introduction
This Test Plan document describes the testing strategy, scope, approach, and resources for the E-commerce web application.  
The objective of testing is to ensure that core functionalities such as authentication, product browsing, cart operations, and checkout work as expected and meet quality standards.

---

## 2. Application Overview
The application is a web-based e-commerce platform that allows users to:
- Log in and log out
- View a list of products with images and prices
- Add and remove products from the cart
- Sort products
- Reset application state
- Place an order through checkout

---

## 3. Scope of Testing

### 3.1 In Scope
The following features will be tested:
- Login functionality
- Logout functionality
- Product listing and product details
- Add to Cart and Remove from Cart
- Cart page validation
- Sort functionality
- Reset App State
- Checkout and order placement
- Navigation via hamburger menu

### 3.2 Out of Scope
The following are excluded from testing:
- Payment gateway integration
- Performance and load testing
- Security testing
- Mobile application testing
- Backend/database testing

---

## 4. Test Approach

### 4.1 Manual Testing
- Manual test cases are created and documented in an Excel sheet.
- Test cases include detailed steps, expected results, priority, and severity.
- Manual testing is used for:
  - UI validation
  - Exploratory testing
  - Low-priority or non-automatable scenarios

### 4.2 Automation Testing
- High-priority and regression test cases are automated.
- Selenium with Python is used for automation.
- Automated scripts cover:
  - Login and Logout
  - Add to Cart
  - Cart validation
  - Reset App State
  - Checkout flow
- Manual test cases are mapped to automation scripts for traceability.

---

## 5. Test Types
The following types of testing will be performed:
- Functional Testing
- Smoke Testing
- Regression Testing
- UI Testing
- Exploratory Testing

---

## 6. Test Environment
- Application Type: Web Application
- Browser: Google Chrome
- Operating System: Windows
- Automation Tool: Selenium
- Programming Language: Python
- Test Case Management: Excel
- Version Control: GitHub

---

## 7. Entry and Exit Criteria

### 7.1 Entry Criteria
- Application is accessible
- Test cases are prepared and reviewed
- Test environment is set up and stable

### 7.2 Exit Criteria
- All critical and high-priority test cases are executed
- No open critical or high-severity defects
- Test execution is completed and documented

---

## 8. Roles and Responsibilities
- QA Engineer:
  - Create test cases
  - Execute manual tests
  - Automate selected test cases
  - Report and track defects

*(For this project, all QA responsibilities are handled by the tester.)*

---

## 9. Test Deliverables
The following deliverables will be produced:
- Test Plan document
- Manual Test Cases (Excel)
- Automation Scripts
- Test Execution Results

---

## 10. Risks and Mitigation

| Risk | Mitigation |
|----|----|
| Application instability | Test during stable periods |
| Limited test data | Use predefined valid and invalid data |
| Time constraints | Prioritize high-risk and critical test cases |

---

## 11. Approval
This Test Plan is reviewed and approved to proceed with testing activities for the application.

---
