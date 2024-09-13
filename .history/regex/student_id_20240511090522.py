import re

def is_student_id(student_id):
    return re.match(r"^\d{8}$", student_id) is not None

student_id = input("Enter your student ID: ")
if is_student_id(student_id):
    print("Valid student ID")
else:
    print("Invalid student ID")
