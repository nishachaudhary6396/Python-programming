# Decorators-> that takes another function or method as input
# function that adds extra functionality without changing the original code

# Types-> 1. Function Decorators->

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()

# 2-> Method Decorators() using @staticmethod

class Demo:
    @staticmethod
    def show():
        print("Sttaic method")

Demo.show()

# Built-in Decorators @property, @staticmethod, @classmethod

#@classmethod->
class student:
    college = "GLA UNIVERSITY"
    @classmethod
    def get_clg(cls):
        return cls.college
    
print(student.get_clg())
