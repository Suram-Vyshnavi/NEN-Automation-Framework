from playwright.sync_api import sync_playwright


def delete_user_profile(base_url: str, user_id: str, bearer_token: str, timeout_ms: int = 30000):
    """Delete a user profile via API.

    Args:
        base_url: API host URL, for example https://dev.nen.wfglobal.org
        user_id: User id to delete (sent as query param userId)
        bearer_token: Authorization token without Bearer prefix
        timeout_ms: Request timeout in milliseconds

    Returns:
        Tuple of (status_code, response_payload)
    """
    endpoint = "/api/v1/profileservice/profile/delete"

    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Authorization": f"Bearer {bearer_token}",
                "Accept": "application/json",
            },
        )

        try:
            response = request_context.delete(
                endpoint,
                params={"userId": user_id},
                timeout=timeout_ms,
            )

            try:
                payload = response.json()
            except Exception:
                payload = response.text()

            print(f"DELETE {endpoint} userId={user_id}")
            print(f"Status: {response.status}")
            print(f"Response: {payload}")

            return response.status, payload
        finally:
            request_context.dispose()
