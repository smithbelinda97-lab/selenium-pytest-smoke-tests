from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def enter_checkout_details(self, first_name, last_name, postal_code):
        self.wait_for_visibility(self.FIRST_NAME).send_keys(first_name)
        self.take_screenshot("first_name_entered")

        self.wait_for_visibility(self.LAST_NAME).send_keys(last_name)
        self.take_screenshot("last_name_entered")

        self.wait_for_visibility(self.POSTAL_CODE).send_keys(postal_code)
        self.take_screenshot("postal_code_entered")

        self.wait_for_clickable(self.CONTINUE_BUTTON).click()
        self.take_screenshot("checkout_continue_clicked")

    def finish_order(self):
        self.wait_for_clickable(self.FINISH_BUTTON).click()
        self.take_screenshot("order_finished")

    def is_order_successful(self):
        element = self.wait_for_visibility(self.SUCCESS_MESSAGE)
        self.take_screenshot("order_success_message")
        return element.is_displayed()
