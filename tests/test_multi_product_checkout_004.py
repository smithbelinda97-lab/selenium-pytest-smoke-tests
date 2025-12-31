from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.mark.order(5)
def test_purchase_multiple_products(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)

    # 1️⃣ Login
    home_page.open_home_page()
    login_page.login("standard_user", "secret_sauce")

    assert home_page.is_products_page_displayed()

    # 2️⃣ Add multiple products
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    for product in products:
        home_page.add_product_to_cart(product)

    # 3️⃣ Verify cart count
    assert home_page.get_cart_count() == len(products)

    # 4️⃣ Go to cart & checkout
    home_page.go_to_cart()
    home_page.proceed_to_checkout()

    # 5️⃣ Enter checkout details
    checkout_page.enter_checkout_details(
        first_name="Multi",
        last_name="Buyer",
        postal_code="600001"
    )

    # 6️⃣ Finish order
    checkout_page.finish_order()

    # 7️⃣ Verify order success
    assert checkout_page.is_order_successful()

    # 8️⃣ Logout
    home_page.logout()
    assert login_page.is_login_page_displayed()
