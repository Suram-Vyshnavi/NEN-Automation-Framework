Feature: RM
    Scenario: Home page validation
        Given RM user is on home page
        Then RM user validates cohorts heading
        Then RM user clicks first active cohort
        Then RM user validates tabs
        Then user clicks on release milestones tab
        Then user clicks on milestone and extends deadline
        Then user clicks on refresh button
        Then RM user validates pagination
        Then RM user navigates to home page

    Scenario: Cohorts validation
        Given RM user is on home page
        Then RM user clicks on cohorts tab
        Then RM user validates direct cohorts heading
        Then RM user validates status heading
        Then RM user clicks on active tab
        Then RM user clicks on 1 active cohort 
        Then RM user validates all the tabs in cohort page
        # Then RM user validates pagination
        Then RM user clicks on inactive tab
        Then RM user search for test cohort
        Then RM user validates incubator cohorts heading
        Then RM user validates incubator status heading
        Then RM user clicks on incubator active tab
        Then RM user clicks on incubator 1 active cohort 
        Then RM user validates incubator all the tabs in cohort page
        # Then RM user validates incubator pagination
        Then RM user search for test cohort in incubator cohorts
        Then RM user navigates to home page
    
    Scenario: Digital Library Validation
        Then user navigates to home page
        Then user clicks on digital library section
        Then user validates digital library page section
        Then user validates latest articles and videos section
        Then user validates what are you looking for section
        Then user validates experts videos section
        Then user validates casestudies section
        Then user validates caselets section
        Then user validates concept notes section
        Then user validates solution kits section
        Then user validates good reads section
        Then user searches test in search input
        Then user clicks on first search result
        Then user validates suggested article videos section and clicks back button
        Then user navigates to home page

    Scenario: Performance page validation
        Then user navigates to home page
        Then user clicks on performance tab
        Then user validates please select the following fields to get the reports heading
        Then user validates program name dropdown and selects the option
        Then user validates status dropdown and selects the option
        Then user validates cohort name dropdown and selects the option
        Then user validates cohort quiz card details and toggle switch button
        Then user validates milestone card details and milestone toggle switch button
        Then user clicks on download cohort performance button
        Then user navigates to home page

    Scenario: Calendar Validation
        Then user navigates to home page
        Then user clicks on calendar section
        Then user validates calendar page
    
    Scenario: Messages and discussions validation
        Then user navigates to home page
        Then user clicks on chat icon
        Then user clicks on send message button
        Then user clicks on first contact in the list
        Then user sends a message
        Then user validates the latest message sent
        Then user clicks on file upload button
        Then user uploads document in to the chat and validates

    Scenario: My Profile validation
        Then user navigates to home page
        Then user clicks on profile icon and navigates to my profile page
        Then user edits profile information name, city, language and save changes
        Then user edits profile again and reverts the changes back to original and save changes
        Then user changes language to Spanish and revert back to English

    Scenario: Settings validation
        Then user navigates to home page
        Then user clicks on profile icon and navigates to settings page
        Then user validates settings page heading and sections
        Then user clicks on accounts section
        Then user clicks on zoom connection section
        Then user validates zoom connection section details
        Then user clicks on whatsapp connection section
        Then user validates whatsapp connection section details
        # Then user clicks on calendar section in settings page
        # Then user validates calendar sync section details
        # Then user navigates to home page
