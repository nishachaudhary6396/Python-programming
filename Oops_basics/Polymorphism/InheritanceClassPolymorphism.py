class Vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def movies(self):
        print("Are")
class car(Vehicle):
    pass
class Toy(Vehicle):
    def movies(self):
        print("You")
class plane(Vehicle):
    def movies(self):
        print("Learning")
c = car("Defender",2021)
t = Toy("Barbie",2022)
p = plane("Indigo",2023)

for i in (c,t,p):
    print(i.model)
    print(i.year)
    i.movies()

