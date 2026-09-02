from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.view_cart_page import ViewCartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

class TestEndToEnd:

    def test_end_to_end(self, page):

        print("Starting end-to-end test...")
        # Home Page
        home_page = HomePage(page)

        home_page.open_home_page()
        home_page.verify_logo_visible()
        home_page.verify_login_link_visible()
        home_page.click_login_link()

        # Login Page
        login_page = LoginPage(page)    

        login_page.verify_login_section_visible()
        login_page.enter_email_address("monika.september@gmail.com")
        login_page.enter_password("test@demo#123")
        login_page.click_login_button()

        # Verify Products link is visible after login
        home_page.verify_products_link_visible()
        
        # Click Products link
        home_page.click_products_link()

        # Products Page
        products_page = ProductsPage(page)

        products_page.verify_product_page_visible()
        products_page.click_product()   

        # Product Details Page
        product_details_page = ProductDetailsPage(page)

       
        product_details_page.click_add_to_cart()
        product_details_page.verify_product_added_to_cart() 

        # View Cart Page
        view_cart_page = ViewCartPage(page)

        view_cart_page.verify_cart_page_visible()
        view_cart_page.verify_product_in_cart("Blue Top")
        view_cart_page.click_proceed_to_checkout()

        # Checkout Page
        checkout_page = CheckoutPage(page)

        checkout_page.verify_checkout_page_visible()
        checkout_page.verify_delivery_address_visible()
        checkout_page.verify_billing_address_visible()
        checkout_page.enter_comment()
        checkout_page.click_place_order()

        # Payment Page
        payment_page = PaymentPage(page)

        payment_page.verify_payment_page_visible()
        payment_page.enter_payment_details()
        page.wait_for_timeout(2000)  # Wait for 2 seconds before clicking Pay and Confirm Order
        payment_page.click_pay_and_confirm_order()
        payment_page.verify_order_placed_message_visible()
        payment_page.click_continue_button()

        home_page.verify_logout_link_visible()
        home_page.click_logout_link()

        print("End-to-end test completed successfully.")

