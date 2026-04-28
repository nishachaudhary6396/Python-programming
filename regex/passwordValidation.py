# At least 1 digit
# At least 1 uppercase
# At least 6 characters

import re
password = input("Enter password: ")
pattern = r"^(?=.*[A-Z](?=.*\d)[A-Za-Z\d]{6,}$)"
if re.match(pattern,password):
    print("Valid")
else:
    print("Not valid")