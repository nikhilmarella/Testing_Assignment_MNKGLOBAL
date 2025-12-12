import pytest
from pages.login_page import LoginPage

def test_login_success(driver, config):
    base = config["base_url"]
    username = config["login"]["username"]
    password = config["login"]["password"]

    login_page = LoginPage(driver, timeout=config.get("explicit_wait", 10))
    login_page.go_to_login(base)
    login_page.login(username, password)

    assert login_page.is_logged_in(), "Login failed: dashboard element not visible"
