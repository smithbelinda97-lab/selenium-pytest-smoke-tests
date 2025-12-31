from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

@pytest.mark.order(3)
def test_invalid_login_error_message(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    home_page.open_home_page()
    login_page.login("invalid_user", "wrong_password")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text
