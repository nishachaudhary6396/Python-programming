import re
pin = input("Enter pin code: ")
pattern = r"^\d{6}$"
if re.match(pattern.pin):
    print("Valid pin")
else:
    print("Invalid pin")