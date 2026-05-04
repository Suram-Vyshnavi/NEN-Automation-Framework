from pages.Evaluator.evaluator_my_profile_page import EvaluatorMyProfilePage


def get_evaluator_my_profile_page(context):
    """Get or create evaluator my profile page object"""
    if not hasattr(context, 'evaluator_my_profile_page'):
        context.evaluator_my_profile_page = EvaluatorMyProfilePage(context.page)
    return context.evaluator_my_profile_page


def evaluator_validate_profile_fields(context):
    """Helper to validate evaluator profile fields"""
    page = get_evaluator_my_profile_page(context)
    page.validate_all_fields()
