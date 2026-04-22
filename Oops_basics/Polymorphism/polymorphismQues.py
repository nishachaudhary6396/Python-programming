# Ques of polymorphism

class Cat:  
    def sound(self):
       print("Meow")
class fox:
    def sound(self):
       print("xyz")

c1 = Cat()
f1 = fox()

for i in (c1,f1):
    i.sound()