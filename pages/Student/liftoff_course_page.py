from locators.student_locators.liftoff_cours_locators import liftoff_course_locators
from utils.helpers import attach_screenshot, highlight_element


class LiftoffCoursePage:
    def __init__(self, page):
        self.page = page
        self.locators = liftoff_course_locators()

    def validate_liftoff_program(self):
        try:
            ele = self.page.locator(self.locators.LIFTOFF_PROGRAM)
            ele.wait_for(state='visible', timeout=15000)
            assert ele.is_visible(), 'Liftoff program heading is not visible'
            highlight_element(self.page, self.locators.LIFTOFF_PROGRAM)
        except Exception as e:
            attach_screenshot(self.page, 'Validate Liftoff Program Failed')
            print(f'Liftoff program validation failed: {e}')
    def validate_choose_your_gaps(self):
        try:
            ele = self.page.locator(self.locators.CHOOSE_YOUR_GAPS)
            ele.wait_for(state='visible', timeout=15000)
            assert ele.is_visible(), 'Choose your Gaps label is not visible'
            highlight_element(self.page, self.locators.CHOOSE_YOUR_GAPS)
        except Exception as e:
            attach_screenshot(self.page, 'Validate Choose Your Gaps Failed')
            print(f'Choose your gaps validation failed: {e}')
    def click_start_now(self):
        try:
            btn = self.page.locator(self.locators.START_NOW_BUTTON)
            btn.wait_for(state='visible', timeout=15000)
            btn.click(force=True)
        except Exception as e:
            attach_screenshot(self.page, 'Click Start Now Failed')
            print(f'Failed to click start now: {e}')
    def validate_program_application(self):
        try:
            ele = self.page.locator(self.locators.VALIDATE_PROGRAM_APPLICATION)
            ele.wait_for(state='visible', timeout=15000)
            assert ele.is_visible(), 'Program Application section is not visible'
            highlight_element(self.page, self.locators.VALIDATE_PROGRAM_APPLICATION)
        except Exception as e:
            attach_screenshot(self.page, 'Validate Program Application Failed')
            print(f'Program application validation failed: {e}')
    def navigate_to_identify_gaps(self):
        try:
            # If section is already visible, skip clicking
            gap_title = self.page.locator(self.locators.GAP_IDENTIFICATION)
            if gap_title.count() > 0 and gap_title.is_visible():
                return

            btn = self.page.locator(self.locators.IDENTIFY_YOUR_GAPS).first
            btn.wait_for(state='attached', timeout=15000)

            # Try safe click patterns to handle active tab or hidden states
            try:
                if btn.is_visible():
                    btn.click(force=True)
                else:
                    handle = btn.element_handle()
                    if handle:
                        self.page.evaluate('(el) => el.click()', handle)
                    else:
                        btn.click(force=True)
            except Exception:
                handle = btn.element_handle()
                if handle:
                    self.page.evaluate('(el) => el.click()', handle)
                else:
                    btn.click(force=True)

            self.page.wait_for_timeout(1000)

            gap_title.wait_for(state='visible', timeout=15000)
            highlight_element(self.page, self.locators.GAP_IDENTIFICATION)
        except Exception as e:
            attach_screenshot(self.page, 'Navigate to Identify Gaps Failed')
            print(f'Failed to navigate to identify gaps: {e}')
    def add_modify_gaps_and_submit(self):
        try:
            action = self.page.locator(self.locators.ADD_MODIFY_GAPS)
            action.wait_for(state='visible', timeout=15000)
            action.click(force=True)

            checkboxes = self.page.locator(self.locators.STRATEGY_AND_PLANNING_CHECKBOX)
            checkboxes.wait_for(state='visible', timeout=15000)

            count = checkboxes.count()
            assert count > 0, 'No gap checkboxes found'

            to_select = min(2, count)
            for i in range(to_select):
                box = checkboxes.nth(i)
                if not box.is_checked():
                    box.check(force=True)

            submit_btn = self.page.locator(self.locators.SUBMIT_BUTTON)
            submit_btn.wait_for(state='visible', timeout=15000)
            submit_btn.click(force=True)

            self.page.wait_for_timeout(2000)
            assert self.page.locator(self.locators.YOUR_SELECTED_GAPS).is_visible(), 'Your Selected Gaps not visible after submit'
        except Exception as e:
            attach_screenshot(self.page, 'Add Modify Gaps and Submit Failed')
            print(f'Add/modify gaps and submit failed: {e}')
    def revert_gaps_and_submit(self):
        try:
            action = self.page.locator(self.locators.ADD_MODIFY_GAPS)
            action.wait_for(state='visible', timeout=15000)
            action.click(force=True)

            checkboxes = self.page.locator(self.locators.STRATEGY_AND_PLANNING_CHECKBOX)
            checkboxes.wait_for(state='visible', timeout=15000)

            total = min(checkboxes.count(), 20)
            for i in range(total):
                box = checkboxes.nth(i)
                if box.is_checked():
                    box.uncheck(force=True)

            submit_btn = self.page.locator(self.locators.SUBMIT_BUTTON)
            submit_btn.wait_for(state='visible', timeout=15000)
            submit_btn.click(force=True)

            self.page.wait_for_timeout(2000)
        except Exception as e:
            attach_screenshot(self.page, 'Revert Gaps and Submit Failed')
            print(f'Revert gaps and submit failed: {e}')
    def navigate_to_personalised_journey(self):
        try:
            btn = self.page.locator(self.locators.PROCEED_TO_PERSONALISED_JOURNEY)
            btn.wait_for(state='visible', timeout=15000)
            btn.click(force=True)

            ele = self.page.locator(self.locators.PERSONALISED_JOURNEY)
            ele.wait_for(state='visible', timeout=15000)
            highlight_element(self.page, self.locators.PERSONALISED_JOURNEY)
        except Exception as e:
            attach_screenshot(self.page, 'Navigate to Personalised Journey Failed')
            print(f'Failed to navigate to personalised journey: {e}')
    def product_iteration_rewatch_and_close(self):
        try:
            container = self.page.locator(self.locators.PRODUCT_ITERATION_GAP_SECTION)
            container.wait_for(state='visible', timeout=20000)
            container.scroll_into_view_if_needed()
            container.click(force=True)

            watch_button = self.page.locator(self.locators.WATCH_AGAIN)
            watch_button.wait_for(state='visible', timeout=20000)
            watch_button.click(force=True)

            # Allow the video modal to appear
            self.page.wait_for_timeout(3000)

            # close video using first available close icon
            close_button = self.page.locator("span.ant-modal-close-x")
            if close_button.count() > 0:
                try:
                    close_button.first.wait_for(state='visible', timeout=10000)
                    close_button.first.click(force=True)
                    return
                except Exception:
                    pass

            # fallback: use ESC key to close the modal/video overlay
            self.page.keyboard.press('Escape')
            self.page.wait_for_timeout(1500)

            # final fallback: click on overlay background to dismiss
            overlay = self.page.locator("div.ant-modal-wrap")
            if overlay.count() > 0:
                try:
                    overlay.first.click(force=True)
                except Exception:
                    pass

        except Exception as e:
            attach_screenshot(self.page, 'Product Iteration Rewatch and Close Failed')
            print(f'Product iteration rewatch and close failed: {e}')
    def navigate_to_submit_pitch(self):
        try:
            btn = self.page.locator(self.locators.SUBMIT_PITCH)
            btn.wait_for(state='visible', timeout=15000)
            btn.click(force=True)

            title = self.page.locator(self.locators.SUBMIT_YOUR_PITCH_DECK)
            title.wait_for(state='visible', timeout=15000)
        except Exception as e:
            attach_screenshot(self.page, 'Navigate to Submit Pitch Failed')
            print(f'Failed to navigate to submit pitch: {e}')
    def click_upload_pitch_section(self):
        try:
            area = self.page.locator(self.locators.UPLOAD_YOUR_PITCH_DECK)
            area.wait_for(state='visible', timeout=15000)
            highlight_element(self.page, self.locators.UPLOAD_YOUR_PITCH_DECK)
            area.click(force=True)
        except Exception as e:
            attach_screenshot(self.page, 'Click Upload Pitch Section Failed')
            print(f'Failed to click upload pitch section: {e}')
    def upload_pitch_deck_and_save(self, file_path='tests/resources/test_pitch_deck.pdf', file_name='Test Pitch Deck'):
        try:
            upload_button = self.page.locator(self.locators.UPLOAD_BUTTON)
            upload_button.wait_for(state='visible', timeout=15000)
            #upload_button.click(force=True)

            # If input[type=file] exists in DOM
            file_input = self.page.locator("input[type='file']")
            if file_input.count() > 0:
                file_input.set_input_files(file_path)
            else:
                # Fallback for custom upload components, maybe after click actual upload occurs
                self.page.wait_for_timeout(3000)

            file_name_input = self.page.locator(self.locators.FILE_NAME_INPUT)
            if file_name_input.count() > 0:
                file_name_input.fill(file_name)
            else:
                # Fallback when file name is a label linked to a hidden input
                file_name_label = self.page.locator(self.locators.FILE_NAME_LABEL)
                if file_name_label.count() > 0:
                    input_after_label = file_name_label.first.locator("xpath=following::input[1]")
                    if input_after_label.count() > 0:
                        input_after_label.fill(file_name)

            save_btn = self.page.locator(self.locators.SAVE_BUTTON)
            save_btn.wait_for(state='visible', timeout=15000)
            save_btn.click(force=True)

        except Exception as e:
            attach_screenshot(self.page, 'Upload Pitch Deck and Save Failed')
            print(f'Failed to upload pitch deck and save: {e}')
    def delete_pitch_deck(self):
        try:
            self.page.locator(self.locators.PITCH_DECK_RECORD).wait_for(state='visible', timeout=15000)
            self.page.locator(self.locators.PITCH_DECK_RECORD).click(force=True)

            opts = self.page.locator(self.locators.MORE_OPTIONS)
            opts.wait_for(state='visible', timeout=15000)
            opts.click(force=True)

            delete_item = self.page.locator(self.locators.DELETE_PITCH_DECK)
            delete_item.wait_for(state='visible', timeout=15000)
            delete_item.click(force=True)

            confirm = self.page.locator(self.locators.DELETE_PITCH_CONFIRM)
            confirm.wait_for(state='visible', timeout=15000)
            confirm.click(force=True)

        except Exception as e:
            attach_screenshot(self.page, 'Delete Pitch Deck Failed')
            print(f'Failed to delete pitch deck: {e}')
