from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

@pytest.mark.order(6)
def test_cart_sort_menu_and_reset_flow(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # 1️⃣ Login
    home_page.open_home_page()
    login_page.login("standard_user", "secret_sauce")
    assert home_page.is_products_page_displayed()

    # 2️⃣ Add 3 products
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    for product in products:
        home_page.add_product(product)

    assert home_page.get_cart_count() == 3

    # 3️⃣ Remove 2 products
    home_page.remove_product("Sauce Labs Bike Light")
    assert home_page.get_cart_count() == 2

    home_page.remove_product("Sauce Labs Bolt T-Shirt")
    assert home_page.get_cart_count() == 1

    # 4️⃣ Sort products Low → High
    home_page.sort_low_to_high()

    # 5️⃣ Open hamburger menu & verify options
    home_page.open_menu()
    assert home_page.are_menu_options_displayed()

    # 6️⃣ Reset app state
    home_page.reset_app_state()

    # Cart should be cleared
    assert home_page.get_cart_count() == 0

    # 7️⃣ Open menu again & verify options still visible
    home_page.open_menu()
    assert home_page.are_menu_options_displayed()

    # 8️⃣ Logout
    home_page.logout()
    assert login_page.is_login_page_displayed()
