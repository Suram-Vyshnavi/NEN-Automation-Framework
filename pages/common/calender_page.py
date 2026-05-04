from locators.common.calender_locators import CalenderLocators
from utils.helpers import attach_screenshot, highlight_element


class CalenderPage:
	def __init__(self, page):
		self.page = page
		self.locators = CalenderLocators()

	def click_calendar_section(self):
		try:
			calendar_btn = self.page.locator(self.locators.CALENDER)
			calendar_btn.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.CALENDER)
		except Exception as e:
			attach_screenshot(self.page, "Click Calendar Section Failed")
			print(f"Failed to click calendar section: {e}")
	def validate_calendar_page(self):
		try:
			calendar_header = self.page.locator(self.locators.CALENDER)
			calendar_header.wait_for(state="visible", timeout=10000)
			assert calendar_header.is_visible(), "Calendar header is not visible"
			highlight_element(self.page, self.locators.CALENDER)
		except Exception as e:
			attach_screenshot(self.page, "Calendar Page Validation Failed")
			print(f"Calendar page validation failed: {e}")
	def click_first_meeting_link(self):
		try:
			self.page.wait_for_timeout(5000)
			meeting_link = self.page.locator(self.locators.FIRST_MEETING)
			meeting_link.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.FIRST_MEETING)
		except Exception as exc:
			attach_screenshot(self.page, "First Meeting Link Not Found")
			print("First meeting link is not visible or clickable")
	def validate_past_activities_section_and_meeting_link(self):
		try:
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
		except Exception as e:
			attach_screenshot(self.page, "Past Activities Validation Failed")
			print(f"Past activities validation failed: {e}")
