class MyClass:
  x = 5
print(MyClass)

# create object
p1 = MyClass()    #p1-> object name and MyClass() will create an object
print(p1.x)

# delete object
del p1   # will dlt the refrence variable to the object
#print(p1) # will cause an error


# example using class and object->
class person:
  def __init__(self , name, age):  #__init__ is dunder method 
    self.name = name
    self.age = age
  def greet(self):
    print("Hello....This is " + self.name + "...My age is " +str(self.age) )

p1 = person("Nisha", 22)
p1.greet()
    