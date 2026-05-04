from behave import then
from pages.common.settings_page import SettingsPage


@then("user clicks on profile icon and navigates to settings page")
def navigate_to_settings_page(context):
    if not hasattr(context, "settings_page"):
        context.settings_page = SettingsPage(context.page)
    context.settings_page.navigate_to_settings_page()


@then("user validates settings page heading and sections")
def validate_settings_page_complete(context):
    if not hasattr(context, "settings_page"):
        context.settings_page = SettingsPage(context.page)
    context.settings_page.validate_settings_page_complete()


@then("user clicks on accounts section")
def click_accounts_section(context):
    context.settings_page.click_accounts_section()


@then("user clicks on zoom connection section")
def expand_zoom_connection_section(context):
    context.settings_page.expand_zoom_connection_section()


@then("user validates zoom connection section details")
def validate_zoom_section_complete(context):
    context.settings_page.validate_zoom_section_complete()


@then("user clicks on zoom connection toggler to connect zoom account")
def connect_zoom_account(context):
    context.settings_page.connect_zoom_account()


@then("user clicks on disconnect button and validates the zoom connection")
def disconnect_zoom_and_validate(context):
    context.settings_page.click_disconnect_button()
    context.settings_page.validate_zoom_signin_button_visible()


@then("user clicks on whatsapp connection section")
def expand_whatsapp_section(context):
    context.settings_page.expand_whatsapp_section()


@then("user validates whatsapp connection section details")
def validate_whatsapp_section_header(context):
    context.settings_page.validate_whatsapp_section_header()


@then("user clicks on whatsapp connection toggler to connect whatsapp account")
def enable_whatsapp_notifications(context):
    context.settings_page.enable_whatsapp_notifications()


@then("user clicks on calendar section in settings page")
def click_calendar_section(context):
    context.settings_page.click_calendar_section()


@then("user validates calendar sync section details")
def validate_sync_google_calendar_option(context):
    context.settings_page.validate_sync_google_calendar_option()
