from locators.student_locators.events_locators import Eventlocators
from utils.helpers import attach_screenshot, highlight_element


class EventsPage:
    def __init__(self, page):
        self.page = page
        self.locators = Eventlocators()

    def click_events_section(self):
        events_heading = self.page.locator(self.locators.EVENTS_HEADING)
        events_heading.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.EVENTS_HEADING)
        attach_screenshot(self.page, "Clicked Events Section")

    def validate_upcoming_events(self):
        upcoming = self.page.locator(self.locators.UPCOMING_EVENTS)
        upcoming.wait_for(state="visible", timeout=10000)
        assert upcoming.is_visible(), "Upcoming Events section is not visible"
        highlight_element(self.page, self.locators.UPCOMING_EVENTS)
        attach_screenshot(self.page, "Upcoming Events Validated")

    def validate_registered_events(self):
        registered = self.page.locator(self.locators.REGISTERED_EVENTS)
        registered.wait_for(state="visible", timeout=10000)
        assert registered.is_visible(), "Registered Events section is not visible"
        highlight_element(self.page, self.locators.REGISTERED_EVENTS)
        attach_screenshot(self.page, "Registered Events Validated")

    def validate_explore_events(self):
        explore = self.page.locator(self.locators.EXPLORE_EVENTS)
        explore.wait_for(state="visible", timeout=10000)
        assert explore.is_visible(), "Explore Events section is not visible"
        highlight_element(self.page, self.locators.EXPLORE_EVENTS)
        attach_screenshot(self.page, "Explore Events Validated")

    def click_view_details_first_upcoming_event(self):
        view_details = self.page.locator(self.locators.VIEW_DETAILS)
        view_details.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.VIEW_DETAILS)
        attach_screenshot(self.page, "Clicked View Details of First Upcoming Event")

    def validate_event_details(self):
        # Basic validation: assert event details header is visible
        details_heading = self.page.locator(self.locators.EVENTS_HEADING)
        details_heading.wait_for(state="visible", timeout=10000)
        assert details_heading.is_visible(), "Event details page is not visible"
        highlight_element(self.page, self.locators.EVENTS_HEADING)
        attach_screenshot(self.page, "Event Details Validated")

    def click_back_button(self):
        back_button = self.page.locator(self.locators.BACK_BUTTON)
        back_button.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.BACK_BUTTON)
        attach_screenshot(self.page, "Clicked Back Button")
