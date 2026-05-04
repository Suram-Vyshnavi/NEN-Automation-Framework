from datetime import datetime

from locators.mentor_locators.connected_ventures_locators import connected_ventures_locators
from locators.mentor_locators.mentor_home_locators import mentor_home_locators
from utils.helpers import attach_screenshot, highlight_element


class MentorConnectedVenturesPage:
    def __init__(self, page):
        self.page = page
        self.locators = connected_ventures_locators()
        self.home_locators = mentor_home_locators()

    def _wait_and_click(self, locator, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        target.first.click()

    def _wait_and_fill(self, locator, value, timeout=15000):
        target = self.page.locator(locator)
        target.first.wait_for(state="visible", timeout=timeout)
        target.first.fill(str(value))

    def validate_mentor_home_page(self):
        try:
            header = self.page.locator(self.home_locators.MENTOR_HOME_PAGE_HEADER)
            header.first.wait_for(state="visible", timeout=20000)
            assert header.first.is_visible(), "Mentor home page header is not visible"
            highlight_element(self.page, self.home_locators.MENTOR_HOME_PAGE_HEADER)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Home Page Validation Failed", force=True)
            raise AssertionError(f"Mentor home page validation failed: {exc}") from exc

    def click_connected_ventures_tab(self):
        try:
            self._wait_and_click(self.locators.CONNECTED_VENTURES_MENU)
            highlight_element(self.page, self.locators.CONNECTED_VENTURES_MENU)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Connected Ventures Menu Click Failed", force=True)
            raise AssertionError(f"Failed to click Connected Ventures menu: {exc}") from exc

    def validate_first_connected_venture(self):
        try:
            card = self.page.locator(self.locators.CONNECTED_VENTURES_CARD)
            card.first.wait_for(state="visible", timeout=15000)
            assert card.first.is_visible(), "First connected venture card is not visible"
            highlight_element(self.page, self.locators.CONNECTED_VENTURES_CARD)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor First Connected Venture Validation Failed", force=True)
            raise AssertionError(f"First connected venture validation failed: {exc}") from exc

    def click_book_session_button(self):
        try:
            self._wait_and_click(self.locators.CONNECTED_VENTURES_BOOK_SESSION_BUTTON)
            highlight_element(self.page, self.locators.CONNECTED_VENTURES_BOOK_SESSION_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Book Session Click Failed", force=True)
            raise AssertionError(f"Failed to click Book Session button: {exc}") from exc

    def fill_required_meeting_details(self):
        try:
            meeting_title = f"Automation Mentor Session {datetime.now().strftime('%H%M%S')}"
            self._wait_and_fill(self.locators.CONNECTED_VENTURES_MEETING_TITLE_INPUT, meeting_title)

            self._wait_and_click(self.locators.CONNECTED_VENTURES_MEETING_DATE_INPUT)
            self._wait_and_click(self.locators.CONNECTED_VENTURES_MEETING_DATE_TODAY)
            self._wait_and_click(self.locators.CONNECTED_VENTURES_MEETING_DATE_OK_BUTTON)

            # Time picker/select can vary by build; first click opens options, second confirms.
            self._wait_and_click(self.locators.CONNECTED_VENTURES_MEETING_TIME_INPUT)

            meeting_checkbox = self.page.locator(self.locators.CONNECTED_VENTURES_MEETING_CHECKBOX)
            meeting_checkbox.first.wait_for(state="visible", timeout=15000)
            if not meeting_checkbox.first.is_checked():
                meeting_checkbox.first.check()
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Fill Meeting Details Failed", force=True)
            raise AssertionError(f"Failed to fill meeting details: {exc}") from exc

    def create_meeting(self):
        try:
            self._wait_and_click(self.locators.CONNECTED_VENTURES_MEETING_CREATE_BUTTON)

            ok_btn = self.page.locator(self.locators.CONNECTED_VENTURES_MEETING_OK_BUTTON)
            if ok_btn.count() > 0:
                ok_btn.first.wait_for(state="visible", timeout=10000)
                ok_btn.first.click()
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Create Meeting Failed", force=True)
            raise AssertionError(f"Failed to create meeting: {exc}") from exc

    def click_chat_button_in_venture_details_page(self):
        try:
            self._wait_and_click(self.locators.CONNECTED_VENTURES_CHAT_BUTTON)
            highlight_element(self.page, self.locators.CONNECTED_VENTURES_CHAT_BUTTON)
            self.page.go_back()  # Navigate back to connected ventures page after clicking chat
        except Exception as exc:
            attach_screenshot(self.page, "Mentor Chat Button Click Failed", force=True)
            raise AssertionError(f"Failed to click chat button: {exc}") from exc
