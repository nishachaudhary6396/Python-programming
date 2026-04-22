# protected properties used a sigle underscore _

class human:
    def __init__(self,name,clg):
        self.name = name
        self._clg  = clg
    def show(self):
        print(self._clg)

h = human("Nisha",22)
print(h.name)
h.show()
#print(h._clg)  # not recommended..should use inside class methods or in child class

