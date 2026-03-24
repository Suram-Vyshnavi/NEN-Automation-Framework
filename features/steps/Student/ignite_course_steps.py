from behave import then
from pages.Student.ignite_course_page import IgniteCoursePage


@then("user validates ignite program in home page")
def validate_ignite_home(context):
    if not hasattr(context, 'ignite_course_page'):
        context.ignite_course_page = IgniteCoursePage(context.page)
    context.ignite_course_page.validate_ignite_program_in_home_page()


@then("user clicks on go to course in home page")
def click_go_to_course(context):
    context.ignite_course_page.click_go_to_course_in_home_page()


@then("user validates overiew section")
def validate_overview(context):
    context.ignite_course_page.validate_overview_section()


@then("user clicks on course content section")
def click_course_content(context):
    context.ignite_course_page.click_course_content_section()


@then("user navigate to venture journey section")
def navigate_venture_journey(context):
    context.ignite_course_page.navigate_to_venture_journey_section()


@then("user clicks on view output")
def click_view_output(context):
    context.ignite_course_page.click_view_output()


@then("user clicks on redo button")
def click_redo(context):
    context.ignite_course_page.click_redo_button()


@then("user clicks on preview button")
def click_preview(context):
    context.ignite_course_page.click_preview_button()


@then("user navigates to performance")
def navigate_performance(context):
    context.ignite_course_page.navigate_to_performance()


@then("user validates your performance section cards")
def validate_performance_cards(context):
    context.ignite_course_page.validate_your_performance_section_cards()


@then("user validates your certificates")
def validate_certificates(context):
    context.ignite_course_page.validate_your_certificates()


@then("user clicks on share and validates download button")
def click_share_validate_download(context):
    context.ignite_course_page.click_share_and_validate_download_button()


@then("user clicks on cohort section")
def click_cohort(context):
    context.ignite_course_page.click_cohort_section()


@then("user validates cohort section")
def validate_cohort_section(context):
    context.ignite_course_page.validate_cohort_section()


@then("user clicks on view venture journey")
def click_view_venture_journey(context):
    context.ignite_course_page.click_view_venture_journey()


@then("user clicks on view venture journey and validates the venture journey detail")
def view_venture_journey_validate(context):
    context.ignite_course_page.click_view_venture_journey_and_validate_details()