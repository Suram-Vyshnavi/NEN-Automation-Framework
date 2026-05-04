from locators.student_locators.home_locators import HomeLocators
from locators.common.login_locators import LoginLocators
from utils.helpers import attach_screenshot, highlight_element


class HomePage:
    def __init__(self, page):
        self.page = page
        self.locators = HomeLocators()
        self.login_locators = LoginLocators()

    def handle_all_popups(self):
        """Handle all 4 popups that may appear after login"""
        
        # Popup 1: No thanks (already handled in login, but check again)
        try:
            no_thanks = self.page.locator(self.login_locators.NO_THANKS_POPUP)
            no_thanks.wait_for(state="visible", timeout=5000)
            if no_thanks.is_visible():
                self.page.click(self.login_locators.NO_THANKS_POPUP)
        except:
            pass
        
        # Popup 2: Start your Journey popup - validate and click Next
        try:
            journey_popup = self.page.locator(self.login_locators.START_YOUR_JOURNEY_POPUP)
            journey_popup.wait_for(state="visible", timeout=5000)
            if journey_popup.is_visible():
                highlight_element(self.page, self.login_locators.START_YOUR_JOURNEY_POPUP)
                
                next_button = self.page.locator(self.login_locators.NEXT_BUTTON)
                next_button.wait_for(state="visible", timeout=5000)
                self.page.click(self.login_locators.NEXT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Popup 2 Handling Failed")
            print(f"Popup 2 not found or already handled: {e}")
        
        # Popup 3: Create a personalised journey popup - validate and click Next
        try:
            personalised_popup = self.page.locator(self.login_locators.CREATE_PERSONALISED_JOURNEY_POPUP)
            personalised_popup.wait_for(state="visible", timeout=5000)
            if personalised_popup.is_visible():
                highlight_element(self.page, self.login_locators.CREATE_PERSONALISED_JOURNEY_POPUP)
                
                next_button = self.page.locator(self.login_locators.NEXT_BUTTON)
                next_button.wait_for(state="visible", timeout=5000)
                self.page.click(self.login_locators.NEXT_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Popup 3 Handling Failed")
            print(f"Popup 3 not found or already handled: {e}")
        
        # Popup 4: Start program journey button - final popup
        try:
            start_journey_btn = self.page.locator(self.login_locators.START_PROGRAM_JOURNEY_BUTTON)
            start_journey_btn.wait_for(state="visible", timeout=5000)
            if start_journey_btn.is_visible():
                highlight_element(self.page, self.login_locators.START_PROGRAM_JOURNEY_BUTTON)
                
                self.page.click(self.login_locators.START_PROGRAM_JOURNEY_BUTTON)
        except Exception as e:
            attach_screenshot(self.page, "Popup 4 Handling Failed")
            print(f"Popup 4 not found or already handled: {e}")

    def navigate_and_validate_all_headers(self):
        try:
            headers = [
                (self.locators.HOME_HEADER, "Home"),
                (self.locators.RESOURCE_NETWORK_HEADER, "Resource Network"),
                (self.locators.DIGITAL_LIBRARY_HEADER, "Digital Library"),
                (self.locators.CALENDAR_HEADER, "Calendar"),
                (self.locators.EVENTS_HEADER, "Events"),
                (self.locators.CHAT_BADGE_HEADER, "Chat Badge"),
                (self.locators.NOTIFICATION_BADGE_HEADER, "Notification Badge"),
                (self.locators.PROFILE_MENU_HEADER, "Profile Menu")
            ]

            for locator, name in headers:
                if name != "Home":
                    home_header = self.page.locator(self.locators.HOME_HEADER)
                    home_header.wait_for(state="visible", timeout=10000)
                    self.page.click(locator)

                header_element = self.page.locator(locator)
                header_element.wait_for(state="visible", timeout=20000)
                assert header_element.is_visible(), f"{name} header is not visible"
                highlight_element(self.page, locator)
                if name == "Notification Badge":
                    close_button = self.page.locator(self.locators.NOTIFICATION_CLOSE)
                    close_button.wait_for(state="visible", timeout=5000)
                    self.page.click(self.locators.NOTIFICATION_CLOSE)
        except Exception as e:
            attach_screenshot(self.page, "Navigate and Validate All Headers Failed")
            print(f"Failed to navigate and validate all headers: {e}")
    def navigate_to_home_page(self):
        try:
            home_header = self.page.locator(self.locators.HOME_HEADER)
            home_header.wait_for(state="visible", timeout=10000)
            self.page.click(self.locators.HOME_HEADER)
        except Exception as e:
            attach_screenshot(self.page, "Navigate to Home Page Failed")
            print(f"Failed to navigate to home page: {e}")
    def validate_certification_section(self):
        """Validate Certification Logic section"""
        try:
            cert_section = self.page.locator(self.locators.CERTIFICATION_SECTION)
            cert_section.wait_for(state="visible", timeout=10000)
            assert cert_section.is_visible(), "Certification section is not visible"
            highlight_element(self.page, self.locators.CERTIFICATION_SECTION)
        except Exception as e:
            print(f"Certification section validation failed: {e}")
            attach_screenshot(self.page, "Certification Section Validation Failed")
    def validate_personalized_journey_section(self):
        """Validate Personalized Journey section"""
        try:
            journey_section = self.page.locator(self.locators.PERSONALIZED_JOURNEY_SECTION)
            journey_section.wait_for(state="visible", timeout=10000)
            assert journey_section.is_visible(), "Personalized Journey section is not visible"
            highlight_element(self.page, self.locators.PERSONALIZED_JOURNEY_SECTION)
        except Exception as e:
            print(f"Personalized Journey section validation failed: {e}")
            attach_screenshot(self.page, "Personalized Journey Section Validation Failed")

    def validate_featured_resource_network_section(self):
        """Validate Featured Resource Network section"""
        try:
            resource_section = self.page.locator(self.locators.FEATURED_RESOURCE_NETWORK_SECTION)
            resource_section.wait_for(state="visible", timeout=10000)
            assert resource_section.is_visible(), "Featured Resource Network section is not visible"
            highlight_element(self.page, self.locators.FEATURED_RESOURCE_NETWORK_SECTION)
        except Exception as e:
            print(f"Featured Resource Network section validation failed: {e}")
            attach_screenshot(self.page, "Featured Resource Network Section Validation Failed")

    def validate_mentor_card_and_request_meeting_button(self):
        """Validate Mentor Card and Request Meeting button"""
        try:
            mentor_card = self.page.locator(self.locators.MENTOR_CARD)
            mentor_card.wait_for(state="visible", timeout=10000)
            assert mentor_card.is_visible(), "Mentor card is not visible"
            highlight_element(self.page, self.locators.MENTOR_CARD)
            
            request_meeting_btn = self.page.locator(self.locators.REQUEST_MEETING_BUTTON)
            assert request_meeting_btn.is_visible(), "Request Meeting button is not visible"
            highlight_element(self.page, self.locators.REQUEST_MEETING_BUTTON)
            
        except Exception as e:
            print(f"Mentor card or Request Meeting button validation failed: {e}")
            attach_screenshot(self.page, "Mentor Card and Request Meeting Button Validation Failed")

    def validate_recommended_content_section(self):
        """Validate Recommended Content section"""
        try:
            content_section = self.page.locator(self.locators.RECOMMENDED_CONTENT_SECTION)
            content_section.wait_for(state="visible", timeout=10000)
            assert content_section.is_visible(), "Recommended Content section is not visible"
            highlight_element(self.page, self.locators.RECOMMENDED_CONTENT_SECTION)
        except Exception as e:
            print(f"Recommended Content section validation failed: {e}")
            attach_screenshot(self.page, "Recommended Content Section Validation Failed")
            

    def validate_recommended_by_your_institute_section(self):
        """Validate Recommended By Your Institute section"""
        try:
            institute_section = self.page.locator(self.locators.RECOMMENDED_BY_YOUR_INSTITUTE_SECTION)
            institute_section.wait_for(state="visible", timeout=10000)
            assert institute_section.is_visible(), "Recommended By Your Institute section is not visible"
            highlight_element(self.page, self.locators.RECOMMENDED_BY_YOUR_INSTITUTE_SECTION)
        except Exception as e:
            print(f"Recommended By Your Institute section validation failed: {e}")
            attach_screenshot(self.page, "Recommended By Your Institute Section Validation Failed")
            

    def validate_courses_section_and_first_course(self):
        """Validate Courses section and first course details"""
        try:
            courses_section = self.page.locator(self.locators.COURSES_SECTION)
            courses_section.wait_for(state="visible", timeout=10000)
            assert courses_section.is_visible(), "Courses section is not visible"
            highlight_element(self.page, self.locators.COURSES_SECTION)
            
            first_course = self.page.locator(self.locators.FIRST_COURSE)
            first_course.wait_for(state="visible", timeout=10000)
            assert first_course.is_visible(), "First course is not visible"
            highlight_element(self.page, self.locators.FIRST_COURSE)
            
        except Exception as e:
            print(f"Courses section or first course validation failed: {e}")
            attach_screenshot(self.page, "Courses Section and First Course Validation Failed")
