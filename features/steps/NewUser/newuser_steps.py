import os

from behave import given, then
from pages.NewUser.newuser_page import NewUserPage


def _get_newuser_page(context):
    if not hasattr(context, "newuser_page"):
        context.newuser_page = NewUserPage(context.page)
    return context.newuser_page


@given("user is on the login page")
def user_is_on_login_page(context):
    """Validate that the login page is displayed (browser opened by environment)."""
    _get_newuser_page(context).validate_login_page()


@then("user clicks on sign up button")
def user_clicks_sign_up(context):
    """Click the Sign Up button on the login page."""
    _get_newuser_page(context).click_sign_up_button()


@then("user fill the email and clicks on create button")
def user_fills_email_and_clicks_create(context):
    """Fill the registration email and click Create."""
    email = os.getenv("TEST_NEW_USER_EMAIL", "testnewuser@yopmail.com")
    _get_newuser_page(context).fill_email_and_click_create(email)


@then("user enters otp and clicks on submit button")
def user_enters_otp_and_submits(context):
    """Enter the OTP received on the registered email and click Submit.

    Set the TEST_OTP environment variable to the OTP value before running.
    """
    otp = os.getenv("TEST_OTP", "")
    if not otp:
        print("WARNING: TEST_OTP env var is not set. OTP field will be empty.")
    _get_newuser_page(context).enter_otp_and_submit(otp)


@then("user fills the password and clicks on confirm password button")
def user_fills_password_and_confirms(context):
    """Fill new password, confirm password, accept terms checkbox, and click Confirm Password."""
    password = os.getenv("TEST_NEW_USER_PASSWORD", "Test@123")
    _get_newuser_page(context).fill_password_and_confirm(password)


@then("user fills all the details in the registration form and clicks on submit button")
def user_fills_registration_form_and_submits(context):
    """Fill first name, last name, country, city, phone, profile type and submit."""
    _get_newuser_page(context).fill_registration_form_and_submit(
        first_name=os.getenv("TEST_FIRST_NAME", "Test"),
        last_name=os.getenv("TEST_LAST_NAME", "User"),
        phone_number=os.getenv("TEST_PHONE_NUMBER", "9876543210"),
    )


@then("user login to home page and clicks on profile icon and logout from the application")
def user_validates_home_and_logs_out(context):
    """Validate that the home page is displayed, click the profile icon, and logout."""
    _get_newuser_page(context).validate_home_click_profile_and_logout()
