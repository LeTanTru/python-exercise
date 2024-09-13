import re

def is_date(date):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", date) is not None
