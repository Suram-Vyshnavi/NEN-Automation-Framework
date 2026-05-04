from behave import then
from pages.RM.rm_cohorts_page import RMCohortsPage


@then("RM user clicks on cohorts tab")
def step_rm_user_clicks_on_cohorts_tab(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_cohorts_tab()


@then("RM user validates direct cohorts heading")
def step_rm_user_validates_direct_cohorts_heading(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_direct_cohorts_heading()


@then("RM user validates status heading")
def step_rm_user_validates_status_heading(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_status_heading()


@then("RM user clicks on active tab")
def step_rm_user_clicks_on_active_tab(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_active_tab()


@then("RM user clicks on 1 active cohort")
def step_rm_user_clicks_on_1_active_cohort(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_first_active_cohort()


@then("RM user validates all the tabs in cohort page")
def step_rm_user_validates_all_tabs_in_cohort_page(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_all_tabs_in_cohort_page()


@then("RM user clicks on inactive tab")
def step_rm_user_clicks_on_inactive_tab(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_inactive_tab()


@then("RM user search for test cohort")
def step_rm_user_search_for_test_cohort(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.search_for_test_cohort()


@then("RM user validates incubator cohorts heading")
def step_rm_user_validates_incubator_cohorts_heading(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_incubator_cohorts_heading()


@then("RM user validates incubator status heading")
def step_rm_user_validates_incubator_status_heading(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_incubator_status_heading()


@then("RM user clicks on incubator active tab")
def step_rm_user_clicks_on_incubator_active_tab(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_incubator_active_tab()


@then("RM user clicks on incubator 1 active cohort")
def step_rm_user_clicks_on_incubator_1_active_cohort(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.click_on_incubator_first_active_cohort()


@then("RM user validates incubator all the tabs in cohort page")
def step_rm_user_validates_incubator_all_tabs_in_cohort_page(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_incubator_all_tabs_in_cohort_page()


@then("RM user validates incubator pagination")
def step_rm_user_validates_incubator_pagination(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.validate_incubator_pagination()


@then("RM user search for test cohort in incubator cohorts")
def step_rm_user_search_for_test_cohort_in_incubator_cohorts(context):
    rm_cohorts_page = RMCohortsPage(context.page)
    rm_cohorts_page.search_for_test_cohort_in_incubator()
