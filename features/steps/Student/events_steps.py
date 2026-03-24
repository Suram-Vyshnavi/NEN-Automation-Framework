from behave import then
from pages.Student.events_page import EventsPage


@then("user clicks on events section")
def click_events_section(context):
    if not hasattr(context, 'events_page'):
        context.events_page = EventsPage(context.page)
    context.events_page.click_events_section()


@then("user validates upcoming events")
def validate_upcoming_events(context):
    context.events_page.validate_upcoming_events()


@then("user validates registered events")
def validate_registered_events(context):
    context.events_page.validate_registered_events()


@then("user validates explore events")
def validate_explore_events(context):
    context.events_page.validate_explore_events()


@then("user clicks on view details of first upcoming event and validates the event details")
def click_view_details_and_validate(context):
    context.events_page.click_view_details_first_upcoming_event()
    context.events_page.validate_event_details()


@then("user clicks on back button")
def click_back_button(context):
    context.events_page.click_back_button()
