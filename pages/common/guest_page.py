from locators.common.guest_locators import GuestLocators
from utils.helpers import attach_screenshot, highlight_element


class GuestPage:
	def __init__(self, page):
		self.page = page
		self.locators = GuestLocators()

	def navigate_to_guest_page(self, url):
		try:
			self.page.goto(url, wait_until="domcontentloaded")
		except Exception as e:
			attach_screenshot(self.page, "Navigate to Guest Page Failed")
			print(f"Failed to navigate to guest page: {e}")
	def click_explore(self):
		try:
			self.page.locator(self.locators.EXPLORE_BUTTON).wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.EXPLORE_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Click Explore Button Failed")
			print(f"Failed to click explore button: {e}")
	def validate_ignite_and_liftoff(self):
		try:
			ignite = self.page.locator(self.locators.VALIDATE_WADHWANI_IGNITE)
			ignite.wait_for(state="visible", timeout=10000)
			assert ignite.is_visible(), "Wadhwani Ignite section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_WADHWANI_IGNITE)

			liftoff = self.page.locator(self.locators.VALIDATE_WADHWANI_LIFTOFF)
			liftoff.wait_for(state="visible", timeout=10000)
			assert liftoff.is_visible(), "Wadhwani Liftoff section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_WADHWANI_LIFTOFF)
		except Exception as e:
			attach_screenshot(self.page, "Ignite and Liftoff Validation Failed")
			print(f"Ignite and Liftoff validation failed: {e}")
	def validate_footer_section(self):
		try:
			footer = self.page.locator(self.locators.VALIDATE_FOOTER_CONTAINER)
			footer.wait_for(state="visible", timeout=10000)
			assert footer.is_visible(), "Footer container is not visible"
			highlight_element(self.page, self.locators.VALIDATE_FOOTER_CONTAINER)

			footer_image = self.page.locator(self.locators.VALIDATE_FOOTER_IMAGE)
			assert footer_image.is_visible(), "Footer image is not visible"
			highlight_element(self.page, self.locators.VALIDATE_FOOTER_IMAGE)

			social_logos = self.page.locator(self.locators.VALIDATE_SOCIAL_LOGOS)
			assert social_logos.count() == 5, f"Expected 5 social logos, found {social_logos.count()}"
			highlight_element(self.page, self.locators.VALIDATE_SOCIAL_LOGOS)

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
		except Exception as e:
			attach_screenshot(self.page, "Footer Section Validation Failed")
			print(f"Footer section validation failed: {e}")
	def click_programs(self):
		try:
			programs = self.page.locator(self.locators.PROGRAMS)
			programs.wait_for(state="visible", timeout=10000)
			self.page.evaluate("window.scrollTo(0, 0)")
			self.page.hover(self.locators.PROGRAMS)
		except Exception as e:
			attach_screenshot(self.page, "Click Programs Menu Failed")
			print(f"Failed to click programs menu: {e}")
	def click_ignite(self):
		try:
			self.page.hover(self.locators.PROGRAMS)
			self.page.click(self.locators.IGNITE_OPTION, force=True)
		except Exception as e:
			attach_screenshot(self.page, "Click Ignite Option Failed")
			print(f"Failed to click ignite option: {e}")
	def validate_cohort_section_and_enroll_button(self):
		try:
			cohort = self.page.locator(self.locators.COHORT_UP_NOW)
			cohort.wait_for(state="visible", timeout=10000)
			assert cohort.is_visible(), "Cohort Up Now section is not visible"
			highlight_element(self.page, self.locators.COHORT_UP_NOW)

			enroll_button = self.page.locator(self.locators.VALIDATE_ENROLL_NOW_BUTTON)
			enroll_button.wait_for(state="visible", timeout=10000)
			assert enroll_button.is_visible(), "Enroll Now button is not visible"
			highlight_element(self.page, self.locators.VALIDATE_ENROLL_NOW_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Cohort Section Validation Failed")
			print(f"Cohort section validation failed: {e}")
	def click_liftoff(self):
		try:
			self.page.hover(self.locators.PROGRAMS)
			self.page.click(self.locators.LIFTOFF_OPTION, force=True)
		except Exception as e:
			attach_screenshot(self.page, "Click Liftoff Option Failed")
			print(f"Failed to click liftoff option: {e}")
	def validate_ready_to_liftoff_and_start_now_button(self):
		try:
			ready_to_liftoff = self.page.locator(self.locators.VALIDATE_READY_TO_LIFTOFF)
			ready_to_liftoff.wait_for(state="visible", timeout=10000)
			assert ready_to_liftoff.is_visible(), "Ready to Liftoff section is not visible"
			highlight_element(self.page, self.locators.VALIDATE_READY_TO_LIFTOFF)

			start_now_button = self.page.locator(self.locators.VALIDATE_START_NOW_BUTTON)
			start_now_button.wait_for(state="visible", timeout=10000)
			assert start_now_button.is_visible(), "Start Now button is not visible"
			highlight_element(self.page, self.locators.VALIDATE_START_NOW_BUTTON)
		except Exception as e:
			attach_screenshot(self.page, "Ready to Liftoff Section Validation Failed")
			print(f"Ready to Liftoff section validation failed: {e}")
