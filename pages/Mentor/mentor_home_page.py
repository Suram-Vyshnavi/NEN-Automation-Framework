from locators.mentor_locators.mentor_home_locators import mentor_home_locators
from utils.helpers import attach_screenshot, highlight_element


class MentorHomePage:
    def __init__(self, page):
        self.page = page
        self.locators = mentor_home_locators()

    def _wait_and_click(self, locator, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        target.first.click()

    def _wait_and_assert_visible(self, locator, message, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        assert target.first.is_visible(), message

    def validate_home_page_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.MENTOR_HOME_PAGE_HEADER,
                "Mentor home page heading is not visible",
            )
            highlight_element(self.page, self.locators.MENTOR_HOME_PAGE_HEADER)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Home Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate mentor home page heading: {exc}") from exc

    def validate_meetings_heading(self):
        try:
            self._wait_and_assert_visible(
                self.locators.MEETINGS_HEADER,
                "Meetings heading is not visible",
            )
            highlight_element(self.page, self.locators.MEETINGS_HEADER)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Meetings Heading Validation Failed", force=True)
            raise AssertionError(f"Failed to validate meetings heading: {exc}") from exc

    def validate_upcoming_meetings_section(self):
        try:
            self._wait_and_assert_visible(
                self.locators.UPCOMING_MEETINGS_TAB,
                "Upcoming meetings section is not visible",
            )
            highlight_element(self.page, self.locators.UPCOMING_MEETINGS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Upcoming Meetings Validation Failed", force=True)
            raise AssertionError(f"Failed to validate upcoming meetings section: {exc}") from exc

    def validate_pending_requests_section(self):
        try:
            self._wait_and_click(self.locators.PENDING_MEETINGS_TAB)
            self._wait_and_assert_visible(
                self.locators.PENDING_MEETINGS_TAB,
                "Pending requests section is not visible",
            )
            highlight_element(self.page, self.locators.PENDING_MEETINGS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Pending Requests Validation Failed", force=True)
            raise AssertionError(f"Failed to validate pending requests section: {exc}") from exc

    def validate_history_section(self):
        try:
            self._wait_and_click(self.locators.HISTORY_MEETINGS_TAB)
            self._wait_and_assert_visible(
                self.locators.HISTORY_MEETINGS_TAB,
                "History section is not visible",
            )
            highlight_element(self.page, self.locators.HISTORY_MEETINGS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor History Section Validation Failed", force=True)
            raise AssertionError(f"Failed to validate history section: {exc}") from exc

    def validate_declined_section(self):
        try:
            self._wait_and_click(self.locators.DECLINED_MEETINGS_TAB)
            self._wait_and_assert_visible(
                self.locators.DECLINED_MEETINGS_TAB,
                "Declined section is not visible",
            )
            highlight_element(self.page, self.locators.DECLINED_MEETINGS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Declined Section Validation Failed", force=True)
            raise AssertionError(f"Failed to validate declined section: {exc}") from exc

    def click_my_availability_menu(self):
        try:
            card = self.page.locator(self.locators.MY_AVAILABILITY_CARD)
            card.first.scroll_into_view_if_needed(timeout=10000)
            self._wait_and_click(self.locators.MY_AVAILABILITY_CARD)
            self.page.wait_for_timeout(1000)
            # Wait for weekly schedule header to confirm navigation completed
            self._wait_and_assert_visible(
                self.locators.WEEKLY_SCHEDULE_HEADER,
                "Weekly schedule header not visible after My Availability click",
                timeout=15000,
            )
            highlight_element(self.page, self.locators.WEEKLY_SCHEDULE_HEADER)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor My Availability Click Failed", force=True)
            raise AssertionError(f"Failed to click My Availability menu: {exc}") from exc

    def validate_weekly_schedule_section(self):
        try:
            self._wait_and_assert_visible(
                self.locators.WEEKLY_SCHEDULE_HEADER,
                "Weekly schedule section is not visible",
            )
            highlight_element(self.page, self.locators.WEEKLY_SCHEDULE_HEADER)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Weekly Schedule Validation Failed", force=True)
            raise AssertionError(f"Failed to validate weekly schedule section: {exc}") from exc

    def select_first_checkbox_in_weekly_schedule(self):
        try:
            checkbox = self.page.locator(self.locators.FIRST_CHECKBOX)
            checkbox.first.wait_for(state="visible", timeout=15000)
            if not checkbox.first.is_checked():
                checkbox.first.check()
            highlight_element(self.page, self.locators.FIRST_CHECKBOX)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Weekly Schedule Checkbox Selection Failed", force=True)
            raise AssertionError(f"Failed to select first checkbox in weekly schedule: {exc}") from exc

    def fill_weekly_schedule_form(self):
        try:
            self._wait_and_click(self.locators.START_TIME_DROPDOWN)
            self._wait_and_click(self.locators.TIME_SELECTION_START)

            self._wait_and_click(self.locators.END_TIME_DROPDOWN)
            self._wait_and_click(self.locators.TIME_SELECTION_END)

            self._wait_and_click(self.locators.COPY_ICON)
            self._wait_and_click(self.locators.COPYTIME_TO_NEXTDAY_CHECKBOX)
            self._wait_and_click(self.locators.APPLY_BUTTON)
            self._wait_and_click(self.locators.CANCEL_SLOT_ICON)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Weekly Schedule Form Fill Failed", force=True)
            raise AssertionError(f"Failed to fill weekly schedule form: {exc}") from exc

    def click_add_override_button(self):
        try:
            self._wait_and_click(self.locators.ADD_OVERRIDE_BUTTON)
            highlight_element(self.page, self.locators.ADD_OVERRIDE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Add Override Click Failed", force=True)
            raise AssertionError(f"Failed to click Add Override button: {exc}") from exc

    def add_date_override(self):
        try:
            self._wait_and_click(self.locators.TODAY_DATE)
            self._wait_and_click(self.locators.OVERRIDE_SAVE_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Add Date Override Failed", force=True)
            raise AssertionError(f"Failed to add date override: {exc}") from exc

    def delete_added_override(self):
        try:
            self._wait_and_click(self.locators.DELETE_ICON)
            save_button = self.page.locator(self.locators.SAVE_BUTTON)
            if save_button.count() > 0 and save_button.first.is_visible():
                save_button.first.click()
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Delete Override Failed", force=True)
            raise AssertionError(f"Failed to delete added override: {exc}") from exc
