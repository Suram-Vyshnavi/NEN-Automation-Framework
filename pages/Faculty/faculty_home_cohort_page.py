from locators.faculty_locators.home_cohort_locators import home_cohort_locators
from locators.common.header_locators import HeaderLocators
from utils.helpers import attach_screenshot, highlight_element
from datetime import datetime
import calendar


class FacultyHomeCohortPage:
    def __init__(self, page):
        self.page = page
        self.locators = home_cohort_locators()
        self.header_locators = HeaderLocators()


    def validate_cohorts_heading(self):
        try:
            cohorts_header = self.page.locator(self.locators.COHORTS_HEADER)
            cohorts_header.wait_for(state="visible", timeout=15000)
            assert cohorts_header.is_visible(), "Cohorts heading is not visible"
            highlight_element(self.page, self.locators.COHORTS_HEADER)
        except Exception as e:
            attach_screenshot(self.page, "Cohorts Heading Validation Failed")
            print(f"Cohorts heading validation failed: {e}")
    def click_active_tab(self):
        try:
            active_tab = self.page.locator(self.locators.ACTIVE_TAB)
            active_tab.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.ACTIVE_TAB)
        except Exception as e:
            attach_screenshot(self.page, "Click Active Tab Failed")
            print(f"Failed to click active tab: {e}")
    def click_first_active_cohort(self):
        try:
            cohort = self.page.locator(self.locators.SELECT_COHORT)
            cohort.wait_for(state="visible", timeout=15000)
            self.page.click(self.locators.SELECT_COHORT)
        except Exception as e:
            attach_screenshot(self.page, "Click First Active Cohort Failed")
            print(f"Failed to click first active cohort: {e}")
    def validate_all_tabs_in_cohort_page(self):
        try:
            tabs = [
                (self.locators.COHORT_DASHBOARD_TAB, "Cohort Dashboard"),
                (self.locators.SCORE_CARD_TAB, "Scorecard"),
                (self.locators.GENERAL_INFO_TAB, "General Info"),
                (self.locators.RELEASE_MILESTONE_TAB, "Release Milestone"),
                (self.locators.COHORT_VENTURES_TAB, "Cohort Ventures"),
                (self.locators.COHORT_MEMBERS_TAB, "Cohort Members"),
            ]
            for locator, tab_name in tabs:
                tab_element = self.page.locator(locator)
                tab_element.wait_for(state="visible", timeout=10000)
                assert tab_element.is_visible(), f"{tab_name} tab is not visible"
                tab_element.click()
                highlight_element(self.page, locator)

                if tab_name == "Cohort Dashboard":
                    download_btn = self.page.locator(self.locators.VALIDATE_DOWNLOAD_EXCEL)
                    download_btn.wait_for(state="visible", timeout=10000)
                    assert download_btn.is_visible(), "Download Excel button is not visible"
                    highlight_element(self.page, self.locators.VALIDATE_DOWNLOAD_EXCEL)

                elif tab_name == "General Info":
                    add_faculty_btn = self.page.locator(self.locators.VALIDATE_ADD_FACULTY_BUTTON)
                    add_faculty_btn.wait_for(state="visible", timeout=10000)
                    assert add_faculty_btn.is_visible(), "Add Faculty button is not visible"
                    highlight_element(self.page, self.locators.VALIDATE_ADD_FACULTY_BUTTON)
            self.page.go_back()
        except Exception as e:
            attach_screenshot(self.page, "Validate All Tabs in Cohort Page Failed")
            print(f"Validate all tabs in cohort page failed: {e}")
    def validate_pagination(self):
        try:
            page_2 = self.page.locator(self.locators.PAGE_NUMBER)
            page_2.wait_for(state="visible", timeout=10000)
            assert page_2.is_visible(), "Pagination page 2 is not visible"
            highlight_element(self.page, self.locators.PAGE_NUMBER)
            self.page.click(self.locators.PAGE_NUMBER)
        except Exception as e:
            attach_screenshot(self.page, "Pagination Validation Failed")
            print(f"Pagination validation failed: {e}")
    def click_inactive_tab(self):
        try:
            home_header = self.page.locator(self.header_locators.HOME_HEADER)
            home_header.wait_for(state="visible", timeout=10000)
            self.page.click(self.header_locators.HOME_HEADER)

            inactive_tab = self.page.locator(self.locators.INACTIVE_TAB)
            inactive_tab.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.INACTIVE_TAB)
        except Exception as e:
            attach_screenshot(self.page, "Click Inactive Tab Failed")
            print(f"Failed to click inactive tab: {e}")
    def search_for_test_cohort(self):
        try:
            search_input = self.page.locator(self.locators.SEARCH_COHORT)
            search_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.SEARCH_COHORT, "Test")
        except Exception as e:
            attach_screenshot(self.page, "Search for Test Cohort Failed")
            print(f"Failed to search for test cohort: {e}")
    def click_create_new_cohort_button(self):
        try:
            create_btn = self.page.locator(self.locators.CREATE_NEW_ACCOUNT_BUTTON)
            create_btn.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.CREATE_NEW_ACCOUNT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Click Create New Cohort Button Failed")
            print(f"Failed to click create new cohort button: {e}")
    def fill_all_details_and_create_cohort(self):
        try:
            cohort_heading = self.page.locator(self.locators.COHORT_DETAILS_HEADING)
            cohort_heading.wait_for(state="visible", timeout=15000)
            assert cohort_heading.is_visible(), "Cohort Details heading is not visible"

            institute_dropdown = self.page.locator(self.locators.INSTITUTE_DETAILS_DROPDOWN)
            institute_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.INSTITUTE_DETAILS_DROPDOWN)
            self.page.locator(self.locators.SELECT_INSTITUTE_DETAILS).wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_INSTITUTE_DETAILS)

            delivery_dropdown = self.page.locator(self.locators.DELIVERY_MODEL_DROPDOWN)
            delivery_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.DELIVERY_MODEL_DROPDOWN)
            self.page.locator(self.locators.SELECT_DELIVERY_MODEL).wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_DELIVERY_MODEL)

            course_dropdown = self.page.locator(self.locators.SELECT_COURSE_DROPDOWN)
            course_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_COURSE_DROPDOWN)
            self.page.locator(self.locators.SELECT_COURSE_OPTION).wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_COURSE_OPTION)

            stage_dropdown = self.page.locator(self.locators.SELECT_STAGE_DROPDOWN)
            stage_dropdown.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_STAGE_DROPDOWN)
            self.page.locator(self.locators.SELECT_STAGE_OPTION).wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SELECT_STAGE_OPTION)

            cohort_name_input = self.page.locator(self.locators.COHORT_NAME)
            cohort_name_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.COHORT_NAME, "Test")

            startdate = self.page.locator(self.locators.START_DATE)
            startdate.wait_for(state="visible", timeout=10000)
            startdate.click()
            # Pick a genuinely visible day cell to avoid hidden calendar panel matches.


            today = datetime.now()

            last_day = calendar.monthrange(today.year, today.month)[1]

            if today.day == last_day:
                selectstartdate = self.page.locator(self.locators.SELECT_START_DATE_LAST)
            else:
                selectstartdate = self.page.locator(self.locators.SELECT_START_DATE)
            selectstartdate.wait_for(state="visible", timeout=10000)
            selectstartdate.click()

            enddate = self.page.locator(self.locators.END_DATE)
            enddate.wait_for(state="visible", timeout=10000)
            enddate.click()
            # Some date pickers keep duplicate hidden panels in DOM; click only visible cells.
            selectenddate = self.page.locator(self.locators.SELECT_END_DATE)
            selectenddate.wait_for(state="visible", timeout=10000)
            selectenddate.click()


            max_students = self.page.locator(self.locators.MAX_STUDENTS_ALLOWED)
            max_students.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.MAX_STUDENTS_ALLOWED, "50")

            max_per_venue = self.page.locator(self.locators.MAX_STUDENTS_ALLOWED_PER_VENUE)
            max_per_venue.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.MAX_STUDENTS_ALLOWED_PER_VENUE, "5")

            save_next_btn = self.page.locator(self.locators.SAVE_NEXT)
            save_next_btn.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SAVE_NEXT)

            copy_code_btn = self.page.locator(self.locators.COPY_COHORT_CODE)
            copy_code_btn.wait_for(state="visible", timeout=15000)
            assert copy_code_btn.is_visible(), "Copy Cohort Code button is not visible after creation"
            highlight_element(self.page, self.locators.COPY_COHORT_CODE)
        except Exception as e:
            attach_screenshot(self.page, "Fill All Details and Create Cohort Failed")
            print(f"Failed to fill all details and create cohort: {e}")
    def click_latest_created_cohort_and_close(self):
        """Click on the latest created cohort and close the cohort"""
        try:
            latest_cohort = self.page.locator(self.locators.FIRST_COHORT_CODE)
            latest_cohort.wait_for(state="visible", timeout=10000)
            latest_cohort.click()

            more_options = self.page.locator(self.locators.COHORT_MORE_OPTIONS)
            more_options.wait_for(state="visible", timeout=10000)
            more_options.click()

            close_cohort = self.page.locator(self.locators.CLOSE_COHORT)
            close_cohort.wait_for(state="visible", timeout=10000)
            close_cohort.click()

            confirm_close = self.page.locator(self.locators.CLOSE_COHORT_CONFIRM)
            confirm_close.wait_for(state="visible", timeout=10000)
            confirm_close.click()
        except Exception as e:
            attach_screenshot(self.page, "Click Latest Created Cohort and Close Failed")
            print(f"Failed to click latest created cohort and close: {e}")
