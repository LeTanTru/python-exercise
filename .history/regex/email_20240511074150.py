import re

def is_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
