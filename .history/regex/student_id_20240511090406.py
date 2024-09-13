import re

def is_student_id(student_id):
    return re.match(r"^\d{8}$", student_id) is not None

training_type = [1, 2, 3, 4, 5, 6, 7, 'B', 'D', '9'
                 ]

student_id = input("Enter your student ID: ")
if is_student_id(student_id):
    print("Valid student ID")
else:
    print("Invalid student ID")
