from behave import then
from pages.Student.my_startup_page import MyStartupPage


@then("user clicks on profile icon and navigates to my startup page")
def click_profile_navigate_startup(context):
    if not hasattr(context, 'my_startup_page'):
        context.my_startup_page = MyStartupPage(context.page)
    context.my_startup_page.click_profile_icon_and_navigate_to_my_startup_page()


@then("user validates my startup page header, ignite and wadhwani sections")
def validate_header_sections(context):
    context.my_startup_page.validate_my_startup_page_header_ignite_wadhwani_sections()


@then("user clicks on view button of ignite section")
def click_view_ignite(context):
    context.my_startup_page.click_view_button_of_ignite_section()


@then("user validates the details in my startup page")
def validate_details(context):
    if not hasattr(context, 'my_startup_page'):
        context.my_startup_page = MyStartupPage(context.page)
    context.my_startup_page.validate_details_in_my_startup_page()


@then("user clicks on basic information section and saves")
def click_basic_save(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.click_basic_information_section_and_save()


@then("user clicks on view venture journey and validates the venture journey details and navigate back to my startup page")
def view_venture_journey(context):
    context.my_startup_page.click_view_venture_journey_and_validate_details_and_navigate_back()


@then("user clicks on youtube video url section and adds a youtube video url and saves")
def add_youtube_url(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.click_youtube_video_url_section_and_add_url_and_save()


@then("user clicks on venture team section and adds a member to the team by searching with name and saves")
def add_member(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.click_venture_team_section_and_add_member_and_save()


@then("user removes the added member from venture team section and saves")
def remove_member(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.remove_added_member_from_venture_team_and_save()


@then("user clicks on venture support section and validates the faculty details")
def validate_faculty(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.click_venture_support_section_and_validate_faculty_details()


@then("user validates Milestone Timeline and validate 1st milestone details")
def validate_milestone(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.validate_milestone_timeline_and_1st_milestone_details()


@then("user validates upcoming activies section")
def validate_upcoming(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.validate_upcoming_activities_section()


@then("user validates meeting and webinar cards")
def validate_cards(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.validate_meeting_and_webinar_cards()


@then("user validates resources section")
def validate_resources(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.validate_resources_section()


@then("user uploads a file in resources section and validates")
def upload_file(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.upload_file_in_resources_section_and_validate()


@then("user deletes the uploaded file in resources section and validates")
def delete_file(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.delete_uploaded_file_in_resources_section_and_validate()
@then("user clicks on view button of liftoff-spark")
def click_view_liftoff_spark(context):
    page = getattr(context, 'ignite_course_page', context.my_startup_page)
    page.click_view_button_of_liftoff_spark_section()