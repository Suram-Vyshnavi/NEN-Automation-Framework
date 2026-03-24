from behave import given, then
from pages.Faculty.faculty_home_cohort_page import FacultyHomeCohortPage


@then("user validates cohorts heading")
def validate_cohorts_heading(context):
    """Validate that the Cohorts heading is visible"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.validate_cohorts_heading()


@then("user clicks on active tab")
def click_active_tab(context):
    """Click on the Active tab in Cohorts section"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.click_active_tab()


@then("user clicks on 1 active cohort")
def click_first_active_cohort(context):
    """Click on the first active cohort"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.click_first_active_cohort()


@then("user validates all the tabs in cohort page")
def validate_all_tabs_in_cohort_page(context):
    """Validate all tabs in the cohort dashboard page"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.validate_all_tabs_in_cohort_page()


@then("user validates pagination")
def validate_pagination(context):
    """Validate pagination is working"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.validate_pagination()


@then("user clicks on inactive tab")
def click_inactive_tab(context):
    """Navigate back to home and click on Inactive tab"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.click_inactive_tab()


@then("user search for test cohort")
def search_for_test_cohort(context):
    """Search for a test cohort"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.search_for_test_cohort()


@then("user clicks on create new cohort button")
def click_create_new_cohort_button(context):
    """Click on the Create New Cohort button"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.click_create_new_cohort_button()


@then("user fills all the details and create new cohort")
def fill_all_details_and_create_cohort(context):
    """Fill all required form fields and create the new cohort"""
    if not hasattr(context, 'faculty_home_cohort_page'):
        context.faculty_home_cohort_page = FacultyHomeCohortPage(context.page)
    context.faculty_home_cohort_page.fill_all_details_and_create_cohort()
