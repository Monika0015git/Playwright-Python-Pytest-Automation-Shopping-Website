import logging
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        # Locate Products link
        self.products_link = self.page.get_by_role("link",name="Products"        )

        # Locate product section
        self.product_section = self.page.locator("section[style='height: auto !important;']")

        # Locate the third Add to Cart button
        self.view_product_button = self.page.locator("a[href='/product_details/2']")

    def verify_product_page_visible(self):

        self.product_section.scroll_into_view_if_needed()

        assert self.product_section.is_visible()

        print("Product section is visible on the products page.")
        logging.info("Product page is verified successfully.")

    def click_product(self):

        self.view_product_button.click()

        print("Product clicked.")
        logging.info("View_Product button is clicked for the selected product on the products page.")