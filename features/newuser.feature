Feature: newuser
    Scenario: New User Registration
        Given user is on the login page
        Then user clicks on sign up button
        Then user fill the email and clicks on create button
        Then user enters otp and clicks on submit button
        Then user fills the password and clicks on confirm password button
        Then user fills all the details in the registration form and clicks on submit button
        Then user login to home page and clicks on profile icon and logout from the application
        
