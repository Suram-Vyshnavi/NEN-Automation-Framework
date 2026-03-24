from behave import then
from pages.Student.myprofile_page import MyProfilePage


@then("user clicks on profile icon and navigates to my profile page")
def click_profile_icon(context):
    if not hasattr(context, 'myprofile_page'):
        context.myprofile_page = MyProfilePage(context.page)
    context.myprofile_page.click_profile_icon()
    context.myprofile_page.validate_my_profile_page()


@then("user edits profile information name, city, language and save changes")
def edit_profile(context):
    context.myprofile_page.edit_profile(first_name='Test_name', last_name='Test_lastname', city='Hyderabad', language='Spanish')
    context.myprofile_page.save_changes()
    


@then("user edits profile again and reverts the changes back to original and save changes")
def revert_profile(context):
    context.myprofile_page.edit_profile(first_name='Vyshnavi', last_name='Suram', city='Bangalore', language='English')
    context.myprofile_page.save_changes()

@then("user changes language to Spanish and revert back to English")
def change_language(context):
    context.myprofile_page.language_selection(language='Spanish')
    context.myprofile_page.save_changes()
    context.myprofile_page.language_selection(language='English')
    context.myprofile_page.save_changes("Spanish")

