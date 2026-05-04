from locators.common.myprofile_locators import MyprofileLocators
from utils.helpers import attach_screenshot, highlight_element


class MyProfilePage:
	def __init__(self, page):
		self.page = page
		self.locators = MyprofileLocators()

	def click_profile_icon(self):
		try:
			icon = self.page.locator(self.locators.MY_PROFILE_ICON)
			icon.wait_for(state="visible", timeout=10000)
			self.page.click(self.locators.MY_PROFILE_ICON)
		except Exception as e:
			attach_screenshot(self.page, "Click Profile Icon Failed")
			print(f"Failed to click profile icon: {e}")
	def validate_my_profile_page(self):
		try:
			heading = self.page.locator(self.locators.MY_PROFILE)
			heading.wait_for(state="visible", timeout=10000)
			assert heading.is_visible(), "My Profile page is not displayed"
			highlight_element(self.page, self.locators.MY_PROFILE)
			heading.click()
		except Exception as e:
			attach_screenshot(self.page, "My Profile Page Validation Failed")
			print(f"My profile page validation failed: {e}")
	def _get_profile_language(self):
		if self.page.locator(self.locators.SELECT_CITY_WRAPPER_SPANISH).count() > 0:
			return "spanish"
		if self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH).count() > 0:
			return "english"
		if self.page.locator(self.locators.VALIDATE_SPANISH_LANGUAGE).count() > 0:
			return "spanish"
		if self.page.locator(self.locators.MY_PROFILE).count() > 0:
			return "english"
		return "english"

	def edit_profile(self, first_name, last_name, city="Hyderabad", language="Spanish"):
		first_name_input = self.page.locator(self.locators.FIRST_NAME)
		first_name_input.wait_for(state="visible", timeout=10000)
		first_name_input.fill(first_name)

		last_name_input = self.page.locator(self.locators.LAST_NAME)
		last_name_input.wait_for(state="visible", timeout=10000)
		last_name_input.fill(last_name)

		current_lang = self._get_profile_language()
		if current_lang == "spanish":
			city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_SPANISH)
			city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_SPANISH)
		else:
			city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH)
			city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_ENGLISH)

		if city_wrapper.count() == 0:
			city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH)
		if city_input.count() == 0:
			city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_ENGLISH)

		city_wrapper.wait_for(state="visible", timeout=10000)
		try:
			city_wrapper.click(timeout=10000)
		except Exception:
			city_wrapper.click(force=True)

		if city_input.count() > 0:
			city_input.fill(city)
		else:
			self.page.keyboard.type(city)

		if city == "Hyderabad":
			option = self.page.locator(self.locators.HYDERABAD_OPTION)
			option.wait_for(state="visible", timeout=5000)
			option.click()
		elif city == "Bangalore":
			option = self.page.locator(self.locators.BANGALORE_OPTION)
			option.wait_for(state="visible", timeout=5000)
			option.click()


	def language_selection(self, language):
		try:
			language_dropdown = self.page.locator(self.locators.LANGUAGE)
			language_dropdown.wait_for(state="visible", timeout=10000)
			language_dropdown.click()

			if language.lower() == "spanish":
				language_option = self.page.locator(self.locators.SPANISH_LANGUAGE)
				language_option.wait_for(state="visible", timeout=10000)
				language_option.click()
			else:
				language_option = self.page.locator(self.locators.ENGLISH_LANGUAGE)
				language_option.wait_for(state="visible", timeout=10000)
				language_option.click()
		except Exception as e:
			attach_screenshot(self.page, "Language Selection Failed")
			print(f"Language selection failed: {e}")
	def save_changes(self, language=None):
		try:
			if language and language.lower() == "spanish":
				save_btn = self.page.locator(self.locators.SAVE_BUTTON_SPANISH)
			else:
				save_btn = self.page.locator(self.locators.SAVE_BUTTON)
			save_btn.wait_for(state="visible", timeout=10000)
			save_btn.click()
		except Exception as e:
			attach_screenshot(self.page, "Save Changes Failed")
			print(f"Failed to save profile changes: {e}")
