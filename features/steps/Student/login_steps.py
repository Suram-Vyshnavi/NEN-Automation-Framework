from behave import given, then
from pages.Student.login_page import LoginPage
from utils.config import Config


@given("user is already logged in")
def user_already_logged_in(context):
    """User is already logged in from before_all hook"""
    # This step doesn't need to do anything as login is done in before_all
    pass


@then("user performs some action")
def perform_some_action(context):
    """Placeholder for actions that need to be performed after login"""
    # Add your test actions here
    from utils.helpers import attach_screenshot
    attach_screenshot(context.page, "Performing Test Action While Logged In")
    pass


@then("user clicks on login")
def click_login_button(context):
    """Click on the Login button"""
    if not hasattr(context, 'login_page'):
        context.login_page = LoginPage(context.page)
    context.login_page.click_login_button()


@then("user enters valid credentials")
def enter_valid_credentials(context):
    """Enter valid email and password credentials"""
    if not hasattr(context, 'login_page'):
        context.login_page = LoginPage(context.page)
    context.login_page.enter_credentials(Config.USERNAME, Config.PASSWORD)


@then("user clicks on sign in button")
def click_sign_in(context):
    """Click on the Sign In button"""
    context.login_page.click_sign_in_button()


@then("user handles no thanks popup if it appears")
def handle_no_thanks_popup(context):
    """Handle all 4 popups after login"""
    context.login_page.handle_all_popups()


@then("user handles all login popups")
def handle_all_login_popups(context):
    """Handle all login popups in sequence"""
    context.login_page.handle_all_popups()


@then("user validates successful login")
def validate_login_success(context):
    """Validate that the login was successful"""
    context.login_page.validate_successful_login()
