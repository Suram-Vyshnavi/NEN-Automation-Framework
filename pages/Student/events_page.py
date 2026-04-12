from locators.student_locators.events_locators import Eventlocators
from utils.helpers import attach_screenshot, highlight_element


class EventsPage:
    def __init__(self, page):
        self.page = page
        self.locators = Eventlocators()

    def click_events_section(self):
        try:
            events_heading = self.page.locator(self.locators.EVENTS_HEADING)
            events_heading.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.EVENTS_HEADING)
        except Exception as e:
            attach_screenshot(self.page, "Click Events Section Failed")
            print(f"Failed to click events section: {e}")
    def validate_upcoming_events(self):
        try:
            upcoming = self.page.locator(self.locators.UPCOMING_EVENTS)
            upcoming.wait_for(state="visible", timeout=10000)
            assert upcoming.is_visible(), "Upcoming Events section is not visible"
            highlight_element(self.page, self.locators.UPCOMING_EVENTS)
        except Exception as e:
            attach_screenshot(self.page, "Upcoming Events Validation Failed")
            print(f"Upcoming events validation failed: {e}")
    def validate_registered_events(self):
        try:
            registered = self.page.locator(self.locators.REGISTERED_EVENTS)
            registered.wait_for(state="visible", timeout=10000)
            assert registered.is_visible(), "Registered Events section is not visible"
            highlight_element(self.page, self.locators.REGISTERED_EVENTS)
        except Exception as e:
            attach_screenshot(self.page, "Registered Events Validation Failed")
            print(f"Registered events validation failed: {e}")
    def validate_explore_events(self):
        try:
            explore = self.page.locator(self.locators.EXPLORE_EVENTS)
            explore.wait_for(state="visible", timeout=10000)
            assert explore.is_visible(), "Explore Events section is not visible"
            highlight_element(self.page, self.locators.EXPLORE_EVENTS)
        except Exception as e:
            attach_screenshot(self.page, "Explore Events Validation Failed")
            print(f"Explore events validation failed: {e}")
    def click_view_details_first_upcoming_event(self):
        try:
            assert self.page.locator(self.locators.VIEW_DETAILS).is_visible(), "View Details button for first upcoming event is not visible"
            view_details = self.page.locator(self.locators.VIEW_DETAILS)
            view_details.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.VIEW_DETAILS)
        except Exception as e:
            attach_screenshot(self.page, "Click View Details Failed")
            print(f"View Details button for first upcoming event is not visible or clickable: {e}")

    def validate_event_details(self):
        try:
            details_heading = self.page.locator(self.locators.EVENTS_HEADING)
            details_heading.wait_for(state="visible", timeout=10000)
            assert details_heading.is_visible(), "Event details page is not visible"
            highlight_element(self.page, self.locators.EVENTS_HEADING)
        except Exception as e:
            attach_screenshot(self.page, "Event Details Validation Failed")
            print(f"Event details page is not visible: {e}")

    def click_back_button(self):
        try:
            back_button = self.page.locator(self.locators.BACK_BUTTON)
            back_button.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.BACK_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Click Back Button Failed")
            print(f"Failed to click back button: {e}")

