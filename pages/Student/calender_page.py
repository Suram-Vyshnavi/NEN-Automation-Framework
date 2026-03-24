from locators.student_locators.calender_locators import CalenderLocators
from utils.helpers import attach_screenshot, highlight_element


class CalenderPage:
    def __init__(self, page):
        self.page = page
        self.locators = CalenderLocators()

    def click_calendar_section(self):
        """Click on the Calendar section from header"""
        calendar_btn = self.page.locator(self.locators.CALENDER)
        calendar_btn.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.CALENDER)
        attach_screenshot(self.page, "Clicked Calendar Section")

    def validate_calendar_page(self):
        """Validate that Calendar page is visible"""
        calendar_header = self.page.locator(self.locators.CALENDER)
        calendar_header.wait_for(state="visible", timeout=10000)
        assert calendar_header.is_visible(), "Calendar header is not visible"
        highlight_element(self.page, self.locators.CALENDER)
        attach_screenshot(self.page, "Calendar Page Validated")

    def click_first_meeting_link(self):
        """Click on the first meeting link"""
        try:
            self.page.wait_for_timeout(5000)  # Wait for meetings to load
            meeting_link = self.page.locator(self.locators.FIRST_MEETING)
            meeting_link.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.FIRST_MEETING)
            attach_screenshot(self.page, "Clicked First Meeting Link")
        except Exception as e:
            attach_screenshot(self.page, "First Meeting Link Not Found")
            raise AssertionError("First meeting link is not visible or clickable") from e
       

    def validate_past_activities_section_and_meeting_link(self):
        """Validate past activities section and the meeting link inside it"""
        self.click_calendar_section()
        past_section = self.page.locator(self.locators.PAST_ACTIVITIES)
        past_section.wait_for(state="visible", timeout=10000)
        assert past_section.is_visible(), "Past Activities section is not visible"
        highlight_element(self.page, self.locators.PAST_ACTIVITIES)

        meeting_link = self.page.locator(self.locators.MEETING_LINK)
        meeting_link.wait_for(state="visible", timeout=10000)
        assert meeting_link.is_visible(), "Meeting link is not visible in Past Activities"
        highlight_element(self.page, self.locators.MEETING_LINK)
        meeting_link.click()
        
        reviewnow_btn = self.page.locator(self.locators.VALIDATE_REVIEW_NOW_BUTTON)
        reviewnow_btn.wait_for(state="visible", timeout=10000)
        assert reviewnow_btn.is_visible(), "Review Now button is not visible after clicking meeting link"
        highlight_element(self.page, self.locators.VALIDATE_REVIEW_NOW_BUTTON)

        notes_section = self.page.locator(self.locators.VALIDATE_NOTES_SECTION)
        notes_section.wait_for(state="visible", timeout=10000)
        assert notes_section.is_visible(), "notes section is not visible after clicking meeting link"
        highlight_element(self.page, self.locators.VALIDATE_NOTES_SECTION)

        attach_screenshot(self.page, "Past Activities and Meeting Link Validated")
