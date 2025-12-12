# Testing_Assignment_MNKGLOBAL
QA Assignment for MNK GLOBAL



# Selenium Automation Assignment (Selenium + Python + pytest)

## Overview
This project automates login and form/checkout flows on https://www.saucedemo.com using Selenium (Python), pytest, and Page Object Model.

## Prerequisites
- Python 3.8+
- pip
- Chrome browser (or adapt to Firefox)
- (Optional) Docker if you plan to run with Selenium grid/container

## Setup
1. Create virtual environment:


python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows


2. Install requirements:


pip install -r requirements.txt


3. Ensure `config.json` contains correct `base_url` and credentials. Example uses `standard_user` for SauceDemo.

## Run tests locally
Generate html report:


pytest -q --html=report.html --self-contained-html

This runs tests and writes `report.html` in project root.

### Run headless
Set env var HEADLESS=true:


export HEADLESS=true # Linux/macOS
set HEADLESS=true # Windows (cmd)

then run pytest:

pytest -q --html=report.html --self-contained-html


## Reports and screenshots
- `report.html` contains pytest-html report.
- Screenshots of failures are saved into `screenshots/` with filename `testname_YYYYMMDD_HHMMSS.png`.

## Docker (optional)
Two approaches:
1. Run tests **inside** a container that has Chrome + chromedriver.
2. Use standalone Selenium docker image and run tests from host using remote webdriver.

### Example docker-compose to run Selenium Chrome:
```yaml
version: "3"
services:
  selenium:
    image: selenium/standalone-chrome:115.0
    ports:
      - "4444:4444"


Then adapt conftest.py to use Remote webdriver at http://localhost:4444/wd/hub instead of local ChromeDriver. (See docs in docker/).

Notes

This project uses webdriver-manager to automatically download the chromedriver version compatible with your Chrome.

Use explicit waits (WebDriverWait) via BasePage.

To embed screenshots in pytest-html, you can add a pytest_html hook to attach binary image content. The current setup saves screenshots in screenshots/ and adds path to report metadata.


---

10) Optional: `docker/Dockerfile` (run tests inside container)
```dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y wget gnupg2 unzip xvfb libnss3 libgconf-2-4 fonts-liberation libasound2 \
    && rm -rf /var/lib/apt/lists/*

# install chrome (example for Debian based)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
 && apt-get update && apt-get install -y google-chrome-stable

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV HEADLESS=true

CMD ["pytest", "-q", "--html=report.html", "--self-contained-html"]


docker-compose.yml can add a volume to collect report.html.

11) Extra: Embedding screenshots into pytest-html (if you want)

Add to conftest.py:

import base64
from pytest_html import extras

def pytest_html_results_table_row(report, cells):
    # optional: modify html table rows
    pass

def pytest_html_results_table_html(report, data):
    # optional hook
    pass

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_extra_html(report):
    pass

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_extra(report):
    # attach screenshot to html if saved
    pass

# Simpler: in pytest_runtest_makereport, after saving screenshot:
if driver is not None:
    png = driver.get_screenshot_as_base64()
    extra = getattr(rep, "extra", [])
    extra.append(pytest_html.extras.image(png, mime_type="image/png"))
    rep.extra = extra


(You may need to from pytest_html import extras at top and ensure plugin installed.)
