from locators.student_locators.ignite_courses_locators import ignite_courses_locators
from utils.helpers import attach_screenshot, highlight_element


class IgniteCoursePage:
    def __init__(self, page):
        self.page = page
        self.locators = ignite_courses_locators()

    def validate_ignite_program_in_home_page(self):
        locator = self.page.locator(self.locators.GO_TO_JOURNEY)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated ignite program in home page')

    def click_go_to_course_in_home_page(self):
        locator = self.page.locator(self.locators.GO_TO_JOURNEY)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked go to course in home page')

    def validate_overview_section(self):
        locator = self.page.locator(self.locators.OVERVIEW)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated overview section')

    def click_course_content_section(self):
        locator = self.page.locator(self.locators.COURSE_CONTENT)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked course content section')

    def navigate_to_venture_journey_section(self):
        locator = self.page.locator(self.locators.VENTURE_JOURNEY)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Navigated to venture journey section')

    def click_view_output(self):
        locator = self.page.locator(self.locators.VIEW_OUTPUT)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked view output')
        self.page.keyboard.press("Escape")

    def click_redo_button(self):
        locator = self.page.locator(self.locators.REDO_BUTTON)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked redo button')
        backventurejpurney = self.page.locator(self.locators.BACK_VENTURE_JOURNEY)
        backventurejpurney.wait_for(state='visible', timeout=10000)
        backventurejpurney.click()

    def click_preview_button(self):
        locator = self.page.locator(self.locators.PREVIEW_BUTTON)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked preview button')
        submissions = self.page.locator(self.locators.SUBMISSIONS)
        submissions.wait_for(state='visible', timeout=10000)
        submissions.click()
        assert submissions.is_visible(), 'Submissions section is not visible after clicking preview button'
        attach_screenshot(self.page, 'Validated submissions section after clicking preview button')
        instructions = self.page.locator(self.locators.INSTRUCTIONS)
        instructions.wait_for(state='visible', timeout=10000)
        instructions.click()
        assert instructions.is_visible(), 'Instructions section is not visible after clicking preview button'
        attach_screenshot(self.page, 'Validated instructions section after clicking preview button')
        self.page.go_back()

    def navigate_to_performance(self):
        locator = self.page.locator(self.locators.PERFORMANCE)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Navigated to performance')

    def validate_your_performance_section_cards(self):
        locator = self.page.locator(self.locators.YOUR_PERFORMANCE)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated your performance section cards')
        mandatory_content_card = self.page.locator(self.locators.MANDATORY_CONTENT_CARD)
        mandatory_content_card.wait_for(state='visible', timeout=10000)
        assert mandatory_content_card.is_visible()
        attach_screenshot(self.page, 'Validated mandatory content card')
        quizzes_card = self.page.locator(self.locators.QUIZZES_CARD)
        quizzes_card.wait_for(state='visible', timeout=10000)
        assert quizzes_card.is_visible()
        attach_screenshot(self.page, 'Validated quizzes card')
        milestone_card = self.page.locator(self.locators.MILESTONE_CARD)
        milestone_card.wait_for(state='visible', timeout=10000)
        assert milestone_card.is_visible()
        attach_screenshot(self.page, 'Validated milestone card')

    def validate_your_certificates(self):
        locator = self.page.locator(self.locators.YOUR_CERTIFICATE)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated your certificates')

    def click_share_and_validate_download_button(self):
        locator_share = self.page.locator(self.locators.SHARE_BUTTON)
        locator_share.wait_for(state='visible', timeout=10000)
        locator_share.click()
        copylink=self.page.locator(self.locators.COPY_LINK)
        copylink.wait_for(state='visible', timeout=10000)
        assert copylink.is_visible()
        copylink.click()
        locator_download = self.page.locator(self.locators.DOWNLOAD_BUTTON)
        locator_download.wait_for(state='visible', timeout=10000)
        assert locator_download.is_visible()
        attach_screenshot(self.page, 'Clicked share and validated download button')

    def click_cohort_section(self):
        locator = self.page.locator(self.locators.COHORT)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked cohort section')

    def validate_cohort_section(self):
        locator = self.page.locator(self.locators.COHORT_GENERAL_INFO)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated cohort general infosection')
        locator_ventures = self.page.locator(self.locators.COHORT_VENTURES)
        locator_ventures.wait_for(state='visible', timeout=10000)
        locator_ventures.click()
        assert locator_ventures.is_visible()
        attach_screenshot(self.page, 'Validated cohort venturessection')
        locator_members = self.page.locator(self.locators.COHORT_MEMBERS)
        locator_members.wait_for(state='visible', timeout=10000)
        locator_members.click()
        assert locator_members.is_visible()
        attach_screenshot(self.page, 'Validated cohort memberssection')
        self.page.go_back()
   

    def click_view_venture_journey(self):
        locator = self.page.locator(self.locators.MY_VENTURE)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        attach_screenshot(self.page, 'Clicked view venture journey')

    def click_basic_information_section_and_save(self):
        locator_basic = self.page.locator(self.locators.BASIC_INFORMATION)
        locator_basic.wait_for(state='visible', timeout=10000)
        locator_basic.click()
        locator_save = self.page.locator(self.locators.SAVE_BUTTON)
        locator_save.wait_for(state='visible', timeout=10000)
        locator_save.click()
        attach_screenshot(self.page, 'Clicked basic information and saved')

    def click_view_venture_journey_and_validate_details(self):
        locator_view = self.page.locator(self.locators.VALIDATE_VIEW_VENTURE_JOURNEY)
        locator_view.wait_for(state='visible', timeout=10000)
        locator_view.click()
        locator_code = self.page.locator(self.locators.VENTURE_CODE)
        locator_code.wait_for(state='visible', timeout=10000)
        assert locator_code.is_visible()
        locator_cohort = self.page.locator(self.locators.COHORT_NAME)
        locator_cohort.wait_for(state='visible', timeout=10000)
        assert locator_cohort.is_visible()
        locator_program = self.page.locator(self.locators.PROGRAM_NAME)
        locator_program.wait_for(state='visible', timeout=10000)
        assert locator_program.is_visible()
        attach_screenshot(self.page, 'Viewed venture journey and validated details')

    # def click_youtube_video_url_section_and_add_url_and_save(self):
    #     locator_url = self.page.locator(self.locators.YOUTUBE_VIDEO_URL)
    #     locator_url.wait_for(state='visible', timeout=10000)
    #     locator_url.fill('https://www.youtube.com/watch?v=example')
    #     locator_save = self.page.locator(self.locators.SAVE_BUTTON)
    #     locator_save.wait_for(state='visible', timeout=10000)
    #     locator_save.click()
    #     attach_screenshot(self.page, 'Added youtube url and saved')

    # def click_venture_team_section_and_add_member_and_save(self):
    #     locator_team = self.page.locator(self.locators.VENTURE_TEAM)
    #     locator_team.wait_for(state='visible', timeout=10000)
    #     locator_team.click()
    #     locator_add = self.page.locator(self.locators.ADD_MEMBER)
    #     locator_add.wait_for(state='visible', timeout=10000)
    #     locator_add.click()
    #     locator_search = self.page.locator(self.locators.SEARCH_MEMBER)
    #     locator_search.wait_for(state='visible', timeout=10000)
    #     locator_search.fill('Test Member')
    #     locator_select = self.page.locator(self.locators.SELECT_MEMBER)
    #     locator_select.wait_for(state='visible', timeout=10000)
    #     locator_select.click()
    #     locator_add_members = self.page.locator(self.locators.ADD_MEMBERS_BUTTON)
    #     locator_add_members.wait_for(state='visible', timeout=10000)
    #     locator_add_members.click()
    #     attach_screenshot(self.page, 'Added member to venture team')

    # def remove_added_member_from_venture_team_and_save(self):
    #     locator_remove = self.page.locator(self.locators.MEMBER_REMOVE_ICON)
    #     locator_remove.wait_for(state='visible', timeout=10000)
    #     locator_remove.click()
    #     locator_save = self.page.locator(self.locators.SAVE_BUTTON)
    #     locator_save.wait_for(state='visible', timeout=10000)
    #     locator_save.click()
    #     attach_screenshot(self.page, 'Removed member from venture team')

    # def click_venture_support_section_and_validate_faculty_details(self):
    #     locator_support = self.page.locator(self.locators.VENTURE_SUPPORT)
    #     locator_support.wait_for(state='visible', timeout=10000)
    #     locator_support.click()
    #     locator_faculty = self.page.locator(self.locators.VENTURE_SUPPPORT_FACULTY)
    #     locator_faculty.wait_for(state='visible', timeout=10000)
    #     assert locator_faculty.is_visible()
    #     attach_screenshot(self.page, 'Validated venture support faculty details')

    # def validate_milestone_timeline_and_1st_milestone_details(self):
    #     locator_timeline = self.page.locator(self.locators.MILESTONE_TIMELINE)
    #     locator_timeline.wait_for(state='visible', timeout=10000)
    #     assert locator_timeline.is_visible()
    #     locator_card = self.page.locator(self.locators.TEST_MILESTONE_CARD)
    #     locator_card.wait_for(state='visible', timeout=10000)
    #     assert locator_card.is_visible()
    #     attach_screenshot(self.page, 'Validated milestone timeline and 1st milestone details')

    # def validate_upcoming_activities_section(self):
    #     locator = self.page.locator(self.locators.UPCOMING_ACTIVITIES)
    #     locator.wait_for(state='visible', timeout=10000)
    #     assert locator.is_visible()
    #     attach_screenshot(self.page, 'Validated upcoming activities section')

    # def validate_meeting_and_webinar_cards(self):
    #     locator_meeting = self.page.locator(self.locators.MEETING_CARD)
    #     locator_meeting.wait_for(state='visible', timeout=10000)
    #     assert locator_meeting.is_visible()
    #     locator_webinar = self.page.locator(self.locators.WEBINAR_CARD)
    #     locator_webinar.wait_for(state='visible', timeout=10000)
    #     assert locator_webinar.is_visible()
    #     attach_screenshot(self.page, 'Validated meeting and webinar cards')

    # def validate_resources_section(self):
    #     locator = self.page.locator(self.locators.RESOURCES)
    #     locator.wait_for(state='visible', timeout=10000)
    #     assert locator.is_visible()
    #     attach_screenshot(self.page, 'Validated resources section')

    # def upload_file_in_resources_section_and_validate(self):
    #     locator_browse = self.page.locator(self.locators.BROWSE_UPLOAD)
    #     locator_browse.wait_for(state='visible', timeout=10000)
    #     locator_browse.click()
    #     file_path = 'files/sample.pdf'
    #     locator_input = self.page.locator(self.locators.FILE_NAME_INPUT)
    #     locator_input.wait_for(state='visible', timeout=10000)
    #     locator_input.set_input_files(file_path)
    #     locator_save = self.page.locator(self.locators.SAVE_BUTTON)
    #     locator_save.wait_for(state='visible', timeout=10000)
    #     locator_save.click()
    #     attach_screenshot(self.page, 'Uploaded file in resources section and validated')

    # def delete_uploaded_file_in_resources_section_and_validate(self):
    #     locator_more = self.page.locator(self.locators.MORE)
    #     locator_more.wait_for(state='visible', timeout=10000)
    #     locator_more.click()
    #     locator_delete = self.page.locator(self.locators.DELETE_RESOURCE)
    #     locator_delete.wait_for(state='visible', timeout=10000)
    #     locator_delete.click()
    #     attach_screenshot(self.page, 'Deleted uploaded file in resources section and validated')