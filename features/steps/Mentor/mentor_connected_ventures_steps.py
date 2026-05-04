from behave import given, then, when

from pages.Mentor.connected_ventures_page import MentorConnectedVenturesPage
from pages.common.navigation_page import NavigationPage
from utils.helpers import attach_screenshot


def _get_mentor_connected_ventures_page(context):
    if not hasattr(context, "mentor_connected_ventures_page"):
        context.mentor_connected_ventures_page = MentorConnectedVenturesPage(context.page)
    return context.mentor_connected_ventures_page


@given("mentor user is on the home page")
def step_mentor_user_on_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.handle_all_popups()

    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.validate_mentor_home_page()
    attach_screenshot(context.page, name="Mentor home page validated", context=context, force=True)


@when("mentor user clicks on the Connected Ventures menu")
def step_mentor_click_connected_ventures_tab(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.click_connected_ventures_tab()
    attach_screenshot(context.page, name="Mentor connected ventures menu clicked", context=context, force=True)


@when("mentor user should validate first card in connected venture")
@then("mentor user should validate first card in connected venture")
def step_mentor_validate_first_connected_venture(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.validate_first_connected_venture()
    attach_screenshot(context.page, name="Mentor first card in connected venture validated", context=context, force=True)


@when("mentor user clicks on the Book Session button")
def step_mentor_click_book_session_button(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.click_book_session_button()
    attach_screenshot(context.page, name="Mentor book session clicked", context=context, force=True)


@when("mentor user fills all the required details")
def step_mentor_fill_required_details(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.fill_required_meeting_details()
    attach_screenshot(context.page, name="Mentor required meeting details filled", context=context, force=True)


@when("mentor user creates a meeting")
def step_mentor_create_meeting(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.create_meeting()
    attach_screenshot(context.page, name="Mentor meeting created", context=context, force=True)


@when("mentor user clicks on the Chat button in the connected venture details page")
def step_mentor_click_chat_button(context):
    mentor_page = _get_mentor_connected_ventures_page(context)
    mentor_page.click_chat_button_in_venture_details_page()
    attach_screenshot(context.page, name="Mentor chat button clicked", context=context, force=True)


@then("mentor user navigates back to the home page")
def step_mentor_navigate_back_home(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.navigate_to_home_page()
    attach_screenshot(context.page, name="Mentor navigated back to home page", context=context, force=True)
