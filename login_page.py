from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def go_to_login(self, base_url):
        self.open(base_url)

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        # verify inventory container visible (dashboard)
        return self.is_element_visible(self.INVENTORY_CONTAINER)
