# Student Login and Registration Regex Practice Problem

import re
#Registeration
name = input("Enter name: ")
address = input("Enter address: ")
student_id = input("Enter student Id: ")
password = input("Enter password: ")

name_pattern = r"^[a-zA-Z ]{3,30}$"
address_pattern = r"^[a-zA-Z ,.-/]{10,100}$"
studentid_pattern = r"^STU\d{4}$"
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$"

if not re.match(name_pattern,name):
    print("Invalid name")
elif not re.match(address_pattern,address):
    print("INvalid address")
elif not re.match(studentid_pattern,student_id):
    print("Invalid student_id")
elif not re.match(password_pattern,password):
    print("Invalid Passowrd")
else:
    print("Registeration Successful!!!!!")
#login
    login_id = input("Enter login Id")
    login_psw = input("Enter login password")
    if login_id==student_id and login_psw==password:
        print("login Successful")
    else:
        print("Invalid student Id or password")








