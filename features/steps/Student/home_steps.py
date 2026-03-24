from behave import given, then
from pages.Student.home_page import HomePage


@given("user is on home page")
def user_on_home_page(context):
    """User is already on home page after login and popup handling"""
    if not hasattr(context, 'home_page'):
        context.home_page = HomePage(context.page)
    # Handle all 4 popups that appear after login
    context.home_page.handle_all_popups()


@then("user navigates to all headers and validates them")
def navigate_and_validate_all_headers(context):
    """Navigate to and validate all header elements"""
    context.home_page.navigate_and_validate_all_headers()


@then("user navigates to home page")
def navigate_to_home_page(context):
    """Navigate back to home page"""
    context.home_page.navigate_to_home_page()


@then("user validates certification section")
def validate_certification_section(context):
    """Validate Certification Logic section"""
    if not hasattr(context, 'home_page'):
        context.home_page = HomePage(context.page)
    context.home_page.validate_certification_section()


@then("user validates personalized journey section")
def validate_personalized_journey_section(context):
    """Validate Personalized Journey section"""
    context.home_page.validate_personalized_journey_section()


@then("user validates Featured Resource Network section")
def validate_featured_resource_network_section(context):
    """Validate Featured Resource Network section"""
    context.home_page.validate_featured_resource_network_section()


@then("validate mentor card and request meeting button")
def validate_mentor_card_and_button(context):
    """Validate Mentor Card and Request Meeting button"""
    context.home_page.validate_mentor_card_and_request_meeting_button()


@then("user validates recommended content section")
def validate_recommended_content_section(context):
    """Validate Recommended Content section"""
    context.home_page.validate_recommended_content_section()


@then("user validates recommended by your institute section")
def validate_recommended_by_institute_section(context):
    """Validate Recommended By Your Institute section"""
    context.home_page.validate_recommended_by_your_institute_section()


@then("user validates courses section and first course details")
def validate_courses_section_and_first_course(context):
    """Validate Courses section and first course details"""
    context.home_page.validate_courses_section_and_first_course()
