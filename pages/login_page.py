from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    # 🔍 Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")


    # 🔹 Actions
    def login(self, username, password):
        self.wait_for_visibility(self.USERNAME_INPUT).send_keys(username)
        # self.take_screenshot("username_entered")

        self.wait_for_visibility(self.PASSWORD_INPUT).send_keys(password)
        self.take_screenshot("username_password_entered")

        time.sleep(2)
        self.wait_for_clickable(self.LOGIN_BUTTON).click()
        self.take_screenshot("login_clicked")

    def is_login_page_displayed(self):
        element = self.wait_for_visibility(self.LOGIN_BUTTON)
        self.take_screenshot("login_page_displayed")
        return element.is_displayed()

    def get_error_message(self):
        error_element = self.wait_for_visibility(self.ERROR_MESSAGE)
        self.take_screenshot("error_message_displayed")
        return error_element.text


