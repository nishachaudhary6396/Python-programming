# hierarchical inheritance is when more than one derived class are created from the single parent class

class person:      #parent class
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)
class student(person):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course

    def display(self):
        print(self.name,self.course)

class Teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(self.name,self.subject)

s = student("Nisha","Cs")
t = Teacher("Chaudhary","DIP")

s.show()
s.display()
t.show()
t.display()

