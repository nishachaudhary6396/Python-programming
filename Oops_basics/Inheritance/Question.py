class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
class student(person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course
    def show(self):
        print(self.course)

obj = student("Nisha","22","Btech")
obj.display()
obj.show()