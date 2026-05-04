Feature: Evaluator
    Scenario: Home page validation
        Given evaluator user is on the home page
        Then evaluator user validates the home page card
        Then evaluator user validates the resources heading
        When evaluator user clicks on Evaluate button in the home page card
        Then evaluator user validates the venture information card
        Then evaluator user validates the Submissions & Evaluation heading
        Then evaluator user validates the Instructions heading
        Then evaluator user validates the Milestone heading
        Then evaluator user validates the Viability Evaluation heading
        Then evaluator user navigates to home page

    Scenario: Ventures validation
        Given evaluator user is on the home page
        Then evaluator user clicks on ventures tab in the home page
        Then evaluator user validates the all ventures heading
        Then evaluator user validates pending ventures heading
        When evaluator user clicks on Evaluate button in the pending ventures section
        Then evaluator user validates the venture information card in venture section
        Then evaluator user validates the venture name in venture information card
        Then evaluator user validates the Submissions & Evaluation heading in venture section
        Then evaluator user validates the Instructions heading in venture section
        Then evaluator user validates the Milestone heading in venture section
        Then evaluator user validates the Viability Evaluation heading in venture section
        Then evaluator user clicks on the Completed Evaluations heading
        Then evaluator user navigates to home page

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
        Then user clicks on calendar section in settings page
        Then user validates calendar sync section details
        Then user navigates to home page

    