Feature: cohort manager
    Scenario: Homepage Validation for Cohort Manager
        Given user is on the homepage
        Then user validates the homepage for cohort manager heading
        Then user validates Active Cohort section
        Then user validates Inactive Cohort section
        Then user clicks on 1st cohort in the Active Cohort section
        Then user validates cohort dashboard and validates the download excel file link
        Then user validates general info section
        Then user validates the upcoming meetings section in general info
        Then user clicks on create meeting button in the upcoming meetings section
        Then user fills all the details in the create meeting form and clicks on create a meeting button
        Then user validates and deletes the created meeting in the upcoming meetings section
        Then user validates cohort venture section
        Then user clicks on the create venture button in the cohort venture section
        Then user fills all the details in the create venture form and clicks on send an invite button
        Then user validates cohort venture heading 
        Then user validates cohort members section
        Then user validates the 1st member in the cohort members section and clicks on 1st chat button
        Then user clicks on create new cohort button in the homepage
        Then user fills all the details in the create new cohort form and clicks on create a cohort button
        Then user validates office hours section in the homepage
        Then user clicks on create button in the office hours section
        Then user fills all the details in the create office hours form and clicks on create meeting button
        Then user clicks on the created meeting in the office hours section and deletes the created meeting
        Then user navigates back to the homepage
        
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

     Scenario: Calendar Validation
        Then user navigates to home page
        Then user clicks on calendar section
        Then user validates calendar page

     Scenario: Messages and discussions validation
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
        Then user clicks on profile icon and navigates to my profile page
        Then user validates all the fields in profile page
        Then user edits profile information name, city, language and save changes 
        Then user edits profile again and reverts the changes back to original and save changes
        Then user changes language to Spanish and revert back to English

    Scenario: Settings validation
        Then user navigates to home page
        Then user clicks on profile icon and navigates to settings page
        Then user clicks on accounts section
        Then user clicks on zoom connection section
        Then user validates zoom connection section details
        Then user clicks on whatsapp connection section
        Then user validates whatsapp connection section details
        Then user clicks on calendar section in settings page
        Then user validates calendar sync section details
        Then user navigates to home page

        