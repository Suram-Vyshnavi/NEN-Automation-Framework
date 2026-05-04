from behave import given, then, when

from pages.ViabilitySpecialist.viability_home_page import ViabilityHomePage
from pages.common.navigation_page import NavigationPage
from utils.helpers import attach_screenshot


def _get_viability_home_page(context):
    if not hasattr(context, "viability_home_page"):
        context.viability_home_page = ViabilityHomePage(context.page)
    return context.viability_home_page


@given("Viability Specialist user is on the home page")
def step_viability_user_on_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.handle_all_popups()

    page = _get_viability_home_page(context)
    page.validate_home_page_card()
    attach_screenshot(context.page, name="Viability Specialist home page validated", context=context, force=True)


@then("Viability Specialist user validates the home page card")
def step_viability_validates_home_page_card(context):
    page = _get_viability_home_page(context)
    page.validate_home_page_card()
    attach_screenshot(context.page, name="Viability home page card validated", context=context, force=True)


@then("Viability Specialist user validates the resource heading")
def step_viability_validates_resource_heading(context):
    page = _get_viability_home_page(context)
    page.validate_resource_heading()
    attach_screenshot(context.page, name="Viability resource heading validated", context=context, force=True)


@when("Viability Specialist user clicks on Evaluate button in the home page")
def step_viability_clicks_evaluate_button(context):
    page = _get_viability_home_page(context)
    page.click_evaluate_button()
    attach_screenshot(context.page, name="Viability evaluate button clicked", context=context, force=True)


@then("Viability Specialist user validates the venture information card")
def step_viability_validates_venture_information_card(context):
    page = _get_viability_home_page(context)
    page.validate_venture_information_card()
    attach_screenshot(context.page, name="Viability venture information card validated", context=context, force=True)


@then("Viability Specialist user validates the Submissions & Evaluation heading")
def step_viability_validates_submissions_evaluation_heading(context):
    page = _get_viability_home_page(context)
    page.validate_submissions_evaluation_heading()
    attach_screenshot(context.page, name="Viability submissions evaluation heading validated", context=context, force=True)


@then("Viability Specialist user validates the Instructions heading")
def step_viability_validates_instructions_heading(context):
    page = _get_viability_home_page(context)
    page.validate_instructions_heading()
    attach_screenshot(context.page, name="Viability instructions heading validated", context=context, force=True)


@then("Viability Specialist user validates the View file link")
def step_viability_validates_view_file_link(context):
    page = _get_viability_home_page(context)
    page.validate_view_file_link()
    attach_screenshot(context.page, name="Viability view file link validated", context=context, force=True)


@then("Viability Specialist user validates the Evaluate heading")
def step_viability_validates_evaluate_heading(context):
    page = _get_viability_home_page(context)
    page.validate_evaluate_heading()
    attach_screenshot(context.page, name="Viability evaluate heading validated", context=context, force=True)


@then("Viability Specialist user validates the My Ratings heading")
def step_viability_validates_my_ratings_heading(context):
    page = _get_viability_home_page(context)
    page.validate_my_ratings_heading()
    attach_screenshot(context.page, name="Viability my ratings heading validated", context=context, force=True)


@then("Viability Specialist user validates the Milestone form section")
def step_viability_validates_milestone_form_section(context):
    page = _get_viability_home_page(context)
    page.validate_milestone_form_section()
    attach_screenshot(context.page, name="Viability milestone form section validated", context=context, force=True)


@then("Viability Specialist user validates the Milestone next form section")
def step_viability_validates_milestone_next_form_section(context):
    page = _get_viability_home_page(context)
    page.validate_milestone_next_form_section()
    attach_screenshot(context.page, name="Viability milestone next form section validated", context=context, force=True)


@then("Viability Specialist user navigates to home page")
def step_viability_navigates_to_home_page(context):
    page = _get_viability_home_page(context)
    page.navigate_to_home_page()
    attach_screenshot(context.page, name="Viability navigated to home page", context=context, force=True)
