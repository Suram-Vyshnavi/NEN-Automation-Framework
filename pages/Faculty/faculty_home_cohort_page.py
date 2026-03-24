from locators.faculty_locators.home_cohort_locators import home_cohort_locators
from utils.helpers import attach_screenshot, highlight_element


class FacultyHomeCohortPage:
    def __init__(self, page):
        self.page = page
        self.locators = home_cohort_locators()

    def validate_cohorts_heading(self):
        """Validate that the Cohorts heading is visible on the home page"""
        cohorts_header = self.page.locator(self.locators.COHORTS_HEADER)
        cohorts_header.wait_for(state="visible", timeout=15000)
        assert cohorts_header.is_visible(), "Cohorts heading is not visible"
        highlight_element(self.page, self.locators.COHORTS_HEADER)
        attach_screenshot(self.page, "Cohorts Heading Validated")

    def click_active_tab(self):
        """Click on the Active tab in Cohorts section"""
        active_tab = self.page.locator(self.locators.ACTIVE_TAB)
        active_tab.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.ACTIVE_TAB)
        attach_screenshot(self.page, "Clicked Active Tab")

    def click_first_active_cohort(self):
        """Click on the first active cohort from the list"""
        cohort = self.page.locator(self.locators.SELECT_COHORT)
        cohort.wait_for(state="visible", timeout=15000)
        self.page.click(self.locators.SELECT_COHORT)
        attach_screenshot(self.page, "Clicked First Active Cohort")

    def validate_all_tabs_in_cohort_page(self):
        """Validate all tabs available in cohort dashboard page"""
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
            tab_element.click()  # Click on the tab to ensure it's working
            highlight_element(self.page, locator)
            attach_screenshot(self.page, f"{tab_name} Tab Validated")
        
            if tab_name == "Cohort Dashboard":
                download_btn = self.page.locator(self.locators.VALIDATE_DOWNLOAD_EXCEL)
                download_btn.wait_for(state="visible", timeout=10000)
                assert download_btn.is_visible(), "Download Excel button is not visible"
                highlight_element(self.page, self.locators.VALIDATE_DOWNLOAD_EXCEL)
                attach_screenshot(self.page, "Download Excel Button Validated")

            elif tab_name == "General Info":
                add_faculty_btn = self.page.locator(self.locators.VALIDATE_ADD_FACULTY_BUTTON)
                add_faculty_btn.wait_for(state="visible", timeout=10000)
                assert add_faculty_btn.is_visible(), "Add Faculty button is not visible"
                highlight_element(self.page, self.locators.VALIDATE_ADD_FACULTY_BUTTON)
                attach_screenshot(self.page, "Add Faculty Button Validated")
        self.page.go_back()  # Navigate back to the cohort list page after validation

    def validate_pagination(self):
        """Validate pagination by clicking on page 2"""
        page_2 = self.page.locator(self.locators.PAGE_NUMBER)
        page_2.wait_for(state="visible", timeout=10000)
        assert page_2.is_visible(), "Pagination page 2 is not visible"
        highlight_element(self.page, self.locators.PAGE_NUMBER)
        self.page.click(self.locators.PAGE_NUMBER)
        attach_screenshot(self.page, "Pagination - Clicked Page 2")

    def click_inactive_tab(self):
        """Navigate to home and click on the Inactive tab in Cohorts section"""
        home_header = self.page.locator(self.locators.HOME_HEADER)
        home_header.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.HOME_HEADER)
        attach_screenshot(self.page, "Navigated Back to Home Page")

        inactive_tab = self.page.locator(self.locators.INACTIVE_TAB)
        inactive_tab.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.INACTIVE_TAB)
        attach_screenshot(self.page, "Clicked Inactive Tab")

    def search_for_test_cohort(self):
        """Search for a test cohort using the search input"""
        search_input = self.page.locator(self.locators.SEARCH_COHORT)
        search_input.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.SEARCH_COHORT, "Test")
        attach_screenshot(self.page, "Searched for Test Cohort")

    def click_create_new_cohort_button(self):
        """Click on the Create New Cohort button"""
        create_btn = self.page.locator(self.locators.CREATE_NEW_ACCOUNT_BUTTON)
        create_btn.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.CREATE_NEW_ACCOUNT_BUTTON)
        attach_screenshot(self.page, "Clicked Create New Cohort Button")

    def fill_all_details_and_create_cohort(self):
        """Fill all required details and create a new cohort"""
        # Validate cohort details heading
        cohort_heading = self.page.locator(self.locators.COHORT_DETAILS_HEADING)
        cohort_heading.wait_for(state="visible", timeout=15000)
        assert cohort_heading.is_visible(), "Cohort Details heading is not visible"
        attach_screenshot(self.page, "Cohort Details Form Opened")

        # Select Institute
        institute_dropdown = self.page.locator(self.locators.INSTITUTE_DETAILS_DROPDOWN)
        institute_dropdown.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.INSTITUTE_DETAILS_DROPDOWN)
        self.page.locator(self.locators.SELECT_INSTITUTE_DETAILS).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_INSTITUTE_DETAILS)
        attach_screenshot(self.page, "Institute Selected")

        # Select Delivery Model
        delivery_dropdown = self.page.locator(self.locators.DELIVERY_MODEL_DROPDOWN)
        delivery_dropdown.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.DELIVERY_MODEL_DROPDOWN)
        self.page.locator(self.locators.SELECT_DELIVERY_MODEL).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_DELIVERY_MODEL)
        attach_screenshot(self.page, "Delivery Model Selected")

        # Select Course
        course_dropdown = self.page.locator(self.locators.SELECT_COURSE_DROPDOWN)
        course_dropdown.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_COURSE_DROPDOWN)
        self.page.locator(self.locators.SELECT_COURSE_OPTION).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_COURSE_OPTION)
        attach_screenshot(self.page, "Course Selected")

        # Select Stage
        stage_dropdown = self.page.locator(self.locators.SELECT_STAGE_DROPDOWN)
        stage_dropdown.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_STAGE_DROPDOWN)
        self.page.locator(self.locators.SELECT_STAGE_OPTION).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_STAGE_OPTION)
        attach_screenshot(self.page, "Stage Selected")

        # Enter Cohort Name
        cohort_name_input = self.page.locator(self.locators.COHORT_NAME)
        cohort_name_input.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.COHORT_NAME, "Test")
        attach_screenshot(self.page, "Cohort Name Entered")

        # Select Start Date
        start_date_input = self.page.locator(self.locators.START_DATE)
        start_date_input.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.START_DATE)
        self.page.locator(self.locators.SELECT_START_DATE).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_START_DATE)
        attach_screenshot(self.page, "Start Date Selected")

        # Select End Date
        end_date_input = self.page.locator(self.locators.END_DATE)
        end_date_input.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.END_DATE)
        self.page.locator(self.locators.SELECT_END_DATE).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SELECT_END_DATE)
        attach_screenshot(self.page, "End Date Selected")

        # Enter Max Students Allowed
        max_students = self.page.locator(self.locators.MAX_STUDENTS_ALLOWED)
        max_students.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.MAX_STUDENTS_ALLOWED, "50")
        attach_screenshot(self.page, "Max Students Entered")

        # Enter Max Students Allowed Per Venue
        max_per_venue = self.page.locator(self.locators.MAX_STUDENTS_ALLOWED_PER_VENUE)
        max_per_venue.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.MAX_STUDENTS_ALLOWED_PER_VENUE, "5")
        attach_screenshot(self.page, "Max Students Per Venue Entered")

        # Click Save & Next
        save_next_btn = self.page.locator(self.locators.SAVE_NEXT)
        save_next_btn.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SAVE_NEXT)
        attach_screenshot(self.page, "Clicked Save and Next")

        # Validate Copy Cohort Code button appears after creation
        copy_code_btn = self.page.locator(self.locators.COPY_COHORT_CODE)
        copy_code_btn.wait_for(state="visible", timeout=15000)
        assert copy_code_btn.is_visible(), "Copy Cohort Code button is not visible after creation"
        highlight_element(self.page, self.locators.COPY_COHORT_CODE)
        attach_screenshot(self.page, "New Cohort Created Successfully")
