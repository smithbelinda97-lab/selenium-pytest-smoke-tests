from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

@pytest.mark.order(2)
def test_valid_login_logout(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    home_page.open_home_page()
    login_page.login("standard_user", "secret_sauce")

    assert home_page.is_products_page_displayed()

    home_page.logout()
    assert login_page.is_login_page_displayed()
