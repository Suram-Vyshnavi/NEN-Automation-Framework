from locators.evaluator_locators.eval_venture_locators import eval_venture_locators
from utils.helpers import attach_screenshot, highlight_element


class EvaluatorVenturePage:
    def __init__(self, page):
        self.page = page
        self.locators = eval_venture_locators()

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
            self._wait_and_click(self.locators.VENTURES_PAGE)
            highlight_element(self.page, self.locators.VENTURES_PAGE)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Click Ventures Tab Failed", force=True)
            raise AssertionError(f"Failed to click evaluator ventures tab: {exc}") from exc

    def validate_all_ventures_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.ALL_VENTURES_HEADING,
                "All Ventures heading is not visible",
            )
            highlight_element(self.page, self.locators.ALL_VENTURES_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator All Ventures Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate All Ventures heading: {exc}") from exc

    def validate_pending_ventures_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.PENDING_EVALUATIONS,
                "Pending Evaluations heading is not visible",
            )
            highlight_element(self.page, self.locators.PENDING_EVALUATIONS)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Pending Ventures Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Pending Evaluations heading: {exc}") from exc

    def click_evaluate_button_in_pending_ventures(self):
        try:
            self._wait_and_click(self.locators.EVALUATE_BUTTON)
            highlight_element(self.page, self.locators.EVALUATE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Pending Ventures Evaluate Click Failed", force=True)
            raise AssertionError(f"Failed to click Evaluate button in pending ventures section: {exc}") from exc

    def validate_venture_information_card(self):
        try:
            self._wait_and_assert_visible(
                self.locators.VENTURE_INFO_CARD,
                "Venture information card is not visible",
            )
            highlight_element(self.page, self.locators.VENTURE_INFO_CARD)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Venture Information Card Validation Failed", force=True)
            raise AssertionError(f"Failed to validate venture information card: {exc}") from exc

    def validate_venture_name_in_information_card(self):
        try:
            venture_card = self._wait_and_assert_visible(
                self.locators.VENTURE_INFO_CARD,
                "Venture information card is not visible",
            )
            venture_name = venture_card.locator("xpath=.//*[self::h1 or self::h2 or self::h3 or self::h4 or self::p][normalize-space()]").first
            venture_name.wait_for(state="visible", timeout=15000)
            assert venture_name.inner_text().strip(), "Venture name is empty in the venture information card"
            highlight_element(self.page, venture_name)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Venture Name Validation Failed", force=True)
            raise AssertionError(f"Failed to validate venture name in venture information card: {exc}") from exc

    def validate_submissions_evaluation_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.SUBMISSIONS_EVALUATION_HEADING,
                "Submissions & Evaluation heading is not visible",
            )
            highlight_element(self.page, self.locators.SUBMISSIONS_EVALUATION_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Submissions And Evaluation Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Submissions & Evaluation heading: {exc}") from exc

    def validate_instructions_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.INSTRUCTIONS_HEADING,
                "Instructions heading is not visible",
            )
            highlight_element(self.page, self.locators.INSTRUCTIONS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Instructions Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Instructions heading: {exc}") from exc

    def validate_milestone_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.MILESTONE_HEADING,
                "Milestone heading is not visible",
            )
            highlight_element(self.page, self.locators.MILESTONE_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Milestone Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Milestone heading: {exc}") from exc

    def validate_viability_evaluation_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.VIABILITY_EVALUATION_HEADING,
                "Viability Evaluation heading is not visible",
            )
            highlight_element(self.page, self.locators.VIABILITY_EVALUATION_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Viability Evaluation Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Viability Evaluation heading: {exc}") from exc
        self.page.go_back()

    def click_completed_evaluations(self):
        try:
            self._wait_and_click(self.locators.COMPLETED_EVALUATIONS)
            highlight_element(self.page, self.locators.COMPLETED_EVALUATIONS)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Click Completed Evaluations Failed", force=True)
            raise AssertionError(f"Failed to click evaluator completed evaluations: {exc}") from exc
