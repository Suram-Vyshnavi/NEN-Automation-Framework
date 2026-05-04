Feature: Viability Specialist
    Scenario: Homepage Validation for Viability Specialist
        Given Viability Specialist user is on the home page
        Then Viability Specialist user validates the home page card
        Then Viability Specialist user validates the resource heading
        When Viability Specialist user clicks on Evaluate button in the home page
        Then Viability Specialist user validates the venture information card
        Then Viability Specialist user validates the Submissions & Evaluation heading
        Then Viability Specialist user validates the Instructions heading
        # Then Viability Specialist user validates the View file link
        Then Viability Specialist user validates the Evaluate heading
        Then Viability Specialist user validates the My Ratings heading
        Then Viability Specialist user validates the Milestone form section
        Then Viability Specialist user validates the Milestone next form section
        Then Viability Specialist user navigates to home page

    Scenario: Ventures validation for Viability Specialist
        Given Viability Specialist user is on the home page
        Then Viability Specialist user clicks on ventures tab in the home page
        Then Viability Specialist user validates the all ventures heading
        Then Viability Specialist user validates pending ventures heading
        When Viability Specialist user clicks on Evaluate button in the pending ventures section
        Then Viability Specialist user validates the venture information card in venture section
        Then Viability Specialist user validates the venture name in venture information card
        Then Viability Specialist user validates the Submissions & Evaluation heading in venture section
        Then Viability Specialist user validates the Instructions heading in venture section
        Then Viability Specialist user validates the Evaluate heading in venture section
        Then Viability Specialist user validates the My Ratings heading in venture section
        Then Viability Specialist user clicks on the Completed Evaluations heading
        Then Viability Specialist validates the first card in completed evaluations section
        Then Viability Specialist user navigates to home page

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
        # Then user clicks on calendar section in settings page
        # Then user validates calendar sync section details
        Then user navigates to home page

