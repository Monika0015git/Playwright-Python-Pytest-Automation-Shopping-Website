import logging

from pages.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.payment_section=self.page.locator("li[class='active']")
        self.name_on_card_input = self.page.locator("input[name='name_on_card']")
        self.card_number_input = self.page.locator("input[name='card_number']")
        self.cvc_input = self.page.locator("input[name='cvc']")
        self.expiration_month_input = self.page.locator("input[name='expiry_month']")
        self.expiration_year_input = self.page.locator("input[name='expiry_year']")
        self.pay_and_confirm_order_button = self.page.locator("button[data-qa='pay-button']")
        self.placed_order_message = self.page.locator("p[style='font-size: 20px; font-family: garamond;']")
        self.continue_button = self.page.locator("a[data-qa='continue-button']")

    def verify_payment_page_visible(self):
        self.payment_section.wait_for(state="visible")
        assert self.payment_section.is_visible()
        print("Payment section is visible on the payment page.")
        logging.info("Payment page is verified successfully.")

    def enter_payment_details(self):
        self.name_on_card_input.fill("Monika Francis")
        self.card_number_input.fill("1234567890901234")
        self.cvc_input.fill("123")
        self.expiration_month_input.fill("!2")
        self.expiration_year_input.fill("2030")
        logging.info("Payment details are entered on the payment page.")

    def click_pay_and_confirm_order(self):
        self.pay_and_confirm_order_button.scroll_into_view_if_needed()
        self.pay_and_confirm_order_button.click()
        print("Pay and Confirm Order button clicked.")
        logging.info("Pay and Confirm Order button is clicked on the payment page.")
        print("Current URL:", self.page.url)

    def verify_order_placed_message_visible(self):
        self.placed_order_message.wait_for(state="visible")
        assert self.placed_order_message.is_visible()
        print("Order placed message is visible on the payment page.")  
        logging.info("Order placed message is verified as visible on the payment page.") 

    def click_continue_button(self):
        self.continue_button.scroll_into_view_if_needed()
        self.continue_button.click()
        print("Continue button clicked.")
        print("Current URL:", self.page.url)
        logging.info("Continue button is clicked on the payment page to navigate back to the home page.")