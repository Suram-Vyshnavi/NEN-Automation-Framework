from datetime import datetime

from locators.Incubator_locators.cohort_home_locators import cohort_home_locators
from utils.helpers import attach_screenshot, highlight_element


class IncubatorCohortHomePage:
    def __init__(self, page):
        self.page = page
        self.locators = cohort_home_locators()

    def _wait_and_click(self, locator, timeout=15000):
        element = self.page.locator(locator)
        element.first.wait_for(state="visible", timeout=timeout)
        element.first.click()
        return element.first

    def _wait_and_fill(self, locator, value, timeout=15000):
        element = self.page.locator(locator)
        element.first.wait_for(state="visible", timeout=timeout)
        element.first.fill(str(value))
        return element.first

    def _fill_number_input(self, index, value, timeout=15000):
        number_input = self.page.locator(self.locators.ADD_NUMBER_INPUT).nth(index)
        number_input.wait_for(state="visible", timeout=timeout)
        number_input.fill(str(value))

    def _select_date_from_picker(self, input_locator, date_locator, timeout=15000):
        self._wait_and_click(input_locator, timeout=timeout)
        date_element = self.page.locator(date_locator)
        if date_element.count() > 0:
            date_element.first.wait_for(state="visible", timeout=timeout)
            date_element.first.click()
        else:
            self.page.keyboard.press("Enter")

    def click_cohorts_tab(self):
        try:
            self._wait_and_click(self.locators.COHORTS)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Cohorts Tab Failed")
            print(f"Incubator click cohorts tab failed: {exc}")

    def validate_cohorts_heading(self):
        try:
            heading = self.page.locator(self.locators.COHORTS_HEADING)
            heading.first.wait_for(state="visible", timeout=15000)
            assert heading.first.is_visible(), "Cohorts heading is not visible"
            highlight_element(self.page, self.locators.COHORTS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Cohorts Heading Validation Failed")
            print(f"Incubator cohorts heading validation failed: {exc}")

    def click_active_tab(self):
        try:
            self._wait_and_click(self.locators.ACTIVE_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Active Tab Failed")
            print(f"Incubator click active tab failed: {exc}")

    def click_first_active_cohort(self):
        try:
            self._wait_and_click(self.locators.SELECT_COHORT)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click First Active Cohort Failed")
            print(f"Incubator click first active cohort failed: {exc}")

    def validate_all_tabs_in_cohort_page(self):
        try:
            tabs = [
                self.locators.COHORT_DASHBOARD_TAB,
                self.locators.GENERAL_INFO_TAB,
                self.locators.COHORT_MEMBERS_TAB,
                self.locators.COHORT_STARTUPS,
            ]
            for tab_locator in tabs:
                tab = self.page.locator(tab_locator)
                tab.first.wait_for(state="visible", timeout=15000)
                assert tab.first.is_visible(), f"Tab is not visible: {tab_locator}"
                tab.first.click()
                highlight_element(self.page, tab_locator)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Cohort Tabs Failed")
            print(f"Incubator validate cohort tabs failed: {exc}")

    def click_general_info_tab(self):
        try:
            self._wait_and_click(self.locators.GENERAL_INFO_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click General Info Tab Failed")
            print(f"Incubator click general info tab failed: {exc}")

    def validate_batch_faculty_and_message_icon(self):
        try:
            faculty_label = self.page.locator(self.locators.BATCH_FACULTY)
            faculty_label.first.wait_for(state="visible", timeout=15000)
            assert faculty_label.first.is_visible(), "Batch Faculty heading is not visible"

            faculty_container = self.page.locator(self.locators.BATCH_FACULTY_CONTAINER)
            faculty_container.first.wait_for(state="visible", timeout=15000)
            assert faculty_container.first.is_visible(), "Batch faculty/message icon container is not visible"

            highlight_element(self.page, self.locators.BATCH_FACULTY)
            highlight_element(self.page, self.locators.BATCH_FACULTY_CONTAINER)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Batch Faculty Validation Failed")
            print(f"Incubator batch faculty validation failed: {exc}")

    def validate_cohort_activity(self):
        try:
            activity_locator = getattr(self.locators, "COHORT_ACTIVITY", None)
            assert activity_locator, "COHORT_ACTIVITY locator is not defined in cohort_home_locators"

            activity = self.page.locator(activity_locator)
            activity.first.wait_for(state="visible", timeout=15000)
            assert activity.first.is_visible(), "Cohort Activity section is not visible"
            highlight_element(self.page, activity_locator)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Cohort Activity Validation Failed")
            print(f"Incubator cohort activity validation failed: {exc}")

    def click_cohort_members_tab(self):
        try:
            self._wait_and_click(self.locators.COHORT_MEMBERS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Cohort Members Tab Failed")
            print(f"Incubator click cohort members tab failed: {exc}")

    def validate_cohort_members_heading(self):
        try:
            members_count = self.page.locator(self.locators.COHORT_MEMBERS_COUNT)
            members_count.first.wait_for(state="visible", timeout=15000)
            assert members_count.first.is_visible(), "Cohort Members heading is not visible"
            highlight_element(self.page, self.locators.COHORT_MEMBERS_COUNT)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Cohort Members Heading Validation Failed")
            print(f"Incubator cohort members heading validation failed: {exc}")

    def validate_student_added_and_max_allowed_students_details(self):
        try:
            students_added = self.page.locator(self.locators.COHORT_MEMBERS_SECTION_TITLE)
            students_added.first.wait_for(state="visible", timeout=15000)
            assert students_added.first.is_visible(), "Student added details are not visible"

            max_allowed = self.page.locator(self.locators.COHORT_MEMBERS_SECTION_SUBTITLE)
            max_allowed.first.wait_for(state="visible", timeout=15000)
            assert max_allowed.first.is_visible(), "Maximum allowed students details are not visible"

            highlight_element(self.page, self.locators.COHORT_MEMBERS_SECTION_TITLE)
            highlight_element(self.page, self.locators.COHORT_MEMBERS_SECTION_SUBTITLE)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Student Count Validation Failed")
            print(f"Incubator student/max allowed details validation failed: {exc}")

    def click_cohort_startups(self):
        try:
            self._wait_and_click(self.locators.COHORT_STARTUPS)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Cohort Startups Failed")
            print(f"Incubator click cohort startups failed: {exc}")

    def validate_cohort_startups_heading_and_startup_details(self):
        try:
            heading = self.page.locator(self.locators.COHORT_STARTUPS_COUNT)
            heading.first.wait_for(state="visible", timeout=15000)
            assert heading.first.is_visible(), "Cohort Startups heading is not visible"

            wf_link_button = self.page.locator(self.locators.WF_LINK_BUTTON)
            wf_link_button.first.wait_for(state="visible", timeout=15000)
            assert wf_link_button.first.is_visible(), "Startup details are not visible"

            highlight_element(self.page, self.locators.COHORT_STARTUPS_COUNT)
            highlight_element(self.page, self.locators.WF_LINK_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Cohort Startups Validation Failed")
            print(f"Incubator cohort startups validation failed: {exc}")

    def click_first_cohort_startup(self):
        try:
            self._wait_and_click(self.locators.WF_LINK_BUTTON)
            self.page.go_back()
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click First Cohort Startup Failed")
            print(f"Incubator click first cohort startup failed: {exc}")
            self.page.go_back()

    def click_inactive_tab(self):
        try:
            self._wait_and_click(self.locators.INACTIVE_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Inactive Tab Failed")
            print(f"Incubator click inactive tab failed: {exc}")

    def search_for_test_cohort_in_cohorts(self):
        try:
            self._wait_and_fill(self.locators.SEARCH_INPUT, "test cohort")
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Search Test Cohort Failed")
            print(f"Incubator search test cohort failed: {exc}")

    def click_create_new_cohort_button(self):
        try:
            self._wait_and_click(self.locators.CREATE_NEW_COHORT)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Create New Cohort Failed")
            print(f"Incubator click create new cohort failed: {exc}")

    def fill_all_details_and_create_cohort(self):
        try:
            timestamp = datetime.now().strftime("%d%m%H%M")
            batch_name = f"test cohort {timestamp}"

            self._wait_and_fill(self.locators.BATCH_NAME_INPUT, batch_name)

            start_date_input = self.page.locator(self.locators.START_DATE_INPUT)
            start_date_input.wait_for(state="visible", timeout=15000)
            start_date_input.click(force=True)
            start_date = self.page.locator(self.locators.SELECT_START_DATE)
            start_date.wait_for(state="visible", timeout=15000)
            start_date.click(force=True)

            end_date_input = self.page.locator(self.locators.END_DATE_INPUT)
            end_date_input.wait_for(state="visible", timeout=15000)
            end_date_input.click()
            end_date = self.page.locator(self.locators.SELECT_END_DATE)
            end_date.wait_for(state="visible", timeout=15000)
            end_date.click(force=True)

            max_students_container = self.page.locator(self.locators.SELECT_MAX_STUDENTS_ALLOWED_NUMBER)
            max_students_container.wait_for(state="visible", timeout=15000)
            max_students_container.fill("50")

            max_per_startup_container = self.page.locator(self.locators.SELECT_MAX_STUDENTS_ALLOWED_PER_STARTUP)
            max_per_startup_container.wait_for(state="visible", timeout=15000)
            max_per_startup_container.fill("5")

            self._wait_and_click(self.locators.CREATE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Fill Cohort Details Failed")
            print(f"Incubator fill cohort details failed: {exc}")

    def validate_office_hours_section_in_cohort_page(self):
        try:
            office_hours = self.page.locator(self.locators.OFFICE_HOURS_HEADING)
            office_hours.wait_for(state="visible", timeout=15000)
            assert office_hours.is_visible(), "Office Hours section is not visible"
            highlight_element(self.page, self.locators.OFFICE_HOURS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Office Hours Validation Failed")
            print(f"Incubator office hours validation failed: {exc}")

    def click_create_button(self):
        try:
            create_btn = self.page.locator(self.locators.OFFICE_CREATE_BUTTON)
            create_btn.wait_for(state="visible", timeout=15000)
            if create_btn.is_enabled():
                create_btn.click()
            else:
                self.page.keyboard.press("Tab")
                self.page.keyboard.press("Enter")
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Create Button Failed")
            print(f"Incubator click create button failed: {exc}")

    def fill_all_details_and_create_meeting(self):
        try:
            session_title = self.page.locator(self.locators.SESSION_TITLE_INPUT)
            if session_title.count() > 0:
                session_title.first.wait_for(state="visible", timeout=15000)
                session_title.first.fill("test")
            else:
                self.page.keyboard.type("test")

            self._select_date_from_picker(self.locators.SELECT_DATE_INPUT, self.locators.SELECT_START_DATE)
            self._select_date_from_picker(self.locators.SELECT_DATE_INPUT, self.locators.SELECT_TODAY_DATE)


            time_input = self.page.locator(self.locators.SELECT_TIME_INPUT)
            time_input.first.wait_for(state="visible", timeout=15000)
            time_input.first.click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            checkbox = self.page.locator(self.locators.CHECKBOX_INPUT)
            checkbox.first.wait_for(state="visible", timeout=15000)
            if not checkbox.first.is_checked():
                checkbox.first.check()

            self._wait_and_click(self.locators.CREATE_MEETING_BUTTON)
            self._wait_and_click(self.locators.OKAY_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Fill Meeting Details Failed")
            print(f"Incubator fill meeting details failed: {exc}")

    def delete_created_meeting(self):
        try:
            meeting_card = self.page.locator(self.locators.OFFICE_HOURS_MEETING_CARD)
            meeting_card.first.wait_for(state="visible", timeout=15000)
            highlight_element(self.page, self.locators.OFFICE_HOURS_MEETING_CARD)

            meeting_title = self.page.locator(self.locators.MEETING_TITLE)
            meeting_title.first.wait_for(state="visible", timeout=15000)
            highlight_element(self.page, self.locators.MEETING_TITLE)
            self._wait_and_click(self.locators.MEETING_TITLE)

            self._wait_and_click(self.locators.DELETE_ICON)

            radio_check = self.page.locator(self.locators.RADIO_CHECK)
            radio_check.wait_for(state="visible", timeout=15000)
            if not radio_check.is_checked():
                radio_check.check()

            reason_to_cancel = self.page.locator(self.locators.REASON_TO_CANCEL)
            if reason_to_cancel.count() > 0:
                reason_to_cancel.wait_for(state="visible", timeout=15000)
                reason_to_cancel.click()

            self._wait_and_click(self.locators.CANCEL_MEETING_BUTTON)
            self._wait_and_click(self.locators.GO_BACK_TO_DASHBOARD_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Delete Meeting Failed")
            print(f"Incubator delete meeting failed: {exc}")
            self._wait_and_click(self.locators.GO_BACK_TO_DASHBOARD_BUTTON)

    # def go_back_to_dashboard(self):
    #     try:
    #         go_back_button = self.page.locator(self.locators.GO_BACK_TO_DASHBOARD_BUTTON)
    #         go_back_button.wait_for(state="visible", timeout=15000)
    #         go_back_button.click()
    #         self._wait_and_click(self.locators.GO_BACK_TO_DASHBOARD_BUTTON)
    #     except Exception as exc:
    #         attach_screenshot(self.page, "Incubator Go Back To Dashboard Failed")
    #         print(f"Incubator go back to dashboard failed: {exc}")
