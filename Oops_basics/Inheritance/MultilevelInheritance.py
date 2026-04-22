# multilevel Inheritance -> the base class and the derived class are further inherted into the derived class.
# grandparent -> parent -> child

class person:     # base class
    def __init__(self,name):
        self.name = name

class student(person):  #intermediate class
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course

class kid(student):
    def __init__(self,name,course,degree):
        super().__init__(name,course)
        self.degree = degree

    def show(self):
        print(self.name)
        print(self.course)
        print(self.degree)

k = kid("Nisha","CS","B.Tech")
k.show()


