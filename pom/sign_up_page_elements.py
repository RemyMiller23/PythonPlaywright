
class SignUpPage:
    def  __init__(self,page):
        self.page = page

    def submit_form(self, name, surname, day, month, year, email, password):
        self.page.get_by_role("textbox", name="First name").fill(name)
        self.page.get_by_role("textbox", name="Surname").fill(surname)
        self.page.get_by_label("Day").select_option(day)
        self.page.get_by_label("Month").select_option(month)
        self.page.get_by_label("Year").select_option(year)
        self.page.get_by_role("radio", name="Female").check()
        self.page.get_by_role("textbox", name="Mobile number or email address").fill(email)
        self.page.get_by_role("textbox", name="New password").fill(password)
        self.page.get_by_role("button", name="Sign Up").click()