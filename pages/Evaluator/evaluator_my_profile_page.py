from locators.evaluator_locators.eval_my_profile_locators import EvalMyProfileLocators
from utils.helpers import attach_screenshot, highlight_element


class EvaluatorMyProfilePage:
    """Page object for Evaluator My Profile"""
    
    def __init__(self, page):
        self.page = page
        self.locators = EvalMyProfileLocators()

    def _wait_visible(self, locator, timeout=15000):
        """Wait for element to be visible and return it"""
        try:
            element = self.page.locator(locator).first
            element.wait_for(state="visible", timeout=timeout)
            return element
        except Exception as exc:
            raise AssertionError(f"Element not visible: {locator}") from exc

    def validate_all_fields(self):
        """Validate all profile fields are visible and accessible"""
        try:
            # List of locators to validate for visibility
            visible_locators = [
                self.locators.FIRST_NAME,
                self.locators.LAST_NAME,
                self.locators.MOBILE_NUMBER,
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
            
            attach_screenshot(self.page, "Evaluator Profile Fields Validated", context=None, force=True)
            
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Validate Profile Fields Failed")
            raise AssertionError(f"Failed to validate evaluator profile fields: {exc}") from exc
