#format 2804-2026

import re
date = input("Enter date : ")
pattern = r"^\d{2}-\d{2}-\d{4}$"
if re.match(pattern,date):
    print("Valid date")
else:
    print("Invalid date")