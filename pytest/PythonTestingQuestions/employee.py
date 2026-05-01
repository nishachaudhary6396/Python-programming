import re
def validate_employee(emp_id,email):
    emp_pattern = r"^EMP-\d{4}$"
    email_pattern = r"^[a-zA-Z]+@company\.com$"

    if not re.match(emp_pattern,emp_id):
        raise ValueError("Invalid Employee Id")
    
    if not re.match(email_pattern,email):
        raise ValueError("Invalid email")
    
    return  "Valid Employee"