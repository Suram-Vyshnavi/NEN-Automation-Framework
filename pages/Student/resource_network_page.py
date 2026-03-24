from locators.student_locators.resource_network_locators import ResourceNetwork_locators
from utils.helpers import attach_screenshot, highlight_element


class ResourceNetworkPage:
    def __init__(self, page):
        self.page = page
        self.locators = ResourceNetwork_locators()

    def click_resource_network_section(self):
        """Click on Resource Network section from header"""
        self.page.wait_for_timeout(4000)  # Wait for page to stabilize
        resource_header = self.page.locator(self.locators.RESOURCE_HEADER)
        resource_header.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.RESOURCE_HEADER)
        attach_screenshot(self.page, "Clicked Resource Network Section")

    def click_explore_section(self):
        """Click on Explore section"""
        explore = self.page.locator(self.locators.EXPLORE)
        explore.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.EXPLORE)
        attach_screenshot(self.page, "Clicked Explore Section")

    def validate_mentors_experts_service_providers_cards(self):
        """Validate Mentors, Experts and Service Providers cards"""
        # Validate Mentors card
        mentors_card = self.page.locator(self.locators.MENTORS_CARD)
        mentors_card.wait_for(state="visible", timeout=10000)
        assert mentors_card.is_visible(), "Mentors card is not visible"
        highlight_element(self.page, self.locators.MENTORS_CARD)

        # Validate Experts card
        experts_card = self.page.locator(self.locators.EXPERTS_CARD)
        assert experts_card.is_visible(), "Experts card is not visible"
        highlight_element(self.page, self.locators.EXPERTS_CARD)

        # Validate Service Providers card
        service_providers_card = self.page.locator(self.locators.SERVICE_PROVIDERS_CARD)
        assert service_providers_card.is_visible(), "Service Providers card is not visible"
        highlight_element(self.page, self.locators.SERVICE_PROVIDERS_CARD)

        attach_screenshot(self.page, "Validated Mentors, Experts and Service Providers Cards")

    def click_mentors_section(self):
        """Click on Mentors section"""
        mentors = self.page.locator(self.locators.MENTORS)
        mentors.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.MENTORS)
        attach_screenshot(self.page, "Clicked Mentors Section")

    def search_test_in_search_network(self):
        """Search for 'test' in search network"""
        search_input = self.page.locator(self.locators.SEARCH_NETWORK)
        search_input.wait_for(state="visible", timeout=10000)
        self.page.fill(self.locators.SEARCH_NETWORK, "test")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)  # Wait for search results
        attach_screenshot(self.page, "Searched for 'test' in Search Network")

    def click_first_search_result_request_meeting_button(self):
        """Click on first search result's request meeting button"""     
        # Click Request Meeting button
        request_meeting = self.page.locator(self.locators.REQUEST_MEETING)
        request_meeting.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.REQUEST_MEETING)
        attach_screenshot(self.page, "Clicked First Search Result and Request Meeting Button")

    def select_slot_and_provide_startup_information(self):
        """Select time slot and provide startup information"""
        # Select time slot
        for i in range(1, 8):  # Check for slots for up to 7 days
            no_slots = self.page.locator(self.locators.CHECK_SLOTS_AVAILABILITY)
            if no_slots.is_visible():
                # If no slots available, try next day
                DAY_SELECTOR = f"{self.locators.WEEK_DAYS}[{i}]"
                week_days = self.page.locator(DAY_SELECTOR)
                week_days.wait_for(state="visible", timeout=5000)
                week_days.click()  # Click on next day
                self.page.wait_for_timeout(2000)  # Wait for slots to load
            else:
                time_slot = self.page.locator(self.locators.SELECT_TIME_SLOT)
                time_slot.wait_for(state="visible", timeout=10000)
                self.page.click(self.locators.SELECT_TIME_SLOT)
                break
            
        
        
        # Fill startup information
        startup_info = self.page.locator(self.locators.STARTUPINFORMATION_TEXT)
        startup_info.wait_for(state="visible", timeout=5000)
        self.page.fill(self.locators.STARTUPINFORMATION_TEXT, "test startup")
        
        # Select startup stage
        startup_stage = self.page.locator(self.locators.WHICH_STAGETEXT)
        startup_stage.wait_for(state="visible", timeout=5000)
        self.page.click(self.locators.WHICH_STAGETEXT)
        scaling_option = self.page.locator(self.locators.SCALING_OPTION)
        scaling_option.wait_for(state="visible", timeout=5000)
        self.page.click(self.locators.SCALING_OPTION)
        
        # Fill LinkedIn URL
        linkedin_url = self.page.locator(self.locators.LINKEDIN_URL)
        linkedin_url.wait_for(state="visible", timeout=5000)
        self.page.fill(self.locators.LINKEDIN_URL, "https://www.linkedin.com/in/testprofile")
        
        # Fill meeting expectation
        meeting_expectation = self.page.locator(self.locators.MEETING_EXPECTATION_TEXTAREA)
        meeting_expectation.wait_for(state="visible", timeout=5000)
        self.page.fill(self.locators.MEETING_EXPECTATION_TEXTAREA, "test expectation")
        
        attach_screenshot(self.page, "Selected Slot and Provided Startup Information")

    def click_request_meeting_button(self):
        """Click on the final request meeting button"""
        confirm_button = self.page.locator(self.locators.CONFIRM_REQUEST_BUTTON)
        confirm_button.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.CONFIRM_REQUEST_BUTTON)
        attach_screenshot(self.page, "Clicked Confirm Request Button")

    def click_experts_section(self):
        """Click on Experts section"""
        experts = self.page.locator(self.locators.EXPERTS)
        experts.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.EXPERTS)
        attach_screenshot(self.page, "Clicked Experts Section")

    def click_service_providers_section(self):
        """Click on Service Providers section"""
        service_providers = self.page.locator(self.locators.SERVICE_PROVIDERS)
        service_providers.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.SERVICE_PROVIDERS)
        attach_screenshot(self.page, "Clicked Service Providers Section")

    def click_my_requests_section(self):
        """Click on My Requests section"""
        my_requests = self.page.locator(self.locators.MY_REQUESTS)
        my_requests.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.MY_REQUESTS)
        attach_screenshot(self.page, "Clicked My Requests Section")

