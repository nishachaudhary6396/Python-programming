class car:
    def __init__(self,brand,year,model):
        self.brand = brand
        self.year = year
        self.model = model

    def show_car(self):
        print(self.brand,self.year,self.model)

car1 = car("bmw",2019,"xyz")
car1.show_car()