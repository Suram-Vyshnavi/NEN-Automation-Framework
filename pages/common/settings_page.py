from locators.common.settings_locators import settings_locators
from utils.helpers import attach_screenshot, highlight_element


class SettingsPage:
	def __init__(self, page):
		self.page = page
		self.locators = settings_locators()
		self.timeout = 10000

	def _wait_for_element(self, locator, timeout=None):
		timeout = timeout or self.timeout
		element = self.page.locator(locator)
		element.wait_for(state="visible", timeout=timeout)
		return element

	def _click_element(self, locator, element_name="", timeout=None):
		element = self._wait_for_element(locator, timeout)
		element.click()
		highlight_element(self.page, locator)
		_ = element_name

	def _verify_element_visible(self, locator, element_name=""):
		element = self._wait_for_element(locator)
		assert element.is_visible(), f"{element_name} is not visible"
		highlight_element(self.page, locator)
		return element

	def _toggle_switch(self, toggle_locator, toggle_name="Toggle", timeout=None):
		timeout = timeout or self.timeout
		toggle = self._wait_for_element(toggle_locator, timeout)
		initial_state = toggle.get_attribute("aria-checked")
		toggle.click()
		self.page.wait_for_timeout(500)
		updated_state = toggle.get_attribute("aria-checked")
		assert updated_state != initial_state, f"{toggle_name} state did not change after click"

	def navigate_to_settings_page(self):
		try:
			self._click_element(self.locators.PROFILE_ICON, "Profile Icon")
			self._verify_element_visible(self.locators.SETTINGS_ICON, "Settings Icon")
			self._click_element(self.locators.SETTINGS_ICON, "Settings Icon",5000)
		except Exception as e:
			attach_screenshot(self.page, "Navigate to Settings Page Failed")
			print(f"Failed to navigate to settings page: {e}")
	def click_back_button(self):
		try:
			self._click_element(self.locators.BACK_ARROW, "Back Arrow")
		except Exception as e:
			attach_screenshot(self.page, "Click Back Button Failed")
			print(f"Failed to click back button: {e}")
	def validate_settings_page_header(self):
		try:
			self._verify_element_visible(self.locators.SETTINGS_HEADER, "Settings Header")
		except Exception as e:
			attach_screenshot(self.page, "Settings Page Header Validation Failed")
			print(f"Settings page header validation failed: {e}")
	def validate_settings_page_sections(self):
		try:
			self._verify_element_visible(self.locators.ACCOUNTS_MENU, "Accounts Menu")
			self._verify_element_visible(self.locators.NOTIFICATIONS_MENU, "Notifications Menu")
			self._verify_element_visible(self.locators.CALENDAR_MENU, "Calendar Menu")
		except Exception as e:
			attach_screenshot(self.page, "Settings Page Sections Validation Failed")
			print(f"Settings page sections validation failed: {e}")
	def validate_settings_page_complete(self):
		self.validate_settings_page_header()
		self.validate_settings_page_sections()

	def click_accounts_section(self):
		try:
			self._click_element(self.locators.ACCOUNTS_MENU, "Accounts Section")
		except Exception as e:
			attach_screenshot(self.page, "Click Accounts Section Failed")
			print(f"Failed to click accounts section: {e}")
	def expand_zoom_connection_section(self):
		try:
			self._click_element(self.locators.ZOOMCONNECTION_ARROW_BUTTON, "Zoom Connection Arrow")
		except Exception as e:
			attach_screenshot(self.page, "Expand Zoom Section Failed")
			print(f"Failed to expand zoom connection section: {e}")
	def validate_zoom_section_header(self):
		try:
			self._verify_element_visible(self.locators.ZOOM_SETTINGS_HEADER, "Zoom Settings Header")
		except Exception as e:
			attach_screenshot(self.page, "Zoom Section Header Validation Failed")
			print(f"Zoom section header validation failed: {e}")
	def validate_zoom_meeting_card(self):
		try:
			self._verify_element_visible(self.locators.TOGGLER_ON, "Zoom is connected")
		except Exception as e:
			attach_screenshot(self.page, "Zoom Meeting Card Validation Failed")
			print(f"Zoom meeting card validation failed: {e}")
	def validate_zoom_section_complete(self):
		self.validate_zoom_section_header()
		self.validate_zoom_meeting_card()
		back=self.page.locator(self.locators.BACK_ARROW)
		back.wait_for(state="visible", timeout=5000)
		self.click_back_button()

	def validate_zoom_disconnect_message(self):
		try:
			self._verify_element_visible(self.locators.MEETINGS_DESCRIPTION, "Disconnect Message")
		except Exception as e:
			attach_screenshot(self.page, "Zoom Disconnect Message Validation Failed")
			print(f"Zoom disconnect message validation failed: {e}")
	def connect_zoom_account(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_OFF, "Zoom Connection")
		except Exception as e:
			attach_screenshot(self.page, "Connect Zoom Account Failed")
			print(f"Failed to connect zoom account: {e}")
	def disconnect_zoom_account_via_toggle(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_ON, "Zoom Connection")
		except Exception as e:
			attach_screenshot(self.page, "Disconnect Zoom Account Failed")
			print(f"Failed to disconnect zoom account via toggle: {e}")
	def click_disconnect_button(self):
		try:
			self._click_element(self.locators.DISCONNECT_BUTTON, "Disconnect Button")
		except Exception as e:
			attach_screenshot(self.page, "Click Disconnect Button Failed")
			print(f"Failed to click disconnect button: {e}")
	def validate_zoom_signin_button_visible(self):
		try:
			self._verify_element_visible(self.locators.SIGNIN_BUTTON, "Zoom Sign In Button")
		except Exception as e:
			attach_screenshot(self.page, "Zoom Sign In Button Validation Failed")
			print(f"Zoom sign in button validation failed: {e}")
	def click_zoom_signin_button(self):
		try:
			self._click_element(self.locators.SIGNIN_BUTTON, "Zoom Sign In Button")
		except Exception as e:
			attach_screenshot(self.page, "Click Zoom Sign In Button Failed")
			print(f"Failed to click zoom sign in button: {e}")
	def expand_whatsapp_section(self):
		try:
			self._click_element(self.locators.NOTIFICATIONS_MENU, "Notifications Menu")
			self._click_element(self.locators.WHATSAPP_NOTIFICATION, "WhatsApp Notification")
		except Exception as e:
			attach_screenshot(self.page, "WhatsApp Section Failed")
			print(f"Failed to expand whatsapp section: {e}")
	def validate_whatsapp_section_header(self):
		try:
			self._verify_element_visible(self.locators.VALIDATE_WHATSAPP_NOTIFICATIONS_HEADING, "WhatsApp Notifications Header")
			self._click_element(self.locators.BACK_ARROW, "Back Arrow")
		except Exception as e:
			attach_screenshot(self.page, "WhatsApp Section Header Validation Failed")
			print(f"WhatsApp section header validation failed: {e}")
	def enable_whatsapp_notifications(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_OFF, "WhatsApp Notifications")
		except Exception as e:
			attach_screenshot(self.page, "Enable WhatsApp Notifications Failed")
			print(f"Failed to enable whatsapp notifications: {e}")
	def disable_whatsapp_notifications(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_ON, "WhatsApp Notifications")
		except Exception as e:
			attach_screenshot(self.page, "Disable WhatsApp Notifications Failed")
			print(f"Failed to disable whatsapp notifications: {e}")
	def click_calendar_section(self):
		try:
			self._click_element(self.locators.CALENDAR_MENU, "Calendar Section")
		except Exception as e:
			attach_screenshot(self.page, "Click Calendar Section Failed")
			print(f"Failed to click calendar section: {e}")
	def validate_sync_google_calendar_option(self):
		try:
			self._verify_element_visible(self.locators.SYNC_GOOGLE_CALENDAR, "Sync Google Calendar")
		except Exception as e:
			attach_screenshot(self.page, "Sync Google Calendar Validation Failed")
			print(f"Sync google calendar validation failed: {e}")
	def enable_google_calendar_sync(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_OFF, "Google Calendar Sync")
		except Exception as e:
			attach_screenshot(self.page, "Enable Google Calendar Sync Failed")
			print(f"Failed to enable google calendar sync: {e}")
	def disable_google_calendar_sync(self):
		try:
			self._toggle_switch(self.locators.TOGGLER_ON, "Google Calendar Sync")
		except Exception as e:
			attach_screenshot(self.page, "Disable Google Calendar Sync Failed")
			print(f"Failed to disable google calendar sync: {e}")
	def click_sync_google_calendar(self):
		try:
			self._click_element(self.locators.SYNC_GOOGLE_CALENDER, "Sync Google Calendar")
		except Exception as e:
			attach_screenshot(self.page, "Click Sync Google Calendar Failed")
			print(f"Failed to click sync google calendar: {e}")
	def click_notifications_section(self):
		try:
			self._click_element(self.locators.NOTIFICATIONS_MENU, "Notifications Section")
		except Exception as e:
			attach_screenshot(self.page, "Click Notifications Section Failed")
			print(f"Failed to click notifications section: {e}")
