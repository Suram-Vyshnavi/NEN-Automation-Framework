from locators.student_locators.Myprofile_locators import MyprofileLocators
from utils.helpers import attach_screenshot, highlight_element


class MyProfilePage:
    def __init__(self, page):
        self.page = page
        self.locators = MyprofileLocators()

    def click_profile_icon(self):
        icon = self.page.locator(self.locators.MY_PROFILE_ICON)
        icon.wait_for(state='visible', timeout=10000)
        self.page.click(self.locators.MY_PROFILE_ICON)
        attach_screenshot(self.page, 'Clicked profile icon')

    def validate_my_profile_page(self):
        heading = self.page.locator(self.locators.MY_PROFILE)
        heading.wait_for(state='visible', timeout=10000)
        assert heading.is_visible(), 'My Profile page is not displayed'
        highlight_element(self.page, self.locators.MY_PROFILE)
        attach_screenshot(self.page, 'My Profile page validated')
        heading.click()  # Click to ensure the page is active

    def _get_profile_language(self):
        # Determine if the page is in Spanish mode or English mode based on existing locators
        if self.page.locator(self.locators.SELECT_CITY_WRAPPER_SPANISH).count() > 0:
            return 'spanish'
        if self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH).count() > 0:
            return 'english'
        if self.page.locator(self.locators.VALIDATE_SPANISH_LANGUAGE).count() > 0:
            return 'spanish'
        if self.page.locator(self.locators.MY_PROFILE).count() > 0:
            return 'english'
        return 'english'

    def edit_profile(self, first_name, last_name, city='Hyderabad', language='Spanish'):
        first_name_input = self.page.locator(self.locators.FIRST_NAME)
        first_name_input.wait_for(state='visible', timeout=10000)
        first_name_input.fill(first_name)

        last_name_input = self.page.locator(self.locators.LAST_NAME)
        last_name_input.wait_for(state='visible', timeout=10000)
        last_name_input.fill(last_name)

        current_lang = self._get_profile_language()
        if current_lang == 'spanish':
            city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_SPANISH)
            city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_SPANISH)
        else:
            city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH)
            city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_ENGLISH)

        if city_wrapper.count() == 0:
            # fallback to generic selectors
            city_wrapper = self.page.locator(self.locators.SELECT_CITY_WRAPPER_ENGLISH)
        if city_input.count() == 0:
            city_input = self.page.locator(self.locators.SELECT_CITY_INPUT_ENGLISH)

        city_wrapper.wait_for(state='visible', timeout=10000)

        city_wrapper.wait_for(state='visible', timeout=10000)

        try:
            city_wrapper.click(timeout=10000)
        except Exception:
            city_wrapper.click(force=True)

        # City text input may differ by language context
        city_search_input = city_input
        if city_search_input.count() > 0:
            city_search_input.fill(city)
        else:
            # fallback: type into currently focused control
            self.page.keyboard.type(city)

        # Wait for the matching city option from the list
        if city == 'Hyderabad':
            hyderabad_option = self.page.locator(self.locators.HYDERABAD_OPTION)
            hyderabad_option.wait_for(state='visible', timeout=5000)
            hyderabad_option.click()
        elif city == 'Bangalore':
            bangalore_option = self.page.locator(self.locators.BANGALORE_OPTION)
            bangalore_option.wait_for(state='visible', timeout=5000)
            bangalore_option.click()
        

        attach_screenshot(self.page, f'Edited profile: {first_name} {last_name}, {city}')

    def language_selection(self, language):
        language_dropdown = self.page.locator(self.locators.LANGUAGE)
        language_dropdown.wait_for(state='visible', timeout=10000)
        language_dropdown.click()

        if language.lower() == 'spanish':
            language_option = self.page.locator(self.locators.SPANISH_LANGUAGE)
            language_option.wait_for(state='visible', timeout=10000)
            language_option.click()
            attach_screenshot(self.page, f'Selected language: {language}')
        else:
            language_option = self.page.locator(self.locators.ENGLISH_LANGUAGE)
            language_option.wait_for(state='visible', timeout=10000)
            language_option.click()
            attach_screenshot(self.page, f'Selected language: {language}')

        

    def save_changes(self,language=None):
        if language and language.lower() == 'spanish':
            save_btn = self.page.locator(self.locators.SAVE_BUTTON_SPANISH)
        else:
            save_btn = self.page.locator(self.locators.SAVE_BUTTON)
        save_btn.wait_for(state='visible', timeout=10000)
        save_btn.click()
        attach_screenshot(self.page, 'Saved profile changes')
        

