# multiple inheritance -> one child -> multiple parents 
class parent1:
    def showA(self):
        print("A")
class parent2:
    def showB(self):
        print("B")
class child(parent1,parent2):
    def showC(self):
        print("i am learning python")
c = child()
c.showA()
c.showB()
c.showC()


