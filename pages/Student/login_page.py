from locators.student_locators.login_locators import LoginLocators
from utils.helpers import attach_screenshot, highlight_element


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.locators = LoginLocators()

    def click_login_button(self):
        """Click on the Login button"""
        login_btn = self.page.locator(self.locators.LOGIN_BUTTON)
        login_btn.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.LOGIN_BUTTON)
        attach_screenshot(self.page, "Clicked Login Button")

    def enter_credentials(self, email, password):
        """Enter email and password credentials"""
        # Enter email
        email_input = self.page.locator(self.locators.EMAIL_INPUT)
        email_input.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.EMAIL_INPUT, email)
        highlight_element(self.page, self.locators.EMAIL_INPUT)
        
        # Enter password
        password_input = self.page.locator(self.locators.PASSWORD_INPUT)
        password_input.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.PASSWORD_INPUT, password)
        highlight_element(self.page, self.locators.PASSWORD_INPUT)
        
        attach_screenshot(self.page, "Credentials Entered")

    def click_sign_in_button(self):
        """Click on the Sign In button"""
        sign_in_btn = self.page.locator(self.locators.SIGN_IN)
        sign_in_btn.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SIGN_IN)
        attach_screenshot(self.page, "Clicked Sign In Button")

    def handle_no_thanks_popup(self):
        """Handle 'No thanks' popup if it appears (Popup 1)"""
        try:
            no_thanks_btn = self.page.locator(self.locators.NO_THANKS_POPUP)
            # Wait for up to 5 seconds for the popup
            no_thanks_btn.wait_for(state="visible", timeout=5000)
            if no_thanks_btn.is_visible():
                self.page.click(self.locators.NO_THANKS_POPUP)
                attach_screenshot(self.page, "Popup 1: Clicked No Thanks")
        except Exception:
            # Popup didn't appear, continue
            pass

    def handle_get_started_popup(self):
        """Handle 'Get Started' popup if it appears (Popup 1.5)"""
        try:
            close_btn = self.page.locator(self.locators.CLOSE_POPUP_GETSTARTED)
            close_btn.wait_for(state="visible", timeout=5000)
            if close_btn.is_visible():
                self.page.click(self.locators.CLOSE_POPUP_GETSTARTED)
                attach_screenshot(self.page, "Popup 1.5: Closed Get Started Popup")
        except Exception:
            # Popup didn't appear, continue
            pass

    def handle_start_journey_popup(self):
        """Handle 'Start your Journey' popup - validate and click Next (Popup 2)"""
        try:
            journey_popup = self.page.locator(self.locators.START_YOUR_JOURNEY_POPUP)
            journey_popup.wait_for(state="visible", timeout=10000)
            
            if journey_popup.is_visible():
                # Validate popup is displayed
                assert journey_popup.is_visible(), "Start your Journey popup is not visible"
                highlight_element(self.page, self.locators.START_YOUR_JOURNEY_POPUP)
                attach_screenshot(self.page, "Popup 2: Start Your Journey Validated")
                
                # Click Next button
                next_btn = self.page.locator(self.locators.NEXT_BUTTON)
                next_btn.wait_for(state="visible", timeout=5000)
                self.page.click(self.locators.NEXT_BUTTON)
                attach_screenshot(self.page, "Popup 2: Clicked Next Button")
        except Exception as e:
            # Popup didn't appear, continue
            attach_screenshot(self.page, "Popup 2: Not Found - Continuing")
            pass

    def handle_personalised_journey_popup(self):
        """Handle 'Create a personalised journey' popup - validate and click Next (Popup 3)"""
        try:
            personalised_popup = self.page.locator(self.locators.CREATE_PERSONALISED_JOURNEY_POPUP)
            personalised_popup.wait_for(state="visible", timeout=10000)
            
            if personalised_popup.is_visible():
                # Validate popup is displayed
                assert personalised_popup.is_visible(), "Create personalised journey popup is not visible"
                highlight_element(self.page, self.locators.CREATE_PERSONALISED_JOURNEY_POPUP)
                attach_screenshot(self.page, "Popup 3: Create Personalised Journey Validated")
                
                # Click Next button
                next_btn = self.page.locator(self.locators.NEXT_BUTTON)
                next_btn.wait_for(state="visible", timeout=5000)
                self.page.click(self.locators.NEXT_BUTTON)
                attach_screenshot(self.page, "Popup 3: Clicked Next Button")
        except Exception as e:
            # Popup didn't appear, continue
            attach_screenshot(self.page, "Popup 3: Not Found - Continuing")
            pass

    def handle_start_program_journey_popup(self):
        """Handle final popup - click 'Start program journey' button (Popup 4)"""
        try:
            start_journey_btn = self.page.locator(self.locators.START_PROGRAM_JOURNEY_BUTTON)
            start_journey_btn.wait_for(state="visible", timeout=10000)
            
            if start_journey_btn.is_visible():
                highlight_element(self.page, self.locators.START_PROGRAM_JOURNEY_BUTTON)
                attach_screenshot(self.page, "Popup 4: Start Program Journey Button Found")
                
                # Click Start program journey button
                self.page.click(self.locators.START_PROGRAM_JOURNEY_BUTTON)
                attach_screenshot(self.page, "Popup 4: Clicked Start Program Journey")
        except Exception as e:
            # Popup didn't appear, continue
            attach_screenshot(self.page, "Popup 4: Not Found - Continuing")
            pass

    def handle_all_popups(self):
        """Handle all 4 popups in sequence"""
        self.handle_no_thanks_popup()
        self.handle_start_journey_popup()
        self.handle_personalised_journey_popup()
        self.handle_start_program_journey_popup()
        self.handle_get_started_popup()

    def validate_successful_login(self):
        """Validate that login was successful by checking for Home element"""
        home_element = self.page.locator(self.locators.VALIDATE_LOGO)
        home_element.wait_for(state="visible", timeout=15000)
        assert home_element.is_visible(), "Home element is not visible - Login may have failed"
        highlight_element(self.page, self.locators.VALIDATE_LOGO)
        attach_screenshot(self.page, "Login Successful - Home Page Loaded")
    
    def logout(self):
        """Logout from the application"""
        try:
            # Click on profile menu first if it exists
            if hasattr(self.locators, 'PROFILE_MENU'):
                try:
                    profile_menu = self.page.locator(self.locators.PROFILE_MENU)
                    profile_menu.wait_for(state="visible", timeout=5000)
                    self.page.click(self.locators.PROFILE_MENU)
                except:
                    pass  # Profile menu might not exist
            
            # Click logout button
            logout_btn = self.page.locator(self.locators.LOGOUT_BUTTON)
            logout_btn.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.LOGOUT_BUTTON)
            attach_screenshot(self.page, "Logout Successful")
        except Exception as e:
            attach_screenshot(self.page, "Logout Failed or Button Not Found")
            raise Exception(f"Logout failed: {e}")
