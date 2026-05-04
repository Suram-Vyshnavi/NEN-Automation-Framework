Feature:Incubator
    Scenario: Incubator Cohorts validation
        # Given user is on home page
        # Then incubator user clicks on cohorts tab
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
        Then incubator user clicks on profile icon
        Then incubator user clicks on partner profile 
        Then incubator user validates partner profile heading
        Then incubator user validates partner name
        Then incubator user validates logo 
        Then incubator user navigates to home page

    Scenario: Program managers validation
        When the user clicks on the profile icon
        And the user clicks on the program managers tab
        Then the user should see the "Manage Program Managers" heading
        When the user clicks on the add program manager button
        And the user fills all the required details and clicks on create button
        Then incubator user navigates to home page
    
    Scenario: Calendar Validation
        Then user clicks on calendar section
        Then user validates calendar page

    # Scenario: Messages and discussions validation
    #     Then user navigates to home page
    #     Then user clicks on chat icon
    #     Then user clicks on send message button
    #     Then user clicks on first contact in the list
    #     Then user sends a message
    #     Then user validates the latest message sent
    #     Then user clicks on file upload button
    #     Then user uploads document in to the chat and validates
    
    Scenario: My Profile validation
        Then user clicks on profile icon and navigates to my profile page
        Then user edits profile information name, city, language and save changes
        Then user edits profile again and reverts the changes back to original and save changes
        Then user changes language to Spanish and revert back to English

    Scenario: Settings validation
        Then user clicks on profile icon and navigates to settings page
        Then user validates settings page heading and sections
        Then user clicks on accounts section
        Then user clicks on zoom connection section
        Then user validates zoom connection section details
