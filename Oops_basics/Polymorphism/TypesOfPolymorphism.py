# complile time polymorphism -> it decides which method or operation will run at the compile time....well python does not support 
#bcz python is a dynamically types language..so it is achieved by using default and variable arguements.....thi is also called method overloading

class Btech:
    def add(self,a=1,b=2,*args):
        result = a*b
        for i in args:
            result *=i
        return result

b = Btech()
print(b.add())
print(b.add(5))
print(b.add(4,5))
print(b.add(6,7,8))


# Run time polymorphism -> overriding
class Subject:
    def show(self):
        return "lots of subjects"
class Maths(Subject):
    def show(self):
        return "Maths is interesting"
class Physics(Subject):
    def show(self):
        return "I like physics"
Sub = [Subject(),Maths(),Physics()]

for i in Sub:
    print(i.show())


# Polymorphism in Built-in Functions ...len() and max()
print(len("Hello")) #String length
print(len([1,2,3])) #list length

print(max(1,2,3))
print(max("l","m","n"))


