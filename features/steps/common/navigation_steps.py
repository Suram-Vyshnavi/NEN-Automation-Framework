from behave import given, then
from pages.common.navigation_page import NavigationPage


@given("user is on home page")
def user_on_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.handle_all_popups()


@then("user navigates to home page")
def navigate_to_home_page(context):
    if not hasattr(context, "navigation_page"):
        context.navigation_page = NavigationPage(context.page)
    context.navigation_page.navigate_to_home_page()
