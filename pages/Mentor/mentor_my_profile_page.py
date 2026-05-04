from locators.mentor_locators.mentor_my_profile_locators import MentorMyProfileLocators
from utils.helpers import attach_screenshot, highlight_element


class MentorMyProfilePage:
    def __init__(self, page):
        self.page = page
        self.locators = MentorMyProfileLocators()

    def _wait_visible(self, locator, timeout=15000):
        """Wait for element to be visible and return it"""
        try:
            element = self.page.locator(locator).first
            element.wait_for(state="visible", timeout=timeout)
            return element
        except Exception as exc:
            raise AssertionError(f"Element not visible: {locator}") from exc

    def _click(self, locator, timeout=15000):
        """Click on element"""
        try:
            element = self._wait_visible(locator, timeout)
            element.click()
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Click Failed")
            raise AssertionError(f"Failed to click: {locator}") from exc

    def _fill(self, locator, value, timeout=15000):
        """Fill input with value"""
        try:
            element = self._wait_visible(locator, timeout)
            element.fill(str(value))
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Fill Failed")
            raise AssertionError(f"Failed to fill: {locator}") from exc

    def validate_all_fields(self, expected_first_name="Test_name", expected_last_name="Test_lastname"):
        """Validate all profile fields are visible and accessible"""
        try:
            # List of locators to validate for visibility
            visible_locators = [
                self.locators.TITLE,
                self.locators.LINKEDIN_PROFILE,
                self.locators.FACEBOOK_PROFILE,
                self.locators.TWITTER_PROFILE,
                self.locators.WEBSITE_URL,
                self.locators.SELECT_INDUSTRY_TYPE,
                self.locators.SELECT_SKILL_TYPE,
                self.locators.CAPACITY,
            ]
            
            # Validate all fields are visible
            for locator in visible_locators:
                self._wait_visible(locator)
                highlight_element(self.page, locator)
            
            highlight_element(self.page, self.locators.TITLE)
            
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Validate Profile Fields Failed")
            raise AssertionError(f"Failed to validate mentor profile fields: {exc}") from exc
