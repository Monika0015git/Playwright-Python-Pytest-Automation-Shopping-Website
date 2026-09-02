import logging

from pages.base_page import BasePage

class HomePage(BasePage):

    # Constructor
    def __init__(self, page):

        # Call the BasePage constructor
        # BasePage will store the page as self.page
        super().__init__(page)

        # Locate the Automation Exercise logo
        self.logo=self.page.locator("img[alt='Website for automation practice']")
        self.login_link=self.page.get_by_role("link", name="Signup / Login")
        self.products_link=self.page.get_by_role("link", name="Products")
        self.logout_link=self.page.locator("a[href='/logout']")

    # Open the home page
    def open_home_page(self):

        # Navigate to Automation Exercise
        self.page.goto("https://www.automationexercise.com/")
        print("Application is opened successfully")
        logging.info("Application is opened successfully at URL: https://www.automationexercise.com/")
        print("Page title:", self.page.title())
        logging.info("Page title displayed as : %s ", self.page.title())

    # Verify that the logo is visible
    def verify_logo_visible(self):
        assert self.logo.is_visible()
        print("Logo is visible on the home page.")  
        logging.info("Home page is verified as Logo is visible on the home page.")

    # Verify that the login link is visible
    def verify_login_link_visible(self):
        assert self.login_link.is_visible()
        print("Login link is visible on the home page.")
        text=f"Login link text: {self.login_link.inner_text()}"
        print(text)
        logging.info("Login link is verified as visible on the home page.")

    # Click the login link
    def click_login_link(self):
        self.login_link.click()
        logging.info("Login link is clicked on the home page.")
        assert self.page.url == "https://www.automationexercise.com/login"
        print("Navigated to login page successfully. Current URL:", self.page.url)
        logging.info("Navigated to login page successfully. Current URL: %s", self.page.url)

    def verify_products_link_visible(self):
        # Wait until Products link is visible
        self.products_link.wait_for(state="visible")
        assert self.products_link.is_visible()
        print("Products link is visible on the home page.")
        logging.info("Products link is verified as visible on the home page.")
        text=f"Products link text: {self.products_link.inner_text()}"
        print(text)     
        logging.info("Products link text displayed as: %s", text)

    def click_products_link(self):
        self.products_link.click()
        assert self.page.url == "https://www.automationexercise.com/products"
        logging.info("Products link is clicked on the home page.")
        print("Navigated to products page successfully. Current URL:", self.page.url)
        logging.info("Navigated to products page successfully. Current URL: %s", self.page.url)

    def verify_logout_link_visible(self):
        # Wait until Logout link is visible
        self.logout_link.wait_for(state="visible")
        assert self.logout_link.is_visible()
        print("Logout link is visible on the home page.")
        logging.info("Logout link is verified as visible on the home page.")
        text=f"Logout link text: {self.logout_link.inner_text()}"
        print(text)
        logging.info("Logout link text displayed as: %s", text)

    def click_logout_link(self):
        self.logout_link.click()
        assert self.page.url == "https://www.automationexercise.com/login"
        logging.info("Logout link is clicked on the home page.")
        print("Logged out successfully. Current URL:", self.page.url)
        logging.info("Logged out successfully. Current URL: %s", self.page.url)
