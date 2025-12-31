from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()

    # Window
    options.add_argument("--start-maximized")

    # 🔥 Run in incognito (no saved passwords, no profile data)
    options.add_argument("--incognito")

    # 🔥 Disable password leak detection & security checks
    options.add_argument("--disable-features=PasswordLeakDetection")

    # 🔥 Disable automation infobars
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # 🔥 Disable password manager completely
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    return driver
