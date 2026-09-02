import logging
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)

        self.login_section=self.page.get_by_text("Login to your account")
        self.email_address=self.page.locator("input[data-qa='login-email']")
        self.password=self.page.locator("input[data-qa='login-password']")
        self.login_button=self.page.locator("button[data-qa='login-button']")

    def verify_login_section_visible(self):
        assert self.login_section.is_visible()
        print("Login section is visible on the login page.")
        logging.info("Login page is verified successfully.")
        text=f"Login section text: {self.login_section.inner_text()}"
        print(text)
        logging.info("Login section text displayed as: %s", text)

    def enter_email_address(self,email):
        self.email_address.fill("monika.september@gmail.com")
        print("Email address entered:", email)
        logging.info("Email address entered")

    def enter_password(self,password):
        self.password.fill("test@demo#123")
        print("Password entered:", password)
        logging.info("Password entered")

    def click_login_button(self):
        self.login_button.click()
        print("Login button clicked.")
        print("Current URL:", self.page.url)
        logging.info("Login button is clicked on the login page.")
        logging.info("Current URL: %s", self.page.url)
    
