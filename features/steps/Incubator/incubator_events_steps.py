from behave import then

from pages.Incubator.events_page import IncubatorEventsPage
from utils.helpers import attach_screenshot


def _get_events_page(context):
    if not hasattr(context, "incubator_events_page"):
        context.incubator_events_page = IncubatorEventsPage(context.page)
    return context.incubator_events_page


@then("incubator user clicks on events tab")
def step_incubator_user_clicks_on_events_tab(context):
    page = _get_events_page(context)
    page.click_events_tab()
    attach_screenshot(context.page, name="Incubator events tab clicked", context=context)


@then("incubator user validates events heading")
def step_incubator_user_validates_events_heading(context):
    page = _get_events_page(context)
    page.validate_events_heading()
    attach_screenshot(context.page, name="Incubator events heading validated", context=context)


@then("incubator user clicks on add event button")
def step_incubator_user_clicks_on_add_event_button(context):
    page = _get_events_page(context)
    page.click_add_event_button()
    attach_screenshot(context.page, name="Incubator add event clicked", context=context)


@then("incubator user fills all the details and click on add speakers")
def step_incubator_user_fills_all_details_and_click_add_speakers(context):
    page = _get_events_page(context)
    page.fill_all_details_and_click_add_speakers()
    attach_screenshot(context.page, name="Incubator event details filled and add speakers clicked", context=context)


@then("incubator user clicks on create event & next")
def step_incubator_user_clicks_on_create_event_next(context):
    page = _get_events_page(context)
    page.click_create_event_next()
    attach_screenshot(context.page, name="Incubator create event next clicked", context=context)


@then("incubator user clicks on add by emails radio button")
def step_incubator_user_clicks_on_add_by_emails_radio_button(context):
    page = _get_events_page(context)
    page.click_add_by_emails_radio()
    attach_screenshot(context.page, name="Incubator add by emails radio clicked", context=context)


@then("incubator user clicks on bulk upload invitation button and uploads the file and submits")
def step_incubator_user_bulk_upload_invitation(context):
    page = _get_events_page(context)
    page.click_bulk_upload_invitation_and_submit()
    attach_screenshot(context.page, name="Incubator bulk upload invitation submitted", context=context)


@then("incubator user deletes the created event")
def step_incubator_user_deletes_the_created_event(context):
    page = _get_events_page(context)
    page.delete_created_event()
    attach_screenshot(context.page, name="Incubator event deleted", context=context)

# NOTE: "incubator user navigates to home page" is defined in incubator_cohort_steps.py
