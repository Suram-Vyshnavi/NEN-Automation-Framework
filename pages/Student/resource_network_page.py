from locators.student_locators.resource_network_locators import ResourceNetwork_locators
from utils.helpers import attach_screenshot, highlight_element


class ResourceNetworkPage:
    def __init__(self, page):
        self.page = page
        self.locators = ResourceNetwork_locators()

    def click_resource_network_section(self):
        try:
            self.page.wait_for_timeout(4000)
            resource_header = self.page.locator(self.locators.RESOURCE_HEADER)
            resource_header.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.RESOURCE_HEADER)
        except Exception as e:
            attach_screenshot(self.page, "Click Resource Network Section Failed")
            print(f"Failed to click resource network section: {e}")
    def click_explore_section(self):
        try:
            explore = self.page.locator(self.locators.EXPLORE)
            explore.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.EXPLORE)
        except Exception as e:
            attach_screenshot(self.page, "Click Explore Section Failed")
            print(f"Failed to click explore section: {e}")
    def validate_mentors_experts_service_providers_cards(self):
        try:
            mentors_card = self.page.locator(self.locators.MENTORS_CARD)
            mentors_card.wait_for(state="visible", timeout=10000)
            assert mentors_card.is_visible(), "Mentors card is not visible"
            highlight_element(self.page, self.locators.MENTORS_CARD)

            experts_card = self.page.locator(self.locators.EXPERTS_CARD)
            assert experts_card.is_visible(), "Experts card is not visible"
            highlight_element(self.page, self.locators.EXPERTS_CARD)

            service_providers_card = self.page.locator(self.locators.SERVICE_PROVIDERS_CARD)
            assert service_providers_card.is_visible(), "Service Providers card is not visible"
            highlight_element(self.page, self.locators.SERVICE_PROVIDERS_CARD)

        except Exception as e:
            attach_screenshot(self.page, "Mentors Experts Service Providers Validation Failed")
            print(f"Mentors/Experts/Service Providers cards validation failed: {e}")
    def click_mentors_section(self):
        try:
            mentors = self.page.locator(self.locators.MENTORS)
            mentors.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.MENTORS)
        except Exception as e:
            attach_screenshot(self.page, "Click Mentors Section Failed")
            print(f"Failed to click mentors section: {e}")
    def search_test_in_search_network(self):
        try:
            search_input = self.page.locator(self.locators.SEARCH_NETWORK)
            search_input.wait_for(state="visible", timeout=10000)
            self.page.fill(self.locators.SEARCH_NETWORK, "Pratibha")
            self.page.keyboard.press("Enter")
            self.page.wait_for_timeout(2000)
        except Exception as e:
            attach_screenshot(self.page, "Search in Network Failed")
            print(f"Search in network failed: {e}")
    def click_first_search_result_request_meeting_button(self):
        try:
            request_meeting = self.page.locator(self.locators.REQUEST_MEETING)
            request_meeting.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.REQUEST_MEETING)
        except Exception as e:
            attach_screenshot(self.page, "Click Request Meeting Button Failed")
            print(f"Failed to click request meeting button: {e}")
    def select_slot_and_provide_startup_information(self):
        try:
            for i in range(1, 8):
                no_slots = self.page.locator(self.locators.CHECK_SLOTS_AVAILABILITY)
                if no_slots.is_visible():
                    DAY_SELECTOR = f"{self.locators.WEEK_DAYS}[{i}]"
                    week_days = self.page.locator(DAY_SELECTOR)
                    week_days.wait_for(state="visible", timeout=5000)
                    week_days.click()
                    self.page.wait_for_timeout(2000)
                else:
                    time_slot = self.page.locator(self.locators.SELECT_TIME_SLOT)
                    time_slot.wait_for(state="visible", timeout=10000)
                    self.page.click(self.locators.SELECT_TIME_SLOT)
                    break

            startup_info = self.page.locator(self.locators.STARTUPINFORMATION_TEXT)
            startup_info.wait_for(state="visible", timeout=5000)
            self.page.fill(self.locators.STARTUPINFORMATION_TEXT, "test startup")

            startup_stage = self.page.locator(self.locators.WHICH_STAGETEXT)
            startup_stage.wait_for(state="visible", timeout=5000)
            self.page.click(self.locators.WHICH_STAGETEXT)
            scaling_option = self.page.locator(self.locators.SCALING_OPTION)
            scaling_option.wait_for(state="visible", timeout=5000)
            self.page.click(self.locators.SCALING_OPTION)

            linkedin_url = self.page.locator(self.locators.LINKEDIN_URL)
            linkedin_url.wait_for(state="visible", timeout=5000)
            self.page.fill(self.locators.LINKEDIN_URL, "https://www.linkedin.com/in/testprofile")

            meeting_expectation = self.page.locator(self.locators.MEETING_EXPECTATION_TEXTAREA)
            meeting_expectation.wait_for(state="visible", timeout=5000)
            self.page.fill(self.locators.MEETING_EXPECTATION_TEXTAREA, "test expectation")

        except Exception as e:
            attach_screenshot(self.page, "Select Slot and Provide Startup Information Failed")
            print(f"Failed to select slot and provide startup information: {e}")
    def click_request_meeting_button(self):
        try:
            confirm_button = self.page.locator(self.locators.CONFIRM_REQUEST_BUTTON)
            confirm_button.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.CONFIRM_REQUEST_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Click Confirm Request Button Failed")
            print(f"Failed to click confirm request button: {e}")
    def click_experts_section(self):
        try:
            experts = self.page.locator(self.locators.EXPERTS)
            experts.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.EXPERTS)
        except Exception as e:
            attach_screenshot(self.page, "Click Experts Section Failed")
            print(f"Failed to click experts section: {e}")
    def click_service_providers_section(self):
        try:
            service_providers = self.page.locator(self.locators.SERVICE_PROVIDERS)
            service_providers.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.SERVICE_PROVIDERS)
        except Exception as e:
            attach_screenshot(self.page, "Click Service Providers Section Failed")
            print(f"Failed to click service providers section: {e}")
    def click_my_requests_section(self):
        try:
            my_requests = self.page.locator(self.locators.MY_REQUESTS)
            my_requests.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.MY_REQUESTS)
        except Exception as e:
            attach_screenshot(self.page, "Click My Requests Section Failed")
            print(f"Failed to click my requests section: {e}")
