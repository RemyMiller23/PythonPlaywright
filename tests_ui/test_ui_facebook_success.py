import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect


from pom.home_page_elements import HomePage
from pom.sign_up_page_elements import SignUpPage
import pytest


PASSWORD = os.environ['PASSWORD']

@pytest.mark.smoke
@pytest.mark.parametrize("name, surname, day, month, year, email, password",
                         [("Julia", "Gleeson", "30", "Apr", "1999", "JuliaG@myspy.com", PASSWORD),
                          pytest.param("Megan", "Joshnton", "22", "Mar", "2001", "MegG@myspy.com", PASSWORD, marks=pytest.mark.xfail),
                          ("Zima", "Miller", "24", "Nov", "1997", "Zima@myspy.com", PASSWORD)])
def test_singup_success(setup, name,surname,day,month,year,email,password) -> None:
    page = setup

    home = HomePage(page)
    signUp = SignUpPage(page)

    home.singUpButton.click()
    signUp.submit_form(name,surname,day,month,year,email,password)

    print(page.get_by_text("It looks like you may have"))

    # ---------------------


@pytest.mark.smoke
def test_singup_success_2(setup) -> None:
    page = setup

    home = HomePage(page)
    signUp = SignUpPage(page)

    home.singUpButton.click()
    signUp.submit_form("Annie", "Baline", "30", "Apr", "2009", "Annie@myspy.com", PASSWORD)

    print(page.get_by_text("It looks like you may have"))

    # ---------------------




