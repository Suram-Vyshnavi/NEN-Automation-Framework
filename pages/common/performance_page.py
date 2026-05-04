from locators.common.performance_locators import PerformanceLocators
from utils.helpers import attach_screenshot, highlight_element
import os
from pathlib import Path
from time import strftime


class PerformancePage:
    def __init__(self, page):
        self.page = page
        self.locators = PerformanceLocators()
        self.USER_TYPE = os.getenv("USER_TYPE", "student").strip().lower()
        self.USER_TYPE = self.USER_TYPE.lower()  # Ensure it's in lowercase for consistency

    def _wait_visible(self, locator, timeout=15000):
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def _click(self, locator):
        element = self._wait_visible(locator)
        highlight_element(self.page, element)
        element.click()

    def _validate_visible(self, locator, message):
        element = self._wait_visible(locator)
        assert element.is_visible(), message
        highlight_element(self.page, locator)

    def click_performance_tab(self):
        try:
            self._click(self.locators.PERFORMANCE_SECTION)
        except Exception as e:
            attach_screenshot(self.page, "Click Performance Tab Failed")
            print(f"Failed to click performance tab: {e}")

    def validate_reports_heading(self):
        try:
            self._validate_visible(
                self.locators.PLEASE_SELECT_HEADING,
                "Please select heading is not visible",
            )
        except Exception as e:
            attach_screenshot(self.page, "Validate Reports Heading Failed")
            print(f"Reports heading validation failed: {e}")

    def validate_program_name_dropdown_and_select_option(self):
        try:
            self._validate_visible(self.locators.PROGRAM_NAME, "Program Name label is not visible")
            self._click(self.locators.PROGRAM_COURSE)
            if "prod" in self.USER_TYPE:
                self._click(self.locators.PROGRAM_COURSE_OPTION_PROD)
            else:
                self._click(self.locators.PROGRAM_COURSE_OPTION_DEV)
        except Exception as e:
            attach_screenshot(self.page, "Validate Program Name Dropdown Failed")
            print(f"Program name dropdown validation failed: {e}")

    def validate_status_dropdown_and_select_option(self):
        try:
            self._validate_visible(self.locators.STATUS, "Status label is not visible")
            self._click(self.locators.STATUS_DROPDOWN)
            self._click(self.locators.STATUS_OPTION)
        except Exception as e:
            attach_screenshot(self.page, "Validate Status Dropdown Failed")
            print(f"Status dropdown validation failed: {e}")

    def validate_cohort_name_dropdown_and_select_option(self):
        try:
            self._validate_visible(self.locators.COHORT_NAME, "Cohort Name label is not visible")
            self._click(self.locators.COHORT_DROPDOWN)
            if "prod" in self.USER_TYPE:
                self._click(self.locators.COHORT_OPTION_PROD)
            else:
                self._click(self.locators.COHORT_OPTION_DEV)
        except Exception as e:
            attach_screenshot(self.page, "Validate Cohort Name Dropdown Failed")
            print(f"Cohort name dropdown validation failed: {e}")

    def validate_cohort_quiz_card_details_and_toggle_switch_button(self):
        try:
            self._validate_visible(
                self.locators.COHORT_QUIZ_SCORECARD,
                "Cohort Quiz Scorecard heading is not visible",
            )
            self._validate_visible(self.locators.QUIZ_STATUS, "Quiz Status text is not visible")
            self._click(self.locators.TOGGLE_SWITCH)
        except Exception as e:
            attach_screenshot(self.page, "Validate Cohort Quiz Card Failed")
            print(f"Cohort quiz card validation failed: {e}")

    def validate_milestone_card_details_and_milestone_toggle_switch_button(self):
        try:
            self._validate_visible(self.locators.MILESTONE_STATUS, "Milestone Status text is not visible")
            self._click(self.locators.MILESTONE_TOGGLE_SWITCH)
        except Exception as e:
            attach_screenshot(self.page, "Validate Milestone Card Failed")
            print(f"Milestone card validation failed: {e}")

    def click_download_cohort_performance_button(self):
        try:
            workspace_root = Path(__file__).resolve().parents[2]
            download_dir = workspace_root / "files" / "downloads"
            download_dir.mkdir(parents=True, exist_ok=True)

            with self.page.expect_download(timeout=30000) as download_info:
                self._click(self.locators.DOWNLOAD_COHORT_PERFORMANCE)

            download = download_info.value
            suggested_name = download.suggested_filename or f"cohort_performance_{strftime('%Y%m%d_%H%M%S')}.xlsx"
            saved_file = download_dir / suggested_name
            download.save_as(str(saved_file))

            assert saved_file.exists(), f"Downloaded file not found: {saved_file}"
            assert saved_file.stat().st_size > 0, f"Downloaded file is empty: {saved_file}"
            print(f"Download verified: {saved_file}")

            saved_file.unlink(missing_ok=True)
            print(f"Downloaded file deleted after verification: {saved_file}")
        except Exception as e:
            attach_screenshot(self.page, "Click Download Cohort Performance Failed")
            print(f"Failed to click download cohort performance button: {e}")
