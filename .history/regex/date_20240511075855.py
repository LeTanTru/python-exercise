import re

def is_date(date):
    return re.match(r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/\d{2}/\d{4}$", date) is not None

date = input("Enter your date: ")
if is_date(date):
    print("Valid date")
else:
    print("Invalid date")
