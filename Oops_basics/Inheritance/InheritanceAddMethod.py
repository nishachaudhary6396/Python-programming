class teacher:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def print(self):
        print(self.fname, self.lname)

class student(teacher):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.dob = year

    def welcome(self):
        print("Welcome", self.fname,self.lname,"to the year of", self.dob)

s = student("Nisha","Chaudhary",2026)
s.welcome()