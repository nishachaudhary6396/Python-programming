# the self parameter links the methods to the specific object
# we can use any other word also in the place of self ...just should be the first paramenter
class Animal:
    def __init__(self,name):
        self.name = name

    def print(self):
        print(self.name)

A1 = Animal("Dog")
A2 = Animal("Cat")

A1.print()
A2.print()


