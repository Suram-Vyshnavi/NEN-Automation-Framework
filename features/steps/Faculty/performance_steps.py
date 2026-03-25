from behave import then
from pages.Faculty.performance_page import PerformancePage


@then("user clicks on performance tab")
def click_performance_tab(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.click_performance_tab()


@then("user validates please select the following fields to get the reports heading")
def validate_reports_heading(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_reports_heading()


@then("user validates program name dropdown and selects the option")
def validate_program_name_dropdown_and_select_option(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_program_name_dropdown_and_select_option()


@then("user validates status dropdown and selects the option")
def validate_status_dropdown_and_select_option(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_status_dropdown_and_select_option()


@then("user validates cohort name dropdown and selects the option")
def validate_cohort_name_dropdown_and_select_option(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_cohort_name_dropdown_and_select_option()


@then("user validates cohort quiz card details and toggle switch button")
def validate_cohort_quiz_card_details_and_toggle_switch_button(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_cohort_quiz_card_details_and_toggle_switch_button()


@then("user validates milestone card details and milestone toggle switch button")
def validate_milestone_card_details_and_milestone_toggle_switch_button(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.validate_milestone_card_details_and_milestone_toggle_switch_button()


@then("user clicks on download cohort performance button")
def click_download_cohort_performance_button(context):
    if not hasattr(context, "performance_page"):
        context.performance_page = PerformancePage(context.page)
    context.performance_page.click_download_cohort_performance_button()
