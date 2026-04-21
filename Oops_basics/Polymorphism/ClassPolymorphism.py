class University:
    def __init__(self,city):
        self.city = city
    def mainly(self):   #mainly is a method name
        print(self.city)
class Bus:
    def __init__(self,govt,number):
        self.govt = govt
        self.number = number
    def mainly(self):
        print(self.govt, self.number)
class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def mainly(self):
        print(self.model,self.year)

uni = University("Mathura")
bus1 = Bus("xyz",1234)
car1 = Car("thails",1991)

for i in (uni,bus1,car1):
    i.mainly()
        