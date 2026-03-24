class ResourceNetwork_locators:
    RESOURCE_HEADER="(//div[text()='Resource Network'])[1]"
    EXPLORE="//div[text()='Explore']"
    MENTORS_CARD="//p[text()='Mentors']"
    EXPERTS_CARD="//p[text()='Experts']"
    SERVICE_PROVIDERS_CARD="//p[text()='Service Providers']"
    BROWSE_MENTOR_BUTTON="//span[text()='Browse Mentors']"
    BROWSE_EXPERTS_BUTTON="//span[text()='Browse Experts']"
    BROWSE_SERVICEPROVIDES_BUTTON="//span[text()='Browse Service Providers']"
    MENTORS="//div[text()='Mentors']"
    SEARCH_NETWORK="//input[@type='search']"
    #enter text tEST
    REQUEST_MEETING="(//span[text()='Request Meeting'])[position()=1]"
    
    STARTUPINFORMATION_TEXT="//textarea[contains(@placeholder,'Briefly')]"
    # enter text "test startup"
    LINKEDIN_URL="//input[@id='linkedIn']"
    # enter text "https://www.linkedin.com/in/testprofile"
    WHICH_STAGETEXT="//input[@id='startupStage']"
    SCALING_OPTION="//div[contains(text(),'Scaling')]"
    MEETING_EXPECTATION_TEXTAREA="//textarea[@id='meetingExpectation']"
    # enter text "test expectation"
    WEEK_DAYS="//div[@class='week-days']"
    #WEEK_DAYS return 7 elements if SELECT_TIME_SLOTE is available select time slot other wise move to next day and check for slots
    CHECK_SLOTS_AVAILABILITY="//div[@class='no-slots']"
    SELECT_TIME_SLOT="(//div[@class='slots']//span)[1]"
    CONFIRM_REQUEST_BUTTON="//span[text()='Confirm Request']"
    EXPERTS="//div[text()='Experts']"
    SEARCH_NETWORK="//input[@type='search']"
    #enter text test
    SERVICE_PROVIDERS="//div[text()='Service Providers']"
    MY_REQUESTS="//div[text()='My Requests']"




