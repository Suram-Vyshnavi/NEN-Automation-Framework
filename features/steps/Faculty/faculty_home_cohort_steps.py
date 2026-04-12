from behave import given, then
from pages.Faculty.faculty_home_cohort_page import FacultyHomeCohortPage
from utils.helpers import attach_screenshot


def _get_home_cohort_page(context):
    if not hasattr(context, "faculty_home_cohort_page"):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    return context.faculty_home_cohort_page


@then("user validates cohorts heading")
def validate_cohorts_heading(context):
    """Validate that the Cohorts heading is visible"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.validate_cohorts_heading()
    attach_screenshot(context.page, name="Cohorts heading validated", context=context)


@then("user clicks on active tab")
def click_active_tab(context):
    """Click on the Active tab in Cohorts section"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.click_active_tab()
    attach_screenshot(context.page, name="Active tab clicked", context=context)


@then("user clicks on 1 active cohort")
def click_first_active_cohort(context):
    """Click on the first active cohort"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.click_first_active_cohort()
    attach_screenshot(context.page, name="First active cohort clicked", context=context)


@then("user validates all the tabs in cohort page")
def validate_all_tabs_in_cohort_page(context):
    """Validate all tabs in the cohort dashboard page"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.validate_all_tabs_in_cohort_page()
    attach_screenshot(context.page, name="All cohort tabs validated", context=context)


@then("user validates pagination")
def validate_pagination(context):
    """Validate pagination is working"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.validate_pagination()
    attach_screenshot(context.page, name="Pagination validated", context=context)


@then("user clicks on inactive tab")
def click_inactive_tab(context):
    """Navigate back to home and click on Inactive tab"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.click_inactive_tab()
    attach_screenshot(context.page, name="Inactive tab clicked", context=context)


@then("user search for test cohort")
def search_for_test_cohort(context):
    """Search for a test cohort"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.search_for_test_cohort()
    attach_screenshot(context.page, name="Test cohort searched", context=context)


@then("user clicks on create new cohort button")
def click_create_new_cohort_button(context):
    """Click on the Create New Cohort button"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.click_create_new_cohort_button()
    attach_screenshot(context.page, name="Create new cohort button clicked", context=context)


@then("user fills all the details and create new cohort")
def fill_all_details_and_create_cohort(context):
    """Fill all required form fields and create the new cohort"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.fill_all_details_and_create_cohort()
    attach_screenshot(context.page, name="New cohort created", context=context)

@then("user clicks on latest created cohort and closes the cohort")
def click_latest_created_cohort_and_close(context):
    """Click on the latest created cohort and close it"""
    home_cohort_page = _get_home_cohort_page(context)
    home_cohort_page.click_latest_created_cohort_and_close()
    attach_screenshot(context.page, name="Latest created cohort closed", context=context)
