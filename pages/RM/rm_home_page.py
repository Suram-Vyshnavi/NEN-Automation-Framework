from locators.rm_locators import home_page_locators as rm_locators
from utils.helpers import attach_screenshot, highlight_element
from datetime import datetime, timedelta
import re


class RMHomePage:
    def __init__(self, page):
        self.page = page

    def navigate_to_home(self):
        try:
            home = self.page.locator(rm_locators.HOME)
            home.wait_for(state="visible", timeout=10000)
            home.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Navigate To Home Failed")
            print(f"RM navigate to home failed: {e}")

    def validate_cohorts_heading(self):
        try:
            heading = self.page.locator(rm_locators.ASSIGNED_COHORTS_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Assigned Cohorts heading is not visible"
            highlight_element(self.page, rm_locators.ASSIGNED_COHORTS_HEADING)
        except Exception as e:
            attach_screenshot(self.page, "RM Cohorts Heading Validation Failed")
            print(f"RM cohorts heading validation failed: {e}")

    def click_first_active_cohort(self):
        try:
            cohort = self.page.locator(rm_locators.SELECT_COHORT)
            cohort.first.wait_for(state="visible", timeout=15000)
            cohort.first.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click First Active Cohort Failed")
            print(f"RM click first active cohort failed: {e}")

    def validate_all_tabs_in_cohort_page(self):
        try:
            tabs = [
                (rm_locators.COHORT_DASHBOARD_TAB, "Cohort Dashboard"),
                (rm_locators.SCORE_CARD_TAB, "Scorecard"),
                (rm_locators.GENERAL_INFO_TAB, "General Info"),
                (rm_locators.RELEASE_MILESTONE_TAB, "Release Milestone"),
                (rm_locators.COHORT_VENTURES_TAB, "Cohort Ventures"),
                (rm_locators.COHORT_MEMBERS_TAB, "Cohort Members"),
            ]

            for locator, tab_name in tabs:
                tab = self.page.locator(locator)
                tab.first.wait_for(state="visible", timeout=10000)
                assert tab.first.is_visible(), f"{tab_name} tab is not visible"
                tab.first.click()
                highlight_element(self.page, locator)

                if tab_name == "Cohort Dashboard":
                    download = self.page.locator(rm_locators.VALIDATE_DOWNLOAD_EXCEL)
                    download.wait_for(state="visible", timeout=10000)
                    assert download.is_visible(), "Download excel button is not visible"
                    highlight_element(self.page, rm_locators.VALIDATE_DOWNLOAD_EXCEL)

                if tab_name == "General Info":
                    add_faculty = self.page.locator(rm_locators.VALIDATE_ADD_FACULTY_BUTTON)
                    add_faculty.wait_for(state="visible", timeout=10000)
                    assert add_faculty.is_visible(), "Add Faculty button is not visible"
                    highlight_element(self.page, rm_locators.VALIDATE_ADD_FACULTY_BUTTON)

            
        except Exception as e:
            attach_screenshot(self.page, "RM Validate All Tabs In Cohort Page Failed")
            print(f"RM validate all tabs in cohort page failed: {e}")

    def validate_pagination(self):
        try:
            homepage= self.page.locator(rm_locators.HOME)
            homepage.wait_for(state="visible", timeout=10000)
            homepage.click()
            
            page_2 = self.page.locator(rm_locators.PAGE_NUMBER)
            page_2.wait_for(state="visible", timeout=10000)
            assert page_2.is_visible(), "Pagination page 2 is not visible"
            highlight_element(self.page, rm_locators.PAGE_NUMBER)
            page_2.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Pagination Validation Failed")
            print(f"RM pagination validation failed: {e}")

    def click_release_milestones_tab(self):
        try:
            tab = self.page.locator(rm_locators.RELEASE_MILESTONE_TAB)
            tab.wait_for(state="visible", timeout=15000)
            tab.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Release Milestones Tab Failed")
            print(f"RM click release milestones tab failed: {e}")

    def click_milestone_and_extend_deadline(self):
        try:
            milestone = self.page.locator(rm_locators.RELEASE_MILESTONE)
            milestone.wait_for(state="visible", timeout=15000)
            milestone.click()

            checkbox = self.page.locator(rm_locators.CHECKBOX)
            checkbox.wait_for(state="visible", timeout=10000)
            checkbox.click()

            extract_date = self.page.locator(rm_locators.EXTRACT_SUBMISSION_DATE)
            extract_date.wait_for(state="visible", timeout=10000)
            submission_date = extract_date.inner_text()

            extend = self.page.locator(rm_locators.EXTEND_DEADLINE)
            extend.wait_for(state="visible", timeout=10000)
            extend.click()

            deadline_input = self.page.locator(rm_locators.SUBMISSION_DEADLINE_INPUT)
            deadline_input.wait_for(state="visible", timeout=10000)
            deadline_input.click()

            extended_submissiondate=self.extract_submission_date(submission_date)
            deadline_input_click=self.page.locator(rm_locators.submission_deadline_date(extended_submissiondate))
            deadline_input_click.wait_for(state="visible", timeout=10000)
            deadline_input_click.click()

            ok_btn = self.page.locator(rm_locators.OK_BUTTON)
            if ok_btn.count() > 0:
                ok_btn.click()

            update_btn = self.page.locator(rm_locators.UPDATE_BUTTON)
            if update_btn.count() > 0:
                update_btn.click()
        except Exception as e:
            attach_screenshot(self.page, "RM Click Milestone And Extend Deadline Failed")
            print(f"RM click milestone and extend deadline failed: {e}")
            self.page.go_back()

    def click_refresh_button(self):
        try:
            refresh = self.page.locator(rm_locators.REFRESH_BUTTON)
            refresh.wait_for(state="visible", timeout=10000)
            refresh.click()
            
        except Exception as e:
            attach_screenshot(self.page, "RM Click Refresh Button Failed")
            print(f"RM click refresh button failed: {e}")
            self.page.go_back()

    def extract_submission_date(self,current_submission_date):
        #format 1 08 Apr, 26
        # final format 2026-04-09
        try:
            # Handle noisy text by extracting only the expected date token.
            match = re.search(r"\b\d{1,2}\s+[A-Za-z]{3},\s*\d{2}\b", str(current_submission_date))
            date_text = match.group(0) if match else str(current_submission_date).strip()

            parsed_date = datetime.strptime(date_text, "%d %b, %y")
            next_date = parsed_date + timedelta(days=1)
            return next_date.strftime("%Y-%m-%d")
        except Exception as e:
            attach_screenshot(self.page, "RM Extract Submission Date Failed")
            print(f"RM extract submission date failed: {e}")
            return ""
        

        
        
