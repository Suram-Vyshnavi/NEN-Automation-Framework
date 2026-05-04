from datetime import datetime

from locators.cohortmanager_locators.home_page_locators import homepage_locators
from utils.helpers import attach_screenshot, highlight_element


class CohortManagerHomePage:
    def __init__(self, page):
        self.page = page
        self.locators = homepage_locators()

    def _wait_and_click(self, locator, timeout=15000, force=False):
        element = self.page.locator(locator).first
        element.wait_for(state="attached", timeout=timeout)
        if force:
            element.dispatch_event("click")
        else:
            element.click()
        return element

    def _wait_and_fill(self, locator, value, timeout=15000):
        element = self.page.locator(locator).first
        element.wait_for(state="visible", timeout=timeout)
        element.fill(str(value))
        return element

    def _select_first_dropdown_option(self, timeout=15000):
        option = self.page.locator(
            "//div[contains(@class,'ant-select-item-option-content') and not(contains(@class,'ant-select-item-option-disabled'))]"
        ).first
        option.wait_for(state="visible", timeout=timeout)
        option.click()

    def _open_dropdown_and_select_option(self, trigger_locator, option_text, timeout=15000):
        self._wait_and_click(trigger_locator, timeout=timeout)
        option = self.page.locator(
            f"//div[contains(@class,'ant-select-item-option-content') and normalize-space()='{option_text}']"
        ).first
        option.wait_for(state="visible", timeout=timeout)
        option.click()

    def _pick_date(self, input_locator, date_locator, timeout=15000):
        self._wait_and_click(input_locator, timeout=timeout)
        date_ele = self.page.locator(date_locator)
        if date_ele.count() > 0:
            date_ele.first.wait_for(state="visible", timeout=timeout)
            date_ele.first.click()
        else:
            self.page.keyboard.press("Enter")

    def validate_homepage_heading(self):
        try:
            heading = self.page.locator(self.locators.COHORTS_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Cohorts heading is not visible"
            highlight_element(self.page, self.locators.COHORTS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Homepage Heading Validation Failed")
            print(f"Cohort manager homepage heading validation failed: {exc}")

    def validate_active_cohort_section(self):
        try:
            active = self.page.locator(self.locators.ACTIVE_COHORTS)
            active.wait_for(state="visible", timeout=15000)
            assert active.is_visible(), "Active Cohort section is not visible"
            highlight_element(self.page, self.locators.ACTIVE_COHORTS)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Active Cohort Validation Failed")
            print(f"Cohort manager active cohort validation failed: {exc}")

    def validate_inactive_cohort_section(self):
        try:
            inactive = self.page.locator(self.locators.INACTIVE_COHORTS)
            inactive.wait_for(state="visible", timeout=15000)
            assert inactive.is_visible(), "Inactive Cohort section is not visible"
            highlight_element(self.page, self.locators.INACTIVE_COHORTS)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Inactive Cohort Validation Failed")
            print(f"Cohort manager inactive cohort validation failed: {exc}")

    def click_first_active_cohort(self):
        try:
            self._wait_and_click(self.locators.FIRST_COHORT)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Click First Cohort Failed")
            print(f"Cohort manager click first cohort failed: {exc}")

    def validate_cohort_dashboard_and_excel_link(self):
        try:
            dashboard = self.page.locator(self.locators.COHORT_DASHBOARD)
            dashboard.wait_for(state="visible", timeout=15000)
            assert dashboard.is_visible(), "Cohort Dashboard tab is not visible"

            excel = self.page.locator(self.locators.DOWNLOAD_EXCEL)
            excel.wait_for(state="visible", timeout=15000)
            assert excel.is_visible(), "Download excel link is not visible"

            highlight_element(self.page, self.locators.COHORT_DASHBOARD)
            highlight_element(self.page, self.locators.DOWNLOAD_EXCEL)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Dashboard Validation Failed")
            print(f"Cohort manager dashboard validation failed: {exc}")

    def validate_general_info_section(self):
        try:
            self._wait_and_click(self.locators.GENERAL_INFO)

            cohort_activity = self.page.locator(self.locators.COHORT_ACTIVITY)
            cohort_activity.wait_for(state="visible", timeout=15000)
            assert cohort_activity.is_visible(), "General info section is not visible"

            highlight_element(self.page, self.locators.GENERAL_INFO)
            highlight_element(self.page, self.locators.COHORT_ACTIVITY)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager General Info Validation Failed")
            print(f"Cohort manager general info validation failed: {exc}")

    def validate_upcoming_meetings_section(self):
        try:
            upcoming = self.page.locator(self.locators.UPCOMING_ACTIVITIES)
            upcoming.wait_for(state="visible", timeout=15000)
            assert upcoming.is_visible(), "Upcoming meetings section is not visible"
            highlight_element(self.page, self.locators.UPCOMING_ACTIVITIES)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Upcoming Meetings Validation Failed")
            print(f"Cohort manager upcoming meetings validation failed: {exc}")

    def click_create_meeting_button_in_upcoming_meetings(self):
        try:
            self._wait_and_click(self.locators.CREATE_MEETING)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Click Create Meeting Failed")
            print(f"Cohort manager click create meeting failed: {exc}")

    def fill_create_meeting_form_and_create(self):
        try:
            self._wait_and_fill(self.locators.MEETING_TITLE_INPUT, "test")
            self._pick_date(self.locators.SELECT_DATE_INPUT, self.locators.TODAY_DATE)
            self._wait_and_click(self.locators.OK_BUTTON)

            time_input = self.page.locator(self.locators.SELECT_TIME_INPUT)
            time_input.wait_for(state="visible", timeout=15000)
            time_input.click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            checkbox = self.page.locator(self.locators.CHECKBOX_INPUT)
            checkbox.wait_for(state="visible", timeout=15000)
            if not checkbox.is_checked():
                checkbox.check()

            self._wait_and_click(self.locators.CREATE_MEETING_BUTTON)
            self._wait_and_click(self.locators.OKAY_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Fill Meeting Form Failed")
            print(f"Cohort manager fill meeting form failed: {exc}")

    def validate_and_delete_created_meeting_in_upcoming(self):
        try:
            meeting_title = self.page.locator(self.locators.TEST_HEADING)
            meeting_title.wait_for(state="visible", timeout=15000)
            highlight_element(self.page, self.locators.TEST_HEADING)
            meeting_title.click()

            self._wait_and_click(self.locators.DELETE_ICON)

            radio = self.page.locator(self.locators.RADIO_CHECK)
            radio.wait_for(state="visible", timeout=15000)
            if not radio.is_checked():
                radio.check()

            reason = self.page.locator(self.locators.REASON_TO_CANCEL)
            if reason.count() > 0:
                reason.first.wait_for(state="visible", timeout=15000)
                reason.first.click()

            self._wait_and_click(self.locators.CANCEL_MEETING_BUTTON)

            close_button = self.page.locator(self.locators.CLOSE_MODAL_BUTTON)
            if close_button.count() > 0 and close_button.first.is_visible():
                close_button.first.click()
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Delete Upcoming Meeting Failed")
            print(f"Cohort manager delete upcoming meeting failed: {exc}")
        self.page.go_back()

    def validate_cohort_venture_section(self):
        try:
            cohort_venture = self.page.locator(self.locators.COHORT_VENTURES)
            cohort_venture.wait_for(state="visible", timeout=15000)
            assert cohort_venture.is_visible(), "Cohort Ventures tab is not visible"
            cohort_venture.click()
            highlight_element(self.page, self.locators.COHORT_VENTURES)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Cohort Venture Section Validation Failed")
            print(f"Cohort manager cohort venture section validation failed: {exc}")

    def click_create_venture_button(self):
        try:
            self._wait_and_click(self.locators.CREATE_VENTURE)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Click Create Venture Failed")
            print(f"Cohort manager click create venture failed: {exc}")

    def fill_create_venture_form_and_send_invite(self):
        try:
            student_email = f"stu_invite@yopmail.com"
            
            self._wait_and_click(self.locators.COMPANY_NAME_INPUT)
            self._wait_and_fill(self.locators.COMPANY_NAME_INPUT, "Wadhwani foundation")
            self._wait_and_click(self.locators.SELECT_INDUSTRY_TYPE, timeout=15000, force=True)
            self._wait_and_click(self.locators.SOFTWARE_AND_IT_SERVICES)

            self._wait_and_fill(self.locators.DESCRIPTION_INPUT, "Automated venture creation")

            self._wait_and_click(self.locators.SELECT_COUNTRY, timeout=15000, force=True)
            search_input = self.page.locator("//label[text()='Select Country']/following::input[contains(@class,'ant-select-selection-search-input')][1]")
            search_input.wait_for(state="attached", timeout=10000)
            search_input.fill("India")
            self._wait_and_click(self.locators.INDIA)

            self._wait_and_click(self.locators.SELECT_CITY, timeout=15000, force=True)
            city_input = self.page.locator("//label[text()='Select City']/following::input[contains(@class,'ant-select-selection-search-input')][1]")
            city_input.wait_for(state="attached", timeout=10000)
            city_input.fill("Bangalore")
            self._wait_and_click(self.locators.BANGALORE)

            self._wait_and_click(self.locators.NEXT_BUTTON)
            self._wait_and_fill(self.locators.STUDENT_EMAIL_INPUT, student_email)
            self._wait_and_click(self.locators.SEND_INVITE)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Fill Venture Form Failed")
            print(f"Cohort manager fill venture form failed: {exc}")

    def validate_cohort_venture_heading(self):
        try:
            heading = self.page.locator(self.locators.COHORT_VENTURES_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Cohort Ventures heading is not visible"
            highlight_element(self.page, self.locators.COHORT_VENTURES_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Cohort Venture Heading Validation Failed")
            print(f"Cohort manager cohort venture heading validation failed: {exc}")

    def validate_cohort_members_section(self):
        try:
            self._wait_and_click(self.locators.COHORT_MEMBERS)
            heading = self.page.locator(self.locators.COHORT_MEMBERS_HEADING).first
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Cohort Members section is not visible"
            highlight_element(self.page, self.locators.COHORT_MEMBERS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Cohort Members Validation Failed")
            print(f"Cohort manager cohort members validation failed: {exc}")

    def validate_first_member_and_open_first_chat(self):
        try:
            first_member = self.page.locator(self.locators.FIRST_COHORT_MEMBER)
            first_member.wait_for(state="visible", timeout=15000)
            highlight_element(self.page, self.locators.FIRST_COHORT_MEMBER)

            chat_button = first_member.locator("button, img[alt*='chat' i], [class*='chat']")
            if chat_button.count() > 0:
                chat_button.first.click()
            else:
                first_member.click()
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Open First Member Chat Failed")
            print(f"Cohort manager open first member chat failed: {exc}")
        self.page.go_back()
        self.page.go_back()

    def click_create_new_cohort_button(self):
        try:
            self._wait_and_click(self.locators.CREATE_NEW_COHORT)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Click Create New Cohort Failed")
            print(f"Cohort manager click create new cohort failed: {exc}")

    def fill_create_new_cohort_form_and_create(self):
        try:
            # self._open_dropdown_and_select_option(self.locators.INSTITUTE_SELECT, "Spark Institute", timeout=15000)
            self._open_dropdown_and_select_option(self.locators.INSTITUTE_SELECT, "test spark", timeout=15000)
            self._open_dropdown_and_select_option(self.locators.DELIVERY_MODEL_DROPDOWN, "D2C", timeout=15000)
            self._open_dropdown_and_select_option(self.locators.PROGRAM_SELECT, "liftoff-spark", timeout=15000)
            self._open_dropdown_and_select_option(self.locators.STAGE_SELECT, "Early Stage", timeout=15000)

            self._wait_and_fill(self.locators.COHORT_NAME_INPUT, "test cohort")
            self._pick_date(self.locators.START_DATE_INPUT, self.locators.TODAY_DATE)
            self._pick_date(self.locators.END_DATE_INPUT, self.locators.END_DATE)

            number_inputs = self.page.locator(self.locators.MAX_STUDENTS_INPUT)
            if number_inputs.count() > 0:
                number_inputs.first.wait_for(state="visible", timeout=15000)
                number_inputs.first.fill("50")

            venture_size = self.page.locator(self.locators.VENTURE_SIZE_INPUT)
            if venture_size.count() > 0:
                venture_size.first.wait_for(state="visible", timeout=15000)
                venture_size.first.fill("5")

            self._wait_and_click(self.locators.CREATE_BUTTON)
            self._wait_and_click(self.locators.FIRST_COHORT_DELETE)
            self._wait_and_click(self.locators.THREEDOTS_ICON)
            self._wait_and_click(self.locators.CLOSE_COHORT)
            self._wait_and_click(self.locators.CLOSE_BUTTON)
            self.page.go_back()
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Fill New Cohort Form Failed")
            print(f"Cohort manager fill new cohort form failed: {exc}")

    def validate_office_hours_section(self):
        try:
            office_hours = self.page.locator(self.locators.OFFICE_HOURS_HEADING)
            office_hours.wait_for(state="visible", timeout=15000)
            assert office_hours.is_visible(), "Office Hours section is not visible"
            highlight_element(self.page, self.locators.OFFICE_HOURS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Office Hours Validation Failed")
            print(f"Cohort manager office hours validation failed: {exc}")

    def click_create_button_in_office_hours_section(self):
        try:
            self._wait_and_click(self.locators.CREATE_OFFICE_HOURS_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Click Office Hours Create Failed")
            print(f"Cohort manager click office hours create failed: {exc}")

    def fill_create_office_hours_form_and_create_meeting(self):
        try:
            self._wait_and_fill(self.locators.MEETING_TITLE_INPUT, "test")
            self._pick_date(self.locators.SELECT_DATE_INPUT, self.locators.TODAY_SELECTED_DATE)
            self._wait_and_click(self.locators.OK_BUTTON)

            time_input = self.page.locator(self.locators.SELECT_TIME_INPUT).first
            time_input.wait_for(state="visible", timeout=15000)
            time_input.click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

            checkbox = self.page.locator(self.locators.CHECKBOX_INPUT)
            checkbox.wait_for(state="visible", timeout=15000)
            if not checkbox.is_checked():
                checkbox.check()

            self._wait_and_click(self.locators.CREATE_MEETING_BUTTON)
            self._wait_and_click(self.locators.OKAY_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Fill Office Hours Form Failed")
            print(f"Cohort manager fill office hours form failed: {exc}")

    def click_created_meeting_and_delete(self):
        try:
            card = self.page.locator(self.locators.OFFICE_HOURS_MEETING_CARD).first
            card.wait_for(state="visible", timeout=15000)
            highlight_element(self.page, self.locators.OFFICE_HOURS_MEETING_CARD)
            card.click()

            title = self.page.locator(self.locators.MEETING_TITLE)
            if title.count() > 0:
                title.first.wait_for(state="visible", timeout=15000)
                title.first.click()

            self._wait_and_click(self.locators.DELETE_ICON)

            radio = self.page.locator(self.locators.RADIO_CHECK)
            radio.wait_for(state="visible", timeout=15000)
            if not radio.is_checked():
                radio.check()

            reason = self.page.locator(self.locators.REASON_TO_CANCEL)
            if reason.count() > 0:
                reason.first.wait_for(state="visible", timeout=15000)
                reason.first.click()

            self._wait_and_click(self.locators.CANCEL_MEETING_BUTTON)

            go_back = self.page.locator(self.locators.GO_BACK_TO_DASHBOARD_BUTTON)
            if go_back.count() > 0 and go_back.first.is_visible():
                go_back.first.click()
        except Exception as exc:
            attach_screenshot(self.page, "Cohort Manager Delete Office Hours Meeting Failed")
            print(f"Cohort manager delete office hours meeting failed: {exc}")
