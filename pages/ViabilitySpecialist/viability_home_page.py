from locators.viabilty_specialist_locators.viability_homepage_locators import viabilityHomepageLocators
from utils.helpers import attach_screenshot, highlight_element


class ViabilityHomePage:
    def __init__(self, page):
        self.page = page
        self.locators = viabilityHomepageLocators()

    def _wait_and_assert_visible(self, locator, message, timeout=15000):
        target = self.page.locator(locator).first
        target.scroll_into_view_if_needed(timeout=timeout)
        target.wait_for(state='visible', timeout=timeout)
        assert target.is_visible(), message

    def _wait_and_click(self, locator, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state='visible', timeout=timeout)
        target.first.click()

    def validate_home_page_card(self):
        try:
            self._wait_and_assert_visible(self.locators.HOMEPAGE_CARD, 'Home page card is not visible')
            highlight_element(self.page, self.locators.HOMEPAGE_CARD)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Home Page Card Validation Failed', force=True)
            raise AssertionError(f'Failed to validate home page card: {exc}') from exc

    def validate_resource_heading(self):
        try:
            target = self.page.locator(self.locators.RESOURCE_HEADING)
            target.first.wait_for(state='attached', timeout=15000)
            assert target.count() > 0, 'Resource heading not found in DOM'
            highlight_element(self.page, self.locators.RESOURCE_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Resource Heading Validation Failed', force=True)
            raise AssertionError(f'Failed to validate resource heading: {exc}') from exc

    def click_evaluate_button(self):
        try:
            self._wait_and_click(self.locators.EVALUATE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Click Evaluate Button Failed', force=True)
            raise AssertionError(f'Failed to click evaluate button: {exc}') from exc

    def validate_venture_information_card(self):
        try:
            self._wait_and_assert_visible(self.locators.VENTURE_CARD, 'Venture information card is not visible')
            highlight_element(self.page, self.locators.VENTURE_CARD)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Venture Card Validation Failed', force=True)
            raise AssertionError(f'Failed to validate venture information card: {exc}') from exc

    def validate_submissions_evaluation_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.SUBMISSIONS_EVALUATION_HEADINGS, 'Submissions & Evaluation heading is not visible')
            highlight_element(self.page, self.locators.SUBMISSIONS_EVALUATION_HEADINGS)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Submissions Heading Validation Failed', force=True)
            raise AssertionError(f'Failed to validate Submissions & Evaluation heading: {exc}') from exc

    def validate_instructions_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.INSTRUCTIONS_HEADINGS, 'Instructions heading is not visible')
            highlight_element(self.page, self.locators.INSTRUCTIONS_HEADINGS)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Instructions Heading Validation Failed', force=True)
            raise AssertionError(f'Failed to validate Instructions heading: {exc}') from exc

    def validate_view_file_link(self):
        try:
            self._wait_and_assert_visible(self.locators.VIEW_FILE_LINK, 'View file link is not visible')
            highlight_element(self.page, self.locators.VIEW_FILE_LINK)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability View File Link Validation Failed', force=True)
            raise AssertionError(f'Failed to validate View file link: {exc}') from exc

    def validate_evaluate_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.EVALUATE_HEADING, 'Evaluate heading is not visible')
            highlight_element(self.page, self.locators.EVALUATE_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Evaluate Heading Validation Failed', force=True)
            raise AssertionError(f'Failed to validate Evaluate heading: {exc}') from exc

    def validate_my_ratings_heading(self):
        try:
            self._wait_and_assert_visible(self.locators.MY_RATINGS_HEADING, 'My Ratings heading is not visible')
            highlight_element(self.page, self.locators.MY_RATINGS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability My Ratings Heading Validation Failed', force=True)
            raise AssertionError(f'Failed to validate My Ratings heading: {exc}') from exc

    def validate_milestone_form_section(self):
        try:
            self._wait_and_assert_visible(self.locators.MILESTONE_FORM_SECTION, 'Milestone form section is not visible')
            highlight_element(self.page, self.locators.MILESTONE_FORM_SECTION)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Milestone Form Section Validation Failed', force=True)
            raise AssertionError(f'Failed to validate Milestone form section: {exc}') from exc

    def validate_milestone_next_form_section(self):
        try:
            self._wait_and_assert_visible(self.locators.MILESTONE_NEXT_FORM, 'Milestone next form section is not visible')
            highlight_element(self.page, self.locators.MILESTONE_NEXT_FORM)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Milestone Next Form Validation Failed', force=True)
            raise AssertionError(f'Failed to validate Milestone next form section: {exc}') from exc

    def navigate_to_home_page(self):
        try:
            self._wait_and_click(self.locators.HOME)
        except Exception as exc:
            attach_screenshot(self.page, 'Viability Navigate to Home Failed', force=True)
            raise AssertionError(f'Failed to navigate to home page: {exc}') from exc
