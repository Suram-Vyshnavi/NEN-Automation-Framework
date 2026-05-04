from pages.Mentor.mentor_my_profile_page import MentorMyProfilePage


def get_mentor_my_profile_page(context):
    """Get or create mentor my profile page object"""
    if not hasattr(context, 'mentor_my_profile_page'):
        context.mentor_my_profile_page = MentorMyProfilePage(context.page)
    return context.mentor_my_profile_page


def mentor_validate_profile_fields(context):
    """Helper to validate mentor profile fields"""
    page = get_mentor_my_profile_page(context)
    page.validate_all_fields()
