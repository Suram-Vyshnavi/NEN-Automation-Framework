import os

class Config:
    

    # Get user type from environment variable, default to 'student'
    USER_TYPE = os.getenv("USER_TYPE", "student").strip().lower()
    USER_TYPE.lower()  # Ensure it's in lowercase for consistency
    if "prod" in USER_TYPE:
        BASE_URL = "https://web.nen.wfglobal.org/en/all-program"
        
    else:
        BASE_URL = "https://dev.nen.wfglobal.org/en/all-program"


    # Credentials based on user type
    if USER_TYPE == "faculty":
        USERNAME = "fac-pk-8dec@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "student":
        USERNAME = "wadhwani.foundation99@gmail.com"
        PASSWORD = "Test@123"
    elif USER_TYPE == "prodstudent":
        USERNAME = "wadhwani.foundation99@gmail.com"
        PASSWORD = "Test@123"
    elif USER_TYPE == "prodfaculty":
        USERNAME = "fac-we-pkprod21@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "rm":
        USERNAME = "rm-pk18oct@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_rm":
        USERNAME = "rm-we-prod-5thmarch@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "incubator":
        USERNAME = "testpartner-12admin@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_incubator":
        USERNAME = "testpartner4-admin@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "mentor":
        USERNAME = "ment-pk5-22july@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_mentor":
        USERNAME = "mentor-sri-1806@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "evaluator":
        USERNAME = "srisakthiev@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_evaluator":
        USERNAME = "ragup@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "viability_specialist":
        USERNAME = "srijury@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_viability_specialist":
        USERNAME = "test-2@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "cohort manager":
        USERNAME = "liftoffsparkcohort10@yopmail.com"
        PASSWORD = "Demo@123"
    elif USER_TYPE == "prod_cohort_manager":
        USERNAME = "testsparkcohort@yopmail.com"
        PASSWORD = "Demo@123"
 
    else:
        # Default to student if invalid type
        USERNAME = "wadhwani.foundation99@gmail.com"
        PASSWORD = "Test@123"

    MESSAGE_TEXT = "hello"
