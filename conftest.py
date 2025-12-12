import json
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from utils.screenshot_helper import save_screenshot

# load config
def load_config():
    cfg_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(cfg_path) as f:
        return json.load(f)

CONFIG = load_config()

@pytest.fixture(scope="session")
def config():
    return CONFIG

@pytest.fixture
def driver(request, config):
    # build chrome options
    chrome_options = Options()
    if os.getenv("HEADLESS", str(config.get("headless", False))).lower() in ("true", "1"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(config.get("implicit_wait", 5))

    yield driver

    driver.quit()

# Hook to take screenshot on failure and attach path to report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            fname = save_screenshot(driver, folder="screenshots", prefix=item.name)
            # Attach path to report (pytest-html will pick up extra)
            if hasattr(rep, "extra"):
                rep.extra.append(("Screenshot", fname))
            else:
                rep.extra = [("Screenshot", fname)]
