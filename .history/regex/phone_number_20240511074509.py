import re

def is_phone_number(phone_number):
    return re.match(r"^\d{10}$", phone_number) is not None

phone_number = input("Enter your phone number: ")

