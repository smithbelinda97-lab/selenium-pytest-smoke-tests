from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.mark.order(4)
def test_complete_purchase_flow(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    checkout_page = CheckoutPage(driver)

    # 1️⃣ Login
    home_page.open_home_page()
    login_page.login("standard_user", "secret_sauce")

    assert home_page.is_products_page_displayed()

    # 2️⃣ Add to cart
    home_page.add_item_to_cart()

    # 3️⃣ Go to cart
    home_page.go_to_cart()

    # 4️⃣ Checkout
    home_page.proceed_to_checkout()

    # 5️⃣ Enter checkout details
    checkout_page.enter_checkout_details(
        first_name="Test",
        last_name="User",
        postal_code="600001"
    )

    # 6️⃣ Finish order
    checkout_page.finish_order()

    # 7️⃣ Verify order success
    assert checkout_page.is_order_successful()

    # 8️⃣ Logout
    home_page.logout()
