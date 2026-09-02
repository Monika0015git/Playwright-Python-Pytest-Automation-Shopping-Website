import logging

from pages.base_page import BasePage

class ProductDetailsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
       
        self.add_to_cart_button=self.page.locator("button[class='btn btn-default cart']")
        self.cart_modal=self.page.locator("//p[text()='Your product has been added to cart.']")
        self.view_cart_link=self.page.locator("a[href='/view_cart']").nth(1)

    def click_add_to_cart(self):
        self.add_to_cart_button.click()
        print("Add to Cart button clicked.")
        print("Current URL:", self.page.url)
        logging.info("Add to Cart button is clicked on the product details page.")
        logging.info("The selected product is added to the cart")

    def verify_product_added_to_cart(self):
        self.cart_modal.wait_for(state="visible")
        assert self.cart_modal.is_visible()
        print("Product added to cart modal is visible.")
        logging.info("Product added to cart successfully --> message is displayed.")
        self.view_cart_link.click()
        print("View Cart link clicked. Navigating to cart page.")
        logging.info("View Cart link is clicked on the product details page to navigate to the cart page.")
    