class BasePage:

    # Constructor
    # This method runs automatically when we create an object
    def __init__(self, page):

        # Store the Playwright page object
        # So other methods in this class can use it
        self.page = page