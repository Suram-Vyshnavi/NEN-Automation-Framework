from playwright.sync_api import sync_playwright
import os
from pages.Student.guest_page import GuestPage
from pages.Student.login_page import LoginPage

# Global flag to track if setup is done
setup_complete = False

def before_all(context):
    """Setup browser once before all tests"""
    # Prefer shell env USER_TYPE over behave.ini userdata so terminal overrides work.
    env_user_type = os.getenv("USER_TYPE")
    userdata_user_type = context.config.userdata.get("USER_TYPE")
    user_type = (env_user_type or userdata_user_type or "student").strip().lower()
    os.environ["USER_TYPE"] = user_type
    from utils.config import Config

    global setup_complete
    
    # Start browser
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, slow_mo=1500,
        args=[
            '--start-maximized',
            '--force-device-scale-factor=1',
            '--high-dpi-support=1',
            '--disable-blink-features=AutomationControlled',
            '--use-fake-ui-for-media-stream',
            '--use-fake-device-for-media-stream'
        ]
    )
    context.browser_context = context.browser.new_context(
        no_viewport=True
    )
    context.page = context.browser_context.new_page()

    # Ensure every click/fill interaction scrolls into view and highlights the target element
    # This wraps Playwright methods at runtime so page objects don't need to change.
    from utils.helpers import highlight_element
    from playwright.sync_api import Locator, Page

    # Wrap Page.click to highlight before clicking
    _orig_page_click = Page.click
    def _highlighted_page_click(self, selector, *args, **kwargs):
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_click(self, selector, *args, **kwargs)
    Page.click = _highlighted_page_click

    # Wrap Locator.click to highlight before clicking
    _orig_locator_click = Locator.click
    def _highlighted_locator_click(self, *args, **kwargs):
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_click(self, *args, **kwargs)
    Locator.click = _highlighted_locator_click

    # Wrap Page.fill to highlight before filling
    _orig_page_fill = Page.fill
    def _highlighted_page_fill(self, selector, text, *args, **kwargs):
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_fill(self, selector, text, *args, **kwargs)
    Page.fill = _highlighted_page_fill

    # Wrap Locator.fill to highlight before filling
    _orig_locator_fill = Locator.fill
    def _highlighted_locator_fill(self, text, *args, **kwargs):
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_fill(self, text, *args, **kwargs)
    Locator.fill = _highlighted_locator_fill

    # Wrap Page.check/uncheck to highlight before interacting
    _orig_page_check = Page.check
    def _highlighted_page_check(self, selector, *args, **kwargs):
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_check(self, selector, *args, **kwargs)
    Page.check = _highlighted_page_check

    _orig_page_uncheck = Page.uncheck
    def _highlighted_page_uncheck(self, selector, *args, **kwargs):
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_uncheck(self, selector, *args, **kwargs)
    Page.uncheck = _highlighted_page_uncheck

    # Wrap Locator.check/uncheck to highlight before interacting
    _orig_locator_check = Locator.check
    def _highlighted_locator_check(self, *args, **kwargs):
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_check(self, *args, **kwargs)
    Locator.check = _highlighted_locator_check

    _orig_locator_uncheck = Locator.uncheck
    def _highlighted_locator_uncheck(self, *args, **kwargs):
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_uncheck(self, *args, **kwargs)
    Locator.uncheck = _highlighted_locator_uncheck

    # Wrap Page.select_option to highlight before selecting
    _orig_page_select_option = Page.select_option
    def _highlighted_page_select_option(self, selector, *args, **kwargs):
        try:
            highlight_element(self, selector)
        except Exception:
            pass
        return _orig_page_select_option(self, selector, *args, **kwargs)
    Page.select_option = _highlighted_page_select_option

    # Wrap Locator.select_option to highlight before selecting
    _orig_locator_select_option = Locator.select_option
    def _highlighted_locator_select_option(self, *args, **kwargs):
        try:
            highlight_element(self.page, self)
        except Exception:
            pass
        return _orig_locator_select_option(self, *args, **kwargs)
    Locator.select_option = _highlighted_locator_select_option

    print("\n========== STEP 2: User Login ==========")
    # Step 2: Perform login
    login_page = LoginPage(context.page)
    # Navigate back to base URL to find login button
    context.page.goto(Config.BASE_URL)
    login_page.click_login_button()
    login_page.enter_credentials(Config.USERNAME, Config.PASSWORD)
    login_page.click_sign_in_button()
    
    # Handle all 4 popups after login
    login_page.handle_all_popups()
    
    # Validate successful login
    login_page.validate_successful_login()
    print("✓ User Login Completed")
    
    setup_complete = True
    print("\n========== STEP 3: Running Test Scenarios ==========")


def before_scenario(context, scenario):
    """Skip setup scenarios as they're already done in before_all"""
    # Tag scenarios to identify which ones to skip
    if 'Validate Guest page' in scenario.name or 'Valid login' in scenario.name:
        scenario.skip("Already executed in before_all hook")


def after_all(context):
    """Logout and cleanup after all tests"""
    print("\n========== STEP 4: User Logout ==========")
    
    try:
        # Perform logout
        login_page = LoginPage(context.page)
        login_page.logout()
        print("✓ User Logout Completed")
    except Exception as e:
        print(f"Logout failed or not needed: {e}")
    
    # Close browser
    context.browser_context.close()
    context.browser.close()
    context.playwright.stop()
    print("\n========== Test Execution Complete ==========")
