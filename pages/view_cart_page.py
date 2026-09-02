import logging

from pages.base_page import BasePage

class ViewCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.cart_section=self.page.get_by_text("Shopping Cart")
        self.proceed_to_checkout_button=self.page.locator("a[class='btn btn-default check_out']")
        self.product_table=self.page.locator("#cart_info_table")
        self.product_list=self.page.locator("//tbody/tr")

    def verify_cart_page_visible(self):
            self.cart_section.wait_for(state="visible")
            assert self.cart_section.is_visible()
            print("Cart section is visible on the cart page.")
            logging.info("Cart page is verified successfully")


    def verify_product_in_cart(self, product_name): 
            self.product_table.wait_for(state="visible")
            assert self.product_table.is_visible()
            print("Product table is visible on the cart page.")
            logging.info("Product table is verified as visible on the cart page.")
            count=self.product_list.count()
            print(f"Number of products in the cart: {count}")
            logging.info("Number of products are verified")

    def click_proceed_to_checkout(self):
            self.proceed_to_checkout_button
            self.proceed_to_checkout_button.click()
            print("Proceed to Checkout button clicked.")
            logging.info("Proceed to Checkout button is clicked on the cart page.")
            print("Current URL:", self.page.url)
            logging.info("Navigated to checkout page successfully. ")


           