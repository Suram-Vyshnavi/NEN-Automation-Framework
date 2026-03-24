from behave import then
from pages.Student.calender_page import CalenderPage


@then("user clicks on calendar section")
def click_calendar_section(context):
    if not hasattr(context, 'calender_page'):
        context.calender_page = CalenderPage(context.page)
    context.calender_page.click_calendar_section()


@then("user validates calendar page")
def validate_calendar_page(context):
    context.calender_page.validate_calendar_page()


@then("user clicks on first meeting link")
def click_first_meeting_link(context):
    context.calender_page.click_first_meeting_link()


@then("user validates past activities section and open meeting")
def validate_past_activities_and_meeting_link(context):
    context.calender_page.validate_past_activities_section_and_meeting_link()
