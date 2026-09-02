import pytest
from playwright.sync_api import sync_playwright


# This fixture is responsible for launching and closing the browser
@pytest.fixture
def page():

    # Start Playwright
    playwright = sync_playwright().start()

    # Launch Chromium browser in headed mode
    # headless=False means we can see the browser window
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context
    # A context is like a fresh browser session
    context = browser.new_context()

    # Open a new page (browser tab)
    page = context.new_page()

    # Send the page to the test
    # The test will run from this point
    yield page

    # Close the browser after the test is completed
    browser.close()

    # Stop Playwright
    playwright.stop()