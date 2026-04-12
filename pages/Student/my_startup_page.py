from locators.student_locators.my_startup_locators import my_startup_locators
from utils.helpers import attach_screenshot, highlight_element


class MyStartupPage:
    def __init__(self, page):
        self.page = page
        self.locators = my_startup_locators()

    def click_profile_icon_and_navigate_to_my_startup_page(self):
        try:
            locator = self.page.locator(self.locators.PROFILE_ICON)
            locator.wait_for(state='visible', timeout=10000)
            locator.click()
            self.page.locator(self.locators.MY_STARTUP_HEADER).wait_for(state='visible', timeout=10000)
        except Exception as e:
            attach_screenshot(self.page, 'Navigate to My Startup Page Failed')
            print(f'Failed to navigate to my startup page: {e}')
    def validate_my_startup_page_header_ignite_wadhwani_sections(self):
        try:
            locator_header = self.page.locator(self.locators.MY_STARTUP_HEADER)
            locator_header.wait_for(state='visible', timeout=10000)
            assert locator_header.is_visible()
            locator_header.click()
            locator_ignite = self.page.locator(self.locators.IGNITE_HEADER)
            locator_ignite.wait_for(state='visible', timeout=10000)
            assert locator_ignite.is_visible()
            locator_wadhwani = self.page.locator(self.locators.WADHWANI)
            locator_wadhwani.wait_for(state='visible', timeout=10000)
            assert locator_wadhwani.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'My Startup Header Validation Failed')
            print(f'My startup header validation failed: {e}')
    def click_view_button_of_ignite_section(self):
        try:
            ignite_view_btn = self.page.locator(self.locators.IGNITE_VIEW_BUTTON)
            ignite_view_btn.wait_for(state='visible', timeout=10000)
            ignite_view_btn.click(force=True)
        except Exception as e:
            attach_screenshot(self.page, 'Click View Button of Ignite Section Failed')
            print(f'Failed to click view button of ignite section: {e}')
    def validate_details_in_my_startup_page(self):
        try:
            venturecode = self.page.locator(self.locators.VENTURE_CODE)
            venturecode.wait_for(state='visible', timeout=10000)
            assert venturecode.is_visible()
            cohortname = self.page.locator(self.locators.COHORT_NAME)
            cohortname.wait_for(state='visible', timeout=10000)
            assert cohortname.is_visible()
            programname = self.page.locator(self.locators.PROGRAM_NAME)
            programname.wait_for(state='visible', timeout=10000)
            assert programname.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'My Startup Details Validation Failed')
            print(f'My startup details validation failed: {e}')
    def click_basic_information_section_and_save(self):
        try:
            basicinformatoon = self.page.locator(self.locators.BASIC_INFORMATION)
            basicinformatoon.wait_for(state='visible', timeout=10000)
            basicinformatoon.click()
            savebutton = self.page.locator(self.locators.SAVE_BUTTON)
            savebutton.wait_for(state='visible', timeout=10000)
            savebutton.click()
        except Exception as e:
            attach_screenshot(self.page, 'Click Basic Information and Save Failed')
            print(f'Failed to click basic information and save: {e}')
    def click_view_venture_journey_and_validate_details_and_navigate_back(self):
        try:
            view_venture_journey_btn = self.page.locator(self.locators.VALIDATE_VIEW_VENTURE_JOURNEY)
            view_venture_journey_btn.wait_for(state='visible', timeout=10000)
            view_venture_journey_btn.click()
            self.page.go_back()
            venturecosde = self.page.locator(self.locators.VENTURE_CODE)
            venturecosde.wait_for(state='visible', timeout=10000)
            assert venturecosde.is_visible()
            cohortname = self.page.locator(self.locators.COHORT_NAME)
            cohortname.wait_for(state='visible', timeout=10000)
            assert cohortname.is_visible()
            programname = self.page.locator(self.locators.PROGRAM_NAME)
            programname.wait_for(state='visible', timeout=10000)
            assert programname.is_visible()
            self.page.keyboard.press('Escape')
        except Exception as e:
            attach_screenshot(self.page, 'View Venture Journey and Navigate Back Failed')
            print(f'Failed to view venture journey and navigate back: {e}')
    def click_youtube_video_url_section_and_add_url_and_save(self):
        try:
            aboutwadhwani = self.page.locator(self.locators.ABOUT_WADHWANI)
            aboutwadhwani.wait_for(state='visible', timeout=10000)
            aboutwadhwani.click()
            youtubelink = self.page.locator(self.locators.YOUTUBE_VIDEO_URL)
            youtubelink.wait_for(state='visible', timeout=10000)
            youtubelink.fill('https://www.youtube.com/watch?v=BysUw7AOUP8')
            save_button = self.page.locator(self.locators.SAVE_BUTTON)
            save_button.wait_for(state='visible', timeout=10000)
            save_button.click()
            video = self.page.locator(self.locators.YOUTUBE_VIDEO)
            video.wait_for(state='visible', timeout=10000)
            assert video.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'Add YouTube URL and Save Failed')
            print(f'Failed to add youtube url and save: {e}')
    def click_venture_team_section_and_add_member_and_save(self):
        try:
            ventureteam = self.page.locator(self.locators.VENTURE_TEAM)
            ventureteam.wait_for(state='visible', timeout=10000)
            assert ventureteam.is_visible()
            addmenber = self.page.locator(self.locators.ADD_MEMBER)
            addmenber.wait_for(state='visible', timeout=10000)
            addmenber.click()
            searchmember = self.page.locator(self.locators.SEARCH_MEMBER)
            searchmember.wait_for(state='visible', timeout=10000)
            searchmember.fill('Test')
            selectmember = self.page.locator(self.locators.SELECT_MEMBER)
            selectmember.wait_for(state='visible', timeout=10000)
            selectmember.click()
            addsearchedmember = self.page.locator(self.locators.ADD_MEMBERS_BUTTON)
            addsearchedmember.wait_for(state='visible', timeout=10000)
            addsearchedmember.click()
        except Exception as e:
            attach_screenshot(self.page, 'Add Member to Venture Team Failed')
            print(f'Failed to add member to venture team: {e}')
    def remove_added_member_from_venture_team_and_save(self):
        try:
            addmenber = self.page.locator(self.locators.ADD_MEMBER)
            addmenber.wait_for(state='visible', timeout=10000)
            addmenber.click()
            memberremoveicon = self.page.locator(self.locators.MEMBER_REMOVE_ICON)
            memberremoveicon.wait_for(state='visible', timeout=10000)
            memberremoveicon.click()
            closeaddmembersection = self.page.locator(self.locators.CLOSE_ADD_MEMBERS_SECTION)
            closeaddmembersection.wait_for(state='visible', timeout=10000)
            closeaddmembersection.click()
        except Exception as e:
            attach_screenshot(self.page, 'Remove Member from Venture Team Failed')
            print(f'Failed to remove member from venture team: {e}')
    def click_venture_support_section_and_validate_faculty_details(self):
        try:
            venturesupport = self.page.locator(self.locators.VENTURE_SUPPORT)
            venturesupport.wait_for(state='visible', timeout=10000)
            assert venturesupport.is_visible()
            faculty = self.page.locator(self.locators.VENTURE_SUPPPORT_FACULTY)
            faculty.wait_for(state='visible', timeout=10000)
            assert faculty.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'Venture Support Faculty Details Validation Failed')
            print(f'Venture support faculty details validation failed: {e}')
    def validate_milestone_timeline_and_1st_milestone_details(self):
        try:
            locator_timeline = self.page.locator(self.locators.MILESTONE_TIMELINE)
            locator_timeline.wait_for(state='visible', timeout=10000)
            assert locator_timeline.is_visible()
            locator_card = self.page.locator(self.locators.TEST_MILESTONE_CARD)
            locator_card.wait_for(state='visible', timeout=10000)
            assert locator_card.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'Milestone Timeline Validation Failed')
            print(f'Milestone timeline validation failed: {e}')
    def validate_upcoming_activities_section(self):
        try:
            locator = self.page.locator(self.locators.UPCOMING_ACTIVITIES)
            locator.wait_for(state='visible', timeout=10000)
            assert locator.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'Upcoming Activities Section Validation Failed')
            print(f'Upcoming activities section validation failed: {e}')
    def validate_meeting_and_webinar_cards(self):
        try:
            locator_meeting = self.page.locator(self.locators.MEETING_CARD)
            locator_meeting.wait_for(state='visible', timeout=10000)
            assert locator_meeting.is_visible()
            locator_webinar = self.page.locator(self.locators.WEBINAR_CARD)
            locator_webinar.wait_for(state='visible', timeout=10000)
            assert locator_webinar.is_visible()
        except Exception as e:
            attach_screenshot(self.page, 'Meeting and Webinar Cards Validation Failed')
            print(f'Meeting and webinar cards validation failed: {e}')
    def validate_resources_section(self):
        try:
            locator = self.page.locator(self.locators.RESOURCES)
            locator.wait_for(state='visible', timeout=10000)
            assert locator.is_visible()
            self.page.go_back()
        except Exception as e:
            attach_screenshot(self.page, 'Resources Section Validation Failed')
            print(f'Resources section validation failed: {e}')
    def click_view_button_of_liftoff_spark_section(self):
        try:
            liftoff_spark = self.page.locator(self.locators.LIFTOFF_SPARK)
            liftoff_spark.wait_for(state='visible', timeout=10000)
            assert liftoff_spark.is_visible()
            viewbutton = self.page.locator(self.locators.LIFTOFF_SPARK_VIEW)
            viewbutton.wait_for(state='visible', timeout=10000)
            viewbutton.click()
        except Exception as e:
            attach_screenshot(self.page, 'Click View Button of Liftoff Spark Section Failed')
            print(f'Failed to click view button of liftoff spark section: {e}')
