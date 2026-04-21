#Question of inheritance from w3school

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name)
        

class Dog(Animal):
    pass
d1 = Dog("Cat")
d1.speak()
    
