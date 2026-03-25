Feature: Faculty
    Scenario: Home page validation
        Given user is on home page
        Then user validates cohorts heading
        Then user clicks on active tab
        Then user clicks on 1 active cohort 
        Then user validates all the tabs in cohort page
        Then user validates pagination
        Then user clicks on inactive tab
        Then user search for test cohort
        Then user clicks on create new cohort button
        Then user fills all the details and create new cohort
        Then user navigates to home page
    
    Scenario: Performance page validation
        Given user is on home page
        Then user clicks on performance tab
        Then user validates please select the following fields to get the reports heading
        Then user validates program name dropdown and selects the option
        Then user validates status dropdown and selects the option
        Then user validates cohort name dropdown and selects the option
        Then user validates cohort quiz card details and toggle switch button
        Then user validates milestone card details and milestone toggle switch button
        Then user clicks on download cohort performance button
        Then user navigates to home page

        