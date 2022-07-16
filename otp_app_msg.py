
SERVER_HEALTH_STATUS = "Server is running fine"
SUCCESS = "SUCCESS"
FAILED = "FAILED"

OTP_NOT_FOUND = "OTP not generated, try again"
CHECK_EMAIL = "Please insert correct email id"

VALID_OTP = "OTP is verified"
OTP_NOT_VALID = "Please check your OTP again"
LIMIT_EXCEEDED = "OTP limit exceeded"

USER_MISSING = "USER NOT MENTION"
INVALID_USER = "User not valid"
NOT_ACTIVE = "User is not active, contact admin"

def create_response(status,messages):

    return {"status": status, "messages" : messages}
