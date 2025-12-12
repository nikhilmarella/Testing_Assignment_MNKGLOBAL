import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.form_page import FormPage

fake = Faker()

@pytest.mark.parametrize("postal_code", ["560001", "110001"])
def test_checkout_flow(driver, config, postal_code):
    # login
    base = config["base_url"]
    username = config["login"]["username"]
    password = config["login"]["password"]

    login = LoginPage(driver, timeout=config.get("explicit_wait", 10))
    login.go_to_login(base)
    login.login(username, password)
    assert login.is_logged_in(), "Login failed"

    # form / checkout flow
    form = FormPage(driver, timeout=config.get("explicit_wait", 10))
    # add first item to cart (on inventory page)
    form.add_first_item_to_cart()
    form.go_to_cart_and_checkout()

    # generate fake user details
    first = fake.first_name()
    last = fake.last_name()
    postal = postal_code  # or fake.postcode() - parameterized to demo

    form.fill_checkout_form(first, last, postal)
    form.finish_checkout()

    assert form.is_checkout_complete(), "Checkout did not complete successfully"
