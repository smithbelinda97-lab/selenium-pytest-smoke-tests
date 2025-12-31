from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):

    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ADD_TO_CART_BUTTON_TEMPLATE = "add-to-cart-{}"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_PANEL = (By.CLASS_NAME, "bm-menu")

    # Hamburger Menu
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    MENU_WRAP = (By.CLASS_NAME, "bm-menu-wrap")
    MENU_ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    MENU_ABOUT = (By.ID, "about_sidebar_link")
    MENU_LOGOUT = (By.ID, "logout_sidebar_link")
    MENU_RESET = (By.ID, "reset_sidebar_link")

    # Product & Cart
    ADD_TO_CART_TEMPLATE = "add-to-cart-{}"
    REMOVE_FROM_CART_TEMPLATE = "remove-{}"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # Sort
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")


    def open_home_page(self):
        self.open_url("https://www.saucedemo.com/")
        self.take_screenshot("home_page_loaded")


    def is_products_page_displayed(self):
        element = self.wait_for_visibility(self.PRODUCTS_TITLE)
        self.take_screenshot("products_page_displayed")
        return element.is_displayed()

    def logout(self):
        # Ensure menu is open
        self.open_menu()

        # Click logout
        self.wait_for_clickable(self.MENU_LOGOUT).click()
        self.take_screenshot("logged_out")

    def add_item_to_cart(self):
        self.wait_for_clickable(self.ADD_TO_CART_BUTTON).click()
        self.take_screenshot("item_added_to_cart")

    def go_to_cart(self):
        self.wait_for_clickable(self.CART_ICON).click()
        self.take_screenshot("cart_opened")

    def proceed_to_checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BUTTON).click()
        self.take_screenshot("checkout_started")

    def add_product_to_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        locator = (By.ID, self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_id))

        self.wait_for_clickable(locator).click()
        self.take_screenshot(f"added_{product_id}")

    def get_cart_count(self):
        badge = self.wait_for_visibility(self.CART_BADGE)
        self.take_screenshot("cart_count_displayed")
        return int(badge.text)

    def add_product(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        locator = (By.ID, self.ADD_TO_CART_TEMPLATE.format(product_id))
        self.wait_for_clickable(locator).click()
        self.take_screenshot(f"added_{product_id}")

    def remove_product(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        locator = (By.ID, self.REMOVE_FROM_CART_TEMPLATE.format(product_id))
        self.wait_for_clickable(locator).click()
        self.take_screenshot(f"removed_{product_id}")

    def get_cart_count(self):
        try:
            badge = self.wait_for_visibility(self.CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def sort_low_to_high(self):
        dropdown = Select(self.wait_for_visibility(self.SORT_DROPDOWN))
        dropdown.select_by_value("lohi")
        self.take_screenshot("sorted_low_to_high")

    def open_menu(self):
        try:
            menu_wrap = self.driver.find_element(*self.MENU_WRAP)

            # If menu is already open, do nothing
            if menu_wrap.get_attribute("aria-hidden") == "false":
                return
        except:
            pass

        # Open menu
        self.wait_for_clickable(self.MENU_BUTTON).click()
        self.take_screenshot("menu_opened")

        # Wait until menu is actually open
        self.wait.until(
            lambda driver: driver.find_element(*self.MENU_WRAP)
            .get_attribute("aria-hidden") == "false"
        )

    def are_menu_options_displayed(self):
        return all([
            self.wait_for_visibility(self.MENU_ALL_ITEMS).is_displayed(),
            self.wait_for_visibility(self.MENU_ABOUT).is_displayed(),
            self.wait_for_visibility(self.MENU_LOGOUT).is_displayed(),
            self.wait_for_visibility(self.MENU_RESET).is_displayed()
        ])

    def reset_app_state(self):
        self.wait_for_clickable(self.MENU_RESET).click()
        self.take_screenshot("app_state_reset")
