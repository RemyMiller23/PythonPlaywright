import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect

from pom.home_page_elements import HomePage
from pom.sign_up_page_elements import SignUpPage
import pytest


PASSWORD = os.environ['PASSWORD']

#@pytest.mark.xfail(reason="not ready")
@pytest.mark.smoke
def test_singup(setup) -> None:
    page = setup

    home = HomePage(page)
    signUp = SignUpPage(page)

    home.singUpButton.click()
    signUp.submit_form("Jess", "Reid", "22", "Feb", "1995", "JessReid@myspy.com", PASSWORD)

    #Success_Message = page.get_by_text("It looks like you may have")
    #expect(Success_Message).to_contain_text("Successfully Created profile")

    # ---------------------




