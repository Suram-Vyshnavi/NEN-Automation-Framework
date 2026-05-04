class CalenderLocators:
	CALENDER = "(//div[text()='Calendar'])[1]"
	FIRST_MEETING = "(//div[contains(text(),'Meeting between')])[1]"
	PAST_ACTIVITIES = "//h4[text()='Past Activities']"
	MEETING_LINK = "(//h4[text()='Past Activities']/parent::div//h4[text()='Meeting'])[1]"
	VALIDATE_REVIEW_NOW_BUTTON = "//button[text()='Review Now']"
	VALIDATE_NOTES_SECTION = "//h4[text()='Notes']"
