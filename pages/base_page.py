import os
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def take_screenshot(self, step_name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        file_path = f"{screenshot_dir}/{timestamp}_{step_name}.png"
        self.driver.save_screenshot(file_path)

        # 🔥 Attach to current pytest node
        try:
            import inspect
            for frame in inspect.stack():
                if "request" in frame.frame.f_locals:
                    request = frame.frame.f_locals["request"]
                    request.node._screenshots.append(file_path)
                    break
        except Exception:
            pass

        return file_path
