import re
email = int(input("enter an email:- "))
pattern = r"^[a-zA-Z0-9._+%-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
if re.match(pattern,email):
    print("Valid email")
else:
    print("Invalid Email")