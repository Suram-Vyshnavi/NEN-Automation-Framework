from behave import given, then
from pages.Student.guest_page import GuestPage
from utils.config import Config


@given("user is on guest page")
def navigate_to_guest_page(context):
    """Navigate to the guest page"""
    guest_page = GuestPage(context.page)
    guest_page.navigate_to_guest_page(Config.BASE_URL)
    context.guest_page = guest_page


@then("User clicks on explore")
def click_explore_button(context):
    """Click on the Explore button"""
    context.guest_page.click_explore()


@then("user Validates ignite and liftoff")
def validate_ignite_liftoff(context):
    """Validate Ignite and Liftoff sections"""
    context.guest_page.validate_ignite_and_liftoff()


@then("user validates footer section")
def validate_footer(context):
    """Validate footer section elements"""
    context.guest_page.validate_footer_section()


@then("user clicks on programs")
def click_programs_menu(context):
    """Click on Programs menu"""
    context.guest_page.click_programs()


@then("user clicks on ignite")
def click_ignite_option(context):
    """Click on Ignite option"""
    context.guest_page.click_ignite()


@then("user validates cohort section and enroll now button")
def validate_cohort_section(context):
    """Validate Cohort section and Enroll Now button"""
    context.guest_page.validate_cohort_section_and_enroll_button()


@then("user clicks on liftoff")
def click_liftoff_option(context):
    """Click on Liftoff option"""
    context.guest_page.click_liftoff()


@then("user validates ready to lift off and start Now button")
def validate_ready_to_liftoff(context):
    """Validate Ready to Liftoff section and Start Now button"""
    context.guest_page.validate_ready_to_liftoff_and_start_now_button()


