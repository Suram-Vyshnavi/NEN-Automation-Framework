from locators.common.digital_library_locators import digital_library_locators
from utils.helpers import attach_screenshot, highlight_element


class DigitalLibraryPage:
	def __init__(self, page):
		self.page = page
		self.locators = digital_library_locators()

	def click_digital_library_section(self):
		try:
			digital_library_header = self.page.locator(self.locators.DIGITAL_LIBRARY_HEADER)
			digital_library_header.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.DIGITAL_LIBRARY_HEADER)
		except Exception as e:
			attach_screenshot(self.page, "Click Digital Library Section Failed")
			print(f"Failed to click digital library section: {e}")
	def validate_digital_library_page_section(self):
		try:
			heading = self.page.locator(self.locators.VALIDATE_DIGITAL_LIBRARY_HEADING)
			heading.wait_for(state="visible", timeout=10000)
			heading.scroll_into_view_if_needed()
			assert heading.is_visible(), "Digital Library heading is not visible"
			highlight_element(self.page, self.locators.VALIDATE_DIGITAL_LIBRARY_HEADING)
		except Exception as e:
			attach_screenshot(self.page, "Digital Library Page Section Validation Failed")
			print(f"Digital library page section validation failed: {e}")
	def validate_latest_articles_and_videos_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_LATEST_ARTICLES_AND_VIDEOS)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Latest Articles & Videos section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_LATEST_ARTICLES_AND_VIDEOS)
		except Exception as e:
			attach_screenshot(self.page, "Latest Articles and Videos Section Validation Failed")
			print(f"Latest articles and videos section validation failed: {e}")
	def validate_what_are_you_looking_for_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_WRU_LOOKING_FOR)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "What are you looking for? section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_WRU_LOOKING_FOR)
		except Exception as e:
			attach_screenshot(self.page, "What Are You Looking For Section Validation Failed")
			print(f"What are you looking for section validation failed: {e}")
	def validate_experts_videos_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_EXPERT_VIDEOS)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Expert Videos section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_EXPERT_VIDEOS)
		except Exception as e:
			attach_screenshot(self.page, "Expert Videos Section Validation Failed")
			print(f"Expert videos section validation failed: {e}")
	def validate_casestudies_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_CASE_STUDIES)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Case Studies section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_CASE_STUDIES)
		except Exception as e:
			attach_screenshot(self.page, "Case Studies Section Validation Failed")
			print(f"Case studies section validation failed: {e}")
	def validate_caselets_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_CASELETS)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Caselets section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_CASELETS)
		except Exception as e:
			attach_screenshot(self.page, "Caselets Section Validation Failed")
			print(f"Caselets section validation failed: {e}")
	def validate_concept_notes_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_CONCEPT_NOTES)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Concept Notes section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_CONCEPT_NOTES)
		except Exception as e:
			attach_screenshot(self.page, "Concept Notes Section Validation Failed")
			print(f"Concept notes section validation failed: {e}")
	def validate_solution_kits_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_SOLUTION_KITS)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Solution Kits section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_SOLUTION_KITS)
		except Exception as e:
			attach_screenshot(self.page, "Solution Kits Section Validation Failed")
			print(f"Solution kits section validation failed: {e}")
	def validate_good_reads_section(self):
		try:
			section = self.page.locator(self.locators.VALIDATE_GOOD_READS)
			section.wait_for(state="visible", timeout=10000)
			section.scroll_into_view_if_needed()
			assert section.is_visible(), "Good Reads section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_GOOD_READS)
		except Exception as e:
			attach_screenshot(self.page, "Good Reads Section Validation Failed")
			print(f"Good reads section validation failed: {e}")
	def search_test_in_search_input(self):
		try:
			search_input = self.page.locator(self.locators.SEARCH_INPUT)
			search_input.wait_for(state="visible", timeout=10000)
			search_input.scroll_into_view_if_needed()
			self.page.fill(self.locators.SEARCH_INPUT, "test")
			self.page.keyboard.press("Enter")
			self.page.wait_for_timeout(2000)
		except Exception as e:
			attach_screenshot(self.page, "Search in Digital Library Failed")
			print(f"Search in digital library failed: {e}")
	def click_first_search_result(self):
		try:
			first_result = self.page.locator(self.locators.FIRST_SEARCH_RESULT)
			first_result.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.FIRST_SEARCH_RESULT)
			self.page.wait_for_timeout(15000)
		except Exception as e:
			attach_screenshot(self.page, "Click First Search Result Failed")
			print(f"Failed to click first search result: {e}")
	def validate_suggested_article_videos_section_and_click_back_button(self):
		try:
			suggested_section = self.page.locator(self.locators.VALIDATE_SUGGESTED_ARTICLES_VIDEOS)
			suggested_section.wait_for(state="visible", timeout=10000)
			assert suggested_section.is_visible(), "Suggested Articles & Videos section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_SUGGESTED_ARTICLES_VIDEOS)
			back_button = self.page.locator(self.locators.BACK_BUTTON)
			back_button.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.BACK_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Suggested Articles Section Validation Failed")
			print(f"Suggested articles section validation failed: {e}")
