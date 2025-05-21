import re
import time
from login_page import LoginPage

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)

    lp = LoginPage(page)

    page.goto("https://rahulshettyacademy.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name=" Login").click()
    time.sleep(2)

    lp.email_input.fill("remy@test.com")
    lp.remember_me.uncheck()
    lp.login_button.click()

    # page.get_by_test_id("email-input").click()
    # page.get_by_test_id("email-input").fill("remy@test.com", timeout=3000)
    # page.get_by_test_id("rememberMeCheckbox").uncheck()
    # page.pause()
    # page.get_by_test_id("btn-login").click()
    page.wait_for_load_state()
    page.get_by_test_id("otp-input-0").click()
    page.get_by_test_id("otp-input-0").fill("1")
    page.get_by_test_id("otp-input-1").fill("5")
    page.get_by_test_id("otp-input-2").fill("4")
    page.get_by_test_id("otp-input-3").fill("2")
    page.get_by_test_id("otp-input-4").fill("2")
    page.get_by_test_id("otp-input-5").fill("2")
    page.get_by_test_id("btn-code").click()
    expect(page.get_by_text("Invalid code. Please try")).to_be_visible()

    print("Success")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
