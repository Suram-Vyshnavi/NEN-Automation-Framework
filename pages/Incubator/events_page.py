import os

from locators.Incubator_locators.events_locators import events_locators
from utils.helpers import attach_screenshot, highlight_element


class IncubatorEventsPage:
    def __init__(self, page):
        self.page = page
        self.locators = events_locators()

    def _wait_and_click(self, locator, timeout=15000, force=False):
        element = self.page.locator(locator)
        elapsed = 0

        while elapsed <= timeout:
            count = element.count()
            for idx in range(count):
                candidate = element.nth(idx)
                if force or candidate.is_visible():
                    candidate.click(force=True)
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
            self._wait_and_click(self.locators.LANGUAGE_SELECTION, force=True)
            self.page.wait_for_timeout(800)
            self._wait_and_click(self.locators.LANGUAGE_OPTION)

            # Event type dropdown
            self._wait_and_click(self.locators.EVENT_TYPE_SELECTION, force=True)
            self.page.wait_for_timeout(800)
            try:
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

            self._wait_and_click(self.locators.BULK_UPLOAD_INVITATION_BUTTON)
            self.page.wait_for_timeout(500)

            file_input = self.page.locator(self.locators.CHOOSE_FILE_INPUT)
            if file_input.count() > 0:
                file_input.first.set_input_files(abs_path)
            else:
                with self.page.expect_file_chooser() as fc_info:
                    self._wait_and_click(self.locators.BULK_UPLOAD_INVITATION_BUTTON)
                fc_info.value.set_files(abs_path)

            self.page.locator(self.locators.UPLOAD_BUTTON).click()
            self.page.wait_for_timeout(1000)
            self.page.locator(self.locators.DOWNLOAD_BUTTON)
            self.page.wait_for_timeout(500)
            self.page.locator(self.locators.CLOSE_MODAL_BUTTON).click()

            submit_buttons = self.page.locator(self.locators.SUBMIT_BUTTON)
            clicked_submit = False
            for idx in range(submit_buttons.count()):
                candidate = submit_buttons.nth(idx)
                if candidate.is_visible() and candidate.is_enabled():
                    candidate.click(force=True)
                    clicked_submit = True
                    break

            if not clicked_submit:
                print("Incubator bulk upload: visible submit button not found, continuing")

            self.page.wait_for_timeout(1000)

        except Exception as exc:
            attach_screenshot(self.page, "Incubator Bulk Upload Invitation Failed")
            print(f"Incubator bulk upload invitation failed: {exc}")


    def delete_created_event(self):
        try:
        #     try:
        #         self._wait_and_click(self.locators.DRAFT_TAB)
        #         self.page.wait_for_timeout(500)
        #     except Exception as exc:
        #         attach_screenshot(self.page, "Draft Tab Not Found or Not Clickable")
        #         print(f"Draft tab not found or not clickable: {exc}")
            # First Delete button opens confirmation; second confirms deletion
            self._wait_and_click(self.locators.DELETE_BUTTON)
            self.page.wait_for_timeout(500)
            self._wait_and_click(self.locators.DELETE_EVENT)
            self.page.wait_for_timeout(1000)
        except Exception as exc:
            attach_screenshot(self.page, "Incubator Delete Event Failed")
            print(f"Incubator delete created event failed: {exc}")
