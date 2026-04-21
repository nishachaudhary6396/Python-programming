# Inheritance allows us to inherit the properties and methods from another class.
# first class is parent class also called base class and another class is child class which is also called derived class ....this is the class that inherits from another class

#parent class
class person:
    def __init__(self,name,lname):
        self.name = name
        self.lname = lname

    def print(self):
        print(self.name, self.lname)

# p1 = person("Nisha","Chaudhary")
# p1.print()

#child class
class student(person):
    # pass
    # def __init__(self,name,lname):
    #     # person.__init__(self,name,lname)
    #     super().__init__(name,lname)  # super keyword automatically inherit the method and properties from its parent
    #     self.fname = "Dharmvir Singh"

    def __init__(self,name,lname,fname):
        super().__init__(name,lname)
        self.name = fname

s = student("Nisha","Chaudhary","dharmvir singh")
print(s.name)
