from behave import then
from pages.Student.liftoff_course_page import LiftoffCoursePage


@then("user validates liftoff program in home page")
def validate_liftoff_program_home(context):
    if not hasattr(context, 'liftoff_page'):
        context.liftoff_page = LiftoffCoursePage(context.page)
    context.liftoff_page.validate_liftoff_program()


@then("user validates choose your gaps")
def validate_choose_your_gaps(context):
    context.liftoff_page.validate_choose_your_gaps()


@then("user clicks on start now button")
def click_start_now_button(context):
    context.liftoff_page.click_start_now()


@then("user validates program application section")
def validate_program_application(context):
    context.liftoff_page.validate_program_application()


@then("user navigates to identify your gaps section")
def navigate_to_identify_your_gaps(context):
    context.liftoff_page.navigate_to_identify_gaps()


@then("user clicks on add modify gaps button and select some gaps and submit")
def add_modify_gaps_and_submit(context):
    context.liftoff_page.add_modify_gaps_and_submit()


@then("revert the changes by clicking on add modify gaps button and deselect the selected gaps and submit")
def revert_add_modify_gaps(context):
    context.liftoff_page.revert_gaps_and_submit()


@then("user navigates to Personalised journey section")
def navigate_to_personalised_journey(context):
    context.liftoff_page.navigate_to_personalised_journey()


@then("user clicks on ProductIteration section and rewatches the video and closes the video")
def product_iteration_rewatch_close(context):
    context.liftoff_page.product_iteration_rewatch_and_close()


@then("user navigates to submit pitch section")
def navigate_to_submit_pitch_section(context):
    context.liftoff_page.navigate_to_submit_pitch()


@then("user clicks on upload pitch section")
def click_upload_pitch_section(context):
    context.liftoff_page.click_upload_pitch_section()


@then("user upload your pitch desk and save")
def upload_pitch_deck_and_save(context):
    file_path = 'C:/Users/VyshnaviSuram/automation/NEN Automation-framework/files/Test_File_Upload.pdf'
    context.liftoff_page.upload_pitch_deck_and_save(file_path=file_path, file_name='Test Pitch Deck')


@then("user clicks on pitch deck records and deletes the pitch")
def delete_pitch_deck_record(context):
    context.liftoff_page.delete_pitch_deck()
