import re

def is_date(date):
    return re.match(r"", date) is not None

date = input("Enter your date: ")
if is_date(date):
    print("Valid date")
else:
    print("Invalid date")
