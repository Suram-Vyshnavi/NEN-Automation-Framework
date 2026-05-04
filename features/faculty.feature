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
        Then user clicks on latest created cohort and closes the cohort
        Then user navigates to home page
    
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
        # Then user clicks on first meeting link
        # Then user validates past activities section and open meeting

    Scenario: Messages and discussions validation
        Then user navigates to home page
        Then user clicks on chat icon
        Then user clicks on send message button
        Then user clicks on first contact in the list
        Then user sends a message
        Then user validates the latest message sent
        Then user clicks on file upload button
        Then user uploads photo in to chat and validates
        Then user clicks on file upload button
        Then user uploads document in to the chat and validates

    Scenario: My Profile validation
        Then user navigates to home page
        Then user clicks on profile icon and navigates to my profile page
        Then user edits profile information name, city, language and save changes
        Then user edits profile again and reverts the changes back to original and save changes
        Then user changes language to Spanish and revert back to English

        