import re

def is_date(date):
    return re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((19|20)\d\d)$", date) is not None

date = input("Enter your date: ")

date = ['1/12/-2024', '1/12/2024', '1/13/2024', '32']

if is_date(date):
    print("Valid date")
else:
    print("Invalid date")
