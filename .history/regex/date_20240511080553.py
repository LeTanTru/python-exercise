import re

def is_date(date):
    return re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((19|20)([02468][048]|[13579][26])|([02468][048]|[13579][26])00)$", date) is not None

# date = input("Enter your date: ")

dates = ['1/12/-2024', '1/12/2024', '01/13/2024', '32/12/2024', '30/2/2024', '01/12/2024', '29/02/2026', '03']
for date in dates:
    if is_date(date):
        print(f"{date} is a VALID date")
    else:
        print(f"{date} is an invalid date")
