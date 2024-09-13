import re

def is_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@hcmute\.edu\.vn$", email) is not None

email = input("Enter your email: ")
if is_email(email):
    print("Valid email")
else:
    
