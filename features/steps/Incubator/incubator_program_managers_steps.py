from behave import then, when

from pages.Incubator.program_managers_page import IncubatorProgramManagersPage
from utils.helpers import attach_screenshot


def _get_program_managers_page(context):
    if not hasattr(context, "incubator_program_managers_page"):
        context.incubator_program_managers_page = IncubatorProgramManagersPage(context.page)
    return context.incubator_program_managers_page


@when("the user clicks on the profile icon")
def step_user_clicks_profile_icon(context):
    page = _get_program_managers_page(context)
    page.click_profile_icon()
    attach_screenshot(context.page, name="Program managers profile icon clicked", context=context)


@when("the user clicks on the program managers tab")
def step_user_clicks_program_managers_tab(context):
    page = _get_program_managers_page(context)
    page.click_program_managers_tab()
    attach_screenshot(context.page, name="Program managers tab clicked", context=context)


@then('the user should see the "{heading}" heading')
def step_user_should_see_heading(context, heading):
    page = _get_program_managers_page(context)
    page.validate_program_managers_heading(heading)
    attach_screenshot(context.page, name="Program managers heading validated", context=context)


@when("the user clicks on the add program manager button")
def step_user_clicks_add_program_manager_button(context):
    page = _get_program_managers_page(context)
    page.click_add_program_manager_button()
    attach_screenshot(context.page, name="Add program manager clicked", context=context)


@when("the user fills all the required details and clicks on create button")
def step_user_fills_required_details_and_creates(context):
    page = _get_program_managers_page(context)
    page.fill_required_details_and_click_create()
    attach_screenshot(context.page, name="Program manager created", context=context)

# NOTE: "Then incubator user navigates to home page" is already defined in incubator_cohort_steps.py
