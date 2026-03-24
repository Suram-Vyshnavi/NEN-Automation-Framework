from locators.student_locators.my_startup_locators import my_startup_locators
from utils.helpers import attach_screenshot, highlight_element


class MyStartupPage:
    def __init__(self, page):
        self.page = page
        self.locators = my_startup_locators()

    def click_profile_icon_and_navigate_to_my_startup_page(self):
        locator = self.page.locator(self.locators.PROFILE_ICON)
        locator.wait_for(state='visible', timeout=10000)
        locator.click()
        self.page.locator(self.locators.MY_STARTUP_HEADER).wait_for(state='visible', timeout=10000)
        attach_screenshot(self.page, 'Navigated to My Startup page')

    def validate_my_startup_page_header_ignite_wadhwani_sections(self):
        locator_header = self.page.locator(self.locators.MY_STARTUP_HEADER)
        locator_header.wait_for(state='visible', timeout=10000)
        assert locator_header.is_visible()
        locator_header.click()  # Click to ensure the page is active
        locator_ignite = self.page.locator(self.locators.IGNITE_HEADER)
        locator_ignite.wait_for(state='visible', timeout=10000)
        assert locator_ignite.is_visible()
        locator_wadhwani = self.page.locator(self.locators.WADHWANI)
        locator_wadhwani.wait_for(state='visible', timeout=10000)
        assert locator_wadhwani.is_visible()
        attach_screenshot(self.page, 'Validated header, ignite and wadhwani sections')

    def click_view_button_of_ignite_section(self):
        ignite_view_btn = self.page.locator(self.locators.IGNITE_VIEW_BUTTON)
        ignite_view_btn.wait_for(state='visible', timeout=10000)
        ignite_view_btn.click(force=True)
        attach_screenshot(self.page, 'Clicked view button of ignite section')

    def validate_details_in_my_startup_page(self):
        venturecode=self.page.locator(self.locators.VENTURE_CODE)
        venturecode.wait_for(state='visible', timeout=10000)
        assert venturecode.is_visible()
        cohortname=self.page.locator(self.locators.COHORT_NAME)
        cohortname.wait_for(state='visible', timeout=10000)
        assert cohortname.is_visible()
        programname=self.page.locator(self.locators.PROGRAM_NAME)
        programname.wait_for(state='visible', timeout=10000)
        assert programname.is_visible()

        attach_screenshot(self.page, 'Validated details in my startup page')

    def click_basic_information_section_and_save(self):
        basicinformatoon=self.page.locator(self.locators.BASIC_INFORMATION)
        basicinformatoon.wait_for(state='visible', timeout=10000)
        basicinformatoon.click()
        savebutton=self.page.locator(self.locators.SAVE_BUTTON)
        savebutton.wait_for(state='visible', timeout=10000)
        savebutton.click()
        attach_screenshot(self.page, 'Clicked basic information and saved')

    def click_view_venture_journey_and_validate_details_and_navigate_back(self):
        view_venture_journey_btn = self.page.locator(self.locators.VALIDATE_VIEW_VENTURE_JOURNEY)
        view_venture_journey_btn.wait_for(state='visible', timeout=10000)
        view_venture_journey_btn.click()
        self.page.go_back()
        venturecosde=self.page.locator(self.locators.VENTURE_CODE)
        venturecosde.wait_for(state='visible', timeout=10000)
        assert venturecosde.is_visible()
        cohortname=self.page.locator(self.locators.COHORT_NAME)
        cohortname.wait_for(state='visible', timeout=10000)
        assert cohortname.is_visible()
        programname=self.page.locator(self.locators.PROGRAM_NAME)
        programname.wait_for(state='visible', timeout=10000)
        assert programname.is_visible()
        self.page.keyboard.press('Escape')
        attach_screenshot(self.page, 'Viewed venture journey and navigated back')

    def click_youtube_video_url_section_and_add_url_and_save(self):
        aboutwadhwani=self.page.locator(self.locators.ABOUT_WADHWANI)
        aboutwadhwani.wait_for(state='visible', timeout=10000)
        aboutwadhwani.click()
        youtubelink=self.page.locator(self.locators.YOUTUBE_VIDEO_URL)
        youtubelink.wait_for(state='visible', timeout=10000)
        youtubelink.fill('https://www.youtube.com/watch?v=BysUw7AOUP8')
        save_button = self.page.locator(self.locators.SAVE_BUTTON)
        save_button.wait_for(state='visible', timeout=10000)
        save_button.click()
        attach_screenshot(self.page, 'Added youtube url and saved')
        video=self.page.locator(self.locators.YOUTUBE_VIDEO)
        video.wait_for(state='visible', timeout=10000)
        assert video.is_visible()
        attach_screenshot(self.page, 'Validated added youtube video')

    def click_venture_team_section_and_add_member_and_save(self):
        ventureteam=self.page.locator(self.locators.VENTURE_TEAM)
        ventureteam.wait_for(state='visible', timeout=10000)
        assert ventureteam.is_visible()
        addmenber=self.page.locator(self.locators.ADD_MEMBER)
        addmenber.wait_for(state='visible', timeout=10000)
        addmenber.click()
        searchmember=self.page.locator(self.locators.SEARCH_MEMBER)
        searchmember.wait_for(state='visible', timeout=10000)
        searchmember.fill('Test')
        selectmember=self.page.locator(self.locators.SELECT_MEMBER)
        selectmember.wait_for(state='visible', timeout=10000)
        selectmember.click()
        addsearchedmember=self.page.locator(self.locators.ADD_MEMBERS_BUTTON)
        addsearchedmember.wait_for(state='visible', timeout=10000)
        addsearchedmember.click()
        attach_screenshot(self.page, 'Added member to venture team')

    def remove_added_member_from_venture_team_and_save(self):

        addmenber=self.page.locator(self.locators.ADD_MEMBER)
        addmenber.wait_for(state='visible', timeout=10000)
        addmenber.click()
        memberremoveicon=self.page.locator(self.locators.MEMBER_REMOVE_ICON)
        memberremoveicon.wait_for(state='visible', timeout=10000)
        memberremoveicon.click()
        closeaddmembersection=self.page.locator(self.locators.CLOSE_ADD_MEMBERS_SECTION)
        closeaddmembersection.wait_for(state='visible', timeout=10000)
        closeaddmembersection.click()
        attach_screenshot(self.page, 'Removed member from venture team')

    def click_venture_support_section_and_validate_faculty_details(self):
        venturesupport=self.page.locator(self.locators.VENTURE_SUPPORT)
        venturesupport.wait_for(state='visible', timeout=10000)
        assert venturesupport.is_visible()
        faculty=self.page.locator(self.locators.VENTURE_SUPPPORT_FACULTY)
        faculty.wait_for(state='visible', timeout=10000)
        assert faculty.is_visible()
        attach_screenshot(self.page, 'Validated venture support faculty details')


    def validate_milestone_timeline_and_1st_milestone_details(self):
        locator_timeline = self.page.locator(self.locators.MILESTONE_TIMELINE)
        locator_timeline.wait_for(state='visible', timeout=10000)
        assert locator_timeline.is_visible()
        locator_card = self.page.locator(self.locators.TEST_MILESTONE_CARD)
        locator_card.wait_for(state='visible', timeout=10000)
        assert locator_card.is_visible()
        attach_screenshot(self.page, 'Validated milestone timeline and 1st milestone details')


    def validate_upcoming_activities_section(self):
        locator = self.page.locator(self.locators.UPCOMING_ACTIVITIES)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated upcoming activities section')


    def validate_meeting_and_webinar_cards(self):
        locator_meeting = self.page.locator(self.locators.MEETING_CARD)
        locator_meeting.wait_for(state='visible', timeout=10000)
        assert locator_meeting.is_visible()
        locator_webinar = self.page.locator(self.locators.WEBINAR_CARD)
        locator_webinar.wait_for(state='visible', timeout=10000)
        assert locator_webinar.is_visible()
        attach_screenshot(self.page, 'Validated meeting and webinar cards')


    def validate_resources_section(self):
        locator = self.page.locator(self.locators.RESOURCES)
        locator.wait_for(state='visible', timeout=10000)
        assert locator.is_visible()
        attach_screenshot(self.page, 'Validated resources section')
        self.page.go_back()  # Navigate back to ensure the page is active for subsequent steps


    def click_view_button_of_liftoff_spark_section(self):
        liftoff_spark=self.page.locator(self.locators.LIFTOFF_SPARK)
        liftoff_spark.wait_for(state='visible', timeout=10000)
        assert liftoff_spark.is_visible()
        viewbutton=self.page.locator(self.locators.LIFTOFF_SPARK_VIEW)
        viewbutton.wait_for(state='visible', timeout=10000)
        viewbutton.click()
        attach_screenshot(self.page, 'Clicked view button of liftoff spark section')
