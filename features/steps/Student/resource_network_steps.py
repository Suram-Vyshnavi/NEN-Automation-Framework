from behave import then
from pages.Student.resource_network_page import ResourceNetworkPage


@then("user click on resource network section")
def click_resource_network_section(context):
    """Click on Resource Network section"""
    if not hasattr(context, 'resource_network_page'):
        context.resource_network_page = ResourceNetworkPage(context.page)
    context.resource_network_page.click_resource_network_section()


@then("user clicks on explore section")
def click_explore_section(context):
    """Click on Explore section"""
    context.resource_network_page.click_explore_section()


@then("user validates mentors, experts and service providers cards")
def validate_mentors_experts_service_providers_cards(context):
    """Validate Mentors, Experts and Service Providers cards"""
    context.resource_network_page.validate_mentors_experts_service_providers_cards()


@then("user clicks on mentors section")
def click_mentors_section(context):
    """Click on Mentors section"""
    context.resource_network_page.click_mentors_section()


@then("user searches test in search network")
def search_test_in_search_network(context):
    """Search for test in search network"""
    context.resource_network_page.search_test_in_search_network()


@then("user clicks on first search result request meeting button")
def click_first_search_result_request_meeting_button(context):
    """Click on first search result and request meeting button"""
    context.resource_network_page.click_first_search_result_request_meeting_button()


@then("select the slot and give statrtup information, select startup stage, linkedin url and meeting expectation")
def select_slot_and_provide_startup_information(context):
    """Select slot and provide startup information"""
    context.resource_network_page.select_slot_and_provide_startup_information()


@then("click on request meeting button")
def click_request_meeting_button(context):
    """Click on request meeting button"""
    context.resource_network_page.click_request_meeting_button()


@then("user clicks on experts section")
def click_experts_section(context):
    """Click on Experts section"""
    context.resource_network_page.click_experts_section()


@then("user clicks on service providers section")
def click_service_providers_section(context):
    """Click on Service Providers section"""
    context.resource_network_page.click_service_providers_section()


@then("user click on my requests section")
def click_my_requests_section(context):
    """Click on My Requests section"""
    context.resource_network_page.click_my_requests_section()


