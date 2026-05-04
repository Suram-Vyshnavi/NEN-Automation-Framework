class mentor_home_locators:
    MENTOR_HOME_PAGE_HEADER = "(//div[text()='Home'])[1]"
    MENTOR_HOME_PAGE_CARD = "//div[@class='welcome-card-v2__left']"
    MEETINGS_HEADER = "//h1[text()='Meetings']"
    UPCOMING_MEETINGS_TAB = "//button[contains(@class,'meetings-tab') and contains(@class,'tab-upcoming')]"
    PENDING_MEETINGS_TAB = "//button[contains(@class,'meetings-tab') and contains(@class,'tab-pending')]"
    HISTORY_MEETINGS_TAB = "//button[contains(@class,'meetings-tab') and contains(@class,'tab-history')]"
    DECLINED_MEETINGS_TAB = "//button[contains(@class,'meetings-tab') and contains(@class,'tab-declined')]"
    MY_AVAILABILITY_CARD = "//div[contains(@class,'welcome-card-v2__cta-box')]"
    MY_AVAILABILITY_HEADER = "//h5[text()='My Availability']"
    WEEKLY_SCHEDULE_HEADER = "//h2[text()='Weekly Schedule']"
    FIRST_CHECKBOX = "//h4[text()='monday']/preceding::div[1]//input"
    START_TIME_DROPDOWN = "(//h4[text()='monday']/ancestor::div[2]//span[@class='ant-select-selection-item'])[1]"
    TIME_SELECTION_START = "//div[contains(text(),'12:00')]"
    END_TIME_DROPDOWN = "(//h4[text()='monday']/ancestor::div[2]//span[@class='ant-select-selection-item'])[2]"
    TIME_SELECTION_END = "//div[contains(text(),'12:30')]"
    COPY_ICON = "//span[@class='anticon anticon-copy action_icon']"
    COPYTIME_TO_NEXTDAY_CHECKBOX = "//span[text()='tuesday']/preceding::span[2]//input"
    APPLY_BUTTON = "//span[text()='Apply']"
    CANCEL_SLOT_ICON = "(//span[@class='anticon anticon-close action_icon'])[1]"
    ADD_OVERRIDE_BUTTON = "//span[text()='Add an Override']"
    TODAY_DATE = "//td[@class='ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today']"
    OVERRIDE_SAVE_BUTTON = "(//span[text()='Save'])[2]"
    DELETE_ICON = "//span[@class='anticon anticon-delete delete_icon']"
    SAVE_BUTTON="//span[text()='Save']"





