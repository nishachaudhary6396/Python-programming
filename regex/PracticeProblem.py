import re
import json
import os

class StudentAuth:

    FILE = "students.json"

    #  Validation methods
    def validate_name(self, name):
        pattern = r"^[a-zA-Z ]{3,30}$"
        return re.match(pattern, name)

    def validate_address(self, address):
        pattern = r"^[a-zA-Z0-9 ,.-/]{10,100}$"
        return re.match(pattern, address)

    def validate_student_id(self, student_id):
        pattern = r"^STU\d{4}$"
        return re.match(pattern, student_id)

    def validate_password(self, password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$"
        return re.match(pattern, password)
    
    def load_data(self):     #to load the data
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                return json.load(f)
        return {}
    
    def save_data(self, data):   #to dump the data
        with open(self.FILE, "w") as f:
            json.dump(data, f)


    #  Registration
    def register(self):
        name = input("Enter name: ")
        if not self.validate_name(name):
            print("Invalid name")
            return
        
        address = input("Enter address: ")
        if not self.validate_address(address):
            print("Invalid address")
            return

        student_id = input("Enter student Id: ")
        if not self.validate_student_id(student_id):
            print("Invalid student ID")
            return

        password = input("Enter password: ")
        if not self.validate_password(password):
            print("Invalid password")
            return
        
        data = self.load_data()    #load existing data

        data[student_id] = password    #save
        self.save_data(data)

        print("Registration Successful!!!!!")

        self.login()

    #  Login
    def login(self):
        login_id = input("Enter login Id: ")
        login_psw = input("Enter login password: ")

        data = self.load_data()

        if login_id in data and data[login_id] == login_psw:
            print("Login Successful")
        else:
            print("Invalid student Id or password")

obj = StudentAuth()
obj.register()