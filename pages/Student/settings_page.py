from locators.student_locators.settings_locators import settings_locators
from utils.helpers import attach_screenshot, highlight_element


class SettingsPage:
    """Settings Page Object Model for handling all settings page interactions."""
    
    def __init__(self, page):
        self.page = page
        self.locators = settings_locators()
        self.timeout = 10000

    # ==================== HELPER METHODS ====================
    
    def _wait_for_element(self, locator, timeout=None):
        """Wait for element to be visible and return it."""
        timeout = timeout or self.timeout
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def _click_element(self, locator, element_name="", timeout=None):
        """Wait for element, click it, and take screenshot."""
        element = self._wait_for_element(locator, timeout)
        element.click()
        highlight_element(self.page, locator)
        if element_name:
            attach_screenshot(self.page, f"Clicked {element_name}")

    def _verify_element_visible(self, locator, element_name=""):
        """Verify that an element is visible."""
        element = self._wait_for_element(locator)
        assert element.is_visible(), f"{element_name} is not visible"
        highlight_element(self.page, locator)
        return element

    def _toggle_switch(self, toggle_locator, toggle_name="Toggle", timeout=None):
        """Toggle a switch element and verify state change."""
        timeout = timeout or self.timeout
        toggle = self._wait_for_element(toggle_locator, timeout)
        
        initial_state = toggle.get_attribute("aria-checked")
        toggle.click()
        self.page.wait_for_timeout(500)
        
        updated_state = toggle.get_attribute("aria-checked")
        assert updated_state != initial_state, f"{toggle_name} state did not change after click"
        attach_screenshot(self.page, f"Toggled {toggle_name}")

    # ==================== NAVIGATION METHODS ====================

    def navigate_to_settings_page(self):
        """Navigate to settings page by clicking profile icon."""
        self._click_element(self.locators.PROFILE_ICON, "Profile Icon")
        self._verify_element_visible(self.locators.SETTINGS_HEADER, "Settings page")
        attach_screenshot(self.page, "Navigated to Settings page")

    def click_back_button(self):
        """Navigate back using the back arrow button."""
        self._click_element(self.locators.BACK_ARROW, "Back Arrow")
        attach_screenshot(self.page, "Clicked Back button")

    # ==================== SETTINGS PAGE VALIDATION ====================

    def validate_settings_page_header(self):
        """Validate that Settings page header is visible."""
        self._verify_element_visible(self.locators.SETTINGS_HEADER, "Settings Header")
        attach_screenshot(self.page, "Settings page header validated")

    def validate_settings_page_sections(self):
        """Validate all main sections are visible on settings page."""
        # Validate Accounts section
        self._verify_element_visible(self.locators.ACCOUNTS_MENU, "Accounts Menu")
        
        # Validate Notifications section
        self._verify_element_visible(self.locators.NOTIFICATIONS_MENU, "Notifications Menu")
        
        # Validate Calendar section
        self._verify_element_visible(self.locators.CALENDAR_MENU, "Calendar Menu")
        
        attach_screenshot(self.page, "All settings sections validated")

    def validate_settings_page_complete(self):
        """Complete validation of settings page header and all sections."""
        self.validate_settings_page_header()
        self.validate_settings_page_sections()

    # ==================== ACCOUNTS SECTION ====================

    def click_accounts_section(self):
        """Click on the Accounts menu section."""
        self._click_element(self.locators.ACCOUNTS_MENU, "Accounts Section")
        attach_screenshot(self.page, "Opened Accounts section")

    # ==================== ZOOM CONNECTION SECTION ====================

    def expand_zoom_connection_section(self):
        """Expand the Zoom connection section by clicking arrow button."""
        self._click_element(self.locators.ZOOMCONNECTION_ARROW_BUTTON, "Zoom Connection Arrow")
        attach_screenshot(self.page, "Expanded Zoom connection section")

    def validate_zoom_section_header(self):
        """Validate Zoom Meetings section header is visible."""
        self._verify_element_visible(self.locators.ZOOM_SETTINGS_HEADER, "Zoom Settings Header")
        attach_screenshot(self.page, "Zoom section header validated")

    def validate_zoom_meeting_card(self):
        """Validate Zoom meeting card is visible."""
        self._verify_element_visible(self.locators.MEETING_CARD, "Zoom Meeting Card")
        attach_screenshot(self.page, "Zoom meeting card validated")

    def validate_zoom_section_complete(self):
        """Complete validation of Zoom section header and meeting card."""
        self.validate_zoom_section_header()
        self.validate_zoom_meeting_card()

    def validate_zoom_disconnect_message(self):
        """Validate the disconnect message is displayed in Zoom section."""
        self._verify_element_visible(self.locators.MEETINGS_DESCRIPTION, "Disconnect Message")
        attach_screenshot(self.page, "Zoom disconnect message validated")

    def connect_zoom_account(self):
        """Connect Zoom account by toggling the off switch."""
        self._toggle_switch(self.locators.TOGGLER_OFF, "Zoom Connection")

    def disconnect_zoom_account_via_toggle(self):
        """Disconnect Zoom account by toggling the on switch."""
        self._toggle_switch(self.locators.TOGGLER_ON, "Zoom Connection")

    def click_disconnect_button(self):
        """Click the Disconnect button in Zoom section."""
        self._click_element(self.locators.DISCONNECT_BUTTON, "Disconnect Button")
        attach_screenshot(self.page, "Clicked Disconnect button")

    def validate_zoom_signin_button_visible(self):
        """Verify Sign In button is visible after disconnection."""
        self._verify_element_visible(self.locators.SIGNIN_BUTTON, "Zoom Sign In Button")
        attach_screenshot(self.page, "Zoom Sign In button is visible after disconnect")

    def click_zoom_signin_button(self):
        """Click the Zoom Sign In button."""
        self._click_element(self.locators.SIGNIN_BUTTON, "Zoom Sign In Button")
        attach_screenshot(self.page, "Clicked Zoom Sign In button")

    # ==================== WHATSAPP NOTIFICATIONS SECTION ====================

    def expand_whatsapp_section(self):
        """Expand the WhatsApp Notifications section."""
        self._click_element(self.locators.WHATSAPP_NOTIFICATION, "WhatsApp Notification")
        self._click_element(self.locators.ZOOMCONNECTION_ARROW_BUTTON, "WhatsApp Arrow Button")
        attach_screenshot(self.page, "Expanded WhatsApp Notifications section")

    def validate_whatsapp_section_header(self):
        """Validate WhatsApp Notifications section header is visible."""
        self._verify_element_visible(self.locators.VALIDATE_WHATSAPP_NOTIFICATIONS_HEADING, 
                                     "WhatsApp Notifications Header")
        attach_screenshot(self.page, "WhatsApp Notifications header validated")

    def enable_whatsapp_notifications(self):
        """Enable WhatsApp notifications by toggling the switch."""
        self._toggle_switch(self.locators.TOGGLER_OFF, "WhatsApp Notifications")

    def disable_whatsapp_notifications(self):
        """Disable WhatsApp notifications by toggling the switch."""
        self._toggle_switch(self.locators.TOGGLER_ON, "WhatsApp Notifications")

    # ==================== CALENDAR SYNC SECTION ====================

    def click_calendar_section(self):
        """Click on the Calendar menu section."""
        self._click_element(self.locators.CALENDAR_MENU, "Calendar Section")
        attach_screenshot(self.page, "Opened Calendar section")

    def validate_sync_google_calendar_option(self):
        """Validate the Sync Google Calendar option is visible."""
        self._verify_element_visible(self.locators.SYNC_GOOGLE_CALENDER, "Sync Google Calendar")
        attach_screenshot(self.page, "Sync Google Calendar option validated")

    def enable_google_calendar_sync(self):
        """Enable Google Calendar sync by toggling the switch."""
        self._toggle_switch(self.locators.TOGGLER_OFF, "Google Calendar Sync")

    def disable_google_calendar_sync(self):
        """Disable Google Calendar sync by toggling the switch."""
        self._toggle_switch(self.locators.TOGGLER_ON, "Google Calendar Sync")

    def click_sync_google_calendar(self):
        """Click on the Sync Google Calendar element."""
        self._click_element(self.locators.SYNC_GOOGLE_CALENDER, "Sync Google Calendar")
        attach_screenshot(self.page, "Clicked Sync Google Calendar")

    # ==================== NOTIFICATIONS SECTION ====================

    def click_notifications_section(self):
        """Click on the Notifications menu section."""
        self._click_element(self.locators.NOTIFICATIONS_MENU, "Notifications Section")
        attach_screenshot(self.page, "Opened Notifications section")
