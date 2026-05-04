from behave import then

from pages.Incubator.partner_profile_page import IncubatorPartnerProfilePage
from utils.helpers import attach_screenshot


@then("incubator user clicks on profile icon")
def step_incubator_user_clicks_profile_icon(context):
    if not hasattr(context, "partner_profile_page"):
        context.partner_profile_page = IncubatorPartnerProfilePage(context.page)
    context.partner_profile_page.click_profile_icon()
    attach_screenshot(context.page, name="Incubator profile icon clicked", context=context)


@then("incubator user clicks on partner profile")
def step_incubator_user_clicks_partner_profile(context):
    if not hasattr(context, "partner_profile_page"):
        context.partner_profile_page = IncubatorPartnerProfilePage(context.page)
    context.partner_profile_page.click_partner_profile_tab()
    attach_screenshot(context.page, name="Incubator partner profile tab clicked", context=context)


@then("incubator user validates partner profile heading")
def step_incubator_user_validates_partner_profile_heading(context):
    if not hasattr(context, "partner_profile_page"):
        context.partner_profile_page = IncubatorPartnerProfilePage(context.page)
    context.partner_profile_page.validate_partner_profile_heading()
    attach_screenshot(context.page, name="Incubator partner profile heading validated", context=context)


@then("incubator user validates partner name")
def step_incubator_user_validates_partner_name(context):
    if not hasattr(context, "partner_profile_page"):
        context.partner_profile_page = IncubatorPartnerProfilePage(context.page)
    context.partner_profile_page.validate_partner_name()
    attach_screenshot(context.page, name="Incubator partner name validated", context=context)


@then("incubator user validates logo")
def step_incubator_user_validates_logo(context):
    context.partner_profile_page.validate_logo()
    attach_screenshot(context.page, name="Incubator partner profile logo validated", context=context)

# NOTE: "incubator user navigates to home page" is already defined in incubator_cohort_steps.py
