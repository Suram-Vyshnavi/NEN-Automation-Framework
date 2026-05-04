from behave import then, when

from pages.Mentor.mentor_home_page import MentorHomePage
from utils.helpers import attach_screenshot


def _get_mentor_home_page(context):
    if not hasattr(context, "mentor_home_page"):
        context.mentor_home_page = MentorHomePage(context.page)
    return context.mentor_home_page


@then("mentor user validates the home page heading")
def step_mentor_validates_home_page_heading(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_home_page_heading()
    attach_screenshot(context.page, name="Mentor home page heading validated", context=context, force=True)


@then("mentor user validates the meetings heading")
def step_mentor_validates_meetings_heading(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_meetings_heading()
    attach_screenshot(context.page, name="Mentor meetings heading validated", context=context, force=True)


@then("mentor user validates the upcoming meetings section")
def step_mentor_validates_upcoming_meetings_section(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_upcoming_meetings_section()
    attach_screenshot(context.page, name="Mentor upcoming meetings section validated", context=context, force=True)


@then("mentor user validates the pending requests section")
def step_mentor_validates_pending_requests_section(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_pending_requests_section()
    attach_screenshot(context.page, name="Mentor pending requests section validated", context=context, force=True)


@then("mentor user validates the history section")
def step_mentor_validates_history_section(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_history_section()
    attach_screenshot(context.page, name="Mentor history section validated", context=context, force=True)


@then("mentor user validates the declined section")
def step_mentor_validates_declined_section(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_declined_section()
    attach_screenshot(context.page, name="Mentor declined section validated", context=context, force=True)


@when("mentor user clicks on My Availability menu")
def step_mentor_clicks_my_availability_menu(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.click_my_availability_menu()
    attach_screenshot(context.page, name="Mentor My Availability menu clicked", context=context, force=True)


@then("mentor user validates the weekly schedule section")
def step_mentor_validates_weekly_schedule_section(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.validate_weekly_schedule_section()
    attach_screenshot(context.page, name="Mentor weekly schedule section validated", context=context, force=True)


@when("mentor user selects the first checkbox in the weekly schedule")
def step_mentor_selects_first_checkbox_weekly_schedule(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.select_first_checkbox_in_weekly_schedule()
    attach_screenshot(context.page, name="Mentor first weekly schedule checkbox selected", context=context, force=True)


@when("mentor user fills the weekly schedule form")
def step_mentor_fills_weekly_schedule_form(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.fill_weekly_schedule_form()
    attach_screenshot(context.page, name="Mentor weekly schedule form filled", context=context, force=True)


@when("mentor user clicks on Add Override button")
def step_mentor_clicks_add_override_button(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.click_add_override_button()
    attach_screenshot(context.page, name="Mentor add override button clicked", context=context, force=True)


@when("mentor user adds a date override")
def step_mentor_adds_date_override(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.add_date_override()
    attach_screenshot(context.page, name="Mentor date override added", context=context, force=True)


@when("mentor user deletes the added override")
def step_mentor_deletes_added_override(context):
    mentor_page = _get_mentor_home_page(context)
    mentor_page.delete_added_override()
    attach_screenshot(context.page, name="Mentor added override deleted", context=context, force=True)
