# Only letters, digits, _
# Length: 5 to 15

import re
username = input("Enter username: ")
pattern = r"^[a-zA-Z0-9_]{5,15}$"
if re.match(pattern,username):
    print("Valid Username")
else:
    print("Invalid Username")