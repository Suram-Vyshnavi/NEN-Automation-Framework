import os

class Config:
    BASE_URL = "https://dev.nen.wfglobal.org/en/all-program"

    # Get user type from environment variable, default to 'student'
    USER_TYPE = os.getenv("USER_TYPE", "student").strip().lower()

    # Credentials based on user type
    if USER_TYPE == "faculty":
        USERNAME = "fac-pk-8dec@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "student":
        USERNAME = "wadhwani.foundation99@gmail.com"
        PASSWORD = "Test@123"
    else:
        # Default to student if invalid type
        USERNAME = "wadhwani.foundation99@gmail.com"
        PASSWORD = "Test@123"

    MESSAGE_TEXT = "hello"
