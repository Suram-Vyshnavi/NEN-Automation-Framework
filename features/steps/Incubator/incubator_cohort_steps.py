from behave import then

from pages.Incubator.cohort_home_page import IncubatorCohortHomePage
from pages.common.navigation_page import NavigationPage
from utils.helpers import attach_screenshot


def _get_incubator_page(context):
    if not hasattr(context, "incubator_cohort_home_page"):
        context.incubator_cohort_home_page = IncubatorCohortHomePage(context.page)
    return context.incubator_cohort_home_page


@then("incubator user clicks on cohorts tab")
def step_incubator_user_clicks_on_cohorts_tab(context):
    page = _get_incubator_page(context)
    page.click_cohorts_tab()
    attach_screenshot(context.page, name="Incubator cohorts tab clicked", context=context)


@then("incubator user validates cohorts heading")
def step_incubator_user_validates_cohorts_heading(context):
    page = _get_incubator_page(context)
    page.validate_cohorts_heading()
    attach_screenshot(context.page, name="Incubator cohorts heading validated", context=context)


@then("incubator user clicks on active tab")
def step_incubator_user_clicks_on_active_tab(context):
    page = _get_incubator_page(context)
    page.click_active_tab()
    attach_screenshot(context.page, name="Incubator active tab clicked", context=context)


@then("incubator user clicks on 1 active cohort")
def step_incubator_user_clicks_on_first_active_cohort(context):
    page = _get_incubator_page(context)
    page.click_first_active_cohort()
    attach_screenshot(context.page, name="Incubator first active cohort clicked", context=context)


@then("incubator user validates all the tabs in cohort page")
def step_incubator_user_validates_all_tabs_in_cohort_page(context):
    page = _get_incubator_page(context)
    page.validate_all_tabs_in_cohort_page()
    attach_screenshot(context.page, name="Incubator cohort tabs validated", context=context)


@then("incubator user clicks on general info tab")
def step_incubator_user_clicks_on_general_info_tab(context):
    page = _get_incubator_page(context)
    page.click_general_info_tab()
    attach_screenshot(context.page, name="Incubator general info tab clicked", context=context)


@then("incubator user validates batch faculty and message icon in general info tab")
def step_incubator_user_validates_batch_faculty_and_message_icon(context):
    page = _get_incubator_page(context)
    page.validate_batch_faculty_and_message_icon()
    attach_screenshot(context.page, name="Incubator batch faculty/message icon validated", context=context)


@then("incubator user validates cohort Activity")
@then("incubator user validates download excel in cohort dashboard")
def step_incubator_user_validates_download_excel_in_cohort_dashboard(context):
    page = _get_incubator_page(context)
    page.validate_download_excel_in_cohort_dashboard()
    attach_screenshot(context.page, name="Incubator download excel validated", context=context)


@then("incubator user clicks on cohorts members tab")
def step_incubator_user_clicks_on_cohorts_members_tab(context):
    page = _get_incubator_page(context)
    page.click_cohort_members_tab()
    attach_screenshot(context.page, name="Incubator cohort members tab clicked", context=context)


@then("incubator user validates cohort members heading")
def step_incubator_user_validates_cohort_members_heading(context):
    page = _get_incubator_page(context)
    page.validate_cohort_members_heading()
    attach_screenshot(context.page, name="Incubator cohort members heading validated", context=context)


@then("incubator user validates student added and maximum allowed students details")
def step_incubator_user_validates_student_and_maximum_allowed_students_details(context):
    page = _get_incubator_page(context)
    page.validate_student_added_and_max_allowed_students_details()
    attach_screenshot(context.page, name="Incubator students details validated", context=context)


@then("incubator user clicks on cohort startups")
def step_incubator_user_clicks_on_cohort_startups(context):
    page = _get_incubator_page(context)
    page.click_cohort_startups()
    attach_screenshot(context.page, name="Incubator cohort startups tab clicked", context=context)


@then("incubator user validates cohort startups heading and startup details")
def step_incubator_user_validates_cohort_startups_heading_and_details(context):
    page = _get_incubator_page(context)
    page.validate_cohort_startups_heading_and_startup_details()
    attach_screenshot(context.page, name="Incubator cohort startups details validated", context=context)


@then("incubator user clicks on 1 cohort startup")
def step_incubator_user_clicks_on_first_cohort_startup(context):
    page = _get_incubator_page(context)
    page.click_first_cohort_startup()
    attach_screenshot(context.page, name="Incubator first cohort startup clicked", context=context)


@then("incubator user search for test cohort in cohorts")
def step_incubator_user_search_for_test_cohort_in_cohorts(context):
    page = _get_incubator_page(context)
    page.search_for_test_cohort_in_cohorts()
    attach_screenshot(context.page, name="Incubator search cohort completed", context=context)


@then("incubator user clicks on inactive tab")
def step_incubator_user_clicks_on_inactive_tab(context):
    page = _get_incubator_page(context)
    page.click_inactive_tab()
    attach_screenshot(context.page, name="Incubator inactive tab clicked", context=context)


@then("incubator user clicks on create new cohort button")
def step_incubator_user_clicks_on_create_new_cohort_button(context):
    page = _get_incubator_page(context)
    page.click_create_new_cohort_button()
    attach_screenshot(context.page, name="Incubator create new cohort clicked", context=context)


@then("incubator user fills all the details and create new cohort")
def step_incubator_user_fills_all_the_details_and_create_new_cohort(context):
    page = _get_incubator_page(context)
    page.fill_all_details_and_create_cohort()
    attach_screenshot(context.page, name="Incubator new cohort created", context=context)


@then("incubator user validates office hours section in cohort page")
def step_incubator_user_validates_office_hours_section_in_cohort_page(context):
    page = _get_incubator_page(context)
    page.validate_office_hours_section_in_cohort_page()
    attach_screenshot(context.page, name="Incubator office hours validated", context=context)


@then("incubator user clicks on create button")
def step_incubator_user_clicks_on_create_button(context):
    page = _get_incubator_page(context)
    page.click_create_button()
    attach_screenshot(context.page, name="Incubator office hours create clicked", context=context)


@then("incubator user fills all the details and create a meeting")
def step_incubator_user_fills_all_details_and_create_a_meeting(context):
    page = _get_incubator_page(context)
    page.fill_all_details_and_create_meeting()
    attach_screenshot(context.page, name="Incubator meeting created", context=context)


@then("incubator user deletes the created meeting")
def step_incubator_user_deletes_the_created_meeting(context):
    page = _get_incubator_page(context)
    page.delete_created_meeting()
    attach_screenshot(context.page, name="Incubator meeting deleted", context=context)


@then("incubator user navigates to home page")
def step_incubator_user_navigates_to_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.navigate_to_home_page()
    attach_screenshot(context.page, name="Incubator navigated to home page", context=context)