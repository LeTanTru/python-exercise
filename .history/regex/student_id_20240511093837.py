import re

def is_student_id(student_id):
    return re.match(r"^[1-7][0-9](0[1-9]|[1-3][0-9]|40)[1-9][0-9]$", student_id) is not None

student_id = input("Enter your student ID: ")
if is_student_id(student_id):
    print("Valid student ID")
else:
    print("Invalid student ID")
