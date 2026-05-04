from behave import given, when, then
from pages.RM.rm_home_page import RMHomePage


@given("RM user is on home page")
def step_rm_user_is_on_home_page(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.navigate_to_home()


@then("RM user validates cohorts heading")
def step_rm_user_validates_cohorts_heading(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.validate_cohorts_heading()


@then("RM user clicks first active cohort")
def step_rm_user_clicks_first_active_cohort(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.click_first_active_cohort()


@then("RM user validates tabs")
def step_rm_user_validates_tabs(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.validate_all_tabs_in_cohort_page()


@then("user clicks on release milestones tab")
def step_user_clicks_on_release_milestones_tab(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.click_release_milestones_tab()


@then("user clicks on milestone and extends deadline")
def step_user_clicks_on_milestone_and_extends_deadline(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.click_milestone_and_extend_deadline()


@then("user clicks on refresh button")
def step_user_clicks_on_refresh_button(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.click_refresh_button()


@then("RM user validates pagination")
def step_rm_user_validates_pagination(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.validate_pagination()


@then("RM user navigates to home page")
def step_rm_user_navigates_to_home_page(context):
    rm_home_page = RMHomePage(context.page)
    rm_home_page.navigate_to_home()
