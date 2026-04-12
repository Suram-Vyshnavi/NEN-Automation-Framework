import os

from locators.Incubator_locators.events_locators import events_locators
from utils.helpers import attach_screenshot, highlight_element


class IncubatorEventsPage:
    def __init__(self, page):
        self.page = page
        self.locators = events_locators()

    def _wait_and_click(self, locator, timeout=15000):
        element = self.page.locator(locator)
        elapsed = 0

        while elapsed <= timeout:
            count = element.count()
            for idx in range(count):
                candidate = element.nth(idx)
                if candidate.is_visible():
                    candidate.click()
                    return

            self.page.wait_for_timeout(200)
            elapsed += 200

        raise TimeoutError(f"No visible element found for locator: {locator}")

    def _wait_and_fill(self, locator, value, timeout=15000):
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        element.fill(str(value))

    def _select_datetime(self, input_locator, date_locator, ok_button_locator):
        self.page.locator(input_locator).click()
        self.page.wait_for_timeout(500)

        date_cell = self.page.locator(date_locator)
        date_cell.wait_for(state="visible", timeout=15000)
        date_cell.click()

        ok_btn = self.page.locator(ok_button_locator)
        if ok_btn.count() > 0 and ok_btn.first.is_visible():
            ok_btn.first.click()

        self.page.wait_for_timeout(500)

    # ------------------------------------------------------------------ #
    #  Scenario methods                                                    #
    # ------------------------------------------------------------------ #

    def click_events_tab(self):
        try:
            self._wait_and_click(self.locators.EVENTS_TAB)
            highlight_element(self.page, self.locators.EVENTS_TAB)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Events Tab Failed")
            print(f"Incubator click events tab failed: {exc}")

    def validate_events_heading(self):
        try:
            heading = self.page.locator(self.locators.EVENTS_HEADING)
            heading.wait_for(state="visible", timeout=15000)
            assert heading.is_visible(), "Events heading not visible"
            highlight_element(self.page, self.locators.EVENTS_HEADING)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Validate Events Heading Failed")
            print(f"Incubator validate events heading failed: {exc}")

    def click_add_event_button(self):
        try:
            self._wait_and_click(self.locators.ADD_EVENT_BUTTON)
            highlight_element(self.page, self.locators.ADD_EVENT_BUTTON)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Add Event Failed")
            print(f"Incubator click add event button failed: {exc}")

    def fill_all_details_and_click_add_speakers(self):
        try:
            # File upload (banner/thumbnail)
            file_path = os.path.join(
                os.path.dirname(__file__), "..", "..", "files", "Wadhwani_Foundation.jpg"
            )
            abs_path = os.path.abspath(file_path)
            file_input = self.page.locator(self.locators.FILE_UPLOAD_IMAGE)
            if file_input.count() > 0:
                file_input.first.set_input_files(abs_path)
                CROP_AND_SAVE_BUTTON = self.page.locator(self.locators.CROP_AND_SAVE_BUTTON)
                CROP_AND_SAVE_BUTTON.wait_for(state="visible", timeout=15000)
                CROP_AND_SAVE_BUTTON.click()
            else:
                self.page.locator(self.locators.FILE_UPLOAD_LABEL).first.click()

            self.page.wait_for_timeout(500)
            # Event name
            self._wait_and_fill(self.locators.EVENT_NAME, "Test Event")

            # Language dropdown
            self._wait_and_click(self.locators.LANGUAGE_SELECTION)
            self.page.wait_for_timeout(300)
            self._wait_and_click(self.locators.LANGUAGE_OPTION)

            # Event type dropdown
            self._wait_and_click(self.locators.EVENT_TYPE_SELECTION)
            self.page.wait_for_timeout(300)
            try:
                for i in range(3):  # Retry mechanism for event type option
                    try:
                        if i == 0:
                            self._wait_and_click(self.locators.EVENT_TYPE_OPTION)
                        elif i == 1:
                            self._wait_and_click("(//span[text()='Meeting'])[1]")  # Ensure correct option is clicked
                        elif i == 2:
                            self._wait_and_click("(//a[text()='Meeting'])[1]")  # Final click to select the option
                        break  # Break loop if click is successful
                    except Exception as exc:
                        print(f"Attempt {i+1}: Event type option not clickable: {exc}")
                        self.page.wait_for_timeout(1000)  # Wait before retrying
                self._wait_and_click(self.locators.EVENT_TYPE_OPTION)
            except Exception as exc:
                attach_screenshot(self.page, "Event Type Option Not Found or Not Clickable")
                print(f"Event type option not found or not clickable: {exc}")
            # Description
            self._wait_and_fill(self.locators.EVENT_DESCRIPTION, "Automation test event description")

            # Start datetime from provided locator set
            self._select_datetime(
                self.locators.START_DATE_TIME,
                self.locators.START_DATE_TIME_INPUT,
                self.locators.START_DATE_TIME_OK_BUTTON,
            )

            # End datetime from provided locator set
            self._select_datetime(
                self.locators.END_DATE_TIME,
                self.locators.END_DATE_TIME_INPUT,
                self.locators.END_DATE_TIME_OK_BUTTON,
            )

            # Registration limit
            self._wait_and_fill(self.locators.REGISTRATION_LIMIT, "100")


            # Click Add Speakers
            self._wait_and_click(self.locators.ADD_SPEAKERS)
            self.page.wait_for_timeout(500)

            # Fill speaker details
            self._wait_and_fill(self.locators.FIRST_NAME_INPUT, "Test")
            self._wait_and_fill(self.locators.LAST_NAME_INPUT, "Speaker")
            self._wait_and_fill(self.locators.EMAIL_INPUT, "testspeaker@yopmail.com")

            # Country
            self._wait_and_fill(self.locators.SELECT_COUNTRY, "India")
            self.page.wait_for_timeout(1000)
            try:
                self._wait_and_click(self.locators.INDIA_OPTION)
            except Exception as exc:
                attach_screenshot(self.page, "India Option Not Found or Not Clickable")
                print(f"India option not found or not clickable: {exc}")

            # Location
            self._wait_and_fill(self.locators.SELECT_LOCATION, "Bangalore")
            self.page.wait_for_timeout(300)
            try:
                self._wait_and_click(self.locators.BANGALORE_OPTION)
            except Exception as exc:
                attach_screenshot(self.page, "Bangalore Option Not Found or Not Clickable")
                print(f"Bangalore option not found or not clickable: {exc}")

            # Title / designation
            self._wait_and_fill(self.locators.TITLE_INPUT, "QA Automation Engineer")

            # Submit speaker
            self._wait_and_click(self.locators.SUBMIT_BUTTON)
            self.page.wait_for_timeout(500)

        except Exception as exc:
            attach_screenshot(self.page, "Incubator Fill Event Details Failed")
            print(f"Incubator fill all details and click add speakers failed: {exc}")

    def click_create_event_next(self):
        try:
            self._wait_and_click(self.locators.CREATE_EVENT_NEXT_BUTTON)
            self.page.wait_for_timeout(1000)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Create Event Next Failed")
            print(f"Incubator click create event & next failed: {exc}")

    def click_add_by_emails_radio(self):
        try:
            self._wait_and_click(self.locators.ADD_BY_EMAILS_RADIO)
            highlight_element(self.page, self.locators.ADD_BY_EMAILS_RADIO)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Click Add By Emails Radio Failed")
            print(f"Incubator click add by emails radio failed: {exc}")

    def click_bulk_upload_invitation_and_submit(self):
        try:
            file_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "files",
                "students-summarized-report-20260401T171553.xlsx",
            )
            abs_path = os.path.abspath(file_path)

            with self.page.expect_file_chooser() as fc_info:
                self._wait_and_click(self.locators.BULK_UPLOAD_INVITATION_BUTTON)
            file_chooser = fc_info.value
            file_chooser.set_files(abs_path)

            self.page.wait_for_timeout(500)
            self._wait_and_click(self.locators.SUBMIT_BUTTON)
            self.page.wait_for_timeout(1000)
            self.page.go_back() 

        except Exception as exc:
            attach_screenshot(self.page, "Incubator Bulk Upload Invitation Failed")
            print(f"Incubator bulk upload invitation failed: {exc}")
            self.page.go_back()


    def delete_created_event(self):
        try:
            try:
                self._wait_and_click(self.locators.DRAFT_TAB)
                self.page.wait_for_timeout(500)
            except Exception as exc:
                attach_screenshot(self.page, "Draft Tab Not Found or Not Clickable")
                print(f"Draft tab not found or not clickable: {exc}")
            # First Delete button opens confirmation; second confirms deletion
            self._wait_and_click(self.locators.DELETE_BUTTON)
            self.page.wait_for_timeout(500)
            self._wait_and_click(self.locators.DELETE_EVENT)
            self.page.wait_for_timeout(1000)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Delete Event Failed")
            print(f"Incubator delete created event failed: {exc}")
