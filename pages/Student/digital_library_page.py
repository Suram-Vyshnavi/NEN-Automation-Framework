from locators.student_locators.digital_library_locators import digital_library_locators
from utils.helpers import attach_screenshot, highlight_element


class DigitalLibraryPage:
    def __init__(self, page):
        self.page = page
        self.locators = digital_library_locators()

    def click_digital_library_section(self):
        """Click on Digital Library section from header"""
        digital_library_header = self.page.locator(self.locators.DIGITAL_LIBRARY_HEADER)
        digital_library_header.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.DIGITAL_LIBRARY_HEADER)
        attach_screenshot(self.page, "Clicked Digital Library Section")

    def validate_digital_library_page_section(self):
        """Validate Digital Library page heading"""
        heading = self.page.locator(self.locators.VALIDATE_DIGITAL_LIBRARY_HEADING)
        heading.wait_for(state="visible", timeout=10000)
        heading.scroll_into_view_if_needed()
        assert heading.is_visible(), "Digital Library heading is not visible"
        highlight_element(self.page, self.locators.VALIDATE_DIGITAL_LIBRARY_HEADING)
        attach_screenshot(self.page, "Digital Library Page Section Validated")

    def validate_latest_articles_and_videos_section(self):
        """Validate Latest Articles & Videos section"""
        section = self.page.locator(self.locators.VALIDATE_LATEST_ARTICLES_AND_VIDEOS)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Latest Articles & Videos section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_LATEST_ARTICLES_AND_VIDEOS)
        attach_screenshot(self.page, "Latest Articles and Videos Section Validated")

    def validate_what_are_you_looking_for_section(self):
        """Validate What are you looking for? section"""
        section = self.page.locator(self.locators.VALIDATE_WRU_LOOKING_FOR)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "What are you looking for? section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_WRU_LOOKING_FOR)
        attach_screenshot(self.page, "What Are You Looking For Section Validated")

    def validate_experts_videos_section(self):
        """Validate Expert Videos section"""
        section = self.page.locator(self.locators.VALIDATE_EXPERT_VIDEOS)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Expert Videos section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_EXPERT_VIDEOS)
        attach_screenshot(self.page, "Expert Videos Section Validated")

    def validate_casestudies_section(self):
        """Validate Case Studies section"""
        section = self.page.locator(self.locators.VALIDATE_CASE_STUDIES)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Case Studies section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_CASE_STUDIES)
        attach_screenshot(self.page, "Case Studies Section Validated")

    def validate_caselets_section(self):
        """Validate Caselets section"""
        section = self.page.locator(self.locators.VALIDATE_CASELETS)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Caselets section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_CASELETS)
        attach_screenshot(self.page, "Caselets Section Validated")

    def validate_concept_notes_section(self):
        """Validate Concept Notes section"""
        section = self.page.locator(self.locators.VALIDATE_CONCEPT_NOTES)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Concept Notes section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_CONCEPT_NOTES)
        attach_screenshot(self.page, "Concept Notes Section Validated")

    def validate_solution_kits_section(self):
        """Validate Solution Kits section"""
        section = self.page.locator(self.locators.VALIDATE_SOLUTION_KITS)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Solution Kits section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_SOLUTION_KITS)
        attach_screenshot(self.page, "Solution Kits Section Validated")

    def validate_good_reads_section(self):
        """Validate Good Reads section"""
        section = self.page.locator(self.locators.VALIDATE_GOOD_READS)
        section.wait_for(state="visible", timeout=10000)
        section.scroll_into_view_if_needed()
        assert section.is_visible(), "Good Reads section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_GOOD_READS)
        attach_screenshot(self.page, "Good Reads Section Validated")

    def search_test_in_search_input(self):
        """Search for 'test' in search input"""
        search_input = self.page.locator(self.locators.SEARCH_INPUT)
        search_input.wait_for(state="visible", timeout=10000)
        search_input.scroll_into_view_if_needed()
        self.page.fill(self.locators.SEARCH_INPUT, "test")
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)  # Wait for search results
        attach_screenshot(self.page, "Searched for 'test' in Search Input")

    def click_first_search_result(self):
        """Click on first search result"""
        first_result = self.page.locator(self.locators.FIRST_SEARCH_RESULT)
        first_result.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.FIRST_SEARCH_RESULT)
        self.page.wait_for_timeout(15000)  # Wait for result details to load
        attach_screenshot(self.page, "Clicked First Search Result")

    def validate_suggested_article_videos_section_and_click_back_button(self):
        """Validate Suggested Articles & Videos section and click back button"""
        suggested_section = self.page.locator(self.locators.VALIDATE_SUGGESTED_ARTICLES_VIDEOS)
        suggested_section.wait_for(state="visible", timeout=10000)
        assert suggested_section.is_visible(), "Suggested Articles & Videos section is not visible"
        highlight_element(self.page, self.locators.VALIDATE_SUGGESTED_ARTICLES_VIDEOS)
        
        # Click back button
        back_button = self.page.locator(self.locators.BACK_BUTTON)
        back_button.wait_for(state="visible", timeout=10000)
        self.page.click(self.locators.BACK_BUTTON)
        attach_screenshot(self.page, "Validated Suggested Articles Videos Section and Clicked Back Button")
