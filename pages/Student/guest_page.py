from locators.student_locators.guest_locators import GuestLocators
from utils.helpers import attach_screenshot, highlight_element


class GuestPage:
    def __init__(self, page):
        self.page = page
        self.locators = GuestLocators()
    


    def navigate_to_guest_page(self, url):
        """Navigate to the guest page"""
        self.page.goto(url, wait_until='domcontentloaded')
        attach_screenshot(self.page, "Guest Page Loaded")

    def click_explore(self):
        """Click on the Explore button"""
        self.page.locator(self.locators.EXPLORE_BUTTON).wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.EXPLORE_BUTTON)
        attach_screenshot(self.page, "Clicked Explore Button")

    def validate_ignite_and_liftoff(self):
        """Validate Wadhwani Ignite and Liftoff sections"""
        ignite = self.page.locator(self.locators.VALIDATE_WADHWANI_IGNITE)
        ignite.wait_for(state="visible", timeout=10000)
        assert ignite.is_visible(), "Wadhwani Ignite section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_WADHWANI_IGNITE)
        
        liftoff = self.page.locator(self.locators.VALIDATE_WADHWANI_LIFTOFF)
        liftoff.wait_for(state="visible", timeout=10000)
        assert liftoff.is_visible(), "Wadhwani Liftoff section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_WADHWANI_LIFTOFF)
        
        attach_screenshot(self.page, "Ignite and Liftoff Validated")

    def validate_footer_section(self):
        """Validate footer section elements"""
        # Validate footer container
        footer = self.page.locator(self.locators.VALIDATE_FOOTER_CONTAINER)
        footer.wait_for(state="visible", timeout=10000)
        assert footer.is_visible(), "Footer container is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_CONTAINER)
        
        # Validate footer image
        footer_image = self.page.locator(self.locators.VALIDATE_FOOTER_IMAGE)
        assert footer_image.is_visible(), "Footer image is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_IMAGE)
        
        # Validate social logos (5 logos)
        social_logos = self.page.locator(self.locators.VALIDATE_SOCIAL_LOGOS)
        assert social_logos.count() == 5, f"Expected 5 social logos, found {social_logos.count()}"
        highlight_element(self.page, self.locators.VALIDATE_SOCIAL_LOGOS)
        
        # Validate footer sections
        about_us = self.page.locator(self.locators.VALIDATE_FOOTER_ABOUT_US)
        assert about_us.is_visible(), "Footer About Us section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_ABOUT_US)
        
        entrepreneurship = self.page.locator(self.locators.VALIDATE_FOOTER_ENTREPRENEURSHIP)
        assert entrepreneurship.is_visible(), "Footer Entrepreneurship section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_ENTREPRENEURSHIP)
        
        our_programs = self.page.locator(self.locators.VALIDATE_FOOTER_OUR_PROGRAMS)
        assert our_programs.is_visible(), "Footer Our Programs section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_OUR_PROGRAMS)
        
        blogs = self.page.locator(self.locators.VALIDATE_FOOTER_BLOGS)
        assert blogs.is_visible(), "Footer Blogs section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_BLOGS)
        
        contact_us = self.page.locator(self.locators.VALIDATE_FOOTER_CONTACT_US)
        assert contact_us.is_visible(), "Footer Contact Us section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_FOOTER_CONTACT_US)
        
        attach_screenshot(self.page, "Footer Section Validated")

    def click_programs(self):
        """Click on Programs menu"""
        programs = self.page.locator(self.locators.PROGRAMS)
        programs.wait_for(state="visible", timeout=10000)
        # Scroll to top to ensure Programs menu is visible
        self.page.evaluate("window.scrollTo(0, 0)")
        # Hover over Programs to open dropdown
        self.page.hover(self.locators.PROGRAMS)
        # Wait for dropdown menu to appear
        attach_screenshot(self.page, "Clicked Programs Menu")

    def click_ignite(self):
        """Click on Ignite option from Programs menu"""
        # Keep hovering over Programs to keep dropdown open
        self.page.hover(self.locators.PROGRAMS)
        ignite_option = self.page.locator(self.locators.IGNITE_OPTION)
        # Click with force if needed
        self.page.click(self.locators.IGNITE_OPTION, force=True)
        attach_screenshot(self.page, "Clicked Ignite Option")

    def validate_cohort_section_and_enroll_button(self):
        """Validate Cohort section and Enroll Now button"""
        cohort = self.page.locator(self.locators.COHORT_UP_NOW)
        cohort.wait_for(state="visible", timeout=10000)
        assert cohort.is_visible(), "Cohort Up Now section is not visible"
        highlight_element(self.page, self.locators.COHORT_UP_NOW)
        
        enroll_button = self.page.locator(self.locators.VALIDATE_ENROLL_NOW_BUTTON)
        enroll_button.wait_for(state="visible", timeout=10000)
        assert enroll_button.is_visible(), "Enroll Now button is not visible"
        highlight_element(self.page, self.locators.VALIDATE_ENROLL_NOW_BUTTON)
        
        attach_screenshot(self.page, "Cohort Section Validated")

    def click_liftoff(self):
        """Click on Liftoff option from Programs menu"""
        # Keep hovering over Programs to keep dropdown open
        self.page.hover(self.locators.PROGRAMS)
        liftoff_option = self.page.locator(self.locators.LIFTOFF_OPTION)
        # Click with force if needed
        self.page.click(self.locators.LIFTOFF_OPTION, force=True)
        attach_screenshot(self.page, "Clicked Liftoff Option")

    def validate_ready_to_liftoff_and_start_now_button(self):
        """Validate Ready to Liftoff section and Start Now button"""
        ready_to_liftoff = self.page.locator(self.locators.VALIDATE_READY_TO_LIFTOFF)
        ready_to_liftoff.wait_for(state="visible", timeout=10000)
        assert ready_to_liftoff.is_visible(), "Ready to Liftoff section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_READY_TO_LIFTOFF)
        
        start_now_button = self.page.locator(self.locators.VALIDATE_START_NOW_BUTTON)
        start_now_button.wait_for(state="visible", timeout=10000)
        assert start_now_button.is_visible(), "Start Now button is not visible"
        highlight_element(self.page, self.locators.VALIDATE_START_NOW_BUTTON)
        
        attach_screenshot(self.page, "Ready to Liftoff Section Validated")
