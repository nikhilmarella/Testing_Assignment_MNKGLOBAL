from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormPage(BasePage):
   
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    CART_ICON = (By.ID, "shopping_cart_container")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_TEXT = (By.CSS_SELECTOR, "h2.complete-header")

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart_and_checkout(self):
        self.click(self.CART_ICON)
        self.click(self.CHECKOUT_BTN)

    def fill_checkout_form(self, first, last, postal):
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def is_checkout_complete(self):
        return self.is_element_visible(self.COMPLETE_TEXT)
