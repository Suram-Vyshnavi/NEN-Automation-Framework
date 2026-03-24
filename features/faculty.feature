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