from behave import given, then

from pages.CohortManager.cohort_manager_home_page import CohortManagerHomePage
from pages.common.navigation_page import NavigationPage
from utils.helpers import attach_screenshot


def _get_cohort_manager_page(context):
    if not hasattr(context, "cohort_manager_home_page"):
        context.cohort_manager_home_page = CohortManagerHomePage(context.page)
    return context.cohort_manager_home_page


@given("user is on the homepage")
def step_user_is_on_the_homepage(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.handle_all_popups()

    page = _get_cohort_manager_page(context)
    page.validate_homepage_heading()
    attach_screenshot(context.page, name="Cohort manager home page validated", context=context)


@then("user validates the homepage for cohort manager heading")
def step_user_validates_homepage_for_cohort_manager_heading(context):
    page = _get_cohort_manager_page(context)
    page.validate_homepage_heading()
    attach_screenshot(context.page, name="Cohort manager heading validated", context=context)


@then("user validates Active Cohort section")
def step_user_validates_active_cohort_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_active_cohort_section()
    attach_screenshot(context.page, name="Active cohort section validated", context=context)


@then("user validates Inactive Cohort section")
def step_user_validates_inactive_cohort_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_inactive_cohort_section()
    attach_screenshot(context.page, name="Inactive cohort section validated", context=context)


@then("user clicks on 1st cohort in the Active Cohort section")
def step_user_clicks_on_first_cohort_in_active_cohort_section(context):
    page = _get_cohort_manager_page(context)
    page.click_first_active_cohort()
    attach_screenshot(context.page, name="First active cohort clicked", context=context)


@then("user validates cohort dashboard and validates the download excel file link")
def step_user_validates_cohort_dashboard_and_download_excel(context):
    page = _get_cohort_manager_page(context)
    page.validate_cohort_dashboard_and_excel_link()
    attach_screenshot(context.page, name="Cohort dashboard and download link validated", context=context)


@then("user validates general info section")
def step_user_validates_general_info_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_general_info_section()
    attach_screenshot(context.page, name="General info section validated", context=context)


@then("user validates the upcoming meetings section in general info")
def step_user_validates_upcoming_meetings_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_upcoming_meetings_section()
    attach_screenshot(context.page, name="Upcoming meetings section validated", context=context)


@then("user clicks on create meeting button in the upcoming meetings section")
def step_user_clicks_create_meeting_in_upcoming_section(context):
    page = _get_cohort_manager_page(context)
    page.click_create_meeting_button_in_upcoming_meetings()
    attach_screenshot(context.page, name="Upcoming meetings create clicked", context=context)


@then("user fills all the details in the create meeting form and clicks on create a meeting button")
def step_user_fills_create_meeting_form_and_creates_meeting(context):
    page = _get_cohort_manager_page(context)
    page.fill_create_meeting_form_and_create()
    attach_screenshot(context.page, name="Create meeting form submitted", context=context)


@then("user validates and deletes the created meeting in the upcoming meetings section")
def step_user_validates_and_deletes_created_meeting_in_upcoming_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_and_delete_created_meeting_in_upcoming()
    attach_screenshot(context.page, name="Created upcoming meeting deleted", context=context)


@then("user validates cohort venture section")
def step_user_validates_cohort_venture_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_cohort_venture_section()
    attach_screenshot(context.page, name="Cohort venture section validated", context=context)


@then("user clicks on the create venture button in the cohort venture section")
def step_user_clicks_create_venture_button_in_cohort_venture(context):
    page = _get_cohort_manager_page(context)
    page.click_create_venture_button()
    attach_screenshot(context.page, name="Create venture clicked", context=context)


@then("user fills all the details in the create venture form and clicks on send an invite button")
def step_user_fills_create_venture_form_and_sends_invite(context):
    page = _get_cohort_manager_page(context)
    page.fill_create_venture_form_and_send_invite()
    attach_screenshot(context.page, name="Create venture form submitted", context=context)


@then("user validates cohort venture heading")
def step_user_validates_cohort_venture_heading(context):
    page = _get_cohort_manager_page(context)
    page.validate_cohort_venture_heading()
    attach_screenshot(context.page, name="Cohort venture heading validated", context=context)


@then("user validates cohort members section")
def step_user_validates_cohort_members_section(context):
    page = _get_cohort_manager_page(context)
    page.validate_cohort_members_section()
    attach_screenshot(context.page, name="Cohort members section validated", context=context)


@then("user validates the 1st member in the cohort members section and clicks on 1st chat button")
def step_user_validates_first_member_and_clicks_first_chat(context):
    page = _get_cohort_manager_page(context)
    page.validate_first_member_and_open_first_chat()
    attach_screenshot(context.page, name="First member and chat validated", context=context)


@then("user clicks on create new cohort button in the homepage")
def step_user_clicks_create_new_cohort_button_in_homepage(context):
    page = _get_cohort_manager_page(context)
    page.click_create_new_cohort_button()
    attach_screenshot(context.page, name="Create new cohort clicked", context=context)


@then("user fills all the details in the create new cohort form and clicks on create a cohort button")
def step_user_fills_create_new_cohort_form_and_creates_cohort(context):
    page = _get_cohort_manager_page(context)
    page.fill_create_new_cohort_form_and_create()
    attach_screenshot(context.page, name="Create cohort form submitted", context=context)


@then("user validates office hours section in the homepage")
def step_user_validates_office_hours_section_in_homepage(context):
    page = _get_cohort_manager_page(context)
    page.validate_office_hours_section()
    attach_screenshot(context.page, name="Office hours section validated", context=context)


@then("user clicks on create button in the office hours section")
def step_user_clicks_create_button_in_office_hours_section(context):
    page = _get_cohort_manager_page(context)
    page.click_create_button_in_office_hours_section()
    attach_screenshot(context.page, name="Office hours create clicked", context=context)


@then("user fills all the details in the create office hours form and clicks on create meeting button")
def step_user_fills_create_office_hours_form_and_creates_meeting(context):
    page = _get_cohort_manager_page(context)
    page.fill_create_office_hours_form_and_create_meeting()
    attach_screenshot(context.page, name="Create office hours form submitted", context=context)


@then("user clicks on the created meeting in the office hours section and deletes the created meeting")
def step_user_clicks_created_meeting_and_deletes_in_office_hours(context):
    page = _get_cohort_manager_page(context)
    page.click_created_meeting_and_delete()
    attach_screenshot(context.page, name="Created office hours meeting deleted", context=context)


@then("user navigates back to the homepage")
def step_user_navigates_back_to_homepage(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.navigate_to_home_page()
    attach_screenshot(context.page, name="Navigated back to home page", context=context)
