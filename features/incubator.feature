Feature:Incubator
    Scenario: Incubator Cohorts validation
        Given user is on home page
        Then incubator user clicks on cohorts tab
        # Then incubator user validates cohorts heading
        # Then incubator user clicks on active tab
        # Then incubator user clicks on 1 active cohort 
        # Then incubator user validates all the tabs in cohort page
        # Then incubator user clicks on general info tab
        # Then incubator user validates batch faculty and message icon in general info tab
        # Then incubator user validates cohort Activity 
        # Then incubator user clicks on cohorts members tab
        # Then incubator user validates cohort members heading
        # Then incubator user validates student added and maximum allowed students details
        # Then incubator user clicks on cohort startups
        # Then incubator user validates cohort startups heading and startup details
        # Then incubator user clicks on 1 cohort startup
        # Then incubator user search for test cohort in cohorts
        # Then incubator user clicks on inactive tab
        # Then incubator user search for test cohort in cohorts
        Then incubator user clicks on create new cohort button
        Then incubator user fills all the details and create new cohort
        Then incubator user validates office hours section in cohort page
        Then incubator user clicks on create button
        Then incubator user fills all the details and create a meeting
        Then incubator user deletes the created meeting
        Then incubator user navigates to home page

    Scenario: Incubator Events validation
        Given user is on home page
        
        Then incubator user clicks on events tab
        Then incubator user validates events heading
        Then incubator user clicks on add event button
        Then incubator user fills all the details and click on add speakers
        Then incubator user clicks on create event & next
        Then incubator user clicks on add by emails radio button
        Then incubator user clicks on bulk upload invitation button and uploads the file and submits
        Then incubator user clicks on events tab
        Then incubator user deletes the created event
        Then incubator user navigates to home page
    
    Scenario: Partner Profile validation
        Given user is on home page
        Then incubator user clicks on profile icon
        Then incubator user clicks on partner profile 
        Then incubator user validates partner profile heading
        Then incubator user validates partner name
        Then incubator user validates logo 
        Then incubator user navigates to home page

    Scenario: Program managers validation
        Given user is on home page
        When the user clicks on the profile icon
        And the user clicks on the program managers tab
        Then the user should see the "Manage Program Managers" heading
        When the user clicks on the add program manager button
        And the user fills all the required details and clicks on create button
        Then incubator user navigates to home page
