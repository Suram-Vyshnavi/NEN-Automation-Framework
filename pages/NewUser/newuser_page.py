import os

from locators.new_user_loactors.newuser_reg_locators import newuser_reg_locators
from locators.common.login_locators import LoginLocators
from utils.helpers import attach_screenshot, highlight_element

# Input locators derived from the label locators in newuser_reg_locators.
# These target the actual <input> sibling next to each floating label.
_OTP_INPUT = "//label[text()='Enter OTP']/following::input[1]"
_FIRST_NAME_INPUT = "//label[text()='First Name']/following::input[1]"
_LAST_NAME_INPUT = "//label[text()='Last Name']/following::input[1]"
_PHONE_NUMBER_INPUT = "//label[text()='Phone Number']/following::input[1]"


class NewUserPage:
    def __init__(self, page):
        self.page = page
        self.locators = newuser_reg_locators()
        self.login_locators = LoginLocators()

    # ------------------------------------------------------------------
    # Step 1: navigate to login page (handled by environment before_scenario)
    # ------------------------------------------------------------------

    def validate_login_page(self):
        """Verify the Login button is visible to confirm we are on the login page."""
        try:
            login_btn = self.page.locator(self.locators.LOGIN_BUTTON)
            login_btn.wait_for(state="visible", timeout=15000)
            assert login_btn.is_visible(), "Login page is not displayed"
            highlight_element(self.page, self.locators.LOGIN_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Login Page Validation Failed")
            print(f"Login page validation failed: {e}")

    # ------------------------------------------------------------------
    # Step 2: click Sign Up
    # ------------------------------------------------------------------

    def click_sign_up_button(self):
        try:
            sign_up = self.page.locator(self.locators.SIGN_UP_BUTTON)
            sign_up.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.SIGN_UP_BUTTON)
            self.page.click(self.locators.SIGN_UP_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Click Sign Up Button Failed")
            print(f"Failed to click Sign Up button: {e}")

    # ------------------------------------------------------------------
    # Step 3: fill email and click Create
    # ------------------------------------------------------------------

    def fill_email_and_click_create(self, email: str):
        try:
            email_input = self.page.locator(self.locators.EMAIL_INPUT)
            email_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.EMAIL_INPUT, email)
            highlight_element(self.page, self.locators.EMAIL_INPUT)

            create_btn = self.page.locator(self.locators.CREATE_BUTTON)
            create_btn.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.CREATE_BUTTON)
            self.page.click(self.locators.CREATE_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Fill Email and Click Create Failed")
            print(f"Failed to fill email or click Create: {e}")

    # ------------------------------------------------------------------
    # Step 4: enter OTP and submit
    # ------------------------------------------------------------------

    def enter_otp_and_submit(self, otp: str):
        """Fill the OTP field and click Submit.

        The OTP value must be passed in.  In CI set TEST_OTP env var; for
        manual runs pass the OTP received on the registered email.
        """
        try:
            # Wait for OTP section to appear
            otp_label = self.page.locator(self.locators.ENTER_OTP)
            otp_label.wait_for(state="visible", timeout=20000)
            highlight_element(self.page, self.locators.ENTER_OTP)

            # Fill the actual input sibling
            otp_input = self.page.locator(_OTP_INPUT)
            otp_input.wait_for(state="visible", timeout=10000)
            self.page.fill(_OTP_INPUT, otp)

            submit_btn = self.page.locator(self.locators.SUBMIT_BUTTON)
            submit_btn.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.SUBMIT_BUTTON)
            self.page.click(self.locators.SUBMIT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Enter OTP and Submit Failed")
            print(f"Failed to enter OTP or click Submit: {e}")

    # ------------------------------------------------------------------
    # Step 5: fill password and click Confirm Password
    # ------------------------------------------------------------------

    def fill_password_and_confirm(self, password: str):
        try:
            pwd_input = self.page.locator(self.locators.ADD_NEW_PASSWORD)
            pwd_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.ADD_NEW_PASSWORD, password)
            highlight_element(self.page, self.locators.ADD_NEW_PASSWORD)

            confirm_input = self.page.locator(self.locators.CONFIRM_PASSWORD)
            confirm_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.CONFIRM_PASSWORD, password)
            highlight_element(self.page, self.locators.CONFIRM_PASSWORD)

            # Accept terms checkbox
            checkbox = self.page.locator(self.locators.CHECKBOX)
            checkbox.wait_for(state="visible", timeout=10000)
            if not checkbox.is_checked():
                self.page.click(self.locators.CHECKBOX)
            highlight_element(self.page, self.locators.CHECKBOX)

            confirm_btn = self.page.locator(self.locators.CONFIRM_PASSWORD_BUTTON)
            confirm_btn.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.CONFIRM_PASSWORD_BUTTON)
            self.page.click(self.locators.CONFIRM_PASSWORD_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Fill Password and Confirm Failed")
            print(f"Failed to fill password or click Confirm Password: {e}")

    # ------------------------------------------------------------------
    # Step 6: fill registration form and submit
    # ------------------------------------------------------------------

    def fill_registration_form_and_submit(
        self,
        first_name: str = "Test",
        last_name: str = "User",
        phone_number: str = "9876543210",
    ):
        try:
            # First Name
            fn_input = self.page.locator(_FIRST_NAME_INPUT)
            fn_input.wait_for(state="visible", timeout=15000)
            self.page.fill(_FIRST_NAME_INPUT, first_name)
            highlight_element(self.page, self.locators.FIRST_NAME)

            # Last Name
            ln_input = self.page.locator(_LAST_NAME_INPUT)
            ln_input.wait_for(state="visible", timeout=10000)
            self.page.fill(_LAST_NAME_INPUT, last_name)
            highlight_element(self.page, self.locators.LAST_NAME)

            # Select Country
            country_dropdown = self.page.locator(self.locators.SELECT_COUNTRY)
            country_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_COUNTRY)
            india_option = self.page.locator(self.locators.INDIA_OPTION)
            india_option.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.INDIA_OPTION)
            self.page.click(self.locators.INDIA_OPTION)

            # Select City
            city_dropdown = self.page.locator(self.locators.SELECT_CITY)
            city_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_CITY)
            bangalore_option = self.page.locator(self.locators.BANGALORE_OPTION)
            bangalore_option.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.BANGALORE_OPTION)
            self.page.click(self.locators.BANGALORE_OPTION)

            # Phone Number
            phone_input = self.page.locator(_PHONE_NUMBER_INPUT)
            phone_input.wait_for(state="visible", timeout=10000)
            self.page.fill(_PHONE_NUMBER_INPUT, phone_number)
            highlight_element(self.page, self.locators.PHONE_NUMBER)

            # Profile Type
            profile_dropdown = self.page.locator(self.locators.PROFILE_TYPE_DROPDOWN)
            profile_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.PROFILE_TYPE_DROPDOWN)
            profile_option = self.page.locator(self.locators.PROFILE_TYPE_OPTION)
            profile_option.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.PROFILE_TYPE_OPTION)
            self.page.click(self.locators.PROFILE_TYPE_OPTION)

            # Submit form
            submit_btn = self.page.locator(self.locators.SUBMIT_BUTTON)
            submit_btn.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.SUBMIT_BUTTON)
            self.page.click(self.locators.SUBMIT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Fill Registration Form Failed")
            print(f"Failed to fill registration form: {e}")

    # ------------------------------------------------------------------
    # Step 7: validate home page, click profile icon, logout
    # ------------------------------------------------------------------

    def validate_home_click_profile_and_logout(self):
        try:
            # Validate home page loaded
            home_element = self.page.locator(self.locators.HOME)
            home_element.wait_for(state="visible", timeout=20000)
            assert home_element.is_visible(), "Home page is not displayed after registration"
            highlight_element(self.page, self.locators.HOME)

            # Click profile icon to open profile menu
            profile_icon = self.page.locator(self.locators.MY_PROFILE_ICON)
            profile_icon.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.locators.MY_PROFILE_ICON)
            self.page.click(self.locators.MY_PROFILE_ICON)

            # Click Logout
            logout_btn = self.page.locator(self.login_locators.LOGOUT_BUTTON)
            logout_btn.wait_for(state="visible", timeout=10000)
            highlight_element(self.page, self.login_locators.LOGOUT_BUTTON)
            self.page.click(self.login_locators.LOGOUT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Home Page or Logout Failed")
            print(f"Failed during home validation or logout: {e}")
