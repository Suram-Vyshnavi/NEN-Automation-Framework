from behave import then, when

from pages.Evaluator.evaluator_venture_page import EvaluatorVenturePage
from utils.helpers import attach_screenshot


def _get_evaluator_venture_page(context):
    if not hasattr(context, "evaluator_venture_page"):
        context.evaluator_venture_page = EvaluatorVenturePage(context.page)
    return context.evaluator_venture_page


@then("evaluator user clicks on ventures tab in the home page")
def step_evaluator_clicks_ventures_tab(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.click_ventures_tab()
    attach_screenshot(context.page, name="Evaluator ventures tab clicked", context=context, force=True)


@then("evaluator user validates the all ventures heading")
def step_evaluator_validates_all_ventures_heading(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_all_ventures_heading()
    attach_screenshot(context.page, name="Evaluator all ventures heading validated", context=context, force=True)


@then("evaluator user validates pending ventures heading")
def step_evaluator_validates_pending_ventures_heading(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_pending_ventures_heading()
    attach_screenshot(context.page, name="Evaluator pending ventures heading validated", context=context, force=True)


@when("evaluator user clicks on Evaluate button in the pending ventures section")
def step_evaluator_clicks_evaluate_button_in_pending_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.click_evaluate_button_in_pending_ventures()
    attach_screenshot(context.page, name="Evaluator pending venture evaluate clicked", context=context, force=True)


@then("evaluator user validates the venture information card in venture section")
def step_evaluator_validates_venture_information_card_in_venture_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_venture_information_card()
    attach_screenshot(context.page, name="Evaluator venture information card validated in venture section", context=context, force=True)


@then("evaluator user validates the venture name in venture information card")
def step_evaluator_validates_venture_name_in_information_card(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_venture_name_in_information_card()
    attach_screenshot(context.page, name="Evaluator venture name validated", context=context, force=True)


@then("evaluator user validates the Submissions & Evaluation heading in venture section")
def step_evaluator_validates_submissions_heading_in_venture_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_submissions_evaluation_heading()
    attach_screenshot(context.page, name="Evaluator submissions heading validated in venture section", context=context, force=True)


@then("evaluator user validates the Instructions heading in venture section")
def step_evaluator_validates_instructions_heading_in_venture_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_instructions_heading()
    attach_screenshot(context.page, name="Evaluator instructions heading validated in venture section", context=context, force=True)


@then("evaluator user validates the Milestone heading in venture section")
def step_evaluator_validates_milestone_heading_in_venture_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_milestone_heading()
    attach_screenshot(context.page, name="Evaluator milestone heading validated in venture section", context=context, force=True)


@then("evaluator user validates the Viability Evaluation heading in venture section")
def step_evaluator_validates_viability_heading_in_venture_section(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.validate_viability_evaluation_heading()
    attach_screenshot(context.page, name="Evaluator viability heading validated in venture section", context=context, force=True)


@then("evaluator user clicks on the Completed Evaluations heading")
def step_evaluator_clicks_completed_evaluations_heading(context):
    evaluator_page = _get_evaluator_venture_page(context)
    evaluator_page.click_completed_evaluations()
    attach_screenshot(context.page, name="Evaluator completed evaluations heading clicked", context=context, force=True)