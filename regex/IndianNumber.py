import re
number = int(input("Enter phone number: "))
pattern = "^[6-9]\d{9}$"
if re.match(pattern, number):
    print("Valid Number")
else:
    print("Not Valid Number")
