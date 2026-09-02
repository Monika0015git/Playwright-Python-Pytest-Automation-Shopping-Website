import logging

from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.checkout_section=self.page.locator("li[class='active']")
        self.delivery_address_section=self.page.locator("#address_delivery")
        self.billing_address_section=self.page.locator("#address_invoice")
        self.delivery_address_details=self.page.locator("//ul[@id='address_delivery']/li")
        self.billing_address_details=self.page.locator("//ul[@id='address_invoice']/li")
        self.add_comment_field=self.page.locator("textarea[name='message']")
        self.place_order_button=self.page.locator("a[class='btn btn-default check_out']")

    def verify_checkout_page_visible(self):
        self.checkout_section.wait_for(state="visible")
        assert self.checkout_section.is_visible()
        print("Checkout section is visible on the checkout page.")
        logging.info("Checkout page is verified successfully.")


    def verify_delivery_address_visible(self):
        self.delivery_address_section.wait_for(state="visible")
        assert self.delivery_address_section.is_visible()
        logging.info("Delivery address section is verified as visible on the checkout page.")
        print("Delivery address section is visible on the checkout page.")
        print("Deliver information : ")
        for details in self.delivery_address_details.all():
            print(details.inner_text())

    def verify_billing_address_visible(self):
        self.billing_address_section.wait_for(state="visible")
        assert self.billing_address_section.is_visible()
        logging.info("Billing address section is verified as visible on the checkout page.")
        print("Billing address section is visible on the checkout page.")   
        print("Billing information : ")
        for details in self.billing_address_details.all():
            print(details.inner_text())    

    def enter_comment(self):
        self.add_comment_field.scroll_into_view_if_needed()
        self.add_comment_field.fill("Leave the package if no one answers the door. Please do not ring the bell.")
        logging.info("Additional delivery instructions are entered in the comment field on the checkout page.")

    def click_place_order(self):
        self.place_order_button.scroll_into_view_if_needed()
        self.place_order_button.click()
        print("Place Order button clicked.")
        print("Current URL:", self.page.url)
        logging.info("Place Order button is clicked on the checkout page to navigate to the payment and order confirmation page.")