import re

def is_student_id(student_id):
    return re.match(r"^\d{8}$", student_id) is not None
