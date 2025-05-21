import pytest
from playwright.sync_api import Playwright

@pytest.fixture()
def setup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com")

    yield page
    page.close()

