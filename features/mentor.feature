Feature: Mentor
    Scenario: Home page validation
        Given mentor user is on the home page
        Then mentor user validates the home page heading
        And mentor user validates the meetings heading
        And mentor user validates the upcoming meetings section
        And mentor user validates the pending requests section
        And mentor user validates the history section
        And mentor user validates the declined section
        When mentor user clicks on My Availability menu
        Then mentor user validates the weekly schedule section
        When mentor user selects the first checkbox in the weekly schedule
        And mentor user fills the weekly schedule form
        When mentor user clicks on Add Override button
        And mentor user adds a date override
        And mentor user deletes the added override
        Then mentor user navigates back to the home page

    Scenario: Connected Ventures validation
        When mentor user clicks on the Connected Ventures menu
        And mentor user should validate first card in connected venture
        When mentor user clicks on the Book Session button
        And mentor user fills all the required details
        And mentor user creates a meeting
        When mentor user clicks on the Chat button in the connected venture details page
        Then mentor user navigates back to the home page

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

