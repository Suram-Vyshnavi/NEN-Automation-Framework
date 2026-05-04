from locators.viabilty_specialist_locators.viability_ventures_locators import viabilityventureslocators
from utils.helpers import attach_screenshot, highlight_element


class ViabilityVenturePage:
    def __init__(self, page):
        self.page = page
        self.locators = viabilityventureslocators()

    def _wait_and_assert_visible(self, locator, message, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        assert target.first.is_visible(), message
        return target.first

    def _wait_and_click(self, locator, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        target.first.click()

    def click_ventures_tab(self):
        try:
            self._wait_and_click(self.locators.VENTURES)
            highlight_element(self.page, self.locators.VENTURES)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Click Ventures Tab Failed", force=True)
            raise AssertionError(f"Failed to click Viability Specialist ventures tab: {exc}") from exc

    def validate_all_ventures_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.ALL_VENTURES, "All Ventures heading is not visible")
            highlight_element(self.page, self.locators.ALL_VENTURES)
        except Exception as exc:
            attach_screenshot(self.page, "Viability All Ventures Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate all ventures heading: {exc}") from exc

    def validate_pending_ventures_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.PENDING_EVALUATIONS, "Pending Evaluations heading is not visible")
            highlight_element(self.page, self.locators.PENDING_EVALUATIONS)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Pending Ventures Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate pending ventures heading: {exc}") from exc

    def click_evaluate_button_in_pending_ventures(self):
        try:
            self._wait_and_click(self.locators.EVALUATE_BUTTON)
            highlight_element(self.page, self.locators.EVALUATE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Pending Ventures Evaluate Click Failed", force=True)
            raise AssertionError(f"Failed to click evaluate button in pending ventures section: {exc}") from exc

    def validate_venture_information_card(self):
        try:
            self._wait_and_assert_visible(self.locators.VENTURE_INFO_CARD, "Venture information card is not visible")
            highlight_element(self.page, self.locators.VENTURE_INFO_CARD)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Venture Information Card Validation Failed", force=True)
            raise AssertionError(f"Failed to validate venture information card: {exc}") from exc

    def validate_venture_name_in_information_card(self):
        try:
            venture_card = self._wait_and_assert_visible(self.locators.VENTURE_INFO_CARD, "Venture information card is not visible")
            venture_name = venture_card.locator("xpath=.//*[self::h1 or self::h2 or self::h3 or self::h4 or self::p][normalize-space()]").first
            venture_name.wait_for(state="visible", timeout=15000)
            assert venture_name.inner_text().strip(), "Venture name is empty in the venture information card"
            highlight_element(self.page, venture_name)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Venture Name Validation Failed", force=True)
            raise AssertionError(f"Failed to validate venture name in venture information card: {exc}") from exc

    def validate_submissions_evaluation_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.SUBMISSIONS_EVALUATION_HEADINGS, "Submissions & Evaluation heading is not visible")
            highlight_element(self.page, self.locators.SUBMISSIONS_EVALUATION_HEADINGS)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Submissions Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate submissions and evaluation heading: {exc}") from exc

    def validate_instructions_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.INSTRUCTIONS_HEADINGS, "Instructions heading is not visible")
            highlight_element(self.page, self.locators.INSTRUCTIONS_HEADINGS)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Instructions Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate instructions heading: {exc}") from exc

    def validate_evaluate_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.EVALUATE_HEADING, "Evaluate heading is not visible")
            highlight_element(self.page, self.locators.EVALUATE_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Evaluate Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate evaluate heading: {exc}") from exc

    def validate_my_ratings_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.MY_RATINGS_HEADING, "My Ratings heading is not visible")
            highlight_element(self.page, self.locators.MY_RATINGS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Viability My Ratings Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate my ratings heading: {exc}") from exc
        self.page.go_back()

    def click_completed_evaluations(self):
        try:
            target = self.page.locator(self.locators.COMPLETED_EVALUATIONS).first
            target.scroll_into_view_if_needed(timeout=15000)
            target.wait_for(state="visible", timeout=15000)
            try:
                target.click(timeout=15000)
            except Exception:
                target.click(force=True)
            highlight_element(self.page, self.locators.COMPLETED_EVALUATIONS)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Completed Evaluations Click Failed", force=True)
            raise AssertionError(f"Failed to click completed evaluations heading: {exc}") from exc

    def validate_first_card_in_completed_evaluations(self):
        try:
            self._wait_and_assert_visible(self.locators.COMPLETED_EVALUATIONS_CARD, "First card in completed evaluations section is not visible")
            highlight_element(self.page, self.locators.COMPLETED_EVALUATIONS_CARD)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Completed Evaluations Card Validation Failed", force=True)
            raise AssertionError(f"Failed to validate first card in completed evaluations section: {exc}") from exc

    def navigate_to_home_page(self):
        try:
            self._wait_and_click(self.locators.HOME)
            highlight_element(self.page, self.locators.HOME)
        except Exception as exc:
            attach_screenshot(self.page, "Viability Navigate Home Failed", force=True)
            raise AssertionError(f"Failed to navigate to home page: {exc}") from exc
