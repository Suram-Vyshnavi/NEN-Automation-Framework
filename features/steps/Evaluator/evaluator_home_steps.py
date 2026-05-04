from behave import given, then, when

from pages.Evaluator.evaluator_home_page import EvaluatorHomePage
from pages.common.navigation_page import NavigationPage
from utils.helpers import attach_screenshot


def _get_evaluator_home_page(context):
    if not hasattr(context, "evaluator_home_page"):
        context.evaluator_home_page = EvaluatorHomePage(context.page)
    return context.evaluator_home_page


@given("evaluator user is on the home page")
def step_evaluator_user_on_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.handle_all_popups()

    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_home_page_card()
    attach_screenshot(context.page, name="Evaluator home page validated", context=context, force=True)


@then("evaluator user validates the home page card")
def step_evaluator_validates_home_page_card(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_home_page_card()
    attach_screenshot(context.page, name="Evaluator home page card validated", context=context, force=True)

@then("evaluator user validates the resources heading")
def step_evaluator_validates_resources_heading(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_resources_heading()
    attach_screenshot(context.page, name="Evaluator resources heading validated", context=context, force=True)



@when("evaluator user clicks on Evaluate button in the home page card")
def step_evaluator_clicks_evaluate_button(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.click_evaluate_button()
    attach_screenshot(context.page, name="Evaluator evaluate button clicked", context=context, force=True)


@then("evaluator user validates the venture information card")
def step_evaluator_validates_venture_info_card(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_venture_information_card()
    attach_screenshot(context.page, name="Evaluator venture information card validated", context=context, force=True)


@then("evaluator user validates the Submissions & Evaluation heading")
def step_evaluator_validates_submissions_and_evaluation_heading(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_submissions_evaluation_heading()
    attach_screenshot(context.page, name="Evaluator submissions and evaluation heading validated", context=context, force=True)


@then("evaluator user validates the Instructions heading")
def step_evaluator_validates_instructions_heading(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_instructions_heading()
    attach_screenshot(context.page, name="Evaluator instructions heading validated", context=context, force=True)


@then("evaluator user validates the Milestone heading")
def step_evaluator_validates_milestone_heading(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_milestone_heading()
    attach_screenshot(context.page, name="Evaluator milestone heading validated", context=context, force=True)


@then("evaluator user validates the Viability Evaluation heading")
def step_evaluator_validates_viability_evaluation_heading(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.validate_viability_evaluation_heading()
    attach_screenshot(context.page, name="Evaluator viability evaluation heading validated", context=context, force=True)


@then("evaluator user navigates to home page")
def step_evaluator_navigates_to_home_page(context):
    evaluator_page = _get_evaluator_home_page(context)
    evaluator_page.navigate_to_home_page()
    attach_screenshot(context.page, name="Evaluator navigated to home page", context=context, force=True)
