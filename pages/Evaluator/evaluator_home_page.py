from locators.evaluator_locators.eval_home_page_locators import eval_home_page_locators
from utils.helpers import attach_screenshot, highlight_element


class EvaluatorHomePage:
    def __init__(self, page):
        self.page = page
        self.locators = eval_home_page_locators()

    def _wait_and_assert_visible(self, locator, message, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        assert target.first.is_visible(), message

    def _wait_and_click(self, locator, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        target.first.click()

    def validate_home_page_card(self):
        try:
            self._wait_and_assert_visible(
                self.locators.HOME_PAGE_CARD,
                "Evaluator home page card is not visible",
            )
            highlight_element(self.page, self.locators.HOME_PAGE_CARD)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Home Page Card Validation Failed", force=True)
            raise AssertionError(f"Failed to validate evaluator home page card: {exc}") from exc
        
    def validate_resources_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.RESOURCES_HEADING,
                "Resources heading is not visible",
            )
            highlight_element(self.page, self.locators.RESOURCES_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Resources Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate Resources heading: {exc}") from exc


    def click_evaluate_button(self):
        try:
            self._wait_and_click(self.locators.EVALUATE_BUTTON)
            highlight_element(self.page, self.locators.EVALUATE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Click Evaluate Button Failed", force=True)
            raise AssertionError(f"Failed to click evaluator evaluate button: {exc}") from exc

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

    def navigate_to_home_page(self):
        try:
            self._wait_and_click(self.locators.HOME_PAGE)
            self._wait_and_assert_visible(
                self.locators.HOME_PAGE_CARD,
                "Evaluator home page card is not visible after navigation",
            )
            highlight_element(self.page, self.locators.HOME_PAGE)
        except Exception as exc:
            attach_screenshot(self.page, "Evaluator Navigate To Home Page Failed", force=True)
            raise AssertionError(f"Failed to navigate evaluator to home page: {exc}") from exc
