import os

from utils.profile_api import delete_user_profile


def test_user_registration(page):
    """Register a user and always delete it after test execution.

    Replace the registration flow block with your actual UI steps and set
    created_user_id from the registration response or UI-captured data.
    """
    base_url = os.getenv("API_BASE_URL", "https://dev.nen.wfglobal.org")
    bearer_token = os.getenv("ADMIN_BEARER_TOKEN")
    created_user_id = None

    try:
        # TODO: Replace this with your real registration steps.
        # Example:
        # created_user_id = registration_page.register_user_and_get_user_id(page)
        page.goto(base_url)

        # Ensure you assign the created user id before assertions complete.
        assert created_user_id, "Set created_user_id from registration flow before assertions"

    finally:
        if created_user_id and bearer_token:
            delete_user_profile(
                base_url=base_url,
                user_id=created_user_id,
                bearer_token=bearer_token,
            )
        elif created_user_id and not bearer_token:
            raise AssertionError("User was created but ADMIN_BEARER_TOKEN is not set for cleanup")
