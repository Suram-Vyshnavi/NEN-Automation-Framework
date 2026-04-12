from locators.Incubator_locators.partner_profile_locators import partner_profile_locators
from utils.helpers import attach_screenshot, highlight_element


class IncubatorPartnerProfilePage:
    def __init__(self, page):
        self.page = page
        self.locators = partner_profile_locators()

    def _wait_and_click(self, locator, timeout=15000):
        element = self.page.locator(locator)
        element.first.wait_for(state="visible", timeout=timeout)
        element.first.click()

    def _wait_for_visible(self, locator, timeout=15000):
        element = self.page.locator(locator)
        element.first.wait_for(state="visible", timeout=timeout)
        return element.first

    def click_profile_icon_and_navigate_partner_profile_page(self):
        try:
            self._wait_and_click(self.locators.MY_PROFILE)
            self._wait_for_visible(self.locators.PARTNER_PROFILE_TAB)
            self._wait_for_visible(self.locators.PARTNER_PROFILE_HEADING)
            highlight_element(self.page, self.locators.PARTNER_PROFILE_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Partner Profile Navigation Failed")
            print(f"Incubator navigate to partner profile failed: {exc}")

    def click_profile_icon(self):
        try:
            self._wait_and_click(self.locators.MY_PROFILE)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Profile Icon Failed")
            print(f"Incubator click profile icon failed: {exc}")

    def click_partner_profile_tab(self):
        try:
            self._wait_and_click(self.locators.PARTNER_PROFILE_TAB)
            self.page.wait_for_timeout(1000)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Partner Profile Tab Failed")
            print(f"Incubator click partner profile tab failed: {exc}")

    def validate_partner_profile_heading(self):
        try:
            heading = self._wait_for_visible(self.locators.PARTNER_PROFILE_HEADING)
            assert heading.is_visible(), "Partner profile heading is not visible"
            highlight_element(self.page, self.locators.PARTNER_PROFILE_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Partner Profile Heading Failed")
            print(f"Incubator validate partner profile heading failed: {exc}")

    def validate_partner_name(self):
        try:
            name_input = self._wait_for_visible(self.locators.NAME_INPUT)
            partner_name = name_input.input_value().strip()
            assert partner_name, "Partner name is empty"
            highlight_element(self.page, self.locators.NAME_INPUT)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Partner Name Failed")
            print(f"Incubator validate partner name failed: {exc}")

    def validate_logo(self):
        try:
            logo = self._wait_for_visible(self.locators.CHANGE_LOGO)
            assert logo.is_visible(), "Partner profile logo/change-logo control is not visible"
            highlight_element(self.page, self.locators.CHANGE_LOGO)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Partner Profile Logo Failed")
            print(f"Incubator validate logo failed: {exc}")
