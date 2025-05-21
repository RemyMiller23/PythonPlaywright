

class LoginPage:
    def __init__(self, page):
            self.email_input = page.get_by_test_id("email-input")
            self.remember_me = page.locator("id=rememberMeCheckbox")
            self.login_button = page.locator("id=btn-login")

