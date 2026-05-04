from locators.common.header_locators import HeaderLocators
from locators.common.login_locators import LoginLocators
from utils.helpers import attach_screenshot, highlight_element


class NavigationPage:
    def __init__(self, page):
        self.page = page
        self.header_locators = HeaderLocators()
        self.login_locators = LoginLocators()

    def handle_all_popups(self):
        popup_steps = [
            (
                self.login_locators.NO_THANKS_POPUP,
                None,
                "Popup 1 - No Thanks Closed",
                "Popup 1",
            ),
            (
                self.login_locators.START_YOUR_JOURNEY_POPUP,
                self.login_locators.NEXT_BUTTON,
                "Popup 2 - Clicked Next",
                "Popup 2",
            ),
            (
                self.login_locators.CREATE_PERSONALISED_JOURNEY_POPUP,
                self.login_locators.NEXT_BUTTON,
                "Popup 3 - Clicked Next",
                "Popup 3",
            ),
            (
                self.login_locators.START_PROGRAM_JOURNEY_BUTTON,
                self.login_locators.START_PROGRAM_JOURNEY_BUTTON,
                "Popup 4 - Clicked Start Program Journey",
                "Popup 4",
            ),
        ]

        for trigger_locator, action_locator, screenshot_name, popup_name in popup_steps:
            try:
                popup = self.page.locator(trigger_locator)
                popup.wait_for(state="visible", timeout=5000)
                if popup.is_visible():
                    highlight_element(self.page, trigger_locator)
                    target_locator = action_locator or trigger_locator
                    self.page.click(target_locator)
            except Exception as exc:
                attach_screenshot(self.page, f"{popup_name} Handling Failed")
                print(f"{popup_name} not found or already handled: {exc}")

    def close_modal_if_open(self):
        try:
            close_btn = self.page.locator("//span[@class='ant-modal-close-x']")
            if close_btn.count() > 0 and close_btn.first.is_visible():
                close_btn.first.click()
                self.page.wait_for_timeout(500)
        except Exception:
            pass

    def navigate_to_home_page(self):
        try:
            self.close_modal_if_open()
            home_header = self.page.locator(self.header_locators.HOME_HEADER)
            home_header.wait_for(state="visible", timeout=10000)
            self.page.click(self.header_locators.HOME_HEADER)
        except Exception as e:
            attach_screenshot(self.page, "Navigate to Home Page Failed")
            print(f"Failed to navigate to home page: {e}")
