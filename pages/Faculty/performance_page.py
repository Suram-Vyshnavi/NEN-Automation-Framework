from locators.faculty_locators.performance_locators import performance_locators
from utils.helpers import attach_screenshot, highlight_element


class PerformancePage:
    def __init__(self, page):
        self.page = page
        self.locators = performance_locators()

    def _wait_visible(self, locator, timeout=15000):
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def _click(self, locator, step_name):
        element = self._wait_visible(locator)
        highlight_element(self.page, element)
        element.click()
        attach_screenshot(self.page, step_name)

    def _validate_visible(self, locator, message):
        element = self._wait_visible(locator)
        assert element.is_visible(), message
        highlight_element(self.page, locator)

    def click_performance_tab(self):
        self._click(self.locators.PERFORMANCE_SECTION, "Clicked Performance tab")

    def validate_reports_heading(self):
        self._validate_visible(
            self.locators.PLEASE_SELECT_HEADING,
            "Please select heading is not visible",
        )
        attach_screenshot(self.page, "Validated reports heading")

    def validate_program_name_dropdown_and_select_option(self):
        self._validate_visible(self.locators.PROGRAM_NAME, "Program Name label is not visible")
        self._click(self.locators.PROGRAM_COURSE, "Clicked Program Name dropdown")
        self._click(self.locators.PROGRAM_COURSE_OPTION, "IgniteX - 1.0")

    def validate_status_dropdown_and_select_option(self):
        self._validate_visible(self.locators.STATUS, "Status label is not visible")
        self._click(self.locators.STATUS_DROPDOWN, "Clicked Status dropdown")
        self._click(self.locators.STATUS_OPTION, "Active")

    def validate_cohort_name_dropdown_and_select_option(self):
        self._validate_visible(self.locators.COHORT_NAME, "Cohort Name label is not visible")
        self._click(self.locators.COHORT_DROPDOWN, "Clicked Cohort Name dropdown")
        self._click(self.locators.COHORT_OPTION, "IPV2-batch-28nov")
        
    def validate_cohort_quiz_card_details_and_toggle_switch_button(self):
        self._validate_visible(
            self.locators.COHORT_QUIZ_SCORECARD,
            "Cohort Quiz Scorecard heading is not visible",
        )
        self._validate_visible(self.locators.QUIZ_STATUS, "Quiz Status text is not visible")
        self._click(self.locators.TOGGLE_SWITCH, "Clicked Cohort Quiz toggle switch")

    def validate_milestone_card_details_and_milestone_toggle_switch_button(self):
        self._validate_visible(self.locators.MILESTONE_STATUS, "Milestone Status text is not visible")
        self._click(self.locators.MILESTONE_TOGGLE_SWITCH, "Clicked Milestone toggle switch")

    def click_download_cohort_performance_button(self):
        self._click(
            self.locators.DOWNLOAD_COHORT_PERFORMANCE,
            "Clicked Download Cohort Performance button",
        )
