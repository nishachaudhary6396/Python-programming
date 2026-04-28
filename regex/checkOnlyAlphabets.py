import re
name = input("Enter name: ")
pattern = r"^[a-zA-Z]+$"
if re.match(pattern,name):
    print("Valid name")
else:
    print("Invalid name")