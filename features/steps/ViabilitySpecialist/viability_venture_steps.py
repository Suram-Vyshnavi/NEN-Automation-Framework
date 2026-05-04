from behave import then, when

from pages.ViabilitySpecialist.viability_venture_page import ViabilityVenturePage
from utils.helpers import attach_screenshot


def _get_viability_venture_page(context):
    if not hasattr(context, "viability_venture_page"):
        context.viability_venture_page = ViabilityVenturePage(context.page)
    return context.viability_venture_page


@then("Viability Specialist user clicks on ventures tab in the home page")
def step_viability_clicks_ventures_tab(context):
    page = _get_viability_venture_page(context)
    page.click_ventures_tab()
    attach_screenshot(context.page, name="Viability ventures tab clicked", context=context, force=True)


@then("Viability Specialist user validates the all ventures heading")
def step_viability_validates_all_ventures_heading(context):
    page = _get_viability_venture_page(context)
    page.validate_all_ventures_heading()
    attach_screenshot(context.page, name="Viability all ventures heading validated", context=context, force=True)


@then("Viability Specialist user validates pending ventures heading")
def step_viability_validates_pending_ventures_heading(context):
    page = _get_viability_venture_page(context)
    page.validate_pending_ventures_heading()
    attach_screenshot(context.page, name="Viability pending ventures heading validated", context=context, force=True)


@when("Viability Specialist user clicks on Evaluate button in the pending ventures section")
def step_viability_clicks_evaluate_button_in_pending_section(context):
    page = _get_viability_venture_page(context)
    page.click_evaluate_button_in_pending_ventures()
    attach_screenshot(context.page, name="Viability evaluate button in pending ventures clicked", context=context, force=True)


@then("Viability Specialist user validates the venture information card in venture section")
def step_viability_validates_venture_information_card_in_venture_section(context):
    page = _get_viability_venture_page(context)
    page.validate_venture_information_card()
    attach_screenshot(context.page, name="Viability venture information card validated in venture section", context=context, force=True)


@then("Viability Specialist user validates the venture name in venture information card")
def step_viability_validates_venture_name_in_information_card(context):
    page = _get_viability_venture_page(context)
    page.validate_venture_name_in_information_card()
    attach_screenshot(context.page, name="Viability venture name validated", context=context, force=True)


@then("Viability Specialist user validates the Submissions & Evaluation heading in venture section")
def step_viability_validates_submissions_heading_in_venture_section(context):
    page = _get_viability_venture_page(context)
    page.validate_submissions_evaluation_heading()
    attach_screenshot(context.page, name="Viability submissions heading validated in venture section", context=context, force=True)


@then("Viability Specialist user validates the Instructions heading in venture section")
def step_viability_validates_instructions_heading_in_venture_section(context):
    page = _get_viability_venture_page(context)
    page.validate_instructions_heading()
    attach_screenshot(context.page, name="Viability instructions heading validated in venture section", context=context, force=True)


@then("Viability Specialist user validates the Evaluate heading in venture section")
def step_viability_validates_evaluate_heading_in_venture_section(context):
    page = _get_viability_venture_page(context)
    page.validate_evaluate_heading()
    attach_screenshot(context.page, name="Viability evaluate heading validated in venture section", context=context, force=True)


@then("Viability Specialist user validates the My Ratings heading in venture section")
def step_viability_validates_my_ratings_heading_in_venture_section(context):
    page = _get_viability_venture_page(context)
    page.validate_my_ratings_heading()
    attach_screenshot(context.page, name="Viability my ratings heading validated in venture section", context=context, force=True)


@then("Viability Specialist user clicks on the Completed Evaluations heading")
def step_viability_clicks_completed_evaluations_heading(context):
    page = _get_viability_venture_page(context)
    page.click_completed_evaluations()
    attach_screenshot(context.page, name="Viability completed evaluations heading clicked", context=context, force=True)


@then("Viability Specialist validates the first card in completed evaluations section")
def step_viability_validates_first_card_in_completed_evaluations(context):
    page = _get_viability_venture_page(context)
    page.validate_first_card_in_completed_evaluations()
    attach_screenshot(context.page, name="Viability first completed evaluations card validated", context=context, force=True)




