
#get method
class human:
    def __init__(self,name,clg):
        self.name = name
        self.__clg = clg

    def get_clg(self):    #  to get the private value
        return self.__clg
    
    def set_clg(self,clg):  #set method-> to changet the private property
        self.__clg = clg

h1 = human("Nisha","gla")
print(h1.name)
print(h1.get_clg())
h1.set_clg("gla University")
print(h1.get_clg())

