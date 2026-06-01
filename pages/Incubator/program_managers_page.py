from datetime import datetime

from locators.Incubator_locators.program_managers_locators import program_managers_locators
from utils.helpers import attach_screenshot, highlight_element


class IncubatorProgramManagersPage:
    def __init__(self, page):
        self.page = page
        self.locators = program_managers_locators()

    def _wait_and_click(self, locator, timeout=15000, force=False):
        element = self.page.locator(locator)
        state = "attached" if force else "visible"
        element.first.wait_for(state=state, timeout=timeout)
        if force:
            element.first.evaluate("el => el.click()")
        else:
            element.first.click()

    def _wait_and_fill(self, locator, value, timeout=15000):
        element = self.page.locator(locator)
        element.first.wait_for(state="visible", timeout=timeout)
        element.first.fill(str(value))

    def _select_dropdown_option(self, selector_locator, search_input_locator, option_locator, value):
        """Select an option from an Ant Design searchable dropdown."""
        self._wait_and_click(selector_locator, force=True)
        search_input = self.page.locator(search_input_locator).first
        search_input.wait_for(state="attached", timeout=10000)
        search_input.fill(str(value))

        option = self.page.locator(option_locator)
        if option.count() > 0:
            option.first.wait_for(state="visible", timeout=10000)
            option.first.click()
        else:
            # Fallback for virtualized lists where option text node is transient.
            search_input.press("Enter")

    def click_profile_icon(self):
        try:
            self._wait_and_click(self.locators.MY_PROFILE)
            highlight_element(self.page, self.locators.MY_PROFILE)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Program Managers Click Profile Icon Failed")
            print(f"Incubator click profile icon failed: {exc}")

    def click_program_managers_tab(self):
        try:
            self._wait_and_click(self.locators.PROGRAM_MANAGERS_TAB)
            highlight_element(self.page, self.locators.PROGRAM_MANAGERS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Program Managers Tab Failed")
            print(f"Incubator click program managers tab failed: {exc}")

    def validate_program_managers_heading(self, expected_heading):
        try:
            heading = self.page.locator(self.locators.PROGRAM_MANAGERS_HEADING)
            heading.first.wait_for(state="visible", timeout=15000)
            actual_heading = heading.first.inner_text().strip()
            assert actual_heading == expected_heading, (
                f"Expected heading '{expected_heading}', but got '{actual_heading}'"
            )
            highlight_element(self.page, self.locators.PROGRAM_MANAGERS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Program Managers Heading Failed")
            print(f"Incubator validate program managers heading failed: {exc}")

    def click_add_program_manager_button(self):
        try:
            self._wait_and_click(self.locators.ADD_PROGRAM_MANAGER_BUTTON)
            highlight_element(self.page, self.locators.ADD_PROGRAM_MANAGER_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Add Program Manager Failed")
            print(f"Incubator click add program manager button failed: {exc}")

    def fill_required_details_and_click_create(self):
        try:
            unique_suffix = datetime.now().strftime("%H%M%S")

            self._wait_and_fill(self.locators.FIRST_NAME_INPUT, "Test")
            self._wait_and_fill(self.locators.LAST_NAME_INPUT, "Manager")
            self._wait_and_fill(self.locators.EMAIL_INPUT, f"test.pm.{unique_suffix}@mailinator.com")
            self._wait_and_fill(self.locators.MOBILE_NUMBER_INPUT, "9876543210")

            self._select_dropdown_option(
                self.locators.SELECT_COUNTRY,
                "//label[text()='Select Country']/following::input[contains(@class,'ant-select-selection-search-input')][1]",
                self.locators.INDIA_OPTION,
                "India",
            )
            self.page.wait_for_timeout(800)

            self._select_dropdown_option(
                self.locators.SELECT_CITY,
                "//label[text()='Select City']/following::input[contains(@class,'ant-select-selection-search-input')][1]",
                self.locators.BANGALORE_OPTION,
                "Bangalore",
            )
            self.page.wait_for_timeout(800)

            self._wait_and_click(self.locators.CREATE_BUTTON)
            self.page.wait_for_timeout(1000)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Create Program Manager Failed")
            print(f"Incubator fill required details and create failed: {exc}")
